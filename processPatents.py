import bs4
import lib.patentparser as patentparser
import lib.openaiapi as openaiapi
import pandas as pd
import lib.constants as constants

with open(constants.INPUT_FILE, "r") as f:
    xml = f.read()

split_xml = xml.split('<?xml version="1.0" encoding="UTF-8"?>')
split_xml = split_xml # for testing

patents_df = pd.DataFrame(columns=['publ_number', 'title', 'abstract', 'claim_data'])

print("start processing", constants.INPUT_FILE)
patents = []
for single_xml in split_xml:
    if len(single_xml) == 0:
        # not an xml doc
        continue
    soup = bs4.BeautifulSoup(single_xml, "xml")

    if not patentparser.isPatentApplication(soup):
        continue

    publ_number = patentparser.getPublicationNumber(soup)
    # print("publ_number", publ_number)

    title = patentparser.getTitle(soup)
    # print("title", title)

    abstract = patentparser.getAbstract(soup)
    # print("abstract", abstract)

    claim_data = patentparser.getClaimData(soup)
    # print("claim_data", claim_data)

    next_patent = pd.DataFrame([{'publ_number': publ_number, 'title': title, 'abstract': abstract, 'claim_data': claim_data}])
    patents_df = pd.concat([patents_df, next_patent])

print("patents_df", patents_df)

print("writing to file", constants.PROCESSED_FILE)
patents_df.to_parquet(constants.PROCESSED_FILE, index=False)
