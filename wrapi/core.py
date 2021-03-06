from base64 import b64encode
from hashlib import sha512
import requests
import json
import hmac


JSON_MIME_TYPE = 'application/json'


def get_basic_authorization_header(key):
    return "Basic %s" % b64encode(key + ":")


def get_signed_authorization_header(key, secret, message):
    return b64encode("%s:%s" % (
        key, hmac.new(secret, message, sha512).hexdigest()))


def result(response):
    if response.status_code == 200:
        rjson = response.json()
        if rjson['status'] == 'success':
            return rjson['result']
    return None


def get(resource, identifier, version,
        url, key, secret, params={}, raw=False):
    response = requests.get(
        '%s/%s/%s/%s' % (url, version, resource, identifier),
        headers={'Content-Type': JSON_MIME_TYPE,
                 'Authorization': get_signed_authorization_header(
                     key, secret,
                     "GET:/{0}/{1}/{2}:{3}".format(
                         version, resource, identifier, JSON_MIME_TYPE))},
        params=params)
    if raw:
        return response
    else:
        return result(response)


def all(resource, version, url, key,
        secret, params={}, raw=False):
    response = requests.get(
        '{0}/{1}/{2}'.format(url, version, resource),
        headers={'Content-Type': JSON_MIME_TYPE,
                 'Authorization': get_signed_authorization_header(
                     key, secret,
                     "GET:/{0}/{1}:{2}".format(
                         version, resource, JSON_MIME_TYPE))},
        params=params)
    if raw:
        return response
    else:
        return result(response)


def post(resource, version,
         url, key, secret, data=None, raw=False):
    response = requests.post(
        '{0}/{1}/{2}'.format(url, version, resource),
        data=json.dumps(data),
        headers={'Content-Type': JSON_MIME_TYPE,
                 'Authorization': get_signed_authorization_header(
                     key, secret,
                     "POST:/{0}/{1}:{2}".format(
                         version, resource, JSON_MIME_TYPE))})
    if raw:
        return response
    else:
        return result(response)


def put(resource, identifier,
        version, url, key, secret, data=None, raw=False):
    response = requests.put(
        '{0}/{1}/{2}/{3}'.format(url, version, resource, identifier),
        data=json.dumps(data),
        headers={'Content-Type': JSON_MIME_TYPE,
                 'Authorization': get_signed_authorization_header(
                     key, secret,
                     "PUT:/{0}/{1}/{2}:{3}".format(
                         version, resource, identifier, JSON_MIME_TYPE))})
    if raw:
        return response
    else:
        return result(response)


def patch(resource, identifier,
          version, url, key, secret, data=None, raw=False):
    response = requests.patch(
        '{0}/{1}/{2}/{3}'.format(url, version, resource, identifier),
        data=json.dumps(data),
        headers={'Content-Type': JSON_MIME_TYPE,
                 'Authorization': get_signed_authorization_header(
                     key, secret,
                     "PATCH:/{0}/{1}/{2}:{3}".format(
                         version, resource, identifier, JSON_MIME_TYPE))})
    if raw:
        return response
    else:
        return result(response)
