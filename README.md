[![PyPI](https://img.shields.io/badge/PyPi-v1.12-f39f37.svg)](https://pypi.python.org/pypi/gnewsclient)
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
The whole 
- Create a NewsClient object:
    For specific topic:
    ```python
    >>> from scraparazzie import scraparazzie
    >>> client = scraparazzie.NewsClient(language = 'english', location = 'Canada', topic = 'Business', max_results = 5)
    ```
    For keyword query: 
    ```python
    >>> from scraparazzie import scraparazzie
    >>> client = scraparazzie.NewsClient(language = 'english', location = 'Canada', query = 'corn', max_results = 5)
    ```
- Get current parameter settings
    ```python
    >>> client.get_config()
    {'location': 'Cananda', 'language': 'english', 'topic': 'Business'}
    ```

- Get news feed
    ```python
    >>> client.print_news()
    All forms of corn exports key to industry, economist says
    Successful Farming
    https://www.agriculture.com/news/crops/all-forms-of-corn-exports-key-to-industry-economist-says
    Tue, 14 Apr 2020 19:59:57 GMT
    Second 2020 Crop Progress Report: Corn at 3% Planted
    Farm Equipment Publication
    https://www.farm-equipment.com/articles/18213-second-2020-crop-progress-report-corn-at-3-planted
    Tue, 14 Apr 2020 19:20:00 GMT
    Can the Market Handle 3 Billion Bushels of New Crop Corn Carryout?
    AgWeb
    https://www.agweb.com/article/can-market-handle-3-billion-bushels-new-crop-corn-carryout
    Tue, 14 Apr 2020 16:04:00 GMT
    Corn School: Get a jump on spring weed control
    RealAgriculture
    https://www.realagriculture.com/2020/04/corn-school-get-a-jump-on-spring-weed-control/
    Tue, 14 Apr 2020 11:40:00 GMT
    How COVID-19 Is Impacting The Ethanol And Corn Producers
    Forbes
    https://www.forbes.com/sites/rrapier/2020/04/12/how-covid-19-is-impacting-the-ethanol-and-corn-producers/
    Sun, 12 Apr 2020 22:07:29 GMT  
    ```

- Changing parameters
    Please aware that query is first priority for the news feed. So if there are both input of query and topic, only query result will show.

    ```python
    >>> client.location = 'Canada'
    >>> client.language = 'english'
    >>> client.topic = 'Business'
    >>> client.query = 'corn'
    >>> client.print_news()
    All forms of corn exports key to industry, economist says
    Successful Farming
    https://www.agriculture.com/news/crops/all-forms-of-corn-exports-key-to-industry-economist-says
    Tue, 14 Apr 2020 19:59:57 GMT
    Second 2020 Crop Progress Report: Corn at 3% Planted
    Farm Equipment Publication
    https://www.farm-equipment.com/articles/18213-second-2020-crop-progress-report-corn-at-3-planted
    Tue, 14 Apr 2020 19:20:00 GMT
    Can the Market Handle 3 Billion Bushels of New Crop Corn Carryout?
    AgWeb
    https://www.agweb.com/article/can-market-handle-3-billion-bushels-new-crop-corn-carryout
    Tue, 14 Apr 2020 16:04:00 GMT
    Corn School: Get a jump on spring weed control
    RealAgriculture
    https://www.realagriculture.com/2020/04/corn-school-get-a-jump-on-spring-weed-control/
    Tue, 14 Apr 2020 11:40:00 GMT
    How COVID-19 Is Impacting The Ethanol And Corn Producers
    Forbes
    https://www.forbes.com/sites/rrapier/2020/04/12/how-covid-19-is-impacting-the-ethanol-and-corn-producers/
    Sun, 12 Apr 2020 22:07:29 GMT  
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