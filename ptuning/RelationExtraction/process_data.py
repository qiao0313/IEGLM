import json


train_file = 'train.json'
valid_file = 'valid1.json'
processed_train_file = 'processed_train.json'
processed_valid_file = 'processed_valid.json'

unused_count = 0
with open(train_file, 'r', encoding='utf-8') as f_in, open(processed_train_file, 'w', encoding='utf-8') as f_out:
    train_data = f_in.readlines()
    for data in train_data:
        dic = {}
        data_ = json.loads(data)
        start, end = data_["instruction"].index('['), data_["instruction"].index(']')
        relation = data_["instruction"][start: end+1]
        instruction = "你现在是一个信息抽取模型。已知候选的关系列表：" + relation + \
            "；句子：" + data_["input"] + \
            "请从句子中抽取出可能存在的头实体(Subject)与尾实体(Object)，并给出对应的关系三元组。" + \
            "请按照(Subject,Relation,Object)的格式回答。"
        output = data_["output"]
        dic['instruction'] = instruction
        dic['output'] = output
        if len(output) > 200:
            unused_count += 1
            continue
        f_out.write(json.dumps(dic, ensure_ascii=False))
        f_out.write("\n")
print(unused_count)

with open(valid_file, 'r', encoding='utf-8') as f_in, open(processed_valid_file, 'w', encoding='utf-8') as f_out:
    valid_data = f_in.readlines()
    for data in valid_data:
        dic = {}
        data_ = json.loads(data)
        start, end = data_["instruction"].index('['), data_["instruction"].index(']')
        relation = data_["instruction"][start: end+1]
        instruction = "你现在是一个信息抽取模型。已知候选的关系列表：" + relation + \
            "；句子：" + data_["input"] + \
            "请从句子中抽取出可能存在的头实体(Subject)与尾实体(Object)，并给出对应的关系三元组。" + \
            "请按照(Subject,Relation,Object)的格式回答。"
        dic['instruction'] = instruction
        dic['output'] = "(杠杆,类型,简单机械),(滑轮,类型,简单机械),(斜面,类型,简单机械)"
        f_out.write(json.dumps(dic, ensure_ascii=False))
        f_out.write("\n")
