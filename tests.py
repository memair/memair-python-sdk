import unittest
from vcr_unittest import VCRTestCase

from memair import Memair, MemairError

class TestMemair(VCRTestCase):

  def test_welformed_access_token(self):
    valid_access_token = '0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef'
    Memair(valid_access_token)

  def test_error_raise_for_missing_access_token(self):
    with self.assertRaises(MemairError):
      Memair(None)

  def test_error_raise_for_short_access_token(self):
    short_access_token = '0123456789abcdef'
    with self.assertRaises(MemairError):
      Memair(short_access_token)

  def test_error_raise_for_non_hex_access_token(self):
    non_hex_access_token = 'some non hex characters 0000000000000000000000000000000000000000'
    with self.assertRaises(MemairError):
      Memair(non_hex_access_token)

  def test_query(self):
    valid_access_token = '0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef'
    query = '{BiometricTypes(){slug}}'
    response = Memair(valid_access_token).query(query)
    biometric_types = response['data']['BiometricTypes']

    self.assertTrue(len(biometric_types), 4)
    self.assertTrue(biometric_types[0]['slug'], 'diastolic_pressure')


if __name__ == '__main__':
    unittest.main()
