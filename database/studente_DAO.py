# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class studenteDao():
    @staticmethod
    def getStudentiDataMatricola(matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * FROM studente where matricola = %s"""
        cursor.execute(query, (matricola,))

        res = None
        for row in cursor:
            res = (Studente(matricola=row["matricola"], nome=row["nome"], cognome=row["cognome"], CDS=row["CDS"]))

        cursor.close()
        cnx.close()

        return res

