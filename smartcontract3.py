from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

#similar to a username of an account
account_1 = "0x948896D461D50b0BFA909D279ED316428cFa943D"
account_2 = "0xb15a49d4E3f3EB8eB66e7361823AE36CCBA1E8A0"

#acts as the password to the account
private_key = "4a05d2154e153ee928bc0ed1a0c14db0d0248e52f2f6f3a05feb924ce3113da4"

# get the nonce: prevents from sending the same transaction twice
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    # wei is the penny to cryptocurrencies, so to speak
    'value': web3.toWei(1, 'ether'),
    # maximum payout to miners
    'gas': 2000000,
    # gwei is a bigger unit of measurement
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(tx_hash)

# shows transaction hash by its address
print(web3.toHex(tx_hash))