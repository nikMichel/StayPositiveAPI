# StayPositiveAPI

## Description

StayPositiveAPI is a simple API that allows you stay positive!

Specifically, the end–user wants to provide an English sentence that has a blank or missing part, 
and receive text suggestions that can fill in the blank in a way that makes the sentence sound positive.

Examples:

Input: have a <blank> day
Output: good, excellent, amazing

Input: the application was <blank>
Output: well designed, so pretty, the best I’ve ever seen

## Usage

We need to send a HTTP POST Request to the the API , with JSON Data in the body with the following schema.

The Phrase should include a `<blank>` where we want the API to return a wword suggestion with a positive sentiment.


## Project Structure

```
.
├── Dockerfile
├── README.md
├── app.py
└── classifier.py
└── mlm.py
└── requirements.txt
└── tests
    └── testPostiveRequest.py
```

## API Endpoints

There are three API endpoints exposed

`/mlmmodel` - This will return the Pretrained model used on rthe English language using a masked language modeling (MLM) objective.

`/all` - This will return the suggestions regardless of sentiment.

`/positive` - This will return only suggestion with a postive sentiment.


## Local Deployment

The local deployment is based on Docker. Thus, to correctly launch our interface, the Docker software must be installed. The deployment is outlined below.

### Clone the Repository

```
git clone https://github.com/nikMichel/StayPositiveAPI.git
```

### Download models

### Build the Docker Image

You need to build the Docker Image based on this repository Dockerfile. To do so, you can use the following command.

`docker build -t {TAG} .`

`{TAG}` is the name you want to give your Docker Image.

### Build the Docker Image

Run the Docker Conatiner based on the Docker Image you just built.

`docker run -d -p 80:8000 {TAG}`


## Logging

Logging has been configured to log to the `staypostiveapi.log` file in project directory.

## Example Usage

### Test script

In the `tests` directory there is the `testPostiveRequest.py` file that we can use to test that the API is working

When run we should get the following response


```{"input": "It would be <blank> to work for Persado"}
{
  "output": [
    "easy",
    "nice",
    "easier",
    "good"
  ]
}
```

### Manually

We can use `curl` to manually test the API

```curl -X 'POST' \
  'http://localhost/positive/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "It would be <blank> to work at Persado"
}'
```
