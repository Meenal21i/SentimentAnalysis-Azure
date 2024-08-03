
# Sentiment Analysis Project

## Project Overview

This project performs sentiment analysis on text data using the Azure Text Analytics API. The sentiment of each sentence in the provided text file is analyzed to determine if it is positive, neutral, or negative. The script processes the text file, splits it into sentences, and uses the Azure API to analyze the sentiment of each sentence in batches.

## Setup Instructions

### 1. Obtain API Keys

1. Sign up for an Azure account if you don’t have one.
2. Create a Text Analytics resource in the Azure portal.
3. Retrieve your API key and endpoint URL from the Azure portal.

### 2. Set Environment Variables

To securely manage your API keys, set the following environment variables:

- **On Windows:**
  ```bash
  set AZURE_KEY=your_api_key_here
  set AZURE_ENDPOINT=your_endpoint_here
  ```

- **On macOS/Linux:**
  ```bash
  export AZURE_KEY=your_api_key_here
  export AZURE_ENDPOINT=your_endpoint_here
  ```

### 3. Install Dependencies

Ensure you have the required Python libraries installed. You can install them using pip:

```bash
pip install azure-ai-textanalytics nltk
```

### 4. Download NLTK Data

The script uses the NLTK library to split text into sentences. Download the necessary data:

```python
import nltk
nltk.download('punkt')
```

## Usage Instructions

1. **Prepare Your Input File**

   Create a text file (e.g., `sample_reviews.txt`) containing the text you want to analyze. Ensure the file is in the same directory as your script or update the path accordingly.

2. **Run the Script**

   Save the following script as `sentiment_analysis.py`:

   ```python
   import os
   from azure.ai.textanalytics import TextAnalyticsClient
   from azure.core.credentials import AzureKeyCredential
   from nltk.tokenize import sent_tokenize
   import nltk
   import math

   # Download the Punkt tokenizer models for sentence splitting
   nltk.download('punkt')

   # Azure Text Analytics setup
   key = os.getenv("AZURE_KEY")  # Fetch key from environment variable
   endpoint = os.getenv("AZURE_ENDPOINT")  # Fetch endpoint from environment variable

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
       content = read_file(file_path)
       sentences = sent_tokenize(content)
       analyze_sentiment(client, sentences)

   # Path to your text file
   file_path = 'sample_reviews.txt'  # Update with the path to your text file

   main(file_path)
   ```

3. **Execute the Script**

   Run the script from your terminal:

   ```bash
   python sentiment_analysis.py
   ```

   Ensure that your environment variables are set correctly and the input file is in the specified path.

---

Feel free to adjust the details according to your specific setup and requirements. If you need any more help, just let me know!
