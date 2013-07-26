try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Webassets require JS filter',
    'long_description': 'Forked from billpull, https://github.com/billpull/webassets-require-js',
    'author': 'Svante Paldan',
    'url': 'https://github.com/zwant/webassets-require-js',
    'download_url': 'https://github.com/zwant/webassets-require-js',
    'author_email': 'zwant',
    'version': '0.2',
    'install_requires': ['webassets'],
    'packages': ['webassets_require'],
    'package_data': {
        "webassets_require": [
            "lib/*.jar",
            "lib/*.js",
        ]
    },
    'scripts': [],
    'name': 'webassets-require',
    'license': 'MIT'
}

setup(**config)