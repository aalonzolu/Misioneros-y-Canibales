from setuptools import setup

setup(name='misioneros-y-canibales',
      version='0.1',
      description='Juegos de misioneros y canibales',
      url='https://github.com/lexoalonzo/Misioneros-y-Canibales',
      author='Lexo Alonzo',
      author_email='lexo@io.gt',
      license='MIT',
      scripts=['misioneros-y-canibales/gm-misionero','misioneros-y-canibales/modulocanibal.py'],
      packages=['misioneros-y-canibales'],
      package_dir={'misioneros-y-canibales': 'misioneros-y-canibales'},
      package_data={'': ['resource/*.jpg','resource/*.png','misioneros-y-canibales/resource/*']},
      py_modules = ['misioneros-y-canibales/modulocanibal'],
      zip_safe=False,
      include_package_data = True)
