import unittest

from exactitude import languages


class LanguagesTest(unittest.TestCase):

    def test_validate(self):
        self.assertTrue(languages.validate('de'))
        self.assertTrue(languages.validate('en'))
        self.assertFalse(languages.validate('us'))
        self.assertFalse(languages.validate(None))

    def test_cleam(self):
        self.assertEquals(languages.clean('de'), 'de')
        self.assertEquals(languages.clean('xx'), None)
        self.assertEquals(languages.clean(None), None)
