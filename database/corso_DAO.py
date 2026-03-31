# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


class corsoDao():
    @staticmethod
    def getAllCorsi():
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM corso"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(codIns = row["codins"], crediti = row["crediti"], nome = row["nome"], pd = row["pd"]))

        cursor.close()
        cnx.close()

        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)

            query = """SELECT s.*FROM studente s , iscrizione i WHERE s.matricola = i.matricola and i.codins = %s"""

            cursor.execute(query, (codins,))

            res = []
            for row in cursor:
                res.append(Studente(row["matricola"],row["cognome"],row["nome"],row["CDS"]))

            cursor.close()
            cnx.close()
            return res

        # QUERY PUNTO 3
       # SELECT *
    # FROM corso c, iscrizione i
    # where c.codins = i.codins and matricola = 168630


