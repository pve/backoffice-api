import xml.etree.ElementTree as ET
#from apis.teachableapi import get_enrollments as tusers

def convert_xml_to_data(xml_data):
    root = ET.fromstring(xml_data)

    data = []
    for principal_element in root.findall('.//principal'):
        name = principal_element.find('name').text
        login = principal_element.find('login').text
        data.append({'name': name, 'login': login})

    return data

def test_convert_xml_to_data():
    xml_data = '''<?xml version="1.0" encoding="utf-8"?>
    <results>
        <status code="ok" />
        <permissions>
            <principal principal-id="2006258745" is-primary="false" type="user"
                        has-children="false" permission-id="host" training-group-id="2007842424">
                <name>Joy Smith</name>
                <login>joy@acme.com</login>
            </principal>
            ...
        </permissions>
    </results>'''

    expected_data = [{'name': 'Joy Smith', 'login': 'joy@acme.com'}]

    data = convert_xml_to_data(xml_data)

    assert data == expected_data
