#!/usr/bin/python

from flask import render_template, request
from uploader_app import app
import subprocess

print(app.config)


@app.route("/", methods=["GET"])
def hello():
    return render_template("index.html", result="")


# https://github.com/jkiddo/ember
@app.route("/upload-ig", methods=["POST"])
def upig():
    data = request.json
    serverBase = data["serverBase"]
    packageId = data["packageId"]
    usePUT = data["usePUT"]
    loadRecursively = data["loadRecursively"]
    packagebase64 = data["packagebase64"]
    if packageId and packagebase64:
        return 404, "Package ID OR package base64 must be provided. Not both."
    if not serverBase:
        return 404, "Server base must be provided."
    if packagebase64:
        # save to disk
        with open("/tmp/package.zip", "wb") as f:
            f.write(packagebase64)

        with open("/tmp/output.log", "w") as output:
            subprocess.call(
                "docker run --rm jkiddo/ember ",
                shell=True,
                stdout=output,
                stderr=output,
            )
            # docker run -v /Users/jkv/.fhir:/home/nonroot/.fhir jkiddo/ember --location=https://build.fhir.org/ig/hl7-eu/gravitate-health/package.tgz

        return 200, "Success"
    if packageId:
        with open("/tmp/output.log", "w") as output:
            subprocess.call(
                "docker run --rm jkiddo/ember --packageId="
                + packageId
                + " --serverBase="
                + serverBase
                + " --usePUT="
                + usePUT
                + " --loadRecursively="
                + loadRecursively,
                shell=True,
                stdout=output,
                stderr=output,
            )
        return 200, "Success"
