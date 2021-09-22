import json

dic = {}
with open("data.txt") as f:
    for i in f:
        cmd, desc = i.strip().split(None, 1)
        dic[cmd] = desc.strip()

out_file = open("test1.json", "w")
json.dump(dic, out_file, indent = 4, sort_keys = True)
out_file.close()