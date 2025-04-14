from regex_processor import classify_with_regex
from bert_processor import classify_with_bert
from llm_processor import classify_with_llm
import pandas as pd

# Used to get labels from label dictionary
def classify(logs):
    lables = []
    for source, log_string in logs:
        label = classify_log_msg(source,log_string)
        lables.append(label)
    return lables


def classify_log_msg(source: str ,log_message: str):
    if source == "LegacyCRM":
        label = classify_with_llm(log_message)
    else:
        label = classify_with_regex(log_message)
        if label is None:
            label =  classify_with_bert(log_message)
    return label


def classify_csv(input_path):
    df = pd.read_csv(input_path)
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

    output_path = "resources/output.csv"
    df.to_csv(output_path, index=False)

