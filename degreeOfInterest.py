from sqlConnection import CRUD
import pandas as pd


# 스마트 리뷰 미포함
def interest():

    db = CRUD()

    # 학원 노출 수
    search_history, serach_history_column = db.readDB(
        schema='haksoop', table='"search-histories"', column='id, "AcademyId", searched_number')
    df_search_history = pd.DataFrame(
        search_history, columns=['id', 'AcademyId', 'searched_number'])

    # PDP 진입 유저수
    click_academy, click_academy_column = db.readDB(
        schema='haksoop', table='"click-academies"', column='*')
    df_click_academy = pd.DataFrame(
        click_academy, columns=click_academy_column)

    academy_id_list = set(df_search_history['AcademyId'].values)
    interest_list = []
    for academy_id in academy_id_list:
        interest_exposure = df_search_history.loc[df_search_history['AcademyId']
                                                  == academy_id]['searched_number'].values[0]
        interest_user = len(
            df_click_academy.loc[df_click_academy['AcademyId'] == academy_id]['academy_clicked'] == True)
        if interest_exposure == 0:
            interestScore == None
        else:
            interestScore = interest_user/interest_exposure * 30
        interest_list.append(
            {'AcademyId': academy_id, 'interest_user': interest_user, 'interest_exposure': interest_exposure, 'interestScore': interestScore})

    df_interest = pd.DataFrame(interest_list, columns=[
                               'AcademyId', 'interest_user', 'interest_exposure', 'interestScore'])
    df_interest.fillna(0)
    df_interest.to_csv(
        './result/interest.csv', encoding='CP949', index=False)
    return df_interest

# 스마트 리뷰 포함


def interest_smart():

    db = CRUD()

    # 학원 노출 수
    search_history, serach_history_column = db.readDB(
        schema='haksoop', table='"search-histories"', column='id, "AcademyId", searched_number')
    df_search_history = pd.DataFrame(
        search_history, columns=['id', 'AcademyId', 'searched_number'])

    # PDP 진입 유저수
    click_academy, click_academy_column = db.readDB(
        schema='haksoop', table='"click-academies"', column='*')
    df_click_academy = pd.DataFrame(
        click_academy, columns=click_academy_column)

    academy_id_list = set(df_search_history['AcademyId'].values)
    interest_list = []
    for academy_id in academy_id_list:
        interest_exposure = df_search_history.loc[df_search_history['AcademyId']
                                                  == academy_id]['searched_number'].values[0]
        interest_user = len(
            df_click_academy.loc[df_click_academy['AcademyId'] == academy_id]['academy_clicked'] == True)
        if interest_exposure == 0:
            interestScore == None
        else:
            interestScore = interest_user/interest_exposure * 10
        interest_list.append(
            {'AcademyId': academy_id, 'interest_user': interest_user, 'interest_exposure': interest_exposure, 'interestScore': interestScore})

    df_interest = pd.DataFrame(interest_list, columns=[
                               'AcademyId', 'interest_user', 'interest_exposure', 'interestScore'])
    df_interest.fillna(0)
    df_interest.to_csv(
        './result/interest.csv', encoding='CP949', index=False)
    return df_interest

# 더미데이터 스마트리뷰 미포함


def interest_v2(df_search_history, df_click_academy):

    # 학원 노출 수    df_search_history

    # PDP 진입 유저수  df_click_academy

    academy_id_list = set(df_search_history['AcademyId'].values)
    interest_list = []
    for academy_id in academy_id_list:
        interest_exposure = df_search_history.loc[df_search_history['AcademyId']
                                                  == academy_id]['searched_number'].values[0]
        interest_user = len(
            df_click_academy.loc[df_click_academy['AcademyId'] == academy_id]['academy_clicked'] == True)
        if interest_exposure == 0:
            interestScore == None
        else:
            interestScore = interest_user/interest_exposure * 30
        interest_list.append(
            {'AcademyId': academy_id, 'interest_user': interest_user, 'interest_exposure': interest_exposure, 'interestScore': interestScore})

    df_interest = pd.DataFrame(interest_list, columns=[
                               'AcademyId', 'interest_user', 'interest_exposure', 'interestScore'])
    df_interest.fillna(0)
    df_interest.to_csv(
        './result/interest.csv', encoding='CP949', index=False)
    return df_interest

# 더미데이터 스마트리뷰 포함


def interest_smart_v2(df_search_history, df_click_academy):

    # 학원 노출 수    df_search_history

    # PDP 진입 유저수  df_click_academy

    academy_id_list = set(df_search_history['AcademyId'].values)
    interest_list = []
    for academy_id in academy_id_list:
        interest_exposure = df_search_history.loc[df_search_history['AcademyId']
                                                  == academy_id]['searched_number'].values[0]
        interest_user = len(
            df_click_academy.loc[df_click_academy['AcademyId'] == academy_id]['academy_clicked'] == True)
        if interest_exposure == 0:
            interestScore == None
        else:
            interestScore = interest_user/interest_exposure * 10
        interest_list.append(
            {'AcademyId': academy_id, 'interest_user': interest_user, 'interest_exposure': interest_exposure, 'interestScore': interestScore})

    df_interest = pd.DataFrame(interest_list, columns=[
                               'AcademyId', 'interest_user', 'interest_exposure', 'interestScore'])
    df_interest.fillna(0)
    df_interest.to_csv(
        './result/interest.csv', encoding='CP949', index=False)
    return df_interest
