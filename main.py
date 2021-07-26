import json, logging

import requests

from flask import Flask, render_template, request, redirect

import service

app = Flask(__name__)


all_variables = service.read_yaml()

behavior_parameters = all_variables['behaviorParameters']
transactional_parameters = all_variables['transactionalParameters']

transactional_parameters.pop('subMerchantDetails')
transactional_parameters.pop('transactionOptions')


@app.route("/", methods=['GET'])
def index():
    if len(request.args) != 0:
        return render_template('index.html', form=service.assign_parameters(transactional_parameters))

    return redirect('/?' + service.url_parser(transactional_parameters))


@app.route("/process-data", methods=['POST'])
def capture_ipn():
    send_body = service.new_body_to_send(transactional_parameters)
    app.logger.info(json.dumps(send_body, indent=4))
    formToken = create_form_token(json.dumps(send_body))

    return render_template(
        'embedded_form.html', 
        api_url=behavior_parameters['api_url'],
        kr_public_key=behavior_parameters['sdk_password_testing'],
        kr_popin=True if request.form.get('kr-popin') else False,
        formToken=formToken, 
    )


@app.route('/ipn', methods=['GET','POST'])
def ipn():
    if request.form.get('kr-answer') == None:
        return "KO - Invalid request.", 400
    app.logger.info(json.dumps(json.loads(request.form.get('kr-answer').replace('"','\"')), indent=4))
    signature = service.compute_hmac_sha256_signature(behavior_parameters['password_testing'], request.form.get('kr-answer'))
    if signature != request.form.get('kr-hash'):
        return "KO - Signatures does not match.", 401

    # Check in your DB if the transaction was already processed
    return "OK - Successful transaction payment.", 200


@app.route('/redirect', methods=['POST'])
def redirect_():
    if request.args.get('status') == 'success':
        signature = service.compute_hmac_sha256_signature(behavior_parameters['sha_key_testing'], request.form.get('kr-answer'))
        app.logger.info(json.dumps(json.loads(request.form.get('kr-answer').replace('"','\"')),indent=4))

        return render_template(
            'redirect.html',
            redirect_obj=request.form,
            signature=signature,
            signature_validation=True if signature == request.form.get('kr-hash') else False,
            kr_answer=json.dumps(json.loads(request.form['kr-answer']), indent=4)
        )
    if request.args.get('status') == 'refused':
        return "Payment decline, exceded retrys attempts."


def create_form_token(entry_body):
    shopId = behavior_parameters['shopId']
    password_testing = behavior_parameters['password_testing']
    string_to_encode = f"{shopId}:{password_testing}"

    URL = f"{behavior_parameters['api_url']}/api-payment/V4/Charge/CreatePayment"
    get_encoder = service.encode_to_base64(string_to_encode)
    set_header = {"Authorization": f"Basic {get_encoder}"}
    return json.loads(requests.post(
        URL, data=entry_body, headers=set_header
    ).text)['answer']['formToken']


if __name__ == "__main__":
    app.debug = behavior_parameters['test_mode']
    logging.basicConfig(filename='lyra.log', level=logging.DEBUG)
    app.run(host="0.0.0.0", port=behavior_parameters['port'])
