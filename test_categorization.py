
import unittest

from surfer import categorize_url_slug

class TestCategorizeUrlSlug(unittest.TestCase):
    def test_ticketmaster(self):
        url = "https://www.ticketmaster.com/sierra-ferrell-shoot-for-the-moon-north-charleston-south-carolina-09-13-2025/event/2D006230B7C543CD"
        self.assertEqual(categorize_url_slug(url), "ticketmaster")

    def test_livenation(self):
        url = "https://concerts.livenation.com/tyler-childers-on-the-road-camden-new-jersey-09-24-2025/event/0200616B900B16DD"
        self.assertEqual(categorize_url_slug(url), "livenation")

    def test_uncategorized(self):
        url = "https://www.example.com/event/123"
        self.assertIsNone(categorize_url_slug(url))

if __name__ == '__main__':
    unittest.main()

