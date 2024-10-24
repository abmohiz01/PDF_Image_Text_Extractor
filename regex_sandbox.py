import json
from utils import extract_datapoints_from_pdf
import pandas as pd
# from PDF_extractor import extract_property_address

with open('parsed_pdfs.json', 'r') as f:
    parsed_pdfs = json.load(f)

datapoints_dict = {}
for case_number, pdf in parsed_pdfs.items():
    # if case_number == "A2303257":
    # if case_number in [
    #     'A2303249', 'A2303257', 'A2303258', 'A2303259', 'A2303260', 'A2303272', 'A2303278'
    #
    # ]:
    datapoints_dict[case_number] = extract_datapoints_from_pdf(pdf)

with open('datapoints_sandbox.json', 'w') as f:
    json.dump(datapoints_dict, f)

# add case number to each dict
for case_number, datapoints in datapoints_dict.items():

    datapoints['case_number'] = case_number

datapoints_list = datapoints_dict.values()
df = pd.DataFrame(datapoints_list)
df.to_csv('datapoints_sandbox.csv', index=False)
