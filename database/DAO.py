from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto


class DAO():

    @staticmethod
    def getAllNodes(id1,id2):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select *
                   from airports
                    where ID=%s or ID=%s"""

        cursor.execute(query, (id1,id2))

        for row in cursor:
            res.append(Aeroporto(**row))
            # res.append(ArtObject(object_id=row["object_id"], ...))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getAllEdgesPesati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select origin_airport_id as origin, destination_airport_id as destination, sum(distance) as peso, count(*) as volte
                    from flights f 
                    group by origin , destination"""
        cursor.execute(query)

        for row in cursor:
            result.append((row["origin"], row["destination"], row["peso"], row["volte"]))
        cursor.close()
        conn.close()
        return result

