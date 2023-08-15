
import psycopg2
from databases import Database
import pandas as pd


class Databases():
    def __init__(self):
        # conn = sqlite3.connect()
        self.db = psycopg2.connect(host='database-haksoop-staging.cntaiwovhafm.ap-northeast-2.rds.amazonaws.com',
                                   dbname='haksoop', user='wmakers', password='Haksoop12!', port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    # SQL 명령을 처리하기 위해 execute  함수를 구현
    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    # commit 함수
    def commit(self):
        self.cursor.commit()


class CRUD(Databases):
    # Read (Select, 조회)
    def readDB(self, schema, table, column):
        sql = "SELECT {column} from {schema}.{table}".format(
            column=column, schema=schema, table=table)
        print(sql)

        try:
            self.cursor.execute(sql)
            if column == '*':
                totalColumn = [column[0] for column in self.cursor.description]
            else:
                totalColumn = column
            result = self.cursor.fetchall()

        except Exception as e:
            result = ("read DB err : ", e)

        return result, totalColumn

    # insert 추가
    def insertDB(self, schema, table, column, data):
        sql = "INSERT INTO {schema}.{table}({column}) VALUES ('{data}')".format(
            schema=schema, table=table, column=column, data=data)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" insert DB err : ", e)

    # update 수정
    def updateDB(self, schema, table, column, value, condition):
        sql = " UPDATE {schema}.{table} SET {column}='{value}' WHERE {column}='{condition}'".format(
            schema=schema, table=table, column=column, value=value, condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" update DB err : ", e)

    # Delete 삭제
    def deleteDB(self, schema, table, condition):
        sql = " delete from {schema}.{table} where {condition}".format(
            schema=schema, table=table, condition=condition)
        try:
            self.cursor.excute(sql)
            self.db.commit()
        except Exception as e:
            print(" delete DB err : ", e)


if __name__ == "__main__":
    db = CRUD()
    academies, totalColumn = (
        db.readDB(schema='haksoop', table='academies', column='*'))
    df_academies = pd.DataFrame(academies, columns=totalColumn)

    search_history, serach_history_column = db.readDB(
        schema='haksoop', table='"search-histories"', column='id, "AcademyId", searched_number')
    df_search_history = pd.DataFrame(
        search_history, columns=['id', 'AcademyId', 'searched_number'])

    click_academy, click_academy_column = db.readDB(
        schema='haksoop', table='"click-academies"', column='*')
    df_click_academy = pd.DataFrame(
        click_academy, columns=click_academy_column)

    # 참여도 계산
    # pdp 진입한 총 유저수
    pdpUser_id_list = set(df_click_academy['UserId'].values)

    # 리뷰탭 클릭수
