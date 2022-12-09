import glob
import re
import asyncio
import glob
import json
from deep_translator import GoogleTranslator
import os


def ReadAllFilesPersianSubStringsFromFolder(FileName, FolderPath=r"C:\Users\USER\source\repos\Madakto-co\MadaktoTS\MadaktoTS.UI\Pages\Reports\Personnel\*.aspx"):
    items = set()
    for itm in glob.glob(FolderPath):
        with open(itm, encoding='utf8') as f:
            content = f.read()
            tempStr = ''
            for i in range(len(content)):
                if content[i] >= 'آ' and content[i] <= 'ی' or content[i] == ' ':
                    tempStr += content[i]
                else:
                    if tempStr != '':
                        items.add(tempStr.strip())
                        tempStr = ''
    items.remove('')
    WordsLen = str(len(items))
    jsonStr = '{\"Words\":['
    c = 1
    for word in items:
        print(str(c)+' Word of '+str(WordsLen))
        jsonStr += str(json.dumps({'Persian': word, 'English': GoogleTranslator(
            source='fa', target='en').translate(word)}, ensure_ascii=False)+',')
        c += 1
    jsonStr += ']}'
    if not os.path.exists(FileName):
        os.mknod(FileName)
    with open(FileName, 'w', encoding='utf8') as f:
        f.write(jsonStr)


FilesName = [
    'test.json',
    'test2.json',
    'test3.json',
    'test4.json',
    'test5.json',
    'test6.json',
    'test7.json',
    'test8.json',
    'test9.json',
    'test10.json',
    'test11.json']
c = 1
for fileName in FilesName:
    content = ''
    with open(fileName, encoding='utf8') as f:
        content = json.loads(f.read())
    xml = ''
    for item in content['Words']:        
        xml += """/// <summary>
                ///   Looks up a localized string similar to {value}.
                /// </summary>
                internal static string {key} {{
                    get {{
                        return ResourceManager.GetString("{key2}", resourceCulture);
                    }}
        }}\n""".format(key2=item['English'], key=item['English'].replace(' ', '_'), value=item['Persian'])
    XmlFileName = r'CsharpFile{counter}.txt'.format(counter=c)
    with open(XmlFileName, 'w', encoding='utf8') as f:
        f.write(xml)
    c += 1
