import json
import urllib.request
from urllib.error import HTTPError
import requests
import time

def retrieve_sizmek_data(APIObject, isProd, SASPlatformUsername, SASPlatformPassword, SASPlatformAPIkey):
    # First, retrieve the authorization token from the SAS platform
    UATUrl = 'https://adapi.uat.sizmek.com'
    ProdUrl= 'https://adapi.sizmek.com'
    loginAPIendpoint = '/sas/login/login'
    loginUrl = (ProdUrl+loginAPIendpoint) if isProd else (UATUrl+loginAPIendpoint)
    payload = {"username": SASPlatformUsername, "password": SASPlatformPassword}
    params = json.dumps(payload).encode('utf8')
    req = urllib.request.Request(loginUrl, data = params, headers = {'content-type': 'application/json', 'api-key': SASPlatformAPIkey})
    response = urllib.request.urlopen(req)
    decodedResponse = response.read().decode('utf8')
    responseAsJson = json.loads(decodedResponse)
    authToken = responseAsJson["result"]["sessionId"] ## here you are the authorization

    # Then, use the Report Builder API to create a report
    APIObjectAsJson = json.dumps(APIObject).encode('utf8')
    saveAndExecUrlUAT = "https://api.uat.dev.sizmek.com/rest/ReportBuilder/reports/saveAndExecute"
    saveAndExecUrlProd =  "https://api.sizmek.com/rest/ReportBuilder/reports/saveAndExecute"
    saveAndExecUrl = saveAndExecUrlProd if isProd else saveAndExecUrlUAT
    req = urllib.request.Request(saveAndExecUrl, data = APIObjectAsJson, headers = {'Authorization': authToken,'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    responseAsJson = json.loads(response.read().decode('utf8'))
    executionID = responseAsJson["result"]["executionID"]
    print("executionID: " + executionID)

    # Finally, query the Report Builder API every few minutes to check if your report is available
    getExecutionUrlUAT = "https://adapi.uat.sizmek.comuat.dev.sizmek.com/rest/ReportBuilder/reports/executions/" + executionID
    getExecutionUrlProd = "https://api.sizmek.com/rest/ReportBuilder/reports/executions/" + executionID
    getExecutionUrl = getExecutionUrlProd if isProd else getExecutionUrlUAT
    timeoutSec = 3 * 50
    sleepTimeSec = 0
    sleepForSec = 15
    while(sleepTimeSec <= timeoutSec):
        req = urllib.request.Request(getExecutionUrl, 
        headers = {'Authorization': authToken,'content-type': 'application/json', 'api-key': SASPlatformAPIkey})
        response = urllib.request.urlopen(req)
        responseAsJson = json.loads(response.read().decode('utf8'))
        if(responseAsJson["result"]["executionStatus"] == "FINISHED"):
            #print("\nThe report finished successfully")
            #print(responseAsJson)
            break
        else:
            #print("The report is not ready yet. Sleeping for " + str(sleepForSec) + "seconds...")
            #print("Total waiting time is: " + str(sleepTimeSec / 60) + " minutes\n")
            #print(responseAsJson)
            sleepTimeSec += sleepForSec
            time.sleep(sleepForSec)

    if(sleepTimeSec > timeoutSec):
        print("Error: Timeout reached. Waited for " + str(sleepTimeSec / 60) + " minutes but the report is still not ready! Exiting...")
    else:
        print("\n The report finished successfully")# + responseAsJson["result"]["files"][0]["url"])

    return responseAsJson["result"]["files"][0]["url"]