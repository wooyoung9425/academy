from sqlConnection import CRUD
import pandas as pd
import random


def reviewScore():
    db = CRUD()
    reviews, reviews_column = db.readDB(
        schema='haksoop', table='reviews', column='*')
    df_reivews = pd.DataFrame(reviews, columns=reviews_column)
    scores = []
    academy_id_list = set(df_reivews['academyId'])
    # 상담 q1:친절

    for aca in academy_id_list:
        temp = []
        df_id_review = df_reivews[df_reivews['academyId'] == aca]
        score = df_id_review[df_id_review['type'] !=
                             'appointment']['question1'].mean() * 4
        teacher = df_id_review[df_id_review['type'] !=
                               'appointment']['question2'].mean() * 3
        management = df_id_review[df_id_review['type'] !=
                                  'appointment']['question3'].mean() * 2
        facility = df_id_review[df_id_review['type'] !=
                                'appointment']['question4'].mean()
        kind = df_id_review[df_id_review['type'] ==
                            'appointment']['question1'].mean()
        level = df_id_review[df_id_review['type'] ==
                             'appointment']['question2'].mean()
        temp.append({'academyId': int(aca), 'score': score, 'teacher': teacher,
                     'management': management, 'facility': facility, 'kind': kind, 'level': level})
        df_temp = pd.DataFrame(temp, columns=[
                               'academyId', 'score', 'teacher', 'management', 'facility', 'kind', 'level'])
        df_temp = df_temp.fillna(0)

        df_temp['total_score'] = df_temp['score']+df_temp['teacher'] + \
            df_temp['management']+df_temp['facility'] + \
            df_temp['kind']+df_temp['level']

        scores.append(dict(df_temp.iloc[0]))
    df_scores = pd.DataFrame(scores, columns=[
                             'academyId', 'score', 'teacher', 'management', 'facility', 'kind', 'level', 'total_score'])
    return df_scores

# 더미데이터


def reviewScore_v2(df_reivews):
    scores = []
    academy_id_list = set(df_reivews['academyId'])

    for aca in academy_id_list:
        temp = []
        df_id_review = df_reivews[df_reivews['academyId'] == aca]
        score = df_id_review[df_id_review['type'] !=
                             'appointment']['question1'].mean() * 4
        teacher = df_id_review[df_id_review['type'] !=
                               'appointment']['question2'].mean() * 3
        management = df_id_review[df_id_review['type'] !=
                                  'appointment']['question3'].mean() * 2
        facility = df_id_review[df_id_review['type'] !=
                                'appointment']['question4'].mean()
        kind = df_id_review[df_id_review['type'] ==
                            'appointment']['question1'].mean()
        level = df_id_review[df_id_review['type'] ==
                             'appointment']['question2'].mean()
        temp.append({'academyId': int(aca), 'score': score, 'teacher': teacher,
                     'management': management, 'facility': facility, 'kind': kind, 'level': level})
        df_temp = pd.DataFrame(temp, columns=[
                               'academyId', 'score', 'teacher', 'management', 'facility', 'kind', 'level'])
        df_temp = df_temp.fillna(0)

        df_temp['total_score'] = df_temp['score']+df_temp['teacher'] + \
            df_temp['management']+df_temp['facility'] + \
            df_temp['kind']+df_temp['level']

        scores.append(dict(df_temp.iloc[0]))
    df_scores = pd.DataFrame(scores, columns=[
                             'academyId', 'score', 'teacher', 'management', 'facility', 'kind', 'level', 'total_score'])

    df_scores.to_csv('./result/reviewScore.csv', encoding='cp949')
    return df_scores


if __name__ == "__main__":
    print(reviewScore())
