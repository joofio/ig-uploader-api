#!/usr/bin/python

from flask import render_template, request, jsonify
from uploader_app import app
import subprocess
import base64

print(app.config)


@app.route("/", methods=["GET"])
def hello():
    return render_template("index.html", result="")


# https://github.com/jkiddo/ember
@app.route("/upload-ig", methods=["POST"])
def upig():
    data = request.json
    print(data)
    serverBase = data["serverBase"]
    packageId = data.get("packageId", None)
    usePUT = data.get("usePUT", True)
    loadRecursively = data.get("loadRecursively", False)
    packagebase64 = data.get("packagebase64", None)
    if packageId and packagebase64:
        return 404, "Package ID OR package base64 must be provided. Not both."
    if not serverBase:
        return 404, "Server base must be provided."
    if packagebase64:
        # save to disk
        package_bytes = base64.b64decode(packagebase64)
        with open("package.zip", "wb") as f:
            f.write(package_bytes)

        with open("logs/output.log", "w") as output:
            command = (
                "docker run --rm jkiddo/ember --location=package.zip"
                + " --serverBase="
                + str(serverBase)
                + " --usePUT="
                + str(usePUT)
                + " --loadRecursively="
                + str(loadRecursively)
            )
            print(command)
            subprocess.call(
                command,
                shell=True,
                stdout=output,
                stderr=output,
            )

        with open("logs/output.log", "r") as output:
            if "ERROR" in output.read():
                with open("logs/output.log", "r") as error_file:
                    error_content = error_file.read()
                return jsonify({"result": "Success", "message": error_content}), 500

        return jsonify(
            {"result": "Success", "message": "Package has been uploaded successfully"}
        )

    return 200, "Success"
    if packageId:
        with open("logs/output.log", "w") as output:
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
            print(command)
            subprocess.call(
                command,
                shell=True,
                stdout=output,
                stderr=output,
            )

        with open("logs/output.log", "r") as output:
            if "ERROR" in output.read():
                with open("logs/output.log", "r") as error_file:
                    error_content = error_file.read()
                return jsonify({"result": "Success", "message": error_content}), 500

        return jsonify(
            {"result": "Success", "message": "Package has been uploaded successfully"}
        )
