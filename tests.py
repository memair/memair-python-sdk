import unittest
from vcr_unittest import VCRTestCase
from random import shuffle
from datetime import date

from memair import Memair, MemairError, is_dns_blocked

class TestMemair(VCRTestCase):

  def test_welformed_access_token(self):
    hex_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    shuffle(hex_characters)
    hex_valid_access_token = ''.join(4 * hex_characters)
    Memair(hex_valid_access_token)

    base64_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '-']
    shuffle(base64_characters)
    base64_valid_access_token = ''.join(base64_characters[0:43])
    Memair(hex_valid_access_token)

  def test_error_raise_for_missing_access_token(self):
    with self.assertRaises(MemairError):
      Memair(None)

  def test_error_raise_for_short_access_token(self):
    short_access_token = '0123456789abcdef'
    with self.assertRaises(MemairError):
      Memair(short_access_token)

  def test_query(self):
    valid_access_token = '0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef'
    query = '{BiometricTypes(){slug}}'
    response = Memair(valid_access_token).query(query)
    biometric_types = response['data']['BiometricTypes']

    self.assertTrue(len(biometric_types), 4)
    self.assertTrue(biometric_types[0]['slug'], 'diastolic_pressure')

  def test_is_dns_blocked(self):
    self.assertTrue(is_dns_blocked(date(2019,1,9)))
    self.assertFalse(is_dns_blocked(date(2019,1,10)))
    self.assertFalse(is_dns_blocked(date(2019,1,11)))
    self.assertTrue(is_dns_blocked(date(2019,1,12)))

    self.assertTrue(is_dns_blocked(date(2019,5,6)))
    self.assertFalse(is_dns_blocked(date(2019,5,7)))
    self.assertTrue(is_dns_blocked(date(2019,5,8)))
    self.assertFalse(is_dns_blocked(date(2019,5,9)))
    self.assertTrue(is_dns_blocked(date(2019,5,10)))


if __name__ == '__main__':
    unittest.main()
