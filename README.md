# StayPositiveAPI

## Description

StayPositiveAPI is a simple API that allows you stay positive!

Specifically, the end–user wants to provide an English sentence that has a blank or missing part, 
and receive text suggestions that can fill in the blank in a way that makes the sentence sound positive.

## Project Structure

```
.
├── Dockerfile
├── README.md
├── app.py
└── requirements.txt
└── tests
    └── testPostiveRequest.py
```

## Local Deployment

The local deployment is based on Docker. Thus, to correctly launch our interface, the Docker software must be installed. The deployment is outlined below.

### Clone the Repository

```
git clone https://github.com/nikMichel/StayPositiveAPI.git
```

### Download models

### Build the Docker Image


## Testing

### Ready script

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

