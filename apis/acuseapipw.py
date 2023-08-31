import requests
from urllib.parse import urljoin, urlencode
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

load_dotenv()
# create users: https://helpx.adobe.com/adobe-connect/webservices/principal-update.html
# https://helpx.adobe.com/adobe-connect/webservices/group-membership-update.html

#list group: ?? https://helpx.adobe.com/adobe-connect/webservices/permissions-info.html  ?
# https://helpx.adobe.com/adobe-connect/webservices/principal-list.html

#curl "https://clubcloudcomputing.adobeconnect.com/api/xml?action=common-info"
#curl "https://clubcloudcomputing.adobeconnect.com/api/xml?action=principal-list"

#https://helpx.adobe.com/adobe-connect/webservices/topics.html

# Set up the URL and header for the request
#url = "https://clubcloudcomputing.adobeconnect.com/api/xml?action=common-info"
#header = {'Content-Type': 'text/xml'}

def get_meetings():
# https://helpx.adobe.com/adobe-connect/webservices/report-my-meetings.html    # Make the API request
    params = {"action": "login", "login": os.environ["AC_USER"], "password": os.environ["AC_PW"]}
    url = urljoin("https://clubcloudcomputing.adobeconnect.com/api/xml", "?" + urlencode(params))    
    response = requests.post(url)
    #print(response.text)
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.text)
        cookies = response.cookies
        ET.dump(root)
    else:
        # Handle the error
        print("Error: API request failed with status code", response.status_code)

    url = "https://clubcloudcomputing.adobeconnect.com/api/xml?action=report-my-meetings"
    print(url)

    response = requests.post(url, cookies=cookies)
    # Parse the XML response
    root = ET.fromstring(response.text)

    ET.dump(root)  # prints

    # Extract the list of meetings
    # name is a sub element of meeting
    # sco-id is an attribute of meeting
    meetings = []
    for meeting in root.findall('.//meeting'):
        meetings.append(meeting.find('./name').text)

    print(meetings)

def get_participants():
# https://helpx.adobe.com/adobe-connect/webservices/permissions-info.html    
#  https://example.com/api/xml?action=permissions-info&acl-id=2006258745 (acl could be sco)
    params = {"action": "login", "login": os.environ["AC_USER"], "password": os.environ["AC_PW"]}
    url = urljoin("https://clubcloudcomputing.adobeconnect.com/api/xml", "?" + urlencode(params))    
    response = requests.post(url)
    #print(response.text)
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.text)
        cookies = response.cookies
        ET.dump(root)
    else:
        # Handle the error
        print("Error: API request failed with status code", response.status_code)

# sco-id="2160861162" CCSK Day 2
    url = "https://clubcloudcomputing.adobeconnect.com/api/xml?action=permissions-info&acl-id=2160861162"
    print(url)

    response = requests.post(url, cookies=cookies)
    # Parse the XML response
    root = ET.fromstring(response.text)

#    ET.dump(root)  # prints

    user_dict = []

    # Itereren over alle 'principal' elementen en de login en naam opslaan in de dictionary
    for principal_element in root.findall('.//principal'):
        name = principal_element.find('name').text
        login = principal_element.find('login').text
        user_dict.append({'name': name, 'login': login})

    # Maak een nieuwe dictionary met alleen de gewenste sleutels
    # filtered_dict = {key: value for key, value in user_dict.items() if key is not None and '@' in key}
    filtered_dict = user_dict
    return(filtered_dict)
    # {'joy@acme.com': 'Joy Smith'}

def do_stuff():
    # Make the API request
    response = requests.post(url)
    #print(response.text)
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.text)
        cookies = response.cookies
        ET.dump(root)

        # Extract the session key from the response
    #    session_key = root.find('./header/session/key').text
        # session_key = root.get('OWASP_CSRFTOKEN')
        # print(session_key)
        # print(root[1].tag)
        # print(root[1].attrib)
    else:
        # Handle the error
        print("Error: API request failed with status code", response.status_code)
        # You can also access the error message by parsing the response text
        # error_message = root.find('./error/message').text
        # print("Error message:", error_message)

    # Parse the XML response
    root = ET.fromstring(response.text)
    # sends a CSRFTOKEN
    # Extract the session key from the response

    for key in root.iter('token'):
        print(key.text)
        session_key = key.text

    # Use the session key to make subsequent API requests
    # Set up the URL and header for the next request
    #url = "https://clubcloudcomputing.adobeconnect.com/api/xml?action=report-my-meetings"
    #url = "https://clubcloudcomputing.adobeconnect.com/api/xml?action=common-info"
    url = "https://clubcloudcomputing.adobeconnect.com/api/xml?action=principal-list"

    print(url)

    response = requests.post(url, cookies=cookies)
    #response = requests.post(url, data=payload) # geeft nologin

    # Parse the XML response
    root = ET.fromstring(response.text)

    ET.dump(root)  # prints

    # Extract the list of meetings
    meetings = []
    for meeting in root.findall('.//meeting'):
        meetings.append(meeting.find('./name').text)

    print(meetings)

    principals = []
    for principal in root[1].findall('./principal'):
        principals.append(principal.find('./name').text)

    for child in root[1]:
        print(child.tag, child.attrib)

    #for key in root.iter('principal'):
    #  print(key.attrib)    
    #  key.attrib['principal-id']

    print(principals)
    # peter 2079729223
    # CCSK 2924190672
    url = "https://clubcloudcomputing.adobeconnect.com/api/xml?action=principal-info&principal-id=2924190672"

    response = requests.post(url, cookies=cookies)
    root = ET.fromstring(response.text)
    #ET.dump(root)
    ET.indent(root)
    print(ET.tostring(root, encoding='unicode'))

if __name__ == "__main__":
#    get_meetings()
    gp = get_participants()

    i = 1