# Flask - Incrusted Form Example

Implementation of the embedded form in Flask - Python

## Installation

1. Clone the repository on your workstation.
1. By default, the new versions of python come with pip, 
run `pip3 help` to check if it is installed. If there 
is an error follow the commands from below.

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

1. Run the following comands to install the project dependencies.

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

To run the example, change the values with a `change_me` on the `variables.yaml` file 
with the values of your shop, thus you can find them on the BackOffice Vendor.

Login to BackOffice Vendor, go to `Configuration > Store` then choose the shop you like,
then go to `API REST Keys` tab and there you will find both production and testing keys.

You will find the keys for `shopId`, `testing_password`, `production_password`, and `rest_api_server_name` at the first part of the page, in the **REST API keys** section.

At the second section, **Javascript client and SDK movil**, you will find the keys for 
`sdk_public_test_key` and `sdk_public_production_key`.

At the third section, at **REST API: keys used to calculate / check the kr-hash field** 
you wil find the HMAC SHA 256 key, to compute the signature, for the values 
`hmac_sha_256_test_key` and `hmac_sha_256_production_key`.

Open your terminal on the project and run the command `python main.py` 
to run the flask project. By default it will run on `127.0.0.1:5000/`, 
go to your browser, go to the url project and you will can use the example.

## License

Each source file included in this distribution is licensed 
under the GNU GENERAL PUBLIC LICENSE (GPL 3.0). Please see 
LICENSE.txt for the full text of the GPL 3.0 license. It is 
also available through the world-wide-web at this 
URL: http://www.gnu.org/licenses/gpl.html.