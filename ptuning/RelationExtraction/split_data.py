import os
import json
import numpy as np
from tqdm import tqdm


def write_file(res, file):
    with open(file, 'w', encoding='utf-8') as f:
        for data in res:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write("\n")
    print(f'write to {file} success, total {len(res)} lines.')


def read_text_pair(data_file):
    res = []
    with open(data_file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data = json.loads(line)
            res.append(data)
    return res


def shuffle(res, dev_ratio, seed=42):
    ''' dev_len若[0,1]则按比例取，若>1则按条数取 '''
    assert dev_ratio > 0 , "dev set ratio should lager than 0."
    # shuffle
    shuffled_res = []
    shuffle_idx = np.random.RandomState(seed=seed).permutation(np.arange(0, len(res))).tolist()
    for idx in tqdm(shuffle_idx):
        shuffled_res.append(res[idx])
    # dev len
    dev_len = int(len(res) * dev_ratio)
    # split
    train_set = shuffled_res[:-dev_len]
    dev_set = shuffled_res[-dev_len:]
    
    return train_set, dev_set


def split_data(dev_ratio):

    train_file = "new_train.json"

    res = read_text_pair(train_file)
    train_data, dev_data = shuffle(res, dev_ratio=dev_ratio)
    print(len(train_data))
    print(len(dev_data))
    train_file = "processed_train.json"
    dev_file = "processed_dev.json"
    write_file(train_data, train_file)
    write_file(dev_data, dev_file)


if __name__ == '__main__':
    dev_ratio = 0.05
    split_data(dev_ratio)
