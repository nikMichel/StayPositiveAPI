from transformers import BertTokenizer, TFBertForMaskedLM, pipeline


classify_model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
classify_model_path = "models/" + classify_model + "/"
#print(classify_model_path)
#classifier = pipeline(model='models/distilbert/distilbert-base-uncased-finetuned-sst-2-english', local_files_only=True)
classifier = pipeline("sentiment-analysis", model=classify_model_path)


def classifyIfPositive(output):
    """
    This function returns only words that have a POSITIVE label
      
    """
    #print(output)
    positive_only = [] 
    output_list = list(output.split(" "))
    #print(output_list)

    #classifier = pipeline(model=classify_model)
    for word in output_list:
       sent = classifier(word)
       #print(word)
       if sent[0]['label'] == "POSITIVE":
           #print(f"{word} is postive!")
           positive_only.append(word)
           #print(positive_only)
    
    return positive_only