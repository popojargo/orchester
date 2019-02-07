import json


def empty_values_rec(val):
    if isinstance(val, dict):
        for k, v in val.items():
            val[k] = empty_values_rec(v)
        return val
    elif isinstance(val, list):
        for k, v in enumerate(val):
            val[k] = empty_values_rec(v)
        return val
    else:
        return ""


with open('.orchester-doc.json') as f:
    data = json.load(f)
    data = empty_values_rec(data)
    print(json.dumps(data, indent=2, sort_keys=True))
