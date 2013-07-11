try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'webassets require JS filter',
    'author': 'William Pullen',
    'url': 'https://github.com/billpull/webassets-require-js',
    'download_url': 'https://github.com/billpull/webassets-require-js',
    'author_email': 'billpull',
    'version': '0.1',
    'install_requires': ['webassets'],
    'packages': ['webassets_require'],
    'scripts': [],
    'name': 'webassets-require',
    'license': 'MIT'
}

setup(**config)