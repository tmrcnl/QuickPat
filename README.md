# QuickPat

QuickPat generates an abstract and additional claims for use in a patent application, based on a single human-authored claim that defines what is new and inventive about the invention.

## Data source
https://bulkdata.uspto.gov/data/patent/application/redbook/fulltext/2020/

## Some commands
- pip install beautifulsoup4
- pip install lxml
- pip install openai

- python read.py

## Project Scripts
### processPatents.py
Processes the raw patent file (xml) into a pandas dataframe with the fields we're interested in.

### indexPatents.py
Reads back the dataframe, encodes each abstract, then indexes into a vector db. The vector db is [FAISS](https://faiss.ai/index.html).

### generateAbstracts.py
Generates some abstracts using GPT4 and writes it to a csv file.

### evaluateAbstracts.py
Evaluates the generated abstracts from previous step using cosine similarity and euclidean distance.

### rag.py
Searches the index for other abstracts that match the search query abstract.

### generateClaims.py
Based on an input claim and claims of similar-abstract applications, generates additional claims using GPT4 and writes to a csv file.
