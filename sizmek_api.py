import pandas as pd
import re
import os
import numpy as np
from datetime import date, datetime, timedelta
#from google.cloud import storage
#from google.oauth2 import service_account
import json
import requests

from retrieve_data import retrieve_sizmek_data
from set_up import api_config

# Configurations. Please change these accordingly. Below is the Documentation to see params for reporting.
# https://developers.sizmek.com/hc/en-us/articles/360037897092-About-the-Reporting-API

def run_sizmek_app():
    isProd = True
    sizmek_api_credentials = {"account_id1": ["API.testOne.All", "password1", "apikey1"],
                          "account_id1": ["API.testTwo.All", "password2", "apikey2"]}
                          
    current_date = date.today()
    account_id = "account_id1" 

    start_date = current_date - timedelta(days = 1)
    end_date = current_date - timedelta(days = 0)

    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    APIObject = api_config(account_id, start_date, end_date)

    SASPlatformUsername, SASPlatformPassword, SASPlatformAPIkey = sizmek_api_credentials[account_id]

    params = {
        "APIObject": APIObject,
        "isProd": isProd,
        "SASPlatformUsername": SASPlatformUsername, 
        "SASPlatformPassword": SASPlatformPassword, 
        "SASPlatformAPIkey": SASPlatformAPIkey
    }
   
    link_json =  retrieve_sizmek_data(**params)
    data_json = requests.get(link_json)
    data_json = json.loads(data_json.text)
    print(data_json )


if __name__ == "__main__":
    run_sizmek_app()
