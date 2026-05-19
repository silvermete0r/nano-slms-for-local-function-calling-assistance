import json

def remove_widget_keys(obj):
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            # skip keys containing "widget"
            if "widget" in k:
                continue
            cleaned[k] = remove_widget_keys(v)
        return cleaned
    elif isinstance(obj, list):
        return [remove_widget_keys(item) for item in obj]
    else:
        return obj

NOTEBOOK_PATH = "../notebooks/SLM_Qwen3_0_0_6B_Fine_Tuning_for_Function_Calling_Tasks.json"

# load
with open(NOTEBOOK_PATH, "r") as f:
    notebook_data = json.load(f)

# clean
cleaned_data = remove_widget_keys(notebook_data)

with open(NOTEBOOK_PATH, "w") as f:
    json.dump(cleaned_data, f, indent=2, ensure_ascii=False)