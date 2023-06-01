# IEGLM

该项目是使用[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)模型在信息抽取（IE）任务上进行高效微调的项目，起名为IEGLM。微调方式参考[ptuning/README.md](ptuning/README.md)。

## 基础版本
模式输入输出形式定义为：

```
input: 你现在是一个信息抽取模型。已知候选的关系列表：[relation1, relation2, ...]；句子：sentence；请从句子中抽取出可能存在的头实体(Subject)与尾实体(Object)，并给出对应的关系三元组。请按照(Subject,Relation,Object)的格式回答。

output: (subject1, relation1, object1),(subject2, relation2, object2),...
```
具体构造方式参考[ptuning/RelationExtraction/process_data.py](ptuning/RelationExtraction/process_data.py)。

## 思维链
除此之外，为了提升模型的推理能力，本项目还尝试利用思维链（Chain-of-thoughts, COT）的方法对输入输出进行改进。于是输入和输出形式定义为：

```
input: 给定句子：sentence
       你现在是一个信息抽取模型。请根据候选的关系列表：[relation1, relation2, ...]，从以上句子中抽取出可能存在的头实体(Subject)与尾实体(Object)，并给出对应的关系三元组。请先找出存在的关系，再将关系三元组按照(Subject,Relation,Object)的格式回答。

output: 句子中存在的关系为：[relation1, relation2]。因此句子中包含的关系三元组为：(subject1, relation1, object1),(subject2, relation2, object2),...
```
具体构造方式参考[ptuning/RelationExtraction/process_data_cot.py](ptuning/RelationExtraction/process_data_cot.py)。
