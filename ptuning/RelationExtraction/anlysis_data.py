import json


processed_train_file = 'processed_train.json'
processed_valid_file = 'processed_valid.json'

train_input_list = []
train_output_list = []
valid_input_list = []

with open(processed_train_file, 'r', encoding='utf-8') as f:
    train_data = f.readlines()
    for data in train_data:
        data_ = json.loads(data)
        train_input_list.append(len(data_['instruction']))
        train_output_list.append(len(data_['output']))

with open(processed_valid_file, 'r', encoding='utf-8') as f:
    valid_data = f.readlines()
    for data in valid_data:
        data_ = json.loads(data)
        valid_input_list.append(len(data_['instruction']))

print(max(train_input_list))
print(max(train_output_list))
print(max(valid_input_list))
