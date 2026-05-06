from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto


class DAO():

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select *
                   from airports
                    """

        cursor.execute(query)

        for row in cursor:
            res.append(Aeroporto(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllEdgesPesati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select ORIGIN_AIRPORT_ID as origin, DESTINATION_AIRPORT_ID as destination, sum(DISTANCE) as peso, count(*) as volte
                    from flights f 
                    group by ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID 
                    """
        cursor.execute(query)

        for row in cursor:
            result.append((row["origin"], row["destination"], row["peso"], row["volte"]))
        cursor.close()
        conn.close()
        return result

