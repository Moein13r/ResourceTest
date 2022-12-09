import glob
import re
import lxml
from bs4 import BeautifulSoup
import glob
import json
from deep_translator import GoogleTranslator
import os
root = ''
with open('temp2.txt','r',encoding='utf8') as f:  
    root = lxml.etree.fromstring(f.read())
xml=''
newSet=dict()
for word in root:
    newSet[word.attrib['name'].lower()]=word.find('value').text
print(newSet)
for word in newSet:    
    xml += """/// <summary>
                ///   Looks up a localized string similar to {value}.
                /// </summary>
                internal static string {key} {{
                    get {{
                        return ResourceManager.GetString("{key2}", resourceCulture);
                    }}
        }}\n""".format(key2=word, key=word.strip().replace(' ', '_'), value=newSet[word])    
with open('temp.txt','w',encoding='utf8') as f:  
    f.write(xml)
