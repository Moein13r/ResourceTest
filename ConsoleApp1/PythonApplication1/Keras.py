filePath=r"C:\Users\USER\source\repos\Madakto-co\MadaktoTS\MadaktoTS.UI\Scripts\Attendance\EnterExitShiftEmployees.js"
with open(filePath,'r',encoding='utf8') as f:  
    content=f.read()
funcName='getResx'
ValidChars=['g','e','t','R','s','x']
tempStr=''
words=set()
l=len(content)
i=0
while l>i:
    if content[i] in ValidChars:
        tempStr+=content[i]
    elif funcName==tempStr:
        word=''
        i+=2
        while content[i]!='\"' and content[i]!='\'':
            word+=content[i]
            i+=1
        print(word)
        words.add('Localize('+word+')')
        i+=1
        tempStr=''
    else:
        tempStr=''
    l=len(content)
    i+=1
print(words)
printStr='pushToPublicResxObj(['
for itm in words:
    printStr+=('\''+itm+'\',')
printStr+=']);'
with open('ExtractJsWords.txt','w',encoding='utf8') as f:  
    f.write(printStr)