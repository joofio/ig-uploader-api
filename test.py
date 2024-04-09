import requests
import base64

# Read the zip file as binary data
with open("/Users/joaoalmeida/Downloads/package_3.tgz", "rb") as file:
    zip_data = file.read()

# Encode the zip file data into base64
base64_data = base64.b64encode(zip_data).decode("utf-8")

# Prepare the payload for the POST request
# ""= {"file": base64_data}
payload = {
    "serverBase": "https://fhir.hl7.pt/r4/fhir",
    # "packageId": "hl7.fhir.eu.laboratory",
    "packagebase64": base64_data,
}
# Make the POST request
response = requests.post("http://127.0.0.1:5005/upload-ig", json=payload)

print(response.text)
# Check the response status
if response.status_code == 200:
    print("File uploaded successfully!")
else:
    print("Failed to upload the file.")
