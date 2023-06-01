# IEGLM

该项目是使用[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)模型在信息抽取（IE）任务上进行高效微调的项目，起名为IEGLM。微调方式与ChatGLM-6B模型方式一致，参考[ptuning/README.md](ptuning/README.md)。

模式输入输出形式定义为：

```
input: 你现在是一个信息抽取模型。已知候选的关系列表：[relation1, relation2, ...]；句子：sentence；请从句子中抽取出可能存在的头实体(Subject)与尾实体(Object)，并给出对应的关系三元组。请按照(Subject,Relation,Object)的格式回答。

output: (subject1, relation1, object1),(subject2, relation2, object2),...
```
