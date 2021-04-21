import scrapy

class UrlSpider(scrapy.Spider):
  name = 'badlist'
  start_urls = ["https://eumostwanted.eu/"]

  def parse(self, response):

    links = response.xpath('//a/@href')
    json = ""
    
    for link in links:
      url = link.get()
      if any(prefix in url for prefix in ["https://eumostwanted.eu"]):
        json += "{url}\n".format(url=url)

    with open("data.html", "w") as page:
      page.write(json)
      page.close()