import biashara
import unittest
import json
from biashara import *

class biashara(unittest.TestCase):

 def test_home(self):
    test = app.test_client()
    response = test.get('/')
    self.assertEqual(response.status_code, 200)


 def test_createbuinsess(self):
    test = app.test_client()
    response = test.get('/business')
    self.assertEqual(response.status_code, 200)


 def test_viewbusiness(self):
    test = app.test_client()
    response = test.get('/business')
    self.assertEqual(response.status_code, 200)


 def test_viewonebusiness(self):
    test = app.test_client()
    response = test.get('/business/1')
    self.assertEqual(response.status_code, 200)


 def test_updatebusiness(self):
    test = app.test_client()
    response = test.get('/business/1')
    self.assertEqual(response.status_code, 200)


 def test_deletebusiness(self):
    test = app.test_client()
    response = test.get('/business')
    self.assertEqual(response.status_code, 200)


if __name__=='__main__':
    unittest.main()
