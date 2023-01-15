import yaml
import json
import time 

start_time = time.perf_counter()

with open('/Users/macpro16/Desktop/labs/lab4/schedule.json', 'r', encoding='utf-8') as file:
    configuration = json.load(file)

with open('/Users/macpro16/Desktop/labs/lab4/toyaml.yaml','w', encoding='utf-8') as yaml_file:
    yaml.dump(configuration, yaml_file, encoding='utf-8')

print(time.perf_counter() - start_time)
