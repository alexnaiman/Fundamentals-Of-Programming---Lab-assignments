import unittest
from Models.Client import Client
from Repositories.Repository import Repository
from Controllers.ClientController import ClientController
from Services.ClientValidator import ClientValidator


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.Client = Client(3, 'name')
        self.repo = Repository('testClients', 'testClients')
        self.controller = ClientController(self.repo)
        if self.controller.getClientById(77) is not False:
            self.controller.removeClient(77)
        if self.controller.getClientById(772) is not False:
            self.controller.removeClient(772)
        if self.controller.getClientById(773) is not False:
            self.controller.removeClient(773)
        if self.controller.getClientById(23) is False:
            self.controller.addClient("23", "name")
        if self.controller.getClientById('233333') is not False:
            self.controller.removeClient('233333')
        if self.controller.getClientById(20) is False:
            self.controller.addClient("20", "name")
        if self.controller.getClientById(200) is False:
            self.controller.addClient("200", "name2")
        if self.controller.getClientById(90) is False:
            self.controller.addClient("90", "name3")
        if self.controller.getClientById(123) is False:
            self.controller.addClient("123", "tion")
        if self.controller.getClientById(234) is False:
            self.controller.addClient("234", "t")
        if self.controller.getClientById(33) is False:
            self.controller.addClient("33", "tit")
        if self.controller.getClientById(90) is not False:
            self.controller.removeClient(99)
        if self.controller.getClientById(323) is False:
            self.controller.addClient("323", "tit")
        if self.controller.getClientById(929) is not False:
            self.controller.removeClient(929)
        if self.controller.getClientById(33) is False:
            self.controller.addClient("333", "tin")
        if self.controller.getClientById(939) is not False:
            self.controller.removeClient(939)

    def test_strClient(self):
        c = Client(2, "lapte")
        self.assertNotEqual(c, Client(3, "lapte"))
        self.assertEqual(str(self.Client), '3, name')

    def test_AddClient(self):
        self.assertEqual(self.controller.addClient('772', 'nume'), True)

    def test_AddClient2(self):
        self.assertEqual(self.controller.addClient('772', 'nume'), True)

    def test_AddClient3(self):
        self.assertEqual(self.controller.addClient('773', 'nume', ), True)

    def test_RemoveClient(self):
        self.assertEqual(self.controller.removeClient(20), True)

    def test_RemoveClient2(self):
        self.assertEqual(self.controller.removeClient(200), True)

    def test_UpdateClient(self):
        self.assertEqual(self.controller.updateClient('23', '233333', "action"), True)

    def test_UpdateClientName(self):
        self.assertEqual(self.controller.updateClientName('90', 'nuuummmeee tesr'), True)

    def test_UpdateClientName2(self):
        self.assertEqual(self.controller.updateClientName('90', 'nuuummmeee test2'), True)

    def test_UpdateClientName3(self):
        self.assertEqual(self.controller.updateClientName('90', 'nuuummmeee test3'), True)

    def test_UpdateClientId(self):
        self.assertEqual(self.controller.updateClientId("33", '99'), True)

    def test_UpdateClientId2(self):
        self.assertEqual(self.controller.updateClientId("323", '929'), True)

    def test_UpdateClientId3(self):
        self.assertEqual(self.controller.updateClientId("333", '939'), None)

    def test_GetAllClients(self):
        repo2 = Repository('ClientUpdateTest', "test2")
        client = Client("2", "223")
        controller2 = ClientController(repo2)
        l = controller2.getAllClients()
        self.assertEqual(controller2.getAllClients(), [client])

    def test_getClientById(self):
        if self.controller.getClientById('11111111') is False:
            self.controller.addClient('11111111', 'sfsdfsf')
        self.assertEqual(self.controller.getClientById('11111111'),
                         Client('11111111', 'sfsdfsf'))

    def test_getClientById2(self):
        if self.controller.getClientById('111211111') is False:
            self.controller.addClient('111211111', 'sfsdfsf')
        self.assertEqual(self.controller.getClientById('111211111'),
                         Client('111211111', 'sfsdfsf'))

    def test_ValidateClient(self):
        self.assertRaises(ValueError, ClientValidator.validate, "", "")
        self.assertRaises(ValueError, ClientValidator.validate, "", ",")
