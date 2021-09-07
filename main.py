import sys, json, logging

from flask import Flask, render_template, request, redirect
import flask
import requests
import service


app = Flask(__name__)


all_variables = service.read_yaml('./variables.yaml')

behavior_parameters = all_variables['behaviorParameters']
transactional_parameters = all_variables['transactionalParameters']

transactional_parameters.pop('subMerchantDetails')
transactional_parameters.pop('transactionOptions')


@app.route("/", methods=['GET'])
def index():
    if len(request.args) != 0:
        return render_template('index.html', form=service.assign_parameters(transactional_parameters))

    return redirect('/?' + service.url_parser(transactional_parameters))


@app.route("/embedded-form", methods=['POST'])
def embedded_form():
    api_url = request.form.get('rest_server_api_url') if request.form.get('rest_server_api_url') is None else behavior_parameters['rest_server_api_url']
    send_body = service.new_body_to_send(transactional_parameters)
    CONTRIB = f"Python_Flask_Embedded_Examples_2.x_1.0.0/{flask.__version__}/{sys.version[:5]}"

    send_body['contrib'] = CONTRIB

    app.logger.info(json.dumps(send_body, indent=4))
    form_token = create_form_token(json.dumps(send_body), api_url)

    if form_token == None:
        return render_template('error.html')

    return render_template(
        'embedded_form.html', 
        rest_static_url=behavior_parameters['rest_static_url'],
        kr_public_key=behavior_parameters['test_public_key'] if behavior_parameters['test_mode'] else behavior_parameters['prod_public_key'],
        kr_popin=True if request.form.get('kr-popin') else False,
        formToken=form_token, 
    )


@app.route('/capture-ipn', methods=['GET','POST'])
def capture_ipn():
    if request.form.get('kr-answer') == None:
        return "KO - Invalid request.", 400

    app.logger.info(json.dumps(json.loads(request.form.get('kr-answer').replace('"', '\"')), indent=4))
    signature = service.compute_hmac_sha256_signature(
        behavior_parameters['test_password'] if behavior_parameters['test_mode'] else behavior_parameters['prod_password'],
        request.form.get('kr-answer')
    )
    if signature != request.form.get('kr-hash'):
        return "KO - Signatures does not match.", 401

    # Check in your DB if the transaction was already processed
    return "OK - Successful transaction payment.", 200


@app.route('/redirect', methods=['POST'])
def redirect_():
    """
    Redirect will proceed with the payment, and will either succeed or refused the payment.
    """
    if request.args.get('status') == 'success':
        signature = service.compute_hmac_sha256_signature(
            behavior_parameters['test_hmac_sha_256_key'] if behavior_parameters['test_mode'] else behavior_parameters['prod_hmac_sha_256_key'],
            request.form.get('kr-answer')
        )
        app.logger.info(json.dumps(json.loads(request.form.get('kr-answer').replace('"', '\"')),indent=4))

        return render_template(
            'redirect.html',
            redirect_obj=request.form,
            signature=signature,
            signature_validation=True if signature == request.form.get('kr-hash') else False,
            kr_answer=json.dumps(json.loads(request.form['kr-answer']), indent=4)
        )
    if request.args.get('status') == 'refused':
        return "Payment decline, exceded retrys attempts."


def create_form_token(entry_body, url=None):
    """
    Create form token to load the payment method
    """
    shop_id = behavior_parameters['shop_id']
    password = behavior_parameters['test_password'] if behavior_parameters['test_mode'] else behavior_parameters['prod_password']
    string_to_encode = f"{shop_id}:{password}"

    if url == None:
        create_payment_url = f"{behavior_parameters['rest_server_api_url']}V4/Charge/CreatePayment"
    else:
        create_payment_url = f"{url}V4/Charge/CreatePayment"

    get_encoder = service.encode_to_base64(string_to_encode)
    set_header = {"Authorization": f"Basic {get_encoder}"}
    try:
        form_token = json.loads(requests.post(
            create_payment_url, data=entry_body, headers=set_header
        ).text)['answer']['formToken']
        return form_token
    except ValueError:
        pass


if __name__ == "__main__":
    app.debug = behavior_parameters['test_mode']
    app.run(host="127.0.0.1", port=behavior_parameters['port'])
    logging.basicConfig(filename='lyra.log', level=logging.DEBUG)
