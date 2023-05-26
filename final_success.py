import json, os
from jsonFormat import jsonFormat

def printPauseExit(s: str = ""):
    print(s)
    input()
    exit()


absPathStr = os.path.dirname(__file__)

filePath = input("請輸入愈讀取的.json檔案: ")
if (not os.path.isabs(filePath)):
    filePath = absPathStr + "\\" + filePath
if ((not os.path.isfile(filePath))):
    printPauseExit("找無此文件")

outputPath = input("請輸入愈寫入的.json檔案: ")
if (not os.path.isabs(outputPath)):
    outputPath = absPathStr + "\\" + outputPath

try:
    with open(filePath, "r", encoding="utf-8") as fp:
        if (fp.readable()): 
            try:
                j = json.load(fp)
            except json.decoder.JSONDecodeError:
                printPauseExit("讀取失敗，請確認檔案內容是否正確")
except FileNotFoundError:
    printPauseExit("讀取失敗，請確認檔案是否存在")

jsonObj = jsonFormat(j)
try:
    json.loads(jsonObj.get())
except json.decoder.JSONDecodeError:
    printPauseExit("出現了例外錯誤-jsonFormat")

with open(outputPath, "w", encoding="utf-8") as fo:
    if (fo.writable()): 
        fo.write(jsonObj.get())
        print("轉換完成")
input() # pause


