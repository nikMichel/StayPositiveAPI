from transformers import BertTokenizer, TFBertForMaskedLM, pipeline
import tensorflow as tf
import numpy as np

mask_model = "bert-base-uncased"
mask_model_path = "models/" + mask_model + "/"
#mask_model = "distilbert/distilbert-base-uncased"
#classify_model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
#tokenizer = BertTokenizer.from_pretrained(mask_model)
#model = TFBertForMaskedLM.from_pretrained(mask_model)

tokenizer = BertTokenizer.from_pretrained(mask_model_path, local_files_only=True)
model = TFBertForMaskedLM.from_pretrained(mask_model_path, local_files_only=True)


def getTopNumOfPredictions(input_string, k=5, tokenizer=tokenizer, model=model) -> str:
    """
    This function uses the model to get a list of suggested works, limited by k taht could be used to relace the [MASK]
      
    """
    tokenized_inputs = tokenizer(input_string, return_tensors="tf")
    outputs = model(tokenized_inputs["input_ids"])
    top_k_indices = tf.math.top_k(outputs.logits, k).indices[0].numpy()
    decoded_output = tokenizer.batch_decode(top_k_indices)
    mask_token = tokenizer.encode(tokenizer.mask_token)[1:-1]
    mask_index = np.where(tokenized_inputs['input_ids'].numpy()[0]==mask_token)[0][0]
    decoded_output_words = decoded_output[mask_index]
    return decoded_output_words