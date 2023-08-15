from degreeOfInterest import interest
from participation import participation
from appointment import appointment

import pandas as pd
from sqlConnection import CRUD
from tqdm import tqdm

# 관심도
interest = interest()
# 참여도
participation = participation()
# 응대
appointment = appointment()


# print(len(interest), len(participation), len(appointment))

# 전체 학원
db = CRUD()
academies, column = db.readDB(schema='haksoop', table='academies', column='*')
df_acadeies = pd.DataFrame(academies, columns=column)
academy_total_id = df_acadeies['id']
score_list = []

print(academy_total_id.values)
for id in tqdm(academy_total_id.values):
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
    score = interestScore + participationScore + appointmentScore
    academy_name = df_acadeies.loc[df_acadeies['id'] == id]['name'].values[0]
    score_list.append({'AcademyId': id, 'name': academy_name, 'score': score})


df_score = pd.DataFrame(score_list, columns=['AcademyId', 'name', 'score'])
df_score = df_score.sort_values(by=['AcademyId'], axis=0, ascending=True)
df_score.to_csv(
    './result/academy_score.csv', encoding='utf-8', index=False)
