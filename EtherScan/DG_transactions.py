from dotenv import load_dotenv
load_dotenv()
import os
import requests

API_KEY = os.environ.get('EtherScan_API_KEY')

URL= f"https://api.etherscan.io/api\
?module=account\
&action=tokennfttx\
&contractaddress=0x48Be0965618ED7B65E577487e1f74f12aca74ef7\
&page=1\
&offset=100\
&startblock=0\
&endblock=27025780\
&sort=desc\
&from=0x130BD65a7401C053015fbd143798B298874E3785\
&apikey={API_KEY}"

print(requests.get(URL).json())
