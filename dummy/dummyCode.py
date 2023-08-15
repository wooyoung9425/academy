from faker import Faker
import random
import pandas as pd
import numpy as np

# search-histories
# id, AcademyId, searched_number, createdAt, updateAt


def searchHistory(n, academy_num):
    fake = Faker('ko_KR')
    Faker.seed(1)

    history_list = []
    for i in range(1, n+1):
        id = i
        AcademyId = random.randint(1, academy_num)
        # searched_number = random.randint(40, 60)
        searched_number = random.randint((n/academy_num)/2, n/academy_num)
        createdAt = fake.date_between(start_date='-1y', end_date='today')
        updateAt = fake.date_between(start_date='-1y', end_date='today')
        history_list.append({
            'id': id,
            'AcademyId': AcademyId,
            'searched_number': searched_number,
            'createdAt': createdAt,
            'updateAt': updateAt
        })
    df_history = pd.DataFrame(history_list, columns=[
                              'id', 'AcademyId', 'searched_number', 'createdAt', 'updateAt'])
    print(df_history)
    return df_history


def click_academies(n, user_num, academy_num):

    fake = Faker('ko_KR')
    Faker.seed(1)
    click_list = []

    academy_click = {True: n * 0.8, False: n*0.2}
    keys, weights = zip(*academy_click.items())
    probs = np.array(weights, dtype=float)/float(sum(weights))

    review_click = {False: n * 0.3, True: n*0.7}
    keys2, weights2 = zip(*review_click.items())
    probs2 = np.array(weights2, dtype=float)/float(sum(weights2))

    # bool_list = [True, False]
    for i in range(1, n+1):
        id = i
        UserId = random.randint(1, user_num)
        AcademyId = random.randint(1, academy_num)
        academy_clicked = str(np.random.choice(keys, 1, p=probs)[0])
        if academy_clicked == 'True':
            reviewTab_clicked = np.random.choice(keys2, 1, p=probs2)[0]
        else:
            reviewTab_clicked = False
        # academy_clicked = random.choice(bool_list)
        # reviewTab_clicked = random.choice(bool_list)
        createdAt = fake.date_between(start_date='-1y', end_date='today')
        updatedAt = fake.date_between(start_date='-1y', end_date='today')
        click_list.append({
            'id': id,
            'UserId': UserId,
            'AcademyId': AcademyId,
            'academy_clicked': academy_clicked,
            'reviewTab_clicked': reviewTab_clicked,
            'createdAt': createdAt,
            'updatedAt': updatedAt
        })
    # print(click_list)
    df_click = pd.DataFrame(click_list, columns=[
                            'id', 'UserId', 'AcademyId', 'academy_clicked', 'reviewTab_clicked', 'createdAt', 'updatedAt'])
    # print(df_click)
    df_click.to_csv('./result/click_academy.csv', encoding='cp949')
    return df_click


def favorite_academy(n, academy_num, user_num):
    fake = Faker('ko_KR')
    Faker.seed(1)
    favorite_list = []

    for i in range(1, n+1):
        academyId = random.randint(1, academy_num)
        userId = random.randint(1, user_num)
        createdAt = fake.date_between(start_date='-1y', end_date='today')
        updateAt = fake.date_between(start_date='-1y', end_date='today')
        favorite_list.append({
            'academyId': academyId,
            'userId': userId,
            'createdAt': createdAt,
            'updateAt': updateAt
        })
    df_favorite = pd.DataFrame(favorite_list, columns=[
        'academyId', 'userId', 'createdAt', 'updateAt'])
    return df_favorite


def appointments(n, user_num, academy_num):
    fake = Faker('ko_KR')
    Faker.seed(1)
    appointment_list = []
    appoint_status = {'pending': n * 0.12, 'confirm': n *
                      0.13, 'cancel': n*0.05, 'consulted': n*0.7}
    keys, weights = zip(*appoint_status.items())
    probs = np.array(weights, dtype=float)/float(sum(weights))

    for i in range(1, n+1):
        id = random.randint(1, i)
        date = fake.date_between(start_date='-1y', end_date='today')
        time1 = '데이터 필요없음'
        time2 = '데이터 필요없음'
        pickedTime = 'time1'
        # status = random.choice(['pending', 'confirm', 'cancel', 'consulted'])

        status = np.random.choice(keys, 1, p=probs)
        ownerName = fake.name()
        ownerTel = [('010-'+str(random.randint(1, 9999)).zfill(4) +
                     '-'+str(random.randint(1, 9999)).zfill(4))]
        course = 'GRD'+str(random.randint(1, 999)).zfill(3)
        grade = ''
        seenBy = ''
        createdAt = fake.date_between(start_date='-1y', end_date='today')
        updatedAt = fake.date_between(start_date='-1y', end_date='today')
        deletedAt = fake.date_between(start_date='-1y', end_date='today')
        academyId = random.randint(1, academy_num)
        userId = random.randint(1, user_num)
        academyOwnerId = random.randint(1, academy_num)

        appointment_list.append({
            'id': id,
            'date': date,
            'time1': time1,
            'time2': time2,
            'pickedTime': pickedTime,
            'status': status,
            'ownerName': ownerName,
            'ownerTel': ownerTel,
            'course': course,
            'grade': grade,
            'seenBy': seenBy,
            'createdAt': createdAt,
            'updatedAt': updatedAt,
            'deletedAt': deletedAt,
            'academyId': academyId,
            'userId': userId,
            'academyOwnerId': academyOwnerId
        })
    df_appointment = pd.DataFrame(appointment_list,
                                  columns=['id', 'date', 'time1', 'time2', 'pickedTime', 'status', 'ownerName',
                                           'ownerTel', 'course', 'grade', 'seenBy', 'createdAt', 'updatedAt'
                                           'deletedAt', 'academyId', 'userId', 'academyOwnerId'
                                           ])
    return df_appointment


def reviews(n, academy_num):
    fake = Faker('ko_KR')
    Faker.seed(1)

    type_list = ['appointment', 'first', 'second']
    reviews = []
    for i in range(1, n+1):
        academy_id = random.randint(1, academy_num)
        question1 = random.randint(1, 5)
        question2 = random.randint(1, 5)
        question3 = random.randint(1, 5)
        type = random.choice(type_list)
        if type == 'appointment':
            question4 = None
        else:
            question4 = random.randint(1, 5)
        reviews.append({'academyId': academy_id, 'question1': question1,
                       'question2': question2, 'question3': question3, 'question4': question4, 'type': type})
    df_reviews = pd.DataFrame(reviews, columns=[
                              'academyId', 'question1', 'question2', 'question3', 'question4', 'type'])
    df_reviews.to_csv('./result/dummy_review.csv', encoding='cp949')
    return df_reviews


if __name__ == '__main__':
    # data_history = searchHistory()
    # data_click = click_academies()
    # data_favorite = favorite_academy()
    # data_appointment = appointments()
    data_reviews = reviews(100, 30)

    # print(data_history.loc[data_history['AcademyId'] == 3].values)
    # print(data_click)
    # print(data_favorite)
    # print(data_appointment)
    print(data_reviews)
