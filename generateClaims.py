import lib.openaiapi as openaiapi
import pandas as pd
import lib.constants as constants
import lib.evaluate as evaluate
import rag

patents_df = pd.read_parquet(constants.PROCESSED_FILE)

# Open AI API parameters
temp_value = 1
max_tokens_value = 2006
top_p_value = 1
frequency_penalty_value = 0
presence_penalty_value = 0

US_claims_system = 'Based on the provided claim 1, generate 19 additional claims to form a complete set of 20 claims that conform to US patent law for a US patent application. The additional claims include both independent and dependent claims. Number the claims so that the subject matter claim categories are grouped together. All terms in the claims require antecedent basis, meaning that the first instance of a term is introduced with the word "a" and subsequent instances are referred to with "the". Do not include advantages in the claims. Example claim sets from other patents are provided for guidance. In the response, do not reproduce the instructions or claim 1.'

# using a single generated abstract and provided claim here for now
# 20200000001
# replace in future
i=0
patent = patents_df.iloc[i]
generated_abstract = "An apparatus is designed to facilitate side-shifting movement of an implement attached to a mobile machine's three-point hitch, which includes an upper attachment point and two lower attachment points. The apparatus consists of a first framework with laterally extending rails, an upper and a lower cross beam, and vertical studs aligned in the framework's plane. It incorporates three attachments for connecting to the hitch points. A second framework, capable of sliding along the rails, has vertical posts and sleeves, with three connectors to link the implement for lateral movement. Included in the design is at least one driver for shifting the second framework along the rails and a guidance system to control the movement. This construction allows the implement to slide side-to-side relative to the machine's three-point hitch."
provided_claim = "1. Apparatus for connecting an implement to a three-point hitch of mobile machinery for controllable side-shifting movement of the connected implement, the three point hitch comprising an upper attachment point and two lower attachment points, the apparatus comprising a) a first framework having a height, a length, and a depth, and comprising at least two parallel, vertically spaced apart, laterally extending rails, an upper cross beam, a lower cross beam, and at least two upwardly extending, laterally spaced apart studs attached to the cross beams and the rails, wherein the rails, the studs, and the cross beams are coplanar in a first framework plane, the first framework plane extending along the height and the length of the first framework; b) three attachments attached to the first framework for attachment to the three-point hitch, the attachments comprising an upper attachment attached to the upper cross beam for attachment to the upper attachment point of the three-point hitch and two lower attachments attached to the lower cross beam for attachment to the lower attachment points of the three-point hitch; c) a slidable second framework comprising at least two upwardly extending, laterally spaced apart posts and at least two sleeves attached to the posts, the posts and the sleeves being coplanar in the first framework plane, and wherein each sleeve is a surrounding sleeve mounted around one of the rails so that the slidable second framework can slide laterally back and forth along the rails; d) three connectors supported by the slidable second framework for connecting the slidable second framework to the implement for movement of the implement by the mobile machinery and the slidable second framework; e) at least one driver connected to the first framework and connected to the slidable second framework for driving the slidable second framework laterally back and forth along the rails; and f) a guidance system for controlling the driver."

df = pd.DataFrame(columns=['i', 'title', 'ground_truth_claims', 'generated_US_claims', 'generated_CA_claims', 'generated_EP_claims'])

top_k = 5 # 5 closest patent records from DB
omit_index = i
results = rag.RAGCall(generated_abstract, top_k, omit_index)
example_claims = ' '.join(map(str, results['claim_data']))

ground_truth_claims = patent["claim_data"]
claims_prompt = 'Claim 1: ' + provided_claim + '\n Example claims: ' + example_claims

api_US_response = openaiapi.sendAPIRequest(US_claims_system, claims_prompt, temp_value, max_tokens_value, top_p_value, frequency_penalty_value, presence_penalty_value)
generated_US_claims = api_US_response.choices[0].message.content

print('Ground truth claims: ', ground_truth_claims)
print('Generated US claims: ' , generated_US_claims)

# generate CA claims

CA_claims_system = 'Based on the provided claim 1, generate 19 additional claims to form a complete set of 20 claims that conform to Canadian patent law for a Canadian patent application. Include multiple dependencies in the additional claims. The additional claims include both independent and dependent claims. Number the claims so that the subject matter claim categories are grouped together. All terms in the claims require antecedent basis, meaning that the first instance of a term is introduced with the word "a" and subsequent instances are referred to with "the". Do not include advantages in the claims. Example claim sets from other patents are provided for guidance. In the response, do not reproduce the instructions or claim 1.'

api_CA_response = openaiapi.sendAPIRequest(CA_claims_system, claims_prompt, temp_value, max_tokens_value, top_p_value, frequency_penalty_value, presence_penalty_value)
generated_CA_claims = api_CA_response.choices[0].message.content

print('Generated CA claims: ' , generated_CA_claims)

# generate EP claims

EP_claims_system = 'Based on the provided claim 1, generate 14 additional claims to form a complete set of 15 claims that conform to European patent law for a European patent application. The claims include multiple dependencies. The additional claims include both independent and dependent claims. Number the claims so that the subject matter claim categories are grouped together. All terms in the claims require antecedent basis, meaning that the first instance of a term is introduced with the word "a" and subsequent instances are referred to with "the". Do not include advantages in the claims. Example claim sets from other patents are provided for guidance. In the response, do not reproduce the instructions or claim 1.'

# EP_claims_system = 'Generate a set of 15 claims for a European patent application based on the provided US and Canadian claims.'

# US_and_CA_claims = 'US claims: ' + generated_US_claims + '\n Canadian claims: ' + generated_CA_claims

api_EP_response = openaiapi.sendAPIRequest(EP_claims_system, claims_prompt, temp_value, max_tokens_value, top_p_value, frequency_penalty_value, presence_penalty_value)
generated_EP_claims = api_EP_response.choices[0].message.content

print('Generated EP claims: ' , generated_EP_claims)


df = df._append({
    'i': i,
    'title': patent["title"],
    'ground_truth_claims': ground_truth_claims,
    'generated_US_claims': generated_US_claims,
    'generated_CA_claims': generated_CA_claims,
    'generated_EP_claims': generated_EP_claims,
}, ignore_index=True)

print("writing to file", constants.GENERATED_CLAIMS_FILE)
df.to_csv(constants.GENERATED_CLAIMS_FILE, index=False)

