# -*- coding: utf-8 -*-
"""
@Time  ： 2023/12/16 19:12
@Author： zhanglongwen02
"""
import pandas as pd
import jieba
from hashlib import md5


class Matcher:
    def __init__(self):
        self.query_answer = {}
        self.query_dict = {}
        # self.answers_datas = self.set_datas()
    
    def set_datas(self):
        datas = pd.read_excel("/Users/zlw/Documents/learning/smart_robot/match_keyword/answers.xlsx").fillna("")
        for q, a in zip(datas["title"].values.tolist(), datas["answer"].values.tolist()):
            self.query_answer[q] = a
            query_list = jieba.lcut(q)
            for word in query_list:
                if word not in self.query_dict:
                    self.query_dict[word] = []
                self.query_dict[word].append(q)
    
    def jaccard_similarity(self, text1, text2):
        """
        jaccard相似度,计算交并比
        param text1: 文本1
        param text2:文本2
        return: float 相似度
        """
        set1, set2 = set(text1), set(text2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union > 0 else 0
    
    def match_query(self, query):
        query_list = jieba.lcut(query)
        query_matchs = []
        for word in query_list:
            if word in self.query_dict:
                query_matchs.extend(self.query_dict[word])
        query_matchs = list(set(query_matchs))
        query_match_scores = [[x, self.jaccard_similarity(query, x)] for x in query_matchs]
        query_match_scores.sort(key=lambda x: x[1], reverse=True)
        answers = [self.query_answer[q[0]] for q in query_match_scores if q[0] in self.query_answer]
        answer = answers[0] if answers else "无法回答"
        if answer != "无法回答":
            query = query_match_scores[0][0]
        return query, answer
