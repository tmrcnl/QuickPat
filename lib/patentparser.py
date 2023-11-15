import bs4

def getDoctype(soup):
    for item in soup.contents:
        if isinstance(item, bs4.Doctype):
            return item

def isPatentApplication(soup):
    doctype = getDoctype(soup)
    return doctype.find("us-patent-application") >= 0

def getPublicationNumber(soup):
    publ_reference = soup.find("publication-reference")
    publ_number = publ_reference.find("doc-number").text
    return publ_number

def getTitle(soup):
    title = soup.find("invention-title").text
    return title

def getAbstract(soup):
    abstract = soup.find("abstract")
    abstract_text = abstract.text
    return abstract_text.strip()

def getClaimData(soup):
    claims = soup.find('claims')
    claim_data = []

    # go through each claim
    for claim in claims:
        text = claim.get_text().strip()
        if text:
            claim_data.append(text)

    return claim_data
