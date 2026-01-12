from database.DB_connect import DBConnect
from model.state import Stato

class DAO:
    @staticmethod
    def get_anni_forme():
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct year(s_datetime) as year, shape
                    from sighting
                    group by s_datetime """

        cursor.execute(query)

        for row in cursor:
            year = row['year']
            shape = row['shape']
            if year not in result:
                result[year] = []
                result[year].append(shape)
            else:
                result[year].append(shape)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_coppie():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select state1, s1.lat as lat1, s1.lng as lng1, state2, s2.lat as lat2, s2. lng as lng2
                    from neighbor n, state s1, state s2
                    where n.state1 = s1.id and n.state2 = s2.id"""

        cursor.execute(query)

        for row in cursor:
            id1 = row['state1']
            id2 = row['state2']
            lat1 = row['lat1']
            lng1 = row['lng1']
            lat2 = row['lat2']
            lng2 = row['lng2']
            stato1 = Stato(id1, lat1, lng1)
            stato2 = Stato(id2, lat2, lng2)
            lista_coppie = [stato1, stato2]
            result.append(lista_coppie)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_coppie_peso(year, shape, stato1, stato2):
        conn = DBConnect.get_connection()

        totale = 0

        cursor = conn.cursor(dictionary=True)
        query = """ select count(*) as totale
                    from sighting
                    where shape = %s and year(s_datetime) = %s and (state = %s or state = %s)"""

        cursor.execute(query,(str(shape), int(year), str(stato1), str(stato2), ))

        for row in cursor:
            totale = row['totale']

        cursor.close()
        conn.close()
        return totale

    @staticmethod
    def get_stati():
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """ select id, lat, lng
                    from state """

        cursor.execute(query)

        for row in cursor:
            state = Stato(row['id'], row['lat'], row['lng'])
            result[row["id"]] = state

        cursor.close()
        conn.close()
        return result
