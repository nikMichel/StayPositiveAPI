#import numpy as np
import re
#import torch
import json
#from transformers import BertTokenizer, TFBertForMaskedLM, pipeline
#import tensorflow as tf
from fastapi import FastAPI, Body
from pydantic import BaseModel, validator
import mlm
import classifier as cl
#from mlm import getTopNumOfPredictions
#from classifier import classifyIfPositive
import logging

logging.basicConfig(level=logging.ERROR, filename='staypostiive_access.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%dT%H:%M:%SZ")
logger = logging.getLogger(__name__)


description = """
StayPositiveAPI is a simple API that allows you stay positive!


You will be able to:


* **Send a request with a sentence, and a blank where you would like a list of only positive responses.**.
"""

class Input(BaseModel):
    input: str

    @validator("input")
    def ensure_blank(cls, v):
        if '<blank>' not in v:
            raise ValueError("You must use <blank> in the sentence.")
        return v

tags_metadata = [
    {
        "name": "positive",
        "description": "Get only positive suggestions.",
    },
    {
        "name": "all",
        "description": "Get all suggestions.",
    },
    {
        "name": "model",
        "description": "Get the current model being used.",
    },
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="StayPositiveAPI",
    description=description,
    version="1.0",
)

@app.get('/mlmmodel', tags=["model"])
async def getModel():
    try:
      logger.info(f"/mlmmodel requested")
      logger.info(f"Returned {mlm.mask_model}")
      return {"MLM Model": mlm.mask_model}
    except Exception as e:
      logger.error("Was unable to get model")
    
@app.post('/postive/', tags=["positive"])
async def positiveResponseOnly(input: Input):
    """ Returns the list of words with positive sentiment """
    try:
      json_input = json.loads(input.json())
      text = (json_input['input'])
      text = re.sub(r"<blank>", "[MASK]", text)
      text = re.sub("\[MASK\]$", "[MASK].", text)
      logger.info(f"input: {text}")
      output = mlm.getTopNumOfPredictions(text)
      positive_only = cl.classifyIfPositive(output)
      logger.info(f"output: {positive_only}")
      return {"output": positive_only}
    except Exception as e:
      logger.error("Was unable to get positive suggestions")

    
@app.post('/all/', tags=["all"])
async def allResponses(input: Input):
    """ Returns the list of all suggested words """
    try:
      json_input = json.loads(input.json())
      text = (json_input['input'])
      text = re.sub(r"<blank>", "[MASK]", text)
      text = re.sub("\[MASK\]$", "[MASK].", text)
      logger.info(f"input: {text}")
      all_responses = mlm.getTopNumOfPredictions(text)
      logger.info(f"output: {all_responses}")
      return {"output": all_responses}
    except Exception as e:
      logger.error("Was unable to get any suggestions")


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("app:app", reload=False, port=8000, host="0.0.0.0")
