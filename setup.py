from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='SubScraper',
    version='2.0.1',
    author = 'm8r0wn',
    author_email = 'm8r0wn@protonmail.com',
    description = 'Subdomain Enumeration Tool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/m8r0wn/subscraper',
    license='GPLv3',
    packages=['subscraper'],
    package_data={
      'subscraper': ['resources/*']
    },
    isntall_requires=[
        'bs4',
        'dnspython',
        'requests',
        'censys'
    ],
    classifiers = [
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Security"
    ],
    entry_points= {
        'console_scripts': ['subscraper=subscraper:main']
    }
)