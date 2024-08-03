from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from nltk.tokenize import sent_tokenize
import nltk
import math

# Download the Punkt tokenizer models for sentence splitting
nltk.download('punkt')

# Azure Text Analytics setup
key = "YOUR_AZURE_KEY"
endpoint = "YOUR_AZURE_ENDPOINT"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return client

client = authenticate_client()

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def analyze_sentiment(client, sentences):
    # Process in batches of 10
    batch_size = 10
    num_batches = math.ceil(len(sentences) / batch_size)
    
    for i in range(num_batches):
        batch = sentences[i*batch_size:(i+1)*batch_size]
        response = client.analyze_sentiment(documents=batch)
        
        for idx, document in enumerate(response):
            print(f"Document {i*batch_size + idx + 1} Sentiment: {document.sentiment}")
            print(f"Overall scores: positive={document.confidence_scores.positive:.2f}; neutral={document.confidence_scores.neutral:.2f}; negative={document.confidence_scores.negative:.2f} \n")
            
            for j, sentence in enumerate(document.sentences):
                print(f"Sentence: {sentence.text}")
                print(f"Sentence {j+1} sentiment: {sentence.sentiment}")
                print(f"Sentence score: positive={sentence.confidence_scores.positive:.2f}; neutral={sentence.confidence_scores.neutral:.2f}; negative={sentence.confidence_scores.negative:.2f} \n")

def main(file_path):
    # Read the content from file
    content = read_file(file_path)
    
    # Split the content into sentences
    sentences = sent_tokenize(content)
    
    # Analyze sentiment for each sentence in batches
    analyze_sentiment(client, sentences)

# Path to your text file
file_path = 'sample_reviews.txt'  # Update with the path to your text file

main(file_path)
