import bs4
import patentparser

# this is a test (TOC)

with open("ipa200102.xml", "r") as f:
    xml = f.read()

split_xml = xml.split('<?xml version="1.0" encoding="UTF-8"?>')
split_xml = split_xml[:100] # for testing

class Patent:
    def __init__(self, publ_number, abstract, claims):
        self.publ_number = publ_number
        self.abstract = abstract
        self.claims = claims

    def __str__(self):
        return f"Publication Number: {self.publ_number}\nAbstract: {self.abstract}\nClaims: {self.claims}"

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

    abstract = patentparser.getAbstract(soup)
    # print("abstract", abstract)

    claim_data = patentparser.getClaimData(soup)
    # print("claim_data", claim_data)

    patents.append(Patent(publ_number, abstract, claim_data))

for patent in patents[:5]:
    print("--------------------------------------------------")
    print(patent)

print(len(patents))
