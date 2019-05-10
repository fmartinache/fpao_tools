import sys

from setuptools import setup

setup(name='fpao_tools',
      version='1.0.0', # defined in the __init__ module
      description='Tools for focal plane based adaptative optics',
      url='http://github.com/fmartinache/fpao_tools',
      author='Frantz Martinache',
      author_email='frantz.martinache@oca.eu',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Professional Astronomers',
          'Topic :: High Angular Resolution Astronomy :: Interferometry',
          'Programming Language :: Python :: 3.6'
      ],
      packages=['fpao_tools'],
      install_requires=['xara', 'xaosim', 'numpy',
                        'scipy', 'matplotlib',
                        'astropy', 'pyqtgraph', 'PyQt5'],
      scripts=["bin/qtzap", "bin/whack"],
      data_files = [('config', ['config/zap.ui', 'config/MrT_fool.png', 'config/scexao_asym_kmodel.fits',
                                'config/whack.ui', 'config/Rambo.png'])],
      include_package_data=True,
      zip_safe=False)

