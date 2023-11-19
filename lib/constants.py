import os

FILES_DIR = "files"
INPUT_FILE = os.path.join(FILES_DIR, "ipa200102.xml")
PROCESSED_FILE = os.path.join(FILES_DIR, "processed-ipa200102.parquet")
INDEX_FILE = os.path.join(FILES_DIR, "index-ipa200102.index")
GENERATED_ABSTRACTS_FILE = os.path.join(FILES_DIR, "generated_abstracts.csv")
EVALUATED_ABSTRACTS_FILE = os.path.join(FILES_DIR, "evaluated_abstracts.csv")

PATENT_INDICES = [0, 100, 1000, 2000, 5000]
# 0       20200000001     SYSTEM FOR CONNECTING IMPLEMENT TO MOBILE MACHINERY
# 100     20200000101     PEST CONTROL COMPOSITION
# 1000    20200001001     LAVAGE DEVICE
# 2000    20200002001     Cabin Arrangement For An Aircraft, And Aircraft
# 5000    20200005001     AUTOMATED PHYSICAL NETWORK MANAGEMENT SYSTEM UTILIZING HIGH RESOLUTION RFID AND OPTICAL SCANNING FOR RFID TAG SPATIAL LOCALIZATION

# run this from QuickPath/ directory to get the above output
# import pandas as pd
# patents_df = pd.read_parquet(PROCESSED_FILE)
# for i in PATENT_INDICES:
#     print(f"{i}\t{patents_df.iloc[i]['publ_number']}\t{patents_df.iloc[i]['title']}")
