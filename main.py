'''
Copyright 2021 Jonathan Moran Silva

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

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
    for file in os.listdir(r"C:\Users\Jonathan\Documents"):
        if ".txt" in file:
            print ("File exist")
            fullPath=os.path.join(r"C:\Users\Jonathan\Documents", file)
            f = open(fullPath, "r")
            parser = MyHTMLParser()
            parser.feed(f.read())
            link=parser.getLink()
            print(link)
            if link != "None":
                print("Downloading: %s"%link)
                req=urllib.request.urlretrieve(link, os.path.join(r"C:\Users\Jonathan\Documents", file.split(".")[0]+'.mp4'))
                print(req)
            f.close()
            os.remove(os.path.join(r"C:\Users\Jonathan\Documents", file))
