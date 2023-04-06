import requests
from dotenv import load_dotenv
load_dotenv()
import os

DappRadar_URL = "https://api.dappradar.com/4tsxo4vuhotaojtl/dapps"
X_BLOBR_KEY= os.environ.get("DappRadar_API_KEY")

### Returns the list of chains supported by DappRadar
def get_supported_chains():
    request_URL = DappRadar_URL+ "/chains"
    headers = {
    "X-BLOBR-KEY": X_BLOBR_KEY
    }

    response = requests.get(request_URL, headers=headers).json()
    print(type(response))
    
    chains=response["chains"]
    print(chains)
    return chains

### Retuns app info, using DappRadar ids' system
def get_apps_by_id(app_id=None):
    headers = {
    "X-BLOBR-KEY": X_BLOBR_KEY
    }
    if app_id:
        request_URL = DappRadar_URL+"/"+str(app_id) ### access ["results"]
    else:
        request_URL = DappRadar_URL
    response = requests.get(request_URL, headers=headers).json()

    print(response)
    return response

def get_apps_by_chain(chain_name=None):
    headers = {
    "X-BLOBR-KEY": X_BLOBR_KEY
    }
    if chain_name:
        params={"chain":chain_name}
        request_URL = DappRadar_URL ### access ["results"]
        response = requests.get(request_URL, headers=headers,params=params)
    else:
        response = requests.get(request_URL, headers=headers)
    #print(response.text.encode("utf-8"))
    return response.json()


def main():
    res=get_apps_by_chain("solana")["results"]
    #get_apps_by_id(3)


main()