# API_Hue_Travel

## FastAPI with MongoDB

This is a simple example of a FastAPI application using MongoDB as the database.

## Prerequisites

- Python 3.7 or above
- MongoDB installed and running

## Installation

1. Clone the repository:
git clone https://github.com/Nhathuyy/API_Hue_Travel


2. Create a virtual environment:

python3 -m venv venv
source venv/bin/activate


3. Install the required packages:

pip install -r requirements.txt


## Configuration

1. Rename the `.env.example` file to `.env`.

2. Open the `.env` file and update the MongoDB connection URL and any other configuration options as needed.

## Usage

1. Start the MongoDB server.

2. Run the FastAPI application:

uvicorn main:app --reload
