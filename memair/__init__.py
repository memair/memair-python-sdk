import json
import requests
import hashlib
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from datetime import datetime, timedelta, date


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
    if len(access_token) not in [43, 64]:
      raise MemairError(f'access_token wrong length. access_token should be either a 64 length hex string or a 43 length base64 string, supplied access_token was {len(access_token)} characters.')

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


def is_dns_blocked(date):
  salt = 'dns.memair.com'
  start_date = datetime(2019,1,1).date()
  state_change_count = 0

  delta = date - start_date

  for i in range(delta.days + 1):
    date         = start_date + timedelta(i)
    change_state = __state_should_change(date, salt)

    if change_state:
      state_change_count += 1

  return state_change_count % 2 != 0


def __state_should_change(date, salt):
  salted_date_string = (date.strftime('%Y-%m-%d') + salt).encode('utf-8')
  salted_date_hex = hashlib.md5(salted_date_string).hexdigest()
  return int(salted_date_hex[-1], 16) % 4 == 0
