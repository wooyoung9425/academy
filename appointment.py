from sqlConnection import CRUD
import pandas as pd

# 총 점 대비 비중: 30%
# 상담예약: 모든 appointments
# 상담완료: appointments 의 status 중 consulted, paymentRequest, completed

# 스마트 리뷰 미포함


def appointment():
    db = CRUD()
    # 응대
    appointment_academy, appointment_column = db.readDB(
        schema='haksoop', table='appointments', column='*'
    )
    df_appointment = pd.DataFrame(
        appointment_academy, columns=appointment_column)

    end_status = ['consulted', 'paymentRequest', 'completed']
    status = df_appointment[['academyId', 'status']]
    academy_id = set(status['academyId'])

    appointment = []
    for id in academy_id:
        count = 0
        academy_appointment = status.loc[status['academyId'] == id]
        # 상담예약
        total_appointment = len(academy_appointment)
        for app in academy_appointment['status']:
            if app in end_status:
                count += 1
        appointmentScore = count/total_appointment*30

        appointment.append({'AcademyId': id, 'total_appointment': total_appointment,
                           'appointment_end': count, 'appointmentScore': appointmentScore})

    df_appointment = pd.DataFrame(
        appointment, columns=['AcademyId', 'total_appointment', 'appointment_end', 'appointmentScore'])
    df_appointment.fillna(0)
    df_appointment.to_csv(
        './result/appointment.csv', encoding='CP949', index=False)
    return df_appointment

# 스마트 리뷰 포함


def appointment_smart():
    db = CRUD()
    # 응대
    appointment_academy, appointment_column = db.readDB(
        schema='haksoop', table='appointments', column='*'
    )
    df_appointment = pd.DataFrame(
        appointment_academy, columns=appointment_column)

    end_status = ['consulted', 'paymentRequest', 'completed']
    status = df_appointment[['academyId', 'status']]
    academy_id = set(status['academyId'])

    appointment = []
    for id in academy_id:
        count = 0
        academy_appointment = status.loc[status['academyId'] == id]
        # 상담예약
        total_appointment = len(academy_appointment)
        for app in academy_appointment['status']:
            if app in end_status:
                count += 1
        appointmentScore = count/total_appointment*10

        appointment.append({'AcademyId': id, 'total_appointment': total_appointment,
                           'appointment_end': count, 'appointmentScore': appointmentScore})

    df_appointment = pd.DataFrame(
        appointment, columns=['AcademyId', 'total_appointment', 'appointment_end', 'appointmentScore'])
    df_appointment.fillna(0)
    df_appointment.to_csv(
        './result/appointment.csv', encoding='CP949', index=False)
    return df_appointment


def appointment_v2(df_appointment):

    end_status = ['consulted', 'paymentRequest', 'completed']
    status = df_appointment[['academyId', 'status']]
    academy_id = set(status['academyId'])

    appointment = []
    for id in academy_id:
        count = 0
        academy_appointment = status.loc[status['academyId'] == id]
        # 상담예약
        total_appointment = len(academy_appointment)
        for app in academy_appointment['status']:
            if app in end_status:
                count += 1
        appointmentScore = count/total_appointment*30

        appointment.append({'AcademyId': id, 'total_appointment': total_appointment,
                           'appointment_end': count, 'appointmentScore': appointmentScore})

    df_appointment = pd.DataFrame(
        appointment, columns=['AcademyId', 'total_appointment', 'appointment_end', 'appointmentScore'])
    df_appointment.fillna(0)
    df_appointment.to_csv(
        './result/appointment.csv', encoding='CP949', index=False)
    return df_appointment


def appointment_smart_v2(df_appointment):
    end_status = ['consulted', 'paymentRequest', 'completed']
    status = df_appointment[['academyId', 'status']]
    academy_id = set(status['academyId'])

    appointment = []
    for id in academy_id:
        count = 0
        academy_appointment = status.loc[status['academyId'] == id]
        # 상담예약
        total_appointment = len(academy_appointment)
        for app in academy_appointment['status']:
            if app in end_status:
                count += 1
        appointmentScore = count/total_appointment*5

        appointment.append({'AcademyId': id, 'total_appointment': total_appointment,
                           'appointment_end': count, 'appointmentScore': appointmentScore})

    df_appointment = pd.DataFrame(
        appointment, columns=['AcademyId', 'total_appointment', 'appointment_end', 'appointmentScore'])
    df_appointment.fillna(0)
    df_appointment.to_csv(
        './result/appointment.csv', encoding='CP949', index=False)
    return df_appointment
