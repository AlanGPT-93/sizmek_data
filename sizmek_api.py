import pandas as pd
import re
import os
import numpy as np
from datetime import date, datetime, timedelta
#from google.cloud import storage
#from google.oauth2 import service_account
import json
import requests

from set_up import api_config
from retrieve_data import retrieve_sizmek_data


# Configurations. Please change these accordingly. Below is the Documentation to see params for reporting.
# https://developers.sizmek.com/hc/en-us/articles/360037897092-About-the-Reporting-API

def run_sizmek_app():
    ## Set-up variables

    ### Acount Keys
    isProd = True
    sizmek_api_credentials = {"account_id1": ["API.testOne.All", "password1", "apikey1"],
                          "account_id1": ["API.testTwo.All", "password2", "apikey2"]}
    
    ### Currencies and Conversion_metrics_ids
    currencies = {"USD": 1, "MXN": 32}
    conv_tags_ids = {"yes": [1145019, 1145016, 950259, 1145015, 1443179, 1443186, 
    1145022, 1366866, 1443183, 1145021, 1145018, 1145017, 1341282, 950258, 1443185, 
    1443180, 1443182, 950257, 1145023, 1145014, 1145020, 1443181, 1443184], "no": []}

    ### Dates                          
    current_date = date.today()
    start_date = current_date - timedelta(days = 1)
    end_date = current_date - timedelta(days = 0)
    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    ### API config
    account_id = "account_id1"
    currency_id = currencies["MXN"]
    APIObject = api_config(account_id, start_date, end_date, currency_id, conv_tags_ids["yes"])
    SASPlatformUsername, SASPlatformPassword, SASPlatformAPIkey = sizmek_api_credentials[account_id]

    params = {
        "APIObject": APIObject,
        "isProd": isProd,
        "SASPlatformUsername": SASPlatformUsername, 
        "SASPlatformPassword": SASPlatformPassword, 
        "SASPlatformAPIkey": SASPlatformAPIkey
    }
    ### Calling Sizmek API
    link_json =  retrieve_sizmek_data(**params)
    data_json = requests.get(link_json)
    data_json = json.loads(data_json.text)
    print(data_json )


if __name__ == "__main__":
    run_sizmek_app()
