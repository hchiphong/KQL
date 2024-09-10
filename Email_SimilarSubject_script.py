import difflib
def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()
result = df
n = df.shape[0]
subject = kargs["subject"]
result["similiar"] = result.apply( lambda row: similar(row['Subject'],subject), axis=1)
