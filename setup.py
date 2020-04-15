from setuptools import setup


def readme():
    with open('README.md') as f:
        descr = f.read()
    return descr


setup(name = 'scraparazzie',
      version = '1.2.1',
      classifiers = [
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
      ],
      keywords = 'google news feed python client feed',
      description = 'Python client for specific topic and keyword query in Google News Feed.',
      long_description = readme(),
      long_description_content_type = "text/markdown",
      url = 'https://herboratory.ai/',
      author = 'Inger Noire',
      author_email = 'herboratory@gmail.com',
      license = 'MIT',
      packages = ['scraparazzie'],
      install_requires = ['beautifulsoup4', 'requests', 'fuzzywuzzy'],
      include_package_data = True,
      zip_safe = False,
      entry_points = {
          'console_scripts': [
              'scraparazzi = scraparazzie.scraparazzie:main'
          ],
      }
      )
