import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGELOG.rst')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'waitress',
    'redis',
    'python-mpd2', # Python interface with MPD
    ]

setup(name='mpd-box',
      version='0.1.2',
      description='MPD-Box start a song in Music Player Daemon by simply scanning a NFC tag.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Environment :: No Input/Output (Daemon)",
        "Topic :: Multimedia :: Sound/Audio :: Players :: MP3",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        ],
      author='Sebastien BARBIER',
      author_email='mdp-box@sebastienbarbier.com',
      url='',
      keywords='MPD MPD-box NFC Music',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="mpd_box",
      # Executable stuff :)
      scripts = [
          'scripts/mpd-box',
          'scripts/mpd-box-daemon'
        ],
      )
