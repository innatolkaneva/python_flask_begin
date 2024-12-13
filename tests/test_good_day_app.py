from good_day_app import app
import unittest
import datetime
from freezegun import freeze_time

weekdays_tuple = ('понедельник','вторник','среда','четверг','пятница','суббота', 'воскресенье')
class TestGoodDayApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/good_day/'
    def test_can_get_user(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time('2024-12-12')
    def get_weekday(self):
        current_day = datetime.datetime.today().weekday()
        return weekdays_tuple[current_day]

    def test_can_get_weekday(self):
        username = 'username'
        weekday = self.get_weekday()[0:-1]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)
