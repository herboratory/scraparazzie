import bs4
from bs4 import BeautifulSoup as soup
from datetime import datetime
from fuzzywuzzy import process
import argparse
import requests
from .utils import locationMap, langMap, topicMap, top_news_url, topic_url, query_url

class NewsClient:
    def __init__(self, location = 'United States', language = 'english', topic = 'Top Stories', query = 'wheat', max_results = 5):
        """
        client initialization
        """
        # list of available locations, languages and topics
        self.locations = list(locationMap)
        self.languages = list(langMap)
        self.topics = list(topicMap)

        # setting initial configuration
        self.location = location
        self.language = language
        self.topic = topic
        self.query = query

        # other settings
        self.max_results = max_results

    def get_config(self):
        """
        function to get current configuration
        """
        config = {
            'location': self.location,
            'language': self.language,
            'topic': self.topic,
            'query': self.query
        }
        return config

    @property
    def params_dict(self):
        """
        function to get params dict for HTTP request
        """
        location_code = 'US'
        language_code = 'en'
        if len(self.location):
            location_code = locationMap[process.extractOne(self.location, self.locations)[0]]
        if len(self.language):
            language_code = langMap[process.extractOne(self.language, self.languages)[0]]
        params = {
            'hl': language_code,
            'gl': location_code,
            'ceid': '{}:{}'.format(location_code, language_code)
        }
        return params

    def get_news(self):
        """
        function to get news articles
        """
        if self.query:
            query_item_url = query_url + self.query
            resp = requests.get(query_item_url, params = self.params_dict)
            xml_page = resp.content
        elif self.topic is None or self.topic == 'Top Stories':
            resp = requests.get(top_news_url, params = self.params_dict)
            xml_page = resp.content
            #Client = urlopen(top_news_url, params = self.params_dict)
            #xml_page = Client.read()
            #Client.close()
        else:
            topic_code = topicMap[process.extractOne(self.topic, self.topics)[0]]
            resp = requests.get(topic_url.format(topic_code), params = self.params_dict)
            xml_page = resp.content
            #Client = urlopen(topic_url.format(topic_code), params = self.params_dict)
            #xml_page = Client.read()
            #Client.close()

        #return self.parse_feed(resp.content)
        soup_page = soup(xml_page,"xml")
        news_list = soup_page.findAll("item")
        return news_list

    def print_news(self):
        news_items = self.get_news()
        NEWS_LIMIT = self.max_results   
        items = []         
        for news in news_items[:NEWS_LIMIT]:
            title = news.title.text.split(' - ', 1)[0]
            source = news.source.text
            link = news.link.text
            pubdate = news.pubDate.text
                   
            item = {       
                    'title': title,
                    'source': source,
                    'link': link,
                    'publish_date': pubdate,
            }              

        ## item output checkpoint
        #    for k, v in item.items():
        #        print("{}: {}".format(k.capitalize(), v))
                        
        #    print("-" * 60)
                   
            items.append(item)
                   
        sorted_items = sorted(items, key = lambda x: datetime.strptime(x['publish_date'], "%a, %d %b %Y %H:%M:%S %Z"), reverse = True)

        for print_item in sorted_items[:NEWS_LIMIT]:
            print(print_item['title'])
            print(print_item['source'])
            print(print_item['link'])
            print(print_item['publish_date'])

def main():
    parser = argparse.ArgumentParser(description="Google News Client CLI!")

    parser.add_argument("-loc", "--location", type = str, default = 'United States',
                        help = "Set news location.")

    parser.add_argument("-lang", "--language", type = str, default = 'english',
                        help = "Set news language.")

    parser.add_argument("-t", "--topic", type = str, default = 'Top Stories',
                        help = "Set news topic.")

    parser.add_argument("-sloc", "--show-locations", action = 'store_true',
                        help = "Show location choices")

    parser.add_argument("-slang", "--show-languages", action = 'store_true',
                        help = "Show language choices")

    parser.add_argument("-st", "--show-topics", action = 'store_true',
                        help = "Show topic choices")

    args = parser.parse_args()
    args_dict = vars(args)

    if args_dict['show_locations']:
        print("\n".join(locationMap.keys()))

    elif args_dict['show_languages']:
        print("\n".join(langMap.keys()))

    elif args_dict['show_topics']:
        print("\n".join(topicMap.keys()))

    client = NewsClient(location = args_dict['location'], language = args_dict['language'], topic = args_dict['topic'])
    client.print_news()


if __name__ == "__main__":
    main()