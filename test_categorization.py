
import unittest

from surfer import categorize_url_slug

class TestCategorizeUrlSlug(unittest.TestCase):
    def test_ticketmaster(self):
        url = "https://www.ticketmaster.com/event/abc"
        self.assertEqual(categorize_url_slug(url), "ticketmaster")

    def test_livenation(self):
        url = "https://www.livenation.com/event/xyz"
        self.assertEqual(categorize_url_slug(url), "livenation")

    def test_uncategorized(self):
        url = "https://www.example.com/event/123"
        self.assertIsNone(categorize_url_slug(url))

if __name__ == '__main__':
    unittest.main()

