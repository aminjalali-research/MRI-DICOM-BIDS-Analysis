import json

with open(
    "/home/amin/MRIProjects/dcm2bids/config_test_original_all_modalities.json"
) as f:
    cfg = json.load(f)

print("Found the following sequence definitions:\n")
for desc in cfg["descriptions"]:
    dt = desc["datatype"]
    suf = desc["suffix"]
    cri = desc.get("criteria", {})
    # metadata keys beyond datatype/suffix/criteria
    extras = {
        k: v for k, v in desc.items() if k not in ("datatype", "suffix", "criteria")
    }

    print(f"- **{dt}**  →  suffix `{suf}`")
    print(f"    • criteria: {cri}")
    if extras:
        print(f"    • additional metadata: {extras}")
    print()
