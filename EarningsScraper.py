import requests
from lxml import html


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
    
    

# pull the listing page for the earning transcripts
page = requests.get("https://seekingalpha.com/earnings/earnings-call-transcripts")
pageHtml = html.fromstring(page.content)
anchors = pageHtml.xpath('//a[@class="dashboard-article-link"]')

#a = anchors[0]
for a in anchors:
    suffixLink = a.attrib["href"]
    filename = a.text + ".txt"
    scrapeTranscript(suffixLink, filename)