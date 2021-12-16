from web3 import Web3

# node connection
alchemy_url = "https://eth-mainnet.alchemyapi.io/v2/vc5yn24LN5SGC2lCl2wY6RkLF_Jt8o1d"

# The following defined web3 function allows us to communicate with the
# blockcain itself
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# My current crypto balance
balance = web3.eth.getBalance("0x7902eD199f5F30251acbD678856891C5c344f8ad")

print(web3.isConnected())
print(web3.eth.blockNumber)
print(web3.fromWei(balance, "ether"))