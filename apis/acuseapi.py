import requests
import xml.etree.ElementTree as ET
# obsolete?

# https://helpx.adobe.com/adobe-connect/webservices/getting-started-connect-web-services.html


# Set up the URL and header for the request
url = "https://clubcloudcomputing.adobeconnect.com/api/xml?action=report-my-meetings"
header = {'Content-Type': 'text/xml'}

# Set up the XML payload for the request
payload = """
<header>
  <version>1.0</version>
  <auth>
    <partner>your_partner_name</partner>
    <key>your_api_key</key>
  </auth>
</header>
"""

# Make the API request
response = requests.post(url, data=payload, headers=header)

# Parse the XML response
root = ET.fromstring(response.text)

# Extract the list of meetings
meetings = []
for meeting in root
    print meeting

