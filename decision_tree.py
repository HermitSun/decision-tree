from data_process import dataset as data, labels
from utils import calc_shannon_entropy
from tree_plotter import create_plot
from typing import List


def split_dataset(dataset: List[List[int]], axis: int, value: int):
    new_dataset = []
    for feat in dataset:
        if feat[axis] == value:
            reduced_feat = feat[:axis]
            reduced_feat.extend(feat[axis + 1:])
            new_dataset.append(reduced_feat)
    return new_dataset


def choose_best_feature_to_split(dataset: List[List[int]]) -> int:
    num_features = len(dataset[0]) - 1
    base_entropy = calc_shannon_entropy(dataset)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        feat_list = [example[i] for example in dataset]
        unique_values = set(feat_list)
        new_entropy = 0.0
        # 计算每一种划分的信息增益
        for value in unique_values:
            sub_dataset = split_dataset(dataset, i, value)
            prob = len(sub_dataset) / float(len(dataset))
            new_entropy += prob * calc_shannon_entropy(sub_dataset)
        info_gain = base_entropy - new_entropy
        # 选出最好的
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature


def create_tree(dataset: List[List[int]], labels: List[str]):
    class_list = [example[-1] for example in dataset]
    # 类别完全相同，不再划分
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 全部遍历完成
    # if len(dataset[0]) == 1:
    #     return majority_count(class_list)
    best_feat = choose_best_feature_to_split(dataset)
    best_feat_label = labels[best_feat]
    decision_tree = {best_feat_label: {}}
    del (labels[best_feat])
    feat_values = [example[best_feat] for example in dataset]
    unique_values = set(feat_values)
    # 构建决策树
    for value in unique_values:
        sub_labels = labels[:]
        decision_tree[best_feat_label][value] = create_tree(
            split_dataset(dataset, best_feat, value),
            sub_labels
        )
    return decision_tree


decision_tree = create_tree(data, labels)

create_plot(decision_tree)
