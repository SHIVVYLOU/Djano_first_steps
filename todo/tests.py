# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
    
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)