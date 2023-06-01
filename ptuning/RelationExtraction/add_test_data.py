import json


test_file = 'processed_valid.json'
pred_file = 'generated_predictions1.txt'
train_file = 'processed_train.json'

test_list = []
with open(test_file, 'r', encoding='utf-8') as f1, \
        open(pred_file, 'r', encoding='utf-8') as f2:
    test_data = f1.readlines()
    pred_data = f2.readlines()
    for test, pred in zip(test_data, pred_data):
        test_dic = {}
        test_d = json.loads(test)
        pred_d = json.loads(pred)
        test_dic["instruction"] = test_d["instruction"]
        test_dic['output'] = pred_d["predict"]
        test_list.append(test_dic)

train_list = []
with open(train_file, 'r', encoding='utf-8') as f3:
    train_data = f3.readlines()
    for train_d in train_data:
        train_list.append(json.loads(train_d))

train_list += test_list
with open('new_train.json', 'w', encoding='utf-8') as f_out:
    for pred in train_list:
        f_out.write(json.dumps(pred, ensure_ascii=False))
        f_out.write('\n')
