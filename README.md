# BAYC NFT Transfer Event Listener

## Overview

This project is a Django application designed to connect to the Ethereum blockchain via Infura to listen for and record transfer events of Bored Ape Yacht Club (BAYC) NFTs.

## Features

- Connects to Ethereum Mainnet using Infura.
- Listens for BAYC NFT transfer events.
- Stores transfer event details in a SQLite database.
- Provides an API endpoint to retrieve transfer history by token ID.

## Technologies Used

- **Django**: Web framework for building the application.
- **Web3.py**: Library to interact with the Ethereum blockchain.
- **SQLite**: Database for storing transfer events.

## Setup Instructions

### Prerequisites

- Python 3.6 or later
- Django
- Web3.py
- An Infura account (sign up at [Infura](https://infura.io/) to get your Project ID).

### Installation

1. Clone this repository:
   git clone https://github.com/CodeCrafter100/BAYC-NFT-Transfer-Event-Listener.git

2. Navigate into the project directory:

   cd BAYC-NFT-Transfer-Event-Listener

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   - On Windows:
     venv\Scripts\activate

   - On macOS/Linux:
     source venv/bin/activate

5. Install the required packages:

   pip install django web3

6. Update the event_listener/infura.py file with your Infura Project ID.

7. Run database migrations:

python manage.py migrate

8. Run the application:

python manage.py runserver

9. Start the event listener:

python manage.py listen_events

## API Usage

To retrieve the transfer history for a specific token ID, visit:

http://127.0.0.1:8000/events/transfer-history/<token_id>/

Replace <token_id> with the actual token ID you wish to query.

## Assumptions and Simplifications

The project focuses on the core functionality and may not include extensive error handling for all edge cases.
It is assumed that the user has a basic understanding of Django and Ethereum concepts.

## Contribution

Feel free to fork the repository and submit a pull request if you want to contribute!
