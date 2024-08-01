# StayPositiveAPI

## Description

StayPositiveAPI is a simple API that allows you stay positive!

Specifically, the end–user wants to provide an English sentence that has a blank or missing part, 
and receive text suggestions that can fill in the blank in a way that makes the sentence sound positive.

## Project Structure

## Local Deployment

The local deployment is based on Docker. Thus, to correctly launch our interface, the Docker software must be installed. The deployment is outlined below.

### Clone the Repository

### Download models

### Build the Docker Image

## Testing

By running the `tests/testPostiveRequest.py` file we can test the API is working

By running the `python3 tests/testPostiveRequest.py`

Should give us the following response

`{"input": "It would be <blank> to work for Persado"}`
`{`
  `"output": [`
    `"easy",`
    `"nice",`
    `"easier",`
    `"good"`
  `]`
`}`



`curl -X GET http://localhost/model`

`code`


