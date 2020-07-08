import json
from flask import Flask, request, Response
from common import Helper

app = Flask(__name__)
hlp = Helper()

@app.route("/v1/get-html-content", methods=["GET"])
def get_html_content():
    try:
        if request.args:
            if len(request.args) == 1:
                fileName = request.args.get("fileName")
                filePath = hlp.get_file_path(fileName)
                if filePath:
                    allText = hlp.get_all_content(filePath)
                    return Response(allText["content"], mimetype = allText["type"])
                else:
                    return "File name not valid. Please enter valid file format file<1-4>.txt"
            else:
                fileName = request.args.get("fileName")
                startLine = int(request.args.get("start"))
                endLine = int(request.args.get("end"))
                filePath = hlp.get_file_path(fileName)
                if filePath:
                    specText = hlp.get_all_content(filePath, startLine, endLine)
                    return Response(specText["content"], mimetype = specText["type"])
                else:
                    return "File name not valid. Please enter valid file format file<1-4>.txt"
                
        else:
            filePath = hlp.get_file_path("file1.txt")
            allText = hlp.get_all_content(filePath)
            return Response(allText["content"], mimetype = allText["type"])
    except Exception as e:
        errorMessage = "<h2> Something went wrong here </h2> \
<p> {} </p>".format(str(e))
        return Response(errorMessage, mimetype= "text/html")

if __name__ == "__main__":
    app.run("0.0.0.0")
