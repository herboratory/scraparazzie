[![PyPI](https://img.shields.io/badge/PyPi-v1.12-f39f37.svg)](https://pypi.org/project/scraparazzie/1.2.7/)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/herboratory/scaparazzie/blob/master/LICENSE.txt)

# scraparazzie

Here I would like to special thank for [Nikhil Kumar Singh](https://github.com/nikhilkumarsingh)'s work.

This package is based on the package [gnewsclient](https://github.com/nikhilkumarsingh/gnewsclient) for modification. which is also an easy-to-use python client for [Google News feeds](https://news.google.com/). This package offers specific topic feeds and keyword query, and the result shows from latest to oldeest datetime order.

For other services and projects, please visit: https://herboratory.ai/.

## Installation

To install scraparazzie, simply with the command below:
```
$ pip install scraparazzie
```

## Usage
Application of this package is similar as gnewsclient:

- Create a NewsClient object:
    For specific topic:
    ```python
    >>> from scraparazzie import scraparazzie
    >>> client = scraparazzie.NewsClient(language = 'english', location = 'Canada', topic = 'Business', max_results = 3)
    ```
    For keyword query: 
    ```python
    >>> from scraparazzie import scraparazzie
    >>> client = scraparazzie.NewsClient(language = 'english', location = 'Canada', query = 'corn', max_results = 3)
    ```
- Get current parameter settings
    ```python
    >>> client.get_config()
    {'location': 'Cananda', 'language': 'english', 'topic': 'Business'}
    ```

- Get news feed
    ```python
    >>> client.print_news()
    Corn Acres Should Be Reconsidered in 2020
    Farm Bureau News
    https://www.fb.org/market-intel/corn-acres-should-be-reconsidered-in-2020
    Wed, 15 Apr 2020 14:03:04 GMT
    ------------------------------------------------------------
    Plant 2020 Questions (Have you seen Corn, Durum Prices?)
    FarmLead
    https://farmlead.com/blog/breakfast-brief/plant-2020-april-durum-prices/
    Wed, 15 Apr 2020 14:00:41 GMT
    ------------------------------------------------------------
    Good year for growing, but corn $$$ low
    Quinte News
    https://www.quintenews.com/2020/04/15/good-year-for-growing-but-corn-low/
    Wed, 15 Apr 2020 10:07:48 GMT
    ------------------------------------------------------------
    ```

- Changing parameters
    Please aware that query is first priority for the news feed. So if there are both input of query and topic, only query result will show.

    ```python
    >>> client.location = 'Canada'
    >>> client.language = 'english'
    >>> client.topic = 'Business'
    >>> client.query = 'corn'
    >>> client.print_news()
    Corn Acres Should Be Reconsidered in 2020
    Farm Bureau News
    https://www.fb.org/market-intel/corn-acres-should-be-reconsidered-in-2020
    Wed, 15 Apr 2020 14:03:04 GMT
    ------------------------------------------------------------
    Plant 2020 Questions (Have you seen Corn, Durum Prices?)
    FarmLead
    https://farmlead.com/blog/breakfast-brief/plant-2020-april-durum-prices/
    Wed, 15 Apr 2020 14:00:41 GMT
    ------------------------------------------------------------
    Good year for growing, but corn $$$ low
    Quinte News
    https://www.quintenews.com/2020/04/15/good-year-for-growing-but-corn-low/
    Wed, 15 Apr 2020 10:07:48 GMT
    ------------------------------------------------------------
    ```

- Export as list
    Items can be export as list by using client.export_news():

    ```python
    >>> items = client.export_news()
    >>> print(items)
    [{'title': 'Corn Acres Should Be Reconsidered in 2020', 'source': 'Farm Bureau News', 'link': 'https://www.fb.org/market-intel/corn-acres-should-be-reconsidered-in-2020', 'publish_date': 'Wed, 15 Apr 2020 14:03:04 GMT'}, {'title': 'Plant 2020 Questions (Have you seen Corn, Durum Prices?)', 'source': 'FarmLead', 'link': 'https://farmlead.com/blog/breakfast-brief/plant-2020-april-durum-prices/', 'publish_date': 'Wed, 15 Apr 2020 14:00:41 GMT'}, {'title': 'Good year for growing, but corn $$$ low', 'source': 'Quinte News', 'link': 'https://www.quintenews.com/2020/04/15/good-year-for-growing-but-corn-low/', 'publish_date': 'Wed, 15 Apr 2020 10:07:48 GMT'}]
    ```

- Get list of available locations, languages and topics
    ```python
    >>> client.locations
    ['Australia', 'Botswana', 'Canada', 'Ethiopia', 'Ghana', 'India ', 'Indonesia', 'Ireland', 'Israel', 'Kenya', 'Latvia',
     'Malaysia', 'Namibia', 'New Zealand', 'Nigeria', 'Pakistan', 'Philippines', 'Singapore', 'South Africa', 'Tanzania', 'Uganda', 
     'United Kingdom', 'United States', 'Zimbabwe', 'Czech Republic', 'Germany', 'Austria', 'Switzerland', 'Argentina', 'Chile',
     'Colombia', 'Cuba', 'Mexico', 'Peru', 'Venezuela', 'Belgium ', 'France', 'Morocco', 'Senegal', 'Italy', 'Lithuania', 
     'Hungary', 'Netherlands', 'Norway', 'Poland', 'Brazil', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Sweden', 'Vietnam',
     'Turkey', 'Greece', 'Bulgaria', 'Russia', 'Ukraine ', 'Serbia', 'United Arab Emirates', 'Saudi Arabia', 'Lebanon', 'Egypt',
     'Bangladesh', 'Thailand', 'China', 'Taiwan', 'Hong Kong', 'Japan', 'Republic of Korea']
    >>> client.languages
    ['english', 'indonesian', 'czech', 'german', 'spanish', 'french', 'italian', 'latvian', 'lithuanian', 'hungarian', 'dutch', 
    'norwegian', 'polish', 'portuguese brasil', 'portuguese portugal', 'romanian', 'slovak', 'slovenian', 'swedish', 'vietnamese', 
    'turkish', 'greek', 'bulgarian', 'russian', 'serbian', 'ukrainian', 'hebrew', 'arabic', 'marathi', 'hindi', 'bengali', 'tamil', 
    'telugu', 'malyalam', 'thai', 'chinese simplified', 'chinese traditional', 'japanese', 'korean']
    >>> client.topics
    ['Top Stories',
     'World',
     'Nation',
     'Business',
     'Technology',
     'Entertainment',
     'Sports',
     'Science',
     'Health']
    ```
# Tips for searching
1. For better result of topics seraching, please set the language as local/native language of the location, e.g. 'chinese traditional' for 'Hong Kong', 'english' for United Kingdom instead of 'english' for 'Hong Kong', 'chinese traditional' for "United Kingdom'.

2. For better searching of non-local/native language new of the location, for example searching English news of Hong Kong, please use search feature, e.g. query = "South China Morning Post", query = "Hong Kong Standard". The result can be shown if you search like query = "South China Morning Post Hong Kong Standard", but not as good as search individually. It is also available to search with specific keywords, e.g. query = "South China Morning Post virus", query = "Hong Kong Standard virus".

# Change log

1.2.1：
- Readme.md revision

1.2.2：
- Export list
- Readme.md revision

1.2.3:
- Readme.md revision

1.2.4:
- Fixed important bug

1.2.5
- Fixed important bug

1.2.6
- improvement for better search experience

1.2.7
- Fixed the bug that is unable to load data
- Fixed the bug in query feature
- Update README.md with searching tips