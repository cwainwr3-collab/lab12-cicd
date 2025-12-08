import base64
import json
import os

import requests

import urllib.parse

from common.constants import (
    ANONYMIZER_BASE_URL,
)

DEFAULT_HEADERS = {"Content-Type": "application/json"}
MULTIPART_HEADERS = {"Content-Type": "multipart/form-data"}
ANONYMIZER_BASE_URL = os.environ.get("ANONYMIZER_BASE_URL", ANONYMIZER_BASE_URL)


def anonymize(data):
    response = requests.post(
        f"{ANONYMIZER_BASE_URL}/anonymize", data=data, headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content


def anonymizers():
    response = requests.get(
        f"{ANONYMIZER_BASE_URL}/anonymizers", headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content



def deanonymize(data):
    response = requests.post(
        f"{ANONYMIZER_BASE_URL}/deanonymize", data=data, headers=DEFAULT_HEADERS
    )
    return response.status_code, response.content

def __get_redact_payload(color_fill):
    payload = {}
    if color_fill:
        payload = {"data": "{'color_fill':'" + str(color_fill) + "'}"}
    return payload


def __get_multipart_form_data(file):
    multipart_form_data = {}
    if file:
        multipart_form_data = {
            "image": (file.name, file, "multipart/form-data"),
        }
    return multipart_form_data

def genz(data):
    json_str = json.dumps(data)
    response = requests.get(
        f"{ANONYMIZER_BASE_URL}/genz",
        params={'data': json_str},  # requests will encode this
        headers=DEFAULT_HEADERS
    )

    print(f"DEBUG: Full URL sent: {response.url}")
    print(f"DEBUG: Response status: {response.status_code}")
    print(f"DEBUG: Response text: {response.text[:500] if response.text else 'Empty'}")

    return response.status_code, response.content