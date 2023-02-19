from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://long-sleek-general.discover.quiknode.pro/28ad22d49d2b80ccd2ca4dcf0346d5814f950346/"))
block=w3.eth.get_block('latest') # get latest block details
block_number=w3.eth.blockNumber # get latest block number
accounts=w3.eth.accounts
test=w3.eth.filter({'address': '0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B'})
#get_transaction_by_block("latest",1)
#get_transaction(block['transactions'][1])
#w3.eth.get_block_transaction_count('latest')
#w3.eth.get_code("0x6f9e2777D267FAe69b0C5A24a402D14DA1fBcaA1")
print(block_number)
print(test)