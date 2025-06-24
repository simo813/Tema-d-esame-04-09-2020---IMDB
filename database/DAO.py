from database.DB_connect import DBConnect
from model.film import Film



class DAO:

    @staticmethod
    def getNodes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select m.id , m.name 
                        from imdb_0408.movies m 
                        where m.`rank` is not null 
                        order by m.name 
                                                    """
            cursor.execute(query,)

            for row in cursor:
                result.append(Film(row["id"], row["name"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getEdges(rank):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select m.id as one, m2.id as two, count(distinct(r.actor_id)) as weight
                        from imdb_0408.movies m, imdb_0408.roles r, imdb_0408.movies m2, imdb_0408.roles r2
                        where  m.rank >= %s
                                and m2.rank >= %s
                                and m.id = r.movie_id
                                and m2.id = r2.movie_id
                                and r.actor_id = r2.actor_id
                                and m.id <> m2.id
                                and m.id > m2.id
                        group by m.id, m2.id
                        having count(distinct(r.actor_id)) > 0
                                                        """
            cursor.execute(query, (rank, rank))

            for row in cursor:
                result.append((row["one"], row["two"], row["weight"]))
            cursor.close()
            cnx.close()
        return result





