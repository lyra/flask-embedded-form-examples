# Flask - Embedded form example

Implementation of the embedded form in Flask - Python.

## Installation

* Clone the repository on your workstation.
* By default, the new versions of Python come with `pip`, run `pip3 help` to check if it is installed. If there is an error, follow the commands below:

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

* Run the following comands to install the project dependencies:

    ``` bash
    # run to create the python virtual environment
    python -m venv .env

    # run to activate the python virtual environment
    source ./.env/bin/activate # for unix/linux
    .\.env\Scripts\activate # for windows

    # install all dependencies to run the example
    pip install -r requirements.txt
    ```

## Running the app

To run the example, change the values with a `change_me` on the `variables.yaml` file with the values of your shop. Thus you can find them on the merchant Back Office.

Login to the merchant Back Office, go to `Configuration > Store` then choose the shop you want, then go to `REST API keys` tab and there you will find both production and test keys.

You will find the values for `shop_id`, `test_password`, `prod_password` and `rest_server_api_url` at the first section named **REST API keys**.

At the second section named **Keys for the JavaScript client and the mobile SDK**, you will find the values for `test_public_key` and `prod_public_key`.

At the third section named **REST API: keys used to calculate / check the kr-hash field**, you will find the values `test_hmac_sha_256_key` and `prod_hmac_sha_256_key`.

Open your terminal on the project and run the command `python main.py` to run the flask project. By default it will run on `127.0.0.1:5000/`, go to your browser and open the project URL, you can now use the example.

## License

Each source file included in this distribution is licensed under the GNU GENERAL PUBLIC LICENSE (GPL 3.0). Please see LICENSE.txt for the full text of the GPL 3.0 license. It is also available through the world-wide-web at this URL: http://www.gnu.org/licenses/gpl.html.