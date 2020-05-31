from django.test import TestCase


class SimpleTest(TestCase):
    """
    Test home, about and timetable pages
    """
    def test_home(self):
        """
        Test home page estatus code
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        """
        Test about page status code
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_timetable(self):
        """
        Test timetable page status code
        """
        response = self.client.get('/timetable/')
        self.assertEqual(response.status_code, 200)
