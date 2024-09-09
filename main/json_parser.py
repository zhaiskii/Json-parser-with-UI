#is it ok to execute it all here
import json


json_path = 'main/dataset.json'

data = []

with open(json_path, 'r') as gg:
    data = json.load(gg)

