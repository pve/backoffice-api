import pandas as pd

# Voorbeeld DataFrame met kolom 'email'
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'email': ['   Alice@example.com   ', '   Bob@Domain.com   ', '   Charlie@Example.com   ']}
df = pd.DataFrame(data)

# Definieer de functie om e-mails schoon te maken
def clean_email(email):
    cleaned_email = email.strip().lower()
    return cleaned_email

# Pas de functie toe op de kolom 'email'
df['email'] = df['email'].apply(clean_email)

print(df)

import pandas as pd
import pytest

# Voorbeeld DataFrame met kolom 'email'
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'email': ['   Alice@example.com   ', '   Bob@Domain.com   ', '   Charlie@Example.com   ']}
df = pd.DataFrame(data)

# Definieer de functie om e-mails schoon te maken
def clean_email(email):
    cleaned_email = email.strip().lower()
    return cleaned_email
#===

# Testfuncties voor pytest
def test_clean_email_lower_case():
    assert clean_email('Alice@example.com') == 'alice@example.com'
    assert clean_email('Bob@Domain.com') == 'bob@domain.com'
    assert clean_email('Charlie@Example.com') == 'charlie@example.com'

def test_clean_email_strip_spaces():
    assert clean_email('   Alice@example.com   ') == 'alice@example.com'
    assert clean_email('   Bob@Domain.com   ') == 'bob@domain.com'
    assert clean_email('   Charlie@Example.com   ') == 'charlie@example.com'

def test_clean_email_combined():
    assert clean_email('   Alice@Example.com   ') == 'alice@example.com'
    assert clean_email('   bOb@Domain.com   ') == 'bob@domain.com'
    assert clean_email('   CHARLIE@Example.com   ') == 'charlie@example.com'

# Voer de tests uit
if __name__ == '__main__':
    pytest.main()
