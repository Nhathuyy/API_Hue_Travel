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

-macos

source venv/bin/activate


-win 

venv\Scripts\activate



3. Install the required packages:

pip install -r requirements.txt


## Configuration

1. Rename the `.env.example` file to `.env`.

2. Open the `.env` file and update the MongoDB connection URL and any other configuration options as needed.

## Usage

1. Start the MongoDB server.

2. Run the FastAPI application:

uvicorn index:app --reload
## Description Json
{
  "id": "001",
  "name": " Đại Nội",
  "link": "https://goo.gl/maps/VQUdsy56dg2DqbSQ6"
}

## User Json
{
  "name": "Nhat Huy",
  "age": 22,
  "email": "NhatHuy@email.com",
  "numberofpp": 4,
  "amount": "10,000,000",
  "interest": " Di Sản Văn Hoá, Trải Nghiệm Mới",
  "ngay_di": "2023-06-10",
  "ngay_den": "2023-06-15"
  "destinations": [
    {
      "id": "001",
      "name": " Đại Nội",
      "link": "https://goo.gl/maps/VQUdsy56dg2DqbSQ6"
    },
    {
      "id": "002",
      "name": "Chùa Thiên Mụ",
      "link": "https://goo.gl/maps/nnsMtcifv9tV6zMC9"
    }
  ]
}
##Journey  

{
  "id": 1,
  "user_id": "6481d5ab80f1f56025f1dc9f",
  "destination_ids": ["001", "002", "003"]
}

