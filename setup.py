from setuptools import setup, find_packages

setup(
  name='memair',
  version='2018.7.27.0',
  description='SDK for Memair',
  long_description=open('README.rst').read(),
  url='https://github.com/memair/memair-python-sdk',
  author='Greg Clarke',
  author_email='greg@gho.st',
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
  ],
  keywords='memair, quantified self, extended mind, lifelogging',
  packages=find_packages(),
  package_data={
    'memair': []
  }
)
