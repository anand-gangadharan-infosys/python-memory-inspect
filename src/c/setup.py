from distutils.core import setup, Extension
import distutils.log

distutils.log.set_verbosity(-1) # Disable logging in disutils
distutils.log.set_verbosity(distutils.log.DEBUG) # Set DEBUG level

setup(name='helloworld', version='1.0',  \
      ext_modules=[Extension('helloworld', ['NativePythonModule.c'])])