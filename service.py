import hashlib, base64, hmac, json

import yaml


def read_yaml():
    with open('./variables.yaml') as f:
        return json.loads(json.dumps(yaml.load(f)))


def encode_to_base64(str_to_encode):
    return base64.b64encode(str_to_encode.encode('ascii')).decode()


def compute_hmac_sha256_signature(key, message):
    """
    `key` argument is the password of the store
    and the `wmessage` argument is all the arguments concatenated, plus the password store
    """
    byte_key = str.encode(key)
    message = str.encode(message)
    signature = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
    return signature
