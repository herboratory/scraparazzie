from scraparazzie import scraparazzie

client = scraparazzie.NewsClient(language ="English", location = "Hong Kong", query = "Hong Kong Standard", max_results = 20)
client.print_news()
items = client.export_news()