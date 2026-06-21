import re
import json
import os 
count=0
words=""
npm_file=open(r"C:\Users\suvad\OneDrive\Desktop\new_package.json")
npm_json=json.load(npm_file)
key_matcher=["preinstall","postinstall","precompile"]
script_dict=dict(npm_json.get("scripts", {}))
for keywords in key_matcher:
    for i, j in script_dict.items():
        if(i==keywords):
            words=re.findall(r"\b(curl|bash|sh|wget)\b",j)
            print(words)
            count=count+1
print("risks found : ", count)
npm_file.close()