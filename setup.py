from setuptools import setup

with open('README.md').read() as long_desc:
    long_description = long_desc

setup(name='seems-legit-cache',
      version='0.1.0',
      description="A dict-based cache that's probably fine to use",
      long_description=long_description,
      author='Luc Perkins',
      author_email='lucperkins@gmail.com',
      license='MIT',
      packages=['seemslegitcache'],
      url='https://github.com/lucperkins/seems-legit-cache',
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'expiringdict'
      ])
