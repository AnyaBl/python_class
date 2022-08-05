import requests
from unittest import TestCase
from unittest.mock import patch
from http import cookies

names = ['GPS', 'YSC', 'VISITOR_INFO1_LIVE', 'MNC']


class Cookies(TestCase):

    def setUp(self):
        respond = requests.get("https://www.youtube.com/")
        self.cookies_dict = respond.cookies._cookies
        self.mock_cookie_MNC = cookies.SimpleCookie()
        self.mock_cookie_MNC['MNC'] = 'MNC'
        self.mock_cookie_MNC['MNC'].domain = '.youtube.com'
        self.mock_cookie_MNC['MNC'].secure = True
        self.mock_cookie_MNC['MNC'].version = 1

    # Задача 1.
    def test_cookies_contain_GPS(self):
        self.assertTrue(names[0] in self.cookies_dict['.youtube.com']['/'].keys())

    def test_cookies_contain_YSC(self):
        self.assertTrue(names[1] in self.cookies_dict['.youtube.com']['/'].keys())

    def test_cookies_contain_VISITOR_INFO1_LIVE(self):
        self.assertTrue(names[2] in self.cookies_dict['.youtube.com']['/'].keys())

    def test_cookies_contain_MNC(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_cookie_MNC):
            self.assertTrue(names[3] in self.cookies_dict['.youtube.com']['/'].keys())

    # Задача 2.
    def test_cookies_domain_in_GPS(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[0]].domain, '.youtube.com')

    def test_cookies_domain_in_YSC(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[1]].domain, '.youtube.com')

    def test_cookies_domain_in_VISITOR_INFO1_LIVE(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[2]].domain, '.youtube.com')

    def test_cookies_secure_in_GPS(self):
        self.assertTrue(self.cookies_dict['.youtube.com']['/'][names[0]].secure)

    def test_cookies_secure_in_YCS(self):
        self.assertTrue(self.cookies_dict['.youtube.com']['/'][names[1]].secure)

    def test_cookies_secure_in_VISITOR_INFO1_LIVE(self):
        self.assertTrue(self.cookies_dict['.youtube.com']['/'][names[2]].secure)

    def test_cookies_version_in_GPS(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[0]].version, 0)

    def test_cookies_version_in_YCS(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[1]].version, 0)

    def test_cookies_version_in_VISITOR_INFO1_LIVE(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[2]].version, 0)

    # Задача 3.
    def test_cookies_MNC_domain(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_cookie_MNC):
            self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[3]].domain, '.youtube.com')

    def test_cookies_MNC_secure(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_cookie_MNC):
            self.assertTrue(self.cookies_dict['.youtube.com']['/'][names[3]].secure)

    def test_cookies_MNC_version(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_cookie_MNC):
            self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[3]].version, 1)
