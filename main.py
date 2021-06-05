from html.parser import HTMLParser
import urllib.request
import os.path
import time

class MyHTMLParser(HTMLParser):
    LinkToDownload="None"

    def handle_data(self, data):
        finalLink="None"
        if "document, player" in data:
            listAll=data.split(",{")
            for each in listAll:
                if "mp4" in each:
                    props=each.split(",")
                    if '"width":720' in props:
                        for eachProp in props:
                            if '"url":' in eachProp and "mp4" in eachProp:
                                finalLink=eachProp.split('"')[3]
                                if "https" in finalLink and "mp4" in finalLink: 
                                    self.LinkToDownload=finalLink
    
    def getLink(self):
        return self.LinkToDownload
                                    
                                

                      

while True:
    print("Waiting for File")
    time.sleep(1)
    for file in os.listdir(r"C:\Users\Jonathan\Documents\vt"):
        if ".txt" in file:
            print ("File exist")
            fullPath=os.path.join(r"C:\Users\Jonathan\Documents\vt", file)
            f = open(fullPath, "r")
            parser = MyHTMLParser()
            parser.feed(f.read())
            link=parser.getLink()
            print(link)
            if link != "None":
                print("Downloading: %s"%link)
                req=urllib.request.urlretrieve(link, os.path.join(r"C:\Users\Jonathan\Documents\vt", file.split(".")[0]+'.mp4'))
                print(req)
            f.close()
            os.remove(os.path.join(r"C:\Users\Jonathan\Documents\vt", file))
