from apis.teachableapi import get_enrollments as tenrollments
from apis.teachableapi import get_users as tusers
from apis.autorespond import get_users as arusers
from apis.acuseapipw import get_participants as acusers
import pandas as pd

if __name__ == "__main__":
    aru = pd.DataFrame(arusers()) # AR Foundation
    print(aru.count())
    acu = pd.DataFrame(acusers()) # Adobe Connect CCSK day 2
    print(acu.count())
    tu = pd.DataFrame(tusers()).rename(columns={'id':'user_id'}).drop_duplicates(subset=['user_id'])
    print(tu.count())
    te = pd.DataFrame(tenrollments("265372")).drop_duplicates(subset=['user_id'])
    print(te.count()) # CASA

    tue = te.merge(tu, how = 'inner', on='user_id', validate='1:1')
    tue.to_csv("reports/teachable_useremail_data.csv", index=False)

    # In Foundation, but not in CASA.
    missingCasa = aru[~aru.email.str.lower().isin(tue.email.str.lower())]
    missingAC = aru[~aru.email.str.lower().isin(acu.login.str.lower())].rename(columns={'firstName':'first-name' , 'lastName': 'last-name'})  
    print(missingCasa[['email']])
    # In AutoRespond, but not in Adobe Connect; AC has other field names. 
    missingAC["login"] = missingAC["email"]
    missingAC["password"] = "husflhff"
    print(missingAC[['first-name', 'last-name', 'email']])
    missingAC[['first-name', 'last-name', 'login', 'email', 'password']].to_csv('reports/missing_from_ac.csv', index=False)
    i =1
