import unittest
from lundpy import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        quotes = [
        "Code is like humor. When you have to explain it, it’s bad. - Cory House",
        "Fix the cause, not the symptom. A thing to do. - Steve Maguire",
        "Optimism is an occupational hazard of programming. A test. - Kent Beck",
        "Simplicity is the soul of efficiency. - Austin Freeman"]
        self.assertIn(response.data, quotes)

if __name__ == "__main__":
    unittest.main()
