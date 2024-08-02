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

- `/mlmmodel` (method: GET): This will return the Pretrained model used on rthe English language using a masked language modeling (MLM) objective. (GET)

- `/all` (method: POST): This will return suggestions regardless of sentiment. Returns JSON string object. Must be a JSON object with the following property:
    
    - `input` (string, required): The phrase or sentence we want to retrieve the all suggested words. Must contain a `<blank>` where we reuired the suggested word.
                                   
- `/positive` (method: POST): This will return only suggestions with a postive sentiment. Returns JSON list object. Must be a JSON object with the following property:

    - `input` (string, required): The phrase or sentence we want to retrieve the all suggested words. Must contain a `<blank>` where we reuired the suggested word.


### Examples

Postive only suggestions

Request:

```curl -X 'POST' \
  'http://127.0.0.1/positive/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "It would be <blank> to work at Persado"
}'
```

Response:

`{"output":["nice","good","easy","great","easier"]}`


All suggestions

```curl -X 'POST' \
  'http://192.168.230.120/all/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "It would be <blank> to work at Persado"
}'
```

Response:

`{"output":"nice good easy great easier"}`


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


## Test scripts

In the `tests` directory there is the `testPostiveRequest.py` file that we can use to test that the API is working

When run we should a response similr to the following


```{"input": "It would be <blank> to work at Persado"}
{
  "output": [
    "easy",
    "nice",
    "easier",
    "good"
  ]
}
```

We can use `curl` to manually test the API

```ccurl -X 'POST' \
  'http://127.0.0.1/positive/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "It would be <blank> to work at Persado"
}'
```

And we should get a response similar to the following:

```{"output":["nice","good","easy","great","easier"]}```