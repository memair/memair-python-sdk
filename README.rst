=================
Memair Python SDK
=================

.. image:: https://badge.fury.io/py/memair.svg
    :target: https://badge.fury.io/py/memair

.. image:: http://img.shields.io/badge/license-MIT-yellow.svg?style=flat
    :target: https://github.com/memair/memair-python-sdk/blob/master/LICENSE

.. image:: https://img.shields.io/badge/contact-Gregology-blue.svg?style=flat
    :target: http://gregology.net/contact/

Overview
--------

SDK for simple interaction with the Memair APIs

Interactive Notebook
--------------------

Explore this package in an  `Interactive Notebook <https://mybinder.org/v2/gh/memair/jupyter/master>`__

.. image:: https://user-images.githubusercontent.com/1595448/47387817-6b88a080-d6de-11e8-822d-ddd4f83fbd9b.png
         :width: 80%

Hosted by `binder <https://mybinder.org>`__

Installation
------------

``memair`` is available on PyPI

http://pypi.python.org/pypi/memair

Install via ``pip``
::

    $ pip install memair

Or via ``easy_install``
::

    $ easy_install memair

Or directly from ``memair``'s `git repo <https://github.com/memair/memair-python-sdk>`__
::

    $ git clone git://github.com/memair/memair-python-sdk.git
    $ cd memair
    $ python setup.py install

Basic usage
-----------

`Generate a temporary access token <https://memair.com/generate_own_access_token>`__

`Validate GraphQL with GraphiQL <https://memair.com/graphiql>`__

::

    >>> from memair import Memair
    >>> api_key = '0000000000000000000000000000000000000000000000000000000000000000'
    >>> user = Memair(api_key)
    >>> latest_location = user.query('''
            {
                Locations(first: 1, order: timestamp_desc) {
                lat
                lon
                timestamp
              }
            }
        ''')
    >>> latest_location['data']['Locations'][0]
    {'lat': 42.909056, 'lon': -74.572508, 'timestamp': '2018-07-27T22:27:21Z'}



Running Test
------------
::

    $ python tests.py

Python compatibility
--------------------

Developed for Python 3. May work but not tested in Python 2.
