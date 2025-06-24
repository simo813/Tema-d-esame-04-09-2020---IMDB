from database.DB_connect import DBConnect



class DAO:

    @staticmethod
    def getGenres():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select g.GenreId , g.Name, (min(t.Milliseconds)/1000) as minD 
                        from itunes.genre g, itunes.track t 
                        where g.GenreId = t.GenreId 
                        group by g.GenreId , g.Name
                        order by g.Name 
                                                    """
            cursor.execute(query,)

            for row in cursor:
                result.append((row["GenreId"], row["Name"], row["minD"]))
            cursor.close()
            cnx.close()
        return result


