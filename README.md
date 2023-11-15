# QuickPat

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

### read.py
Makes a sample call to openai to generate an abstract

### rag.py
Searches the index for other abstracts that match the search query abstract.
