#!/usr/bin/python

from flask import render_template_string, request, jsonify, Blueprint
from uploader_app import app
import subprocess
import base64
import re
import os

print(app.config)
bp = Blueprint("burritos", __name__)


def run_command_and_output(command):
    pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z\s{0,2}(\w+)\s{1}\d{1}\s{1}\-\-\-\s{1}\[.+\] (.+)"
    hapi_pattern = r"(HAPI-\d{0,4}\: .+\n)"
    error = False
    error_content = ""
    parsed_content = []
    hapi_error = ""
    with open("logs/output.log", "w") as output:
        print(command)
        subprocess.call(
            command,
            shell=True,
            stdout=output,
            stderr=output,
        )
    with open("logs/output.log", "r") as output:
        if "ERROR" in output.read():
            error = True
            with open("logs/output.log", "r") as error_file:
                error_content = error_file.read()
                print(error_content)
            parsed_content = re.findall(pattern, error_content, re.MULTILINE)
            hapi_error = re.findall(hapi_pattern, error_content, re.MULTILINE)

    return parsed_content, error_content, hapi_error, error


@bp.route("/", methods=["GET"])
def hello():
    return render_template_string("""<!DOCTYPE html>
<html>
<head>
    <title>Intro Page</title>
</head>
<body>
    <h1>IG Uploader</h1>
    <p>Check <a href="apidocs">here</a> for docs</p>
                                  <p>This is a wrapper around <a href="https://github.com/jkiddo/ember">https://github.com/jkiddo/ember</a></p>
</body>
</html>""")


# https://github.com/jkiddo/ember
@bp.route("/upload-ig", methods=["POST"])
def upig():
    """
    file: docs/upload-ig.yml
    """
    data = request.json
    # print(data)
    serverBase = data["serverBase"]
    packageId = data.get("packageId", None)
    usePUT = data.get("usePUT", True)
    loadRecursively = data.get("loadRecursively", False)
    packagebase64 = data.get("packagebase64", None)
    packageURL = data.get("packageURL", None)
    print([packageId is not None, packagebase64 is not None, packageURL is not None])
    if (
        sum([packageId is not None, packagebase64 is not None, packageURL is not None])
        > 1
    ):
        return (
            "Only 1 of Package ID OR package base64 OR package URL must be provided. Not more than 1.",
            404,
        )
    if not serverBase:
        return "Server base must be provided.", 404
    if packagebase64:
        # Create folder if it doesn't exist
        if not os.path.exists("tmp"):
            os.makedirs("tmp")

        # save to disk
        package_bytes = base64.b64decode(packagebase64)
        with open("tmp/package.tgz", "wb") as f:
            f.write(package_bytes)

        command = (
            "docker run -v tmp/:/app/mypackagefolder/jkiddo/ember --location=file:/app/mypackagefolder/package.tgz"
            + " --serverBase="
            + str(serverBase)
            + " --usePUT="
            + str(usePUT)
            + " --loadRecursively="
            + str(loadRecursively)
        )

        parsed_content, error_content, hapi_error, error = run_command_and_output(
            command
        )

    if packageId:
        command = (
            "docker run --rm jkiddo/ember --packageId="
            + str(packageId)
            + " --serverBase="
            + str(serverBase)
            + " --usePUT="
            + str(usePUT)
            + " --loadRecursively="
            + str(loadRecursively)
        )

        parsed_content, error_content, hapi_error, error = run_command_and_output(
            command
        )

    if packageURL:
        command = (
            "docker run --rm jkiddo/ember --location="
            + str(packageURL)
            + " --serverBase="
            + str(serverBase)
            + " --usePUT="
            + str(usePUT)
            + " --loadRecursively="
            + str(loadRecursively)
        )

        parsed_content, error_content, hapi_error, error = run_command_and_output(
            command
        )

    if error:
        return jsonify(
            {
                "result": "ERROR",
                "parsed_content": parsed_content,
                "raw_message": error_content,
                "hapi_error": hapi_error,
            }
        ), 500
    else:
        return jsonify(
            {
                "result": "Success",
                "message": "Package has been uploaded successfully",
            }
        )


app.register_blueprint(bp, url_prefix="/ig-uploader-api")
