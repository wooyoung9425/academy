from dummy import dummyCode
from appointment import appointment_smart_v2
from participation import participation_smart_v2
from degreeOfInterest import interest_smart_v2
from reviewScore import reviewScore_v2
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

user_num = 300
academy_num = 30

# search_history_num = 1000
search_history_num = 3000
click_num = 900
favorite_num = 900
appointment_num = 900
review_num = 900

df_search_history = dummyCode.searchHistory(search_history_num, academy_num)
df_click_academy = dummyCode.click_academies(click_num, user_num, academy_num)
df_favorite_academy = dummyCode.favorite_academy(
    favorite_num, academy_num, user_num)
df_appointment = dummyCode.appointments(appointment_num, user_num, academy_num)
df_reviews = dummyCode.reviews(review_num, academy_num)

interest = interest_smart_v2(df_search_history, df_click_academy)
participation = participation_smart_v2(
    df_click_academy, df_favorite_academy, df_appointment)
appointment = appointment_smart_v2(df_appointment)
reviews = reviewScore_v2(df_reviews)


score_list = []

for id in tqdm(range(1, academy_num+1)):
    try:
        interestScore = interest.loc[interest['AcademyId']
                                     == id]['interestScore'].values[0]
    except:
        interestScore = 0
    try:
        participationScore = participation.loc[participation['AcademyId']
                                               == id]['participationScore'].values[0]
    except:
        participationScore = 0
    try:
        appointmentScore = appointment.loc[appointment['AcademyId']
                                           == id]['appointmentScore'].values[0]
    except:
        appointmentScore = 0
    try:
        reviewScore = reviews.loc[reviews['academyId']
                                  == id]['total_score'].values[0]
    except:
        reviewScore = 0
    score = interestScore + participationScore + appointmentScore + reviewScore
    score_list.append({'AcademyId': id, 'name': '학원'+str(id), 'score': score})


df_score = pd.DataFrame(score_list, columns=['AcademyId', 'name', 'score'])
df_score = df_score.sort_values(by=['AcademyId'], axis=0, ascending=True)

df_score.to_csv(
    './result/dummy_review_score.csv', encoding='utf-8', index=False)

# 정규화
mean = df_score.mean()['score']
st = 0
for i in range(0, len(df_score)):
    v = (df_score.iloc[i]['score'] - mean) ** 2
    st += v
standardization = (st / len(df_score)) ** 0.5
print(">>>>>>>>>>>>>> 평균 : ", mean, "   표준 편차  : ", standardization)
score = sorted(df_score['score'].values)
score_x = (df_score['score']-mean)/standardization
print(score_x)
# for val in score:
#     print(val)

plt.rc("font", family="NanumGothic")
plt.title(" 정규분포 ")


# print(min(x), max(x))
plt.xlabel("학원지수")
plt.ylabel("정규화")
plt.plot(score, norm.pdf(score, loc=mean, scale=standardization))
# plt.plot(score_x, norm.pdf(score_x, loc=0, scale=1))
plt.show()
