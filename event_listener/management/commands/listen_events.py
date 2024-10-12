from web3 import Web3
from django.core.management.base import BaseCommand
from event_listener.models import TransferEvent
from event_listener.infura import get_web3

# BAYC's Ethereum contract address
BAYC_CONTRACT_ADDRESS = '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'

# We're only interested in the 'Transfer' event, so here's the minimal ABI for that
TRANSFER_EVENT_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "from", "type": "address"},
            {"indexed": True, "name": "to", "type": "address"}, 
            {"indexed": True, "name": "tokenId", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"      
    }
]

class Command(BaseCommand):
    """
    This script listens for BAYC NFT transfer events on Ethereum 
    and saves them to the local SQLite database.
    """
    help = 'Listens for BAYC NFT transfers and saves them in the database.'

    def handle(self, *args, **kwargs):
        """
        Core logic for fetching and processing events.
        Connects to Ethereum, grabs past events, and keeps an ear out for new ones.
        """
       
        web3 = get_web3()
        checksummed_address = Web3.to_checksum_address(BAYC_CONTRACT_ADDRESS)
        contract = web3.eth.contract(address=checksummed_address, abi=TRANSFER_EVENT_ABI)

        print("Connected to contract: ", contract)

        try:
            latest_block = web3.eth.block_number

            event_filter = contract.events.Transfer.create_filter(from_block=latest_block - 10, to_block='latest')

            for event in event_filter.get_all_entries():
                self.process_event(event)

            while True:
                new_events = event_filter.get_new_entries()
                for event in new_events:
                    self.process_event(event)

        except Exception as e:
            print(f"Error: {str(e)}")

    def process_event(self, event):
        """
        Takes an event, pulls out the important bits, and saves it to the database.
        """
        token_id = event['args']['tokenId'] 
        from_address = event['args']['from'] 
        to_address = event['args']['to'] 
        transaction_hash = event['transactionHash'].hex() 
        block_number = event['blockNumber'] 

        # Save the event details to the database 
        transfer_event = TransferEvent(
            token_id=token_id,
            from_address=from_address,
            to_address=to_address,
            transaction_hash=transaction_hash,
            block_number=block_number
        )
        transfer_event.save()

        print(f'Saved Transfer: Token ID {token_id} | From {from_address} | To {to_address}')
