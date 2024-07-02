from database.DAO import DAO
from model.model import Model

myModel = Model()
myModel.creaGrafo(2010, "circle")
printPesi=myModel.pesiArchiAdiacenti()
printPesi.sort(key=lambda x: x[0])

for a in printPesi:
    print(a)

