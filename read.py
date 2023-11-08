import bs4
import patentparser
import openaiapi

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

# Open AI API parameters
temp_value = 1
max_tokens_value = 256
top_p_value = 1
frequency_penalty_value = 0
presence_penalty_value = 0

abstract_prompt = 'Generate a patent abstract from the provided claim that is suitable for use in a patent application. In the abstract, do not make reference to itself, or the words "abstract", "invention", "patent", "patent application", or "document". Avoid discussing the advantages or improvements of what is described. Use simple and plain language, but avoid using slang. Limit the abstract to 150 words.'

for patent in patents[:5]:
    print("--------------------------------------------------")
    # print(patent)

    api_response = openaiapi.sendAPIRequest(abstract_prompt, patent.abstract, temp_value, max_tokens_value, top_p_value, frequency_penalty_value, presence_penalty_value)
    generated_abstract = api_response.choices[0].message.content

    print('Ground truth abstract: ', patent.abstract)
    print('Generated abstract: ' , generated_abstract)

print(len(patents))
