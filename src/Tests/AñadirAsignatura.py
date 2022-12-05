import unittest
from src.Modelo.Asignatura import Asignatura

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
        self.session = Session ()

        self.asignatura1 = Asignatura (id = 'AS001', nombre = "ArquitecturaEmpresarial" , nota = 12, credito = 4, promedio =[])
        self.asignatura2 = Asignatura (id = 'AS002', nombre = "RedesDelComputador" , nota = 14, credito = 5, promedio =[])
        self.asignatura3 = Asignatura (id = 'AS003', nombre = "ConstruccionDeSoftware" , nota = 16, credito = 4, promedio =[])
        self.asignatura4 = Asignatura (id = 'AS004', nombre = "SistemasOperativos" , nota = 11, credito = 3, promedio =[])

        self.session.add (self.asignatura1)
        self.session.add (self.asignatura2)
        self.session.add (self.asignatura3)
        self.session.add (self.asignatura4)

        self.session.conmit()
        self.session.close()

    def tearDown (self):
        self.session = Session ()

        busqueda = self.session.query (Asignatura).all()

        for Asignatura in busqueda:
            self.session.delete (Asignatura)

        self.session.conmit
        self.session.close


if __name__ == '__main__':
    unittest.main()
