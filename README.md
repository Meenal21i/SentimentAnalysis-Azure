
# Sentiment Analysis Project

## Project Overview

This project performs sentiment analysis on text data using the Azure Text Analytics API. The sentiment of each sentence in the provided text file is analyzed to determine if it is positive, neutral, or negative. The script processes the text file, splits it into sentences, and uses the Azure API to analyze the sentiment of each sentence in batches.

## Setup Instructions

### 1. Obtain API Keys

1. Sign up for an Azure account if you don’t have one.
2. Create a Text Analytics resource in the Azure portal.
3. Retrieve your API key and endpoint URL from the Azure portal.


### 2. Install Dependencies

Ensure you have the required Python libraries installed. You can install them using pip:

```bash
pip install azure-ai-textanalytics nltk
```

### 3. Download NLTK Data

The script uses the NLTK library to split text into sentences. Download the necessary data:

```python
import nltk
nltk.download('punkt')
```

## Usage Instructions

1. **Prepare Your Input File**

   Create a text file (e.g., `sample_reviews.txt`) containing the text you want to analyze. Ensure the file is in the same directory as your script or update the path accordingly.

2. **Run the Script**

   Provided code

3. **Execute the Script**

   Run the script from your terminal:

   ```bash
   python sentiment_analysis.py
   ```

   Ensure that your environment variables are set correctly and the input file is in the specified path.

---

Feel free to adjust the details according to your specific setup and requirements. If you need any more help, just let me know!
