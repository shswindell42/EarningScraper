import requests
from lxml import html
import time

def scrapeTranscript(linkSuffix, filename):
    prefix = "https://seekingalpha.com"
    link = prefix + linkSuffix
    tsPage = requests.get(link)
    tsHtml = html.fromstring(tsPage.content)
    transcript = tsHtml.xpath("//p/text()")
    text = " ".join(transcript)

    fh = open(filename, "w")
    fh.write(text)
    fh.close()

def scrapeListing(url):
    page = requests.get(url)
    pageHtml = html.fromstring(page.content)
    anchors = pageHtml.xpath('//a[@class="dashboard-article-link"]')

    #a = anchors[0]
    for a in anchors:
        suffixLink = a.attrib["href"]
        filename = a.text + ".txt"
        print("Getting {0}".format(suffixLink))
        scrapeTranscript(suffixLink, filename)
        time.sleep(5)
    
if __name__ == "__main__":
    baseUrl = "https://seekingalpha.com/earnings/earnings-call-transcripts"
    for i in range(1, 1001):
        url = baseUrl
        if i > 1:
            url = baseUrl + "/{0}".format(i)
        
        scrapeListing(url)