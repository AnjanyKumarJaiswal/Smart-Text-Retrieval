import torch
import os
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

my_hf_key = os.getenv('hf_api_key')


model_id = 'facebook/bart-large-cnn'

def load_summarizer(model_id=model_id):
    if torch.cuda.is_available():
        device = torch.device('cuda:0')
    else:
        device = torch.device('cpu')
    
    try:
        print("starting pipeline model!")
        summarizer = pipeline('summarization', model=model_id , device=device)
        print("Completed pipeline model! :)")
    except:
        print("Did not load the model!! :(")
    return summarizer
    
