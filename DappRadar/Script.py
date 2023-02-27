import requests
from dotenv import load_dotenv
load_dotenv()
import os

DappRadar_URL = "https://api.dappradar.com/4tsxo4vuhotaojtl/dapps/"
X_BLOBR_KEY= os.environ.get("DappRadar_KEY")

### Returns the list of chains supported by DappRadar
def get_supported_chains():
    request_URL = DappRadar_URL+ "chains"
    headers = {
    "X-BLOBR-KEY": X_BLOBR_KEY
    }

    response = requests.get(request_URL, headers=headers).json()
    print(type(response))
    
    chains=response["chains"]
    print(chains)
    return chains

### Retuns app info, using DappRadar ids' system
def get_apps_by_id(app_id):
    request_URL = DappRadar_URL+str(app_id)
    headers = {
    "X-BLOBR-KEY": X_BLOBR_KEY
    }

    response = requests.get(request_URL, headers=headers).json()

    print(response["results"])

def main():
    get_apps_by_id(4000)


main()