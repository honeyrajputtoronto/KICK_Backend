"""Testing adding"""

from calc import add
from django.test import SimpleTestCase

class calcTest(SimpleTestCase):

    def test_add(self):

        res = add(5,6)
        self.assertEqual(res, 11)