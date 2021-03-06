from setuptools import setup

setup(name='rsd-pandoc-tool',
      version='0.01',
      description='Scons module assisting UCL RSD papers and talks',
      author='James Hetherington',
      author_email='j.hetherington@ucl.ac.uk',
      packages=['rsdpandoc'],
      package_data={
      'rsdpandoc':
      	[
      		'assets/*'
      	]
      }
)