import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from string import hexdigits


class MemairError(Exception):
  pass


class Memair(object):
  def __init__(self, access_token):
    self.__validate_access_token(access_token)
    self.access_token = access_token

  def __validate_access_token(self, access_token):
    if access_token == None:
      raise MemairError('access_token not supplied. Visit https://memair.com/generate_own_access_token to generate a temporary access token or see the https://docs.memair.com')
    if not isinstance(access_token, str):
      raise MemairError('access_token should be string.')
    if len(access_token) != 64:
      raise MemairError(f'access_token wrong length. access_token should be 64 characters, supplied access_token was {len(access_token)} characters.')
    if not all(c in hexdigits for c in access_token):
      raise MemairError('access_token is not hexdigits.')

  def retry_if_connection_error(exception):
    return isinstance(exception, requests.exceptions.ConnectionError) or isinstance(exception, json.decoder.JSONDecodeError)

  def __requests_retry_session(self):
    retries = 10
    backoff_factor = 5
    session = requests.Session()
    retry = Retry(
      total            = retries,
      read             = retries,
      connect          = retries,
      backoff_factor   = backoff_factor,
      status_forcelist = [500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries = retry)
    session.mount('https://', adapter)
    return session

  def query(self, query):
    data = {
      'query': query,
      'access_token': self.access_token
    }
    r = self.__requests_retry_session().post("https://memair.com/graphql", data)
    return json.loads(r.text)
