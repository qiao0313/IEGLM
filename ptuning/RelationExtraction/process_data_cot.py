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
        instruction = "给定句子：" + data_["input"] + "\n" + "你现在是一个信息抽取模型。" + \
            "请根据候选的关系列表：" + relation + "，" + \
            "从以上句子中抽取出可能存在的头实体(Subject)与尾实体(Object)，并给出对应的关系三元组。" + \
            "请先找出存在的关系，再将关系三元组按照(Subject,Relation,Object)的格式回答。"
        relation_set = set()
        kg_list = data_["kg"]
        for kg in kg_list:
            s, r, o = kg[0], kg[1], kg[2]
            relation_set.add(r)
        relation_list = list(relation_set)
        output = data_["output"]
        response = "句子中存在的关系为：" + str(relation_list) + "。" + \
            "因此句子中包含的关系三元组为：" + output
        dic['instruction'] = instruction
        dic['output'] = response
        if len(response) > 250:
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
        instruction = "给定句子：" + data_["input"] + "\n" + "你现在是一个信息抽取模型。" + \
            "请根据候选的关系列表：" + relation + "," + \
            "从以上句子中抽取出可能存在的头实体(Subject)与尾实体(Object)，并给出对应的关系三元组。" + \
            "请先找出存在的关系，再将关系三元组按照(Subject,Relation,Object)的格式回答。"
        dic['instruction'] = instruction
        dic['output'] = "句子中存在的关系为：['事件','位于','名称由来']。" + \
            "因此句子中包含的关系三元组包含：" + \
            "(浅草神社,事件,三社祭),(浅草神社,位于,浅草),(台东区,位于,东京都),(浅草寺,位于,浅草),(浅草寺,名称由来,浅草)"
        f_out.write(json.dumps(dic, ensure_ascii=False))
        f_out.write("\n")
