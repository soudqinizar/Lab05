from database.corso_DAO import corsoDao
from database.studente_DAO import studenteDao


class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return corsoDao.getAllCorsi()

    def getStudentiCorso(self, codins):
        return corsoDao.getStudentiCorso(codins)


    def getStudentiDataMatricola(self, matricola):
        return studenteDao.getStudentiDataMatricola(matricola)























    def getCodins(self):
        return corsoDao.getCodins()


    def getCorsiPd(self, pd):
        return corsoDao.getCorsiPD(pd)

    def getCorsiPDwithIscritti(self, pd):
        return corsoDao.getCorsiPDwithIscritti(pd)



    def getCDSofCorso(self, codins):
        cds = corsoDao.getCDSofCorso(codins)
        cds.sort(key=lambda c: c[1], reverse=True)
        return cds
