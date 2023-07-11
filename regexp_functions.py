import json
def clean_decimals(input_string):
    """
    Remove decimals except the 5 elements after the period.

    Used when rounding float values ​​in multi-layered and complex dictinaries.
    """
    # Remove content between '.' and '}', except the 5 elements after the period.
    cleaned_string = re.sub(r"\.(.{5}).\d+}", r".\1}", input_string)
    # Remove content between '.' and ',', except the 5 elements after the period.
    cleaned_string = re.sub(r"\.(.{5}).\d+,", r".\1,", cleaned_string)
    return cleaned_string
# Usage
json_data = json.loads(clean_decimals(json.dumps(json_data)))
