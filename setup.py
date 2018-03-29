from setuptools import setup

setup(name='dynamon',
      version='0.1',
      description='Python API for dynamon.io',
      url='http://github.com/dynamon-io/dynamon-python',
      author='Viktor Qvarfordt',
      author_email='viktor.qvarfordt@gmail.com',
      license='MIT',
      packages=['dynamon', 'requests'],
      zip_safe=False)
