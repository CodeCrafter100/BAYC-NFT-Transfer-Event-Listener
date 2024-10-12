from web3 import Web3

INFURA_PROJECT_ID = 'dbd45933e311406ba6a847a304cf7cd4'

def get_web3():
    infura_url = f'https://mainnet.infura.io/v3/dbd45933e311406ba6a847a304cf7cd4'
    web3 = Web3(Web3.HTTPProvider(infura_url))
    if not web3.is_connected():
        raise ConnectionError("Failed to connect to Infura")
    return web3

