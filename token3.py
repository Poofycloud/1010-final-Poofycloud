import json
from web3 import Web3

# node connection
alchemy_url = "https://eth-mainnet.alchemyapi.io/v2/vc5yn24LN5SGC2lCl2wY6RkLF_Jt8o1d"

# The following defined web3 function allows us to communicate with the
# blockcain itself
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# My current crypto balance
balance = web3.eth.getBalance("0x7902eD199f5F30251acbD678856891C5c344f8ad")

# json array that describes what the smart contract looks like
' d'

abi = ""

# address of the deployed smart contract on the blockchain
address = "0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0"