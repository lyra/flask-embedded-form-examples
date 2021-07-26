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
    python -m venv .env

    source ./.env/bin/activate # for unix/linux
    .\.env\Scripts\activate # for windows

    pip install -r requirements.txt
    ```

## Running the app

Change the values with a `change_me` on the `variables.yaml` file with 
the values of your shop, thus you can find them on the BackOffice Vendor.

Login to BackOffice Vendor, go to `Configuration > Store` then choose the shop you like,
then go to `API REST Keys` tab and there you will find both production and 
testing keys.

You will find the keys for `shopId`, `password_testing`, `password_production`, and `api_url` 
at the first part of the page, in the rest apis keys section.

At the second section, Javascript client and SDK movil, you will find the keys for 
`sdk_password_testing` and `sdk_password_production`.

At the third section you wil find the HMAC SHA 256 key, to compute the signature, for the 
values `sha_key_testing` and `sha_key_production`.

Open your terminal on the project and run the command `python main.py` 
to run the flask project. By default it will run on `0.0.0.0:5000`, 
go to your browser, go to the url project and you will can use the example.

## License

Each source file included in this distribution is licensed 
under the GNU GENERAL PUBLIC LICENSE (GPL 3.0). Please see 
LICENSE.txt for the full text of the GPL 3.0 license. It is 
also available through the world-wide-web at this 
URL: http://www.gnu.org/licenses/gpl.html.