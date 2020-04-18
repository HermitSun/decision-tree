from numpy import log2
from typing import List


# 计算香农熵
def calc_shannon_entropy(dataset: List[List[int]]) -> float:
    feat_counts = len(dataset)
    feat_dict = {}
    # 将每一种可能的特征加入dict
    for feat in dataset:
        current_feat = feat[-1]
        if current_feat not in feat_dict:
            feat_dict[current_feat] = 0
        feat_dict[current_feat] += 1
    # 根据概率计算香农熵
    shannon_entropy = 0.0
    for feat in feat_dict:
        probability = float(feat_dict[feat]) / feat_counts
        shannon_entropy -= probability * log2(probability)
    return shannon_entropy
