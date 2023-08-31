import xml.etree.ElementTree as ET

def test_convert_ac():
    xml_data = '''<?xml version="1.0" encoding="utf-8"?>
    <results>
        <status code="ok" />
        <permissions>
            <principal principal-id="2006258745" is-primary="false" type="user" 
                        has-children="false" permission-id="host" training-group-id="2007842424">
                <name>Joy Smith</name>
                <login>joy@acme.com</login>
            </principal>
        </permissions>
    </results>'''

    # Parsen van de XML-data
    root = ET.fromstring(xml_data)

    # Lijst om logins op te slaan
    logins = []

    # Itereren over alle 'login'-elementen en deze aan de lijst toevoegen
    for login_element in root.iter('login'):
        logins.append(login_element.text)

    # Printen van de lijst van logins
    print(logins)
    assert(logins == ['joy@acme.com'])

    user_dict = {
        'joy@acme.com': 'Joy Smith',
        'john': 'John Doe',
        'jane@acme.com': 'Jane Smith',
        'mark': 'Mark Johnson'
    }

    # Maak een nieuwe dictionary met alleen de gewenste sleutels
    filtered_dict = {key: value for key, value in user_dict.items() if '@' in key}

    assert( filtered_dict == {'joy@acme.com': 'Joy Smith', 'jane@acme.com': 'Jane Smith'})
