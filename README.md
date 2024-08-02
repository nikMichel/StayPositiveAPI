# StayPositiveAPI

## Description

StayPositiveAPI is a simple API that allows stay positive by getting only positive word suggestions!

Specifically, it is an API that provides positive suggestions to a phrase submitted by the end-user.

Examples:

 - Input: Today was a '<blank>' day
 - Output: good, excellent, amazing

 - Input: the food was "<blank>"
 - Output: good, delicious, amazing, great,



## Project Structure

```
.
├── Dockerfile
├── README.md
└── requirements.txt
└── src
    └── app.py
    └── classifier.py
    └── downloadModels.py
    └── mlm.py
└── tests
    └── testPostiveRequest.py
    └── testAllRequest.py
```

## API Endpoints

There are three API endpoints exposed

1. `/mlmmodel` (method: GET, response: JSON String): This will return the Pretrained model used on the English language using a masked language modeling (MLM) objective.

2. `/all` (method: POST, response: JSON String): This will return suggestions regardless of sentiment (maximum 5). Body must be a JSON object with the following property:
    
     - `input` (string, required): The phrase or sentence we want to retrieve all suggested words. Must contain a `<blank>` in place where we require the suggested word.
                                   
3. `/positive` (method: POST, response JSON List): This will return only suggestions with a positive sentiment (maximum 5). Body must be a JSON object with the following property:

     - `input` (string, required): The phrase or sentence we want to retrieve a suggested word with positive sentiment. Must contain a `<blank>` in place we require the suggested positive word.


### Examples

Recieve only positive suggestions

Request:

```
curl -X 'POST' \
  'http://127.0.0.1/positive/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "It would be <blank> to work at Persado"
}'
```

Response:

`{"output":["nice","good","easy","great","easier"]}`


Recieve all suggestions

```
curl -X 'POST' \
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

### Build the Docker Image

You need to build the Docker Image based on this repository Dockerfile. To do so, you can use the following command. Change into the `StayPosiiveAPI` directory created.

`sudo docker build -t {IMAGE_TAG} .`

`{IMAGE_TAG}` is the name you want to give your Docker Image.

Example: `sudo docker build -t staypositiveapi .`

### Build the Docker Image

Run the Docker Conatiner based on the Docker Image name you just built.

`sudo docker run -d --name {CONTAINER_NAME} -p 80:8000 {TAG}`

Example:

`sudo docker run -d --name staypositive --rm -p 80:8000 staypositiveapi`

### Check Container status

We then should be able to see the Container running using the `docker ps` command.

`sudo docker ps`

Example:

```
sudo docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                                   NAMES
440d7aec7b48   staypositiveapi   "uvicorn app:app --h…"   3 minutes ago   Up 3 minutes   0.0.0.0:80->8000/tcp, :::80->8000/tcp   staypositive
```

### Use Docker Compose

An simple `docker-compose.yml` file could be like the following:

```
version: '3'
services:
 staypositive:
  image: staypositiveapi
  container_name: staypositive
  ports:
   - "80:8000"
```



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
