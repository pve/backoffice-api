#!pip install 'openpyxl>=3.0.0'
import glob
import pandas as pd
rosters = glob.glob("CCSK Class Roster*")
print(rosters)
canarydf = pd.DataFrame([["canary87@d1g.nl"]], columns=["Email"])
#L = [pd.read_excel(i, skiprows=17).append(canarydf, ignore_index=True, sort=False) for i in rosters]
#rostercontentraw = pd.concat(L, sort=True, ignore_index=True)
dfs = [pd.read_excel(i, skiprows=17) for i in rosters]
L = pd.concat(dfs + [canarydf], ignore_index=True, sort=False)
rostercontent = L[(L.Email != "ewinters@cloudsecurityalliance.org")].dropna(subset=["Email"])
print(rostercontent.Email.count())
rostercontent[rostercontent.Email.str.find('dom')>=0].head()

# duplicates in roster leden is niet goed.
cr = rostercontent.Email.str.lower()
print("duplicate emails: ")
#cr[cr.duplicated(subset=['Email'], keep=False)]
cr[cr.duplicated(keep=False)]
cr.value_counts() #The resulting object will be in descending order so that the first element is the most frequently-occurring element