import unittest
import os
import ejercicio3
import tempfile

class ejercicio3TestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, paginaEstatica.app.config['DATABASE'] = tempfile.mkstemp()
        ejercicio3.app.config['TESTING'] = True
        self.app = ejercicio3.app.test_client()
        #paginaEstatica.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(ejercicio3.app.config['DATABASE'])

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_name_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/user/manuel')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
