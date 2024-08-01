#import numpy as np
import re
#import torch
import json
from transformers import BertTokenizer, TFBertForMaskedLM, pipeline
#import tensorflow as tf
from fastapi import FastAPI, Body
from pydantic import BaseModel, validator
import mlm
import classifier
from mlm import getTopNumOfPredictions
from classifier import classifyIfPositive
import logging

logging.basicConfig(level=logging.ERROR, filename='staypostiive_access.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%dT%H:%M:%SZ")
logger = logging.getLogger(__name__)



# Specify model
#mask_model = "bert-base-uncased"
#classify_model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

description = """
StayPositiveAPI is a simple API that allows you stay positive!


You will be able to:


* **Send a request with a sentence, and a blank where you would like a list of only positive responses.**.
"""

#validation
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

#tokenizer = BertTokenizer.from_pretrained(mask_model)
#model = TFBertForMaskedLM.from_pretrained(mask_model)

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
      output = getTopNumOfPredictions(text)
      positive_only = classifyIfPositive(output)
      logger.info(f"output: {positive_only}")
      return {"output": positive_only}
    except Exception as e:
      logger.error("Was unable to get postive suggestions")

    
@app.post('/all/', tags=["all"])
async def allResponses(input: Input):
    """ Returns the list of all suggested words """
    try:
      json_input = json.loads(input.json())
      text = (json_input['input'])
      text = re.sub(r"<blank>", "[MASK]", text)
      text = re.sub("\[MASK\]$", "[MASK].", text)
      logger.info(f"input: {text}")
      all_responses = getTopNumOfPredictions(text)
      logger.info(f"output: {all_responses}")
      return {"output": all_responses}
    except Exception as e:
      logger.error("Was unable to get any suggestions")


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("app:app", reload=True, port=8000, host="0.0.0.0")

#def get_top_k_predictions(input_string, k=5, tokenizer=tokenizer, model=model) -> str:
#    """
#    This function uses the model to get a list of suggested works, limited by k taht could be used to relace the [MASK]
#      
#    """
#    tokenized_inputs = tokenizer(input_string, return_tensors="tf")
#    outputs = model(tokenized_inputs["input_ids"])
#    top_k_indices = tf.math.top_k(outputs.logits, k).indices[0].numpy()
#    decoded_output = tokenizer.batch_decode(top_k_indices)
#    mask_token = tokenizer.encode(tokenizer.mask_token)[1:-1]
#    mask_index = np.where(tokenized_inputs['input_ids'].numpy()[0]==mask_token)[0][0]
#    decoded_output_words = decoded_output[mask_index]
#    return decoded_output_words


#def classifyIfPositive(output):
#    """
#    This function returns only words that have a POSITIVE label
#      
#    """
#    #print(output)
#    positive_only = [] 
#    output_list = list(output.split(" "))
#    #print(output_list)

#    classifier = pipeline("sentiment-analysis", model=classify_model)
#    for word in output_list:
#       sent = classifier(word)
#       #print(word)
#       if sent[0]['label'] == "POSITIVE":
#           #print(f"{word} is postive!")
#           positive_only.append(word)
#           #print(positive_only)
#    
#    return positive_only
