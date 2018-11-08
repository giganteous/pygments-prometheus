from setuptools import setup, find_packages

setup(name='pygments-prometheus',
      version='1.0',
      description='Pygments lexer for prometheus metrics',
      long_description=open('README.rst').read() + '\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
      ],
      keywords='pygments prometheus',
      author='Kai Storbeck',
      author_email='kai@xs4all.nl',
      url='https://github.com/giganteous/pygments-prometheus',
      license='BSD',
      py_modules=['prom'],
      zip_safe=True,
      install_requires=[
          'setuptools',
          'pygments',
      ],
      tests_require=[
          'nose',
      ],
      entry_points={
          'pygments.lexers': 'prometheus=prom:PrometheusLexer',
      },
)
