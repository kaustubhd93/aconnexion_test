import re
import os
from bs4 import BeautifulSoup


class Helper():
    def get_file_path(self, fileName):
        currentDir = os.getcwd()
        fileConfig = {"file1.txt" : currentDir + "/content/file1.txt",
                    "file2.txt": currentDir + "/content/file2.txt",
                    "file3.txt": currentDir + "/content/file3.txt",
                    "file4.txt": currentDir + "/content/file4.txt"}
        if re.match(r'file[1-4]\.txt', fileName):
            return fileConfig[fileName]
        else:
            return None

    def get_all_content(self, filePath, startLine=None, endLine=None):
        with open(filePath, "r") as fileData:
            if not startLine and not endLine:
                content = fileData.read()
            else:
                tmpTxt = fileData.readlines()
                if startLine >= 0 and endLine <= len(tmpTxt):
                    tmpContent = tmpTxt[startLine:endLine]
                    content = "".join(tmpContent)
                else:
                    content = "<h2> Value for start or end is incorrect. </h2> \
<p> It should be between 0 and {} inclusive </p>".format(len(tmpTxt))
            isHtml = bool(BeautifulSoup(content, "html.parser").find())
            if isHtml:
                contentType = "html"
            else:
                contentType = "plain" 
        return {"content": content, "type": "text/" + contentType}
                
