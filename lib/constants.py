import os

FILES_DIR = "files"

# INPUT_FILE = os.path.join(FILES_DIR, "ipa200102.xml")
# PROCESSED_FILE = os.path.join(FILES_DIR, "processed-ipa200102.parquet")
# INDEX_FILE = os.path.join(FILES_DIR, "index-ipa200102.index")

# GENERATED_ABSTRACTS_FILE = os.path.join(FILES_DIR, "generated_abstracts.csv")
# GENERATED_ABSTRACTS_LLAMA2_FILE = os.path.join(FILES_DIR, "generated_abstracts_llama2.csv")
# EVALUATED_ABSTRACTS_FILE = os.path.join(FILES_DIR, "evaluated_abstracts.csv")

# GENERATED_ABSTRACTS_BASELINE_FILE = os.path.join(FILES_DIR, "generated_abstracts-baseline.csv")
# EVALUATED_ABSTRACTS_BASELINE_FILE = os.path.join(FILES_DIR, "evaluated_abstracts-baseline.csv")

# GENERATED_CLAIMS_FILE = os.path.join(FILES_DIR, "generated_claims.csv")
# EVALUATED_CLAIMS_FILE = os.path.join(FILES_DIR, "evaluated_claims.csv")

INPUT_FILE = os.path.join(FILES_DIR, "ipa231130.xml")
PROCESSED_FILE = os.path.join(FILES_DIR, "processed-ipa231130.parquet")
INDEX_FILE = os.path.join(FILES_DIR, "index-ipa231130.index")

GENERATED_ABSTRACTS_FILE = os.path.join(FILES_DIR, "generated_abstracts_ipa231130.csv")
GENERATED_ABSTRACTS_LLAMA2_FILE = os.path.join(FILES_DIR, "generated_abstracts_llama2_ipa231130.csv")
EVALUATED_ABSTRACTS_FILE = os.path.join(FILES_DIR, "evaluated_abstracts_ipa231130.csv")
EVALUATED_ABSTRACTS_LLAMA2_FILE = os.path.join(FILES_DIR, "evaluated_abstracts_llama2_ipa231130.csv")

GENERATED_ABSTRACTS_BASELINE_FILE = os.path.join(FILES_DIR, "generated_abstracts-baseline_ipa231130.csv")
EVALUATED_ABSTRACTS_BASELINE_FILE = os.path.join(FILES_DIR, "evaluated_abstracts-baseline_ipa231130.csv")

GENERATED_CLAIMS_FILE = os.path.join(FILES_DIR, "generated_claims_ipa231130.csv")
EVALUATED_CLAIMS_FILE = os.path.join(FILES_DIR, "evaluated_claims_ipa231130.csv")


PATENT_INDICES = [0, 100, 1000, 2000, 5001]
# 0       20200000001     SYSTEM FOR CONNECTING IMPLEMENT TO MOBILE MACHINERY
# 100     20200000101     PEST CONTROL COMPOSITION
# 1000    20200001001     LAVAGE DEVICE
# 2000    20200002001     Cabin Arrangement For An Aircraft, And Aircraft
# 5001    20200005002     METHODS OF MAKING AND USING AN IDENTIFICATION TAG SYSTEM FOR USE WITH AN ELECTROMAGNETIC ENERGY CABLE

# run this from QuickPath/ directory to get the above output
# import pandas as pd
# patents_df = pd.read_parquet(PROCESSED_FILE)
# for i in PATENT_INDICES:
#     print(f"{i}\t{patents_df.iloc[i]['publ_number']}\t{patents_df.iloc[i]['title']}")
