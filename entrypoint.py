import os
import sys
import json

import traceback
from typing import Callable

import requests

import googleapiclient
import google.auth.transport.requests
import google.oauth2.id_token
from googleapiclient import discovery



def test_fixture(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    """

    type_= request.json['resourceType']
    body = request.json


    parent = 'projects/{}/locations/{}/datasets/'.format(
        os.environ.get('PROJECT_ID'),
        os.environ.get('LOCATION'),
        os.environ.get('DATASET_ID'),
    )

    try:
        response = 'use `service` to create and execute() a request'


        print(response)
    except googleapiclient.errors.HttpError as exc:
        print(exc)
        raise exc


def make_authorized_get_request(service_url, json):
    """
    make_authorized_get_request makes a GET request to the specified HTTP endpoint
    in service_url (must be a complete URL) by authenticating with the
    ID token obtained from the google-auth client library.
    """

    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, service_url)

    headers: dict = {
        "Authorization": f"Bearer {id_token}"
    }

    return requests.Request(service_url, json=json, headers=headers)


def wrapper(func: Callable, data: tuple):

    try:
        func(*data)
    except Exception as exc:
        print(traceback.format_exc())
        return 1

    return 0


def main():

    func: Callable = test_fixture
    with open('payload.json', 'r', encoding='utf-8') as payload:
        json_payload = json.loads(payload.read())
        request = make_authorized_get_request(os.environ.get('URL'), json_payload)

    return wrapper(func, (request,))


if __name__ == "__main__":
    sys.exit(main())
