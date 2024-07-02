from database.DB_connect import DBConnect
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYear():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(YEAR(s.`datetime`)) as year
                    from sighting s 
                    order by YEAR(s.`datetime`)"""

        cursor.execute(query,)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllShape():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(shape)
                    from sighting s 
                    where s.shape != "" """

        cursor.execute(query, )

        for row in cursor:
            result.append(row["shape"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state s  """

        cursor.execute(query, )

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def calcolaPeso(anno, forma, v0, v1):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as peso
                    from sighting s, sighting s1
                    where YEAR(s.datetime)=%s
                    and s.shape=%s
                    and s.state=%s
                    and s1.state=%s
                    and YEAR(s.datetime)=YEAR(s1.`datetime`)
                    and s.shape=s1.shape"""

        cursor.execute(query, (anno, forma, v0, v1) )

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result
