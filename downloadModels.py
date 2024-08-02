#!/usr/bin/env python3

from transformers import BertTokenizer, TFBertForMaskedLM, pipeline
import os

mask_model = "bert-base-uncased"
classify_model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

def downloadMLMModel(model_path, model_name):
    """Download a Hugging Face model and tokenizer to the specified directory"""
    try:
       # Check if the directory already exists  
      if not os.path.exists(model_path):
        # Create the directory
        os.makedirs(model_path)
    except Exception as e:
        print(f"Was unable to create directory { model_path } for model { model_name }")

    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = TFBertForMaskedLM.from_pretrained(model_name)

    # Save the model and tokenizer to the specified directory
    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)

def downloadClassifierModel(model_path, model_name):
    """Download a Hugging Face model for Sentiment Analysis"""
    try:
      # Check if the directory already exists  
      if not os.path.exists(model_path):
        # Create the directory
        os.makedirs(model_path)
    except Exception as e:
        print(f"Was unable to create directory { model_path } for model { model_name }")

    classifier = pipeline(model=model_name)

    # Save the model and tokenizer to the specified directory
    classifier.save_pretrained(model_path)


downloadMLMModel('models/' + mask_model, 'bert-base-uncased')
downloadClassifierModel('models/' + classify_model, classify_model)


tokenizer = BertTokenizer.from_pretrained('models/' + mask_model, local_files_only=True)
model = TFBertForMaskedLM.from_pretrained('models/' + mask_model, local_files_only=True)
classifier = pipeline('sentiment-analysis', model='models/' + classify_model, local_files_only=True)

