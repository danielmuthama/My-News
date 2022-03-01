import unittest
from app.models import Article

class NewsTest(unittest.TestCase):
    """
    Test class to test behavior of class
    """
    def setUp(self):
        """
        run before every test
        """
        self.new_article = Article("News", "https://newslink.com", "main author", "https://url", "22/3/4456" )
    
    def test_instance(self):
        """Test instance"""
        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
        """"
        Test initialization
        """
        self.assertEqual(self.new_article.title, "News")
        self.assertEqual(self.new_article.urlImage, "https://newslink.com")
        self.assertEqual(self.new_article.author, "main author")
        self.assertEqual(self.new_article.url, "https://url")
        self.assertEqual(self.new_article.date, "22/3/4456")

