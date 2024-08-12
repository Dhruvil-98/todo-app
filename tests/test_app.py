import unittest
from app import create_app

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Todo', response.data)

    def test_add_todo(self):
        response = self.client.post('/add', data={'todo': 'Test Todo'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertIn(b'Test Todo', response.data)

    def test_delete_todo(self):
        self.client.post('/add', data={'todo': 'Todo to Delete'})
        response = self.client.post('/delete/0')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertNotIn(b'Todo to Delete', response.data)

if __name__ == '__main__':
    unittest.main()
