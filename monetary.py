from requests import get
from constants import monetary_api_latest

def list_idvariables():
    return get(monetary_api_latest).json()

print(list_idvariables())
