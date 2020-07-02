"""
Functions for working with the Petfinder API.
"""

import os
import md5
import requests as req

URL = "http://api.petfinder.com/"


#####
# Security
#####

def key(api_key=None):
    """Save your Petfinder API key."""
    if api_key:
        os.environ['PETFINDER_API_KEY'] = api_key
    else:
        api_key = os.environ.get('PETFINDER_API_KEY', '')
    return api_key


def secret(secret_key=None):
    """Store your Petfinder API secret key."""
    if secret_key:
        os.environ['PETFINDER_SECRET_KEY'] = secret_key
    else:
        secret_key = os.environ.get('PETFINDER_SECRET_KEY', '')
    return secret_key


def sign():
    """Create the MD5 signature of a user."""
    api_key = key()
    secret_key = secret()
    # I find this "security" pretty stupid.
    return md5.new(secret_key + 'key=' + api_key).digest()


#####
# Requests
#####

def get(path, **params):
    """Perform a GET request against the Petfinder API."""
    params['format'] = 'json'
    params['key'] = key()
    endpoint = URL + path
    response = req.get(endpoint, params=params)
    return response.json


def breeds(animal=None, **params):
    """Find breeds available for a certain type of animal."""
    animals = ['barnyard', 'bird', 'cat', 'dog', 'horse', 'pig',
               'reptile', 'smallfurry']
    if not animal:
        return animals
    params['animal'] = animal
    return get('breed.list', **params)


def pet(identifier, location, **params):
    """Get the record for a specific pet."""
    params['id'] = identifier
    params['location'] = location
    return get('pet.get', **params)


def shelters(location, **params):
    """Find shelters for a given location."""
    params['location'] = location
    response = get('shelter.find', **params)
    return response['petfinder']['shelters']['shelter']
