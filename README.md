# StayPositiveAPI

## Description

StayPositiveAPI is a simple API that allows you stay positive!

Specifically, it is an API that provides positive suggestions to a phrase submitted by the end-user.

Examples:

Input: Today was a <blank> day
Output: good, excellent, amazing

Input: the food was <blank>
Output: good, delicious, amazing, great,



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

`/mlmmodel` (method: GET): This will return the Pretrained model used on the English language using a masked language modeling (MLM) objective.

`/all` (method: POST, response: JSON String): This will return suggestions regardless of sentiment. Body must be a JSON object with the following property:
    
    `input` (string, required): The phrase or sentence we want to retrieve the all suggested words. Must contain a `<blank>` where we reuired the suggested word.
                                   
`/positive` (method: POST, response JSON List): This will return only suggestions with a postive sentiment. Body must be a JSON object with the following property:

    `input` (string, required): The phrase or sentence we want to retrieve the all suggested words. Must contain a `<blank>` where we reuired the suggested word.


### Examples

Postiive only suggestions

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

The local deployment is based on Docker. Therefore, to correctly launch the API Service, Docker software must be installed. The deployment is outlined below.

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

Logging has been configured to log to the `staypositive_access.log` file.


## Test scripts

In the `tests` directory there are two scripts that can be use to test the API.

- `testPostiveRequest.py` Used to test Positive only responses, that is the `/positive` API endpoint.
- `testAllRequest.py` Used to test All responses, that is the `/all` API endpoint


When run the `testPostiveRequest.py` script, we should a response similar to the following

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

When run the `testAllRequest.py` script, we should a response similar to the following

```{"input": "It would be <blank> to work at Persado"}
{
  "output": "nice good easy great easier"
}
```
