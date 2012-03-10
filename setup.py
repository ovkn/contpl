from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(name='contpl',
      version='1.0',
      description='Command-line templates processor',
      long_description=long_description,
      author='OVK',
      author_email='me@ovk.name',
      url='https://github.com/ovkn/contpl',
      scripts=['contpl'])
