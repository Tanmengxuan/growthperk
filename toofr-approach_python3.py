
# This Python file uses the following encoding: utf-8

# ## Anyway u can start scraping for sales related personal for company size above 10?
# # Workflow
# # 1. Use bing to generate
# #
#
# import sys, json, csv
# from bing_web_search_api import Client
#
# apikey = 'Your Ocp-Apim-Subscription-Key'
# client = Client(apikey='adb7950db602499293d32a30a7f1c5a5')
#
# def convert(data):
#   if isinstance(data, bytes):      return data.decode()
#   if isinstance(data, (str, int)): return str(data)
#   if isinstance(data, dict):       return dict(map(convert, data.items()))
#   if isinstance(data, tuple):      return tuple(map(convert, data))
#   if isinstance(data, list):       return list(map(convert, data))
#   if isinstance(data, set):        return set(map(convert, data))
#


def xray_linkedin_url_bing(title,industry,location):
    title = title.strip().replace(" ", "+")
    industry = industry.strip().replace(" ", "+")
    location = location.strip().replace(" ", "+")
    return 'site:linkedin.com “{0}” “location {2}” {1} -dir'.format(title,industry,location)
 #
# def bing_get_urls(query,output_filename, limit):
#     offset=0
#     if limit == 0:
#         limit = sys.maxsize
#     try:
#         with open(output_filename, 'w') as writefile:
#             while offset<limit:
#                 response, content = client.search(q=query,count=50,offset=offset)
#                 print(json.dumps(json.loads(convert(content)),indent=4))
#                 # print(json.loads(convert(content))["webPages"]["value"])
#                 for i in json.loads(convert(content))["webPages"]["value"]:
#                     writefile.write("{0}\n".format(i["url"]))
#                 offset+=50
#     except:
#         pass
#
#
#
# bing_get_urls(target,"HR-Logistics-Singapore.txt", 1000)
# target = (xray_linkedin_url_bing("Human Resource","Logistics","Singapore"))


#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
#import urllib,urllib2
import urllib.parse
import urllib.request

def search(query, output_filename):
    number = 1

    with open(output_filename, 'w')as writefile:
        while number<2000:
            print (number)
            #address = "http://www.bing.com/search?q={0}&first={1}".format((urllib.quote_plus(query)),number)
            address = "http://www.bing.com/search?q={0}&first={1}".format((urllib.parse.quote(query)),number) #formating the url, number(11) : the 11th search result


            #getRequest = urllib2.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
            getRequest = urllib.request.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}) #thebrowser

            #urlfile = urllib2.urlopen(getRequest)
            urlfile = urllib.request.urlopen(getRequest) #opening the request
            htmlResult = urlfile.read(200000) #reading from the result, html file
            #print(htmlResult)
            urlfile.close()

            soup = BeautifulSoup(htmlResult,"lxml") #parser

            [s.extract() for s in soup('span')] #extract span elements from file
            #print(soup)
            unwantedTags = ['strong', 'cite'] #remove tags from html files
            for tag in unwantedTags:
                for match in soup.findAll(tag):
                    match.replaceWithChildren() #replace with nothing

            results = soup.findAll('li', { "class" : "b_algo" }) #list, class-tagsb_algo
            for result in results:
                print(result)
                # print str(result.find('a')).split('"')[1]
                writefile.write(str(result.find('a')).split('"')[3]+"\n")
            number+=11

if __name__=='__main__':

    print(xray_linkedin_url_bing("HR Business Partner","","Singapore"))
    search(xray_linkedin_url_bing("HR Business Partner","","Singapore"), "outputfile-HRBizPrac.txt")
    # print(xray_linkedin_url_bing("COO", "", "Singapore"))
    # search(xray_linkedin_url_bing("COO", "", "Singapore"), "outputfile-COO.txt")


    # print(xray_linkedin_url_bing("Owner","Jewelry","Singapore"))
    # search(xray_linkedin_url_bing("Owner","Jewelry","Singapore"), "outputfile-jewel-owner.txt")
    # print(xray_linkedin_url_bing("Director", "Jewelry", "Singapore"))
    # search(xray_linkedin_url_bing("Director", "Jewelry", "Singapore"), "outputfile-jewel-director.txt")
    # print(xray_linkedin_url_bing("Marketing", "Jewelry", "Singapore"))
    # search(xray_linkedin_url_bing("Marketing", "Jewelry", "Singapore"), "outputfile-jewel-marketing.txt")


    # print(xray_linkedin_url_bing("Owner","Aesthetic Clinic","Singapore"))
    # search(xray_linkedin_url_bing("Owner","Aesthetic Clinic","Singapore"), "outputfile-AC-owner.txt")
    # print(xray_linkedin_url_bing("Director", "Aesthetic Clinic", "Singapore"))
    # search(xray_linkedin_url_bing("Director", "Aesthetic Clinic", "Singapore"), "outputfile-AC-director.txt")
    # print(xray_linkedin_url_bing("Marketing", "Aesthetic Clinic", "Singapore"))
    # search(xray_linkedin_url_bing("Marketing", "Aesthetic Clinic", "Singapore"), "outputfile-AC-marketing.txt")
    #
    #
    # print(xray_linkedin_url_bing("Owner","Gym","Singapore"))
    # search(xray_linkedin_url_bing("Owner","Gym","Singapore"), "outputfile-Gym-owner.txt")
    # print(xray_linkedin_url_bing("Director", "Gym", "Singapore"))
    # search(xray_linkedin_url_bing("Director", "Gym", "Singapore"), "outputfile-Gym-director.txt")
    # print(xray_linkedin_url_bing("Marketing", "Gym", "Singapore"))
    # search(xray_linkedin_url_bing("Marketing", "Gym", "Singapore"), "outputfile-Gym-marketing.txt")
    #
    #
    # print(xray_linkedin_url_bing("Owner","F&B","Singapore"))
    # search(xray_linkedin_url_bing("Owner","F&B","Singapore"), "outputfile-fnb-owner.txt")
    # print(xray_linkedin_url_bing("Director", "F&B", "Singapore"))
    # search(xray_linkedin_url_bing("Director", "F&B", "Singapore"), "outputfile-fnb-director.txt")
    # print(xray_linkedin_url_bing("Marketing", "F&B", "Singapore"))
    # search(xray_linkedin_url_bing("Marketing", "F&B", "Singapore"), "outputfile-fnb-marketing.txt")
