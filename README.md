# Flask - Embedded form example

Implementation of Lyra Embedded Form using Flask(Python)

## Cloud Deployment

* Create an [Heroku account](https://signup.heroku.com/)
* Deploy using the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
  * *heroku create*
  * *git push heroku master*
  * *heroku open*
* Alternatively you can easily deploy using this button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://github.com/lyra/flask-embedded-form-examples)

## Local Installation

1. Clone the repository

    ```bash
    git clone https://github.com/lyra/flask-embedded-form-examples
    ```

1. By default, the new versions of Python come with `pip`, however run 
`pip3 help` to check if it is installed. If there is an error, follow the 
commands below:

    ```bash
    # Windows
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    pip help

    # Unix
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    pip help
    ```

1. Run the following comands to install the project dependencies:

    ``` bash
    cd flask-embedded-form-examples
    # run to create the python virtual environment
    python -m venv .venv

    # run to activate the python virtual environment
    source ./.venv/bin/activate # for unix/linux
    .\.venv\Scripts\activate # for windows
    source ./.venv/Scripts/activate # if you are using git bash on windows

    # install all dependencies to run the example
    pip install -r requirements.txt
    ```

## Running the app

All the necesary environment variables to run the backend application, are 
on the Merchant Back Office.

Login to the merchant Back Office, go to `Configuration > Store` then choose 
the shop you want, then go to `REST API keys` tab and there you will find 
both production and test keys.

You will find the values for `shop_id`, `test_password`, `prod_password` 
and `rest_server_api_url` at the first section named **REST API keys**.

At the second section named **Keys for the JavaScript client and the mobile 
SDK**, you will find the values for `test_public_key` and `prod_public_key`.

At the third section named **REST API: keys used to calculate / check the 
kr-hash field**, you will find the values `test_hmac_sha_256_key` and 
`prod_hmac_sha_256_key`.

### Local deployment

Create a new file with the name `.env`, copy and paste the same information 
that there is in the `.env.example` file.

Also, at the `.env` file, theres a `retry` field, which is the number of 
attempts of a transaction can fail. It can be set to a **max value of 3 
attempts** per transaction.

To run the example, change the values with a `change_me` on the `.env` file 
with the values of your shop.

Open your terminal on the project and run the command `python wsgi.py` to 
run the flask project. By default it will run on `127.0.0.1:5000/`, go to 
your browser and open the project URL, you can now use the example.

## License

Each source file included in this distribution is licensed under the GNU 
GENERAL PUBLIC LICENSE (GPL 3.0). Please see LICENSE.txt for the full text 
of the GPL 3.0 license. It is also available through the world-wide-web at 
this URL: http://www.gnu.org/licenses/gpl.html.