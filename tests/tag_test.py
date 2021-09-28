import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Groceries")
    
    def test_tag_has_name(self):
        self.assertEqual("Groceries", self.tag.name)
    
    def test_tag_has_id(self):
        self.assertEqual(None, self.tag.id)
    
    def test_tag_is_active(self):
        self.assertEqual(True, self.tag.active)