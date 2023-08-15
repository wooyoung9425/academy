from sqlConnection import CRUD
import pandas as pd

# 스마트리뷰 미포함


def participation():
    db = CRUD()

    #### DB에서 필요한 테이블 가져오기 #######
    # PDP진입
    click_academy, click_academy_column = db.readDB(
        schema='haksoop', table='"click-academies"', column='*')
    df_click_academy = pd.DataFrame(
        click_academy, columns=click_academy_column)

    # 관심학원
    favorite_academy, favorite_academy_column = db.readDB(
        schema='haksoop', table='"favorite-academy"', column='*')
    df_favorite_academy = pd.DataFrame(
        favorite_academy, columns=favorite_academy_column)

    # 상담예약
    appointment_academy, appointment_column = db.readDB(
        schema='haksoop', table='appointments', column='*'
    )
    df_appointment = pd.DataFrame(
        appointment_academy, columns=appointment_column)

    #### 학원지수 공식 변수들 계산 ##########
    # pdp 진입한 총 유저수
    pdpUser_id_list = set(df_click_academy['UserId'].values)
    pdpUser_num = len(pdpUser_id_list)

    academy_id_list = set(df_click_academy['AcademyId'].values)
    academy_score = []

    for id in academy_id_list:
        # 학원별 pdp진입 유저수
        user_num = len(
            df_click_academy.loc[df_click_academy['AcademyId'] == id])

        # 리뷰탭 수
        reviewTab_acadmey = df_click_academy.loc[df_click_academy['AcademyId']
                                                 == id]
        reviewTab_num = len(
            reviewTab_acadmey.loc[reviewTab_acadmey['reviewTab_clicked'] == True])

        # 관심학원 등록수 = 학원 id에 따른 유저수
        favorite_user_num = len(
            df_favorite_academy.loc[df_favorite_academy['academyId'] == id])

        # 상담예약 수
        appointment_num = len(
            df_appointment.loc[df_appointment['academyId'] == id])
        participationScore = (((reviewTab_num+favorite_user_num +
                              appointment_num)/3)/int(pdpUser_num))*40
        # print(participationScore)
        academy_score.append({'AcademyId': id, 'pdp_user_num': user_num, 'reviewTab_clicked': reviewTab_num, 'favoriteNum': favorite_user_num,
                             'appointment': appointment_num, 'participationScore': participationScore})
    df_academy_score = pd.DataFrame(
        academy_score, columns=['AcademyId', 'pdp_user_num', 'reviewTab_clicked', 'favoriteNum', 'appointment', 'participationScore'])

    df_academy_score.fillna(0)
    df_academy_score.to_csv(
        './result/participation.csv', encoding='CP949', index=False)
    return df_academy_score

# 스마트리뷰 포함


def participation_smart():
    db = CRUD()

    #### DB에서 필요한 테이블 가져오기 #######
    # PDP진입
    click_academy, click_academy_column = db.readDB(
        schema='haksoop', table='"click-academies"', column='*')
    df_click_academy = pd.DataFrame(
        click_academy, columns=click_academy_column)

    # 관심학원
    favorite_academy, favorite_academy_column = db.readDB(
        schema='haksoop', table='"favorite-academy"', column='*')
    df_favorite_academy = pd.DataFrame(
        favorite_academy, columns=favorite_academy_column)

    # 상담예약
    appointment_academy, appointment_column = db.readDB(
        schema='haksoop', table='appointments', column='*'
    )
    df_appointment = pd.DataFrame(
        appointment_academy, columns=appointment_column)

    #### 학원지수 공식 변수들 계산 ##########
    # pdp 진입한 총 유저수
    pdpUser_id_list = set(df_click_academy['UserId'].values)
    pdpUser_num = len(pdpUser_id_list)

    academy_id_list = set(df_click_academy['AcademyId'].values)
    academy_score = []

    for id in academy_id_list:
        # 학원별 pdp진입 유저수
        user_num = len(
            df_click_academy.loc[df_click_academy['AcademyId'] == id])

        # 리뷰탭 수
        reviewTab_acadmey = df_click_academy.loc[df_click_academy['AcademyId']
                                                 == id]
        reviewTab_num = len(
            reviewTab_acadmey.loc[reviewTab_acadmey['reviewTab_clicked'] == True])

        # 관심학원 등록수 = 학원 id에 따른 유저수
        favorite_user_num = len(
            df_favorite_academy.loc[df_favorite_academy['academyId'] == id])

        # 상담예약 수
        appointment_num = len(
            df_appointment.loc[df_appointment['academyId'] == id])
        participationScore = (((reviewTab_num+favorite_user_num +
                              appointment_num)/3)/int(pdpUser_num))*10
        # print(participationScore)
        academy_score.append({'AcademyId': id, 'pdp_user_num': user_num, 'reviewTab_clicked': reviewTab_num, 'favoriteNum': favorite_user_num,
                             'appointment': appointment_num, 'participationScore': participationScore})
    df_academy_score = pd.DataFrame(
        academy_score, columns=['AcademyId', 'pdp_user_num', 'reviewTab_clicked', 'favoriteNum', 'appointment', 'participationScore'])

    df_academy_score.fillna(0)
    df_academy_score.to_csv(
        './result/participation.csv', encoding='CP949', index=False)
    return df_academy_score

# 더미데이터


def participation_v2(df_click_academy, df_favorite_academy, df_appointment):

    # PDP진입 df_click_academy
    # 관심학원 df_favorite_academy
    # 상담예약 df_appointment

    #### 학원지수 공식 변수들 계산 ##########
    # pdp 진입한 총 유저수
    pdpUser_id_list = set(df_click_academy['UserId'].values)
    pdpUser_num = len(pdpUser_id_list)

    academy_id_list = set(df_click_academy['AcademyId'].values)
    academy_score = []

    for id in academy_id_list:
        # 학원별 pdp진입 유저수
        user_num = len(
            df_click_academy.loc[df_click_academy['AcademyId'] == id])

        # 리뷰탭 수
        reviewTab_acadmey = df_click_academy.loc[df_click_academy['AcademyId']
                                                 == id]
        reviewTab_num = len(
            reviewTab_acadmey.loc[reviewTab_acadmey['reviewTab_clicked'] == True])

        # 관심학원 등록수 = 학원 id에 따른 유저수
        favorite_user_num = len(
            df_favorite_academy.loc[df_favorite_academy['academyId'] == id])

        # 상담예약 수
        appoint = df_appointment.loc[df_appointment['academyId'] == id]
        appointment_num = len(
            appoint.loc[appoint['status'] != 'cancel'])

        participationScore = (((reviewTab_num+favorite_user_num +
                              appointment_num)/3)/int(user_num))*40
        # print(participationScore)
        academy_score.append({'AcademyId': id, 'pdp_user_num': user_num, 'reviewTab_clicked': reviewTab_num, 'favoriteNum': favorite_user_num,
                             'appointment': appointment_num, 'participationScore': participationScore})
    df_academy_score = pd.DataFrame(
        academy_score, columns=['AcademyId', 'pdp_user_num', 'reviewTab_clicked', 'favoriteNum', 'appointment', 'participationScore'])

    df_academy_score.fillna(0)
    df_academy_score.to_csv(
        './result/participation.csv', encoding='CP949', index=False)
    return df_academy_score


def participation_smart_v2(df_click_academy, df_favorite_academy, df_appointment):

    # PDP진입 df_click_academy
    # 관심학원 df_favorite_academy
    # 상담예약 df_appointment

    #### 학원지수 공식 변수들 계산 ##########
    # pdp 진입한 총 유저수
    pdpUser_id_list = set(df_click_academy['UserId'].values)
    pdpUser_num = len(pdpUser_id_list)

    academy_id_list = set(df_click_academy['AcademyId'].values)
    academy_score = []

    for id in academy_id_list:
        # 학원별 pdp진입 유저수
        user_num = len(
            df_click_academy.loc[df_click_academy['AcademyId'] == id])

        # 리뷰탭 수
        reviewTab_acadmey = df_click_academy.loc[df_click_academy['AcademyId']
                                                 == id]
        reviewTab_num = len(
            reviewTab_acadmey.loc[reviewTab_acadmey['reviewTab_clicked'] == True])

        # 관심학원 등록수 = 학원 id에 따른 유저수
        favorite_user_num = len(
            df_favorite_academy.loc[df_favorite_academy['academyId'] == id])

        # 상담예약 수
        appoint = df_appointment.loc[df_appointment['academyId'] == id]
        appointment_num = len(
            appoint.loc[appoint['status'] != 'cancel'])

        participationScore = (((reviewTab_num+favorite_user_num +
                              appointment_num)/3)/int(user_num))*15
        # print(participationScore)
        academy_score.append({'AcademyId': id, 'pdp_user_num': user_num, 'reviewTab_clicked': reviewTab_num, 'favoriteNum': favorite_user_num,
                             'appointment': appointment_num, 'participationScore': participationScore})
    df_academy_score = pd.DataFrame(
        academy_score, columns=['AcademyId', 'pdp_user_num', 'reviewTab_clicked', 'favoriteNum', 'appointment', 'participationScore'])

    df_academy_score.fillna(0)
    df_academy_score.to_csv(
        './result/participation.csv', encoding='CP949', index=False)
    return df_academy_score
