"""
The root of forum tests.
"""
import unittest

from djangobb_forum.tests.postmarkup import PostmarkupTestCase

def suite():
    cases = (PostmarkupTestCase,
            )
    tests = unittest.TestSuite(
        unittest.TestLoader().loadTestsFromTestCase(x)\
        for x in cases)
    return tests