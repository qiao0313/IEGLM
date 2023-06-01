import json


def post_process(predict_file, test_file, submit_file):
    pred_list = []
    with open(predict_file, 'r', encoding='utf-8') as f1, \
        open(test_file, 'r', encoding='utf-8') as f2:
        predict_data = f1.readlines()
        test_data = f2.readlines()
        for pred, test in zip(predict_data, test_data):
            pred_dic = {}
            pred_d = json.loads(pred)
            test_d = json.loads(test)
            pred_dic['id'] = test_d['id']
            pred_dic['cate'] = test_d['cate']
            pred_dic['input'] = test_d['input']
            pred_dic['output'] = '[' + pred_d['predict'] + ']'
            pred_tmp = pred_d['predict']
            pred_tmp = pred_tmp.split('),')
            kg_list = []
            for p in pred_tmp:
                p = p.replace('(', '').replace(')', '')
                p = p.split(',')
                if len(p) != 3:
                    continue
                if p not in kg_list:
                    kg_list.append(p)
            pred_dic['kg'] = kg_list
            # print(kg_list)
            # output_str = ""
            # for kg in kg_list:
            #     print(kg)
            #     output_str += "(" + kg[0] + "," + kg[1] + "," + kg[2] + "),"
            # output_str = "[" + output_str[:-1] + "]"
            # pred_dic['output'] = output_str
            pred_list.append(pred_dic)

    with open(submit_file, 'w', encoding='utf-8') as f:
        for pred in pred_list:
            f.write(json.dumps(pred, ensure_ascii=False))
            f.write('\n')


if __name__ == '__main__':
    predict_file = 'generated_predictions.txt'
    test_file = 'valid1.json'
    submit_file = 'result1.json'
    post_process(predict_file, test_file, submit_file)
