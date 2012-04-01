try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Michael Lennon',
    'url': 'URL to get at it',
    'download_url': 'Where to download it',
    'author_email': 'mlennon3@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages':, ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
