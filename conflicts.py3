import pandas as pd
import os

submissions = pd.read_csv("submissions.csv")

email_header = "Username"
name_header = "Full Name"
giving_talk_header = "Will you give a talk at this year's Mock AMS?"
no_talk_header = "If you answered \"no\", please explain."
constraints_header = "Do you have any scheduling constraints?"
yes_constraints_header = "If you answered \"yes\", please explain."
title_header = "Title of your Mock AMS talk."
abstract_header = "Abstract of your Mock AMS talk."
content_header = "How would you describe the content of your talk?"

print("                  CONFLICTS AND CONSTRAINTS FOR MOCK AMS                  ")
print("                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                  ")
print("                                                                          ")

# Cannot Attend

cannot_attend = submissions.loc[ submissions[giving_talk_header] == "No" ]

template="""
{Name}, {Email}
Reason: {Reason}
"""

print("~~~~~~~~~~~~~~~~~~~~~~ The Following Cannot Attend ~~~~~~~~~~~~~~~~~~~~~~")

for index, row in cannot_attend.iterrows():
    name = row[name_header].strip()
    email = row[email_header].strip()
    reason = row[no_talk_header].strip()
    print( template.format(Name=name, Email=email, Reason=reason) )

# Scheduling Constriants

scheduling_constraint = submissions.loc[ submissions[constraints_header] == "Yes" ] 
    
template="""
{Name}, {Email}
Constraint: {Constraint}
"""

print("~~~~~~~~~~~~~~ The Following Have Scheduling Constraints ~~~~~~~~~~~~~~")

for index, row in scheduling_constraint.iterrows():
    name = row[name_header].strip()
    email = row[email_header].strip()
    constraint = row[yes_constraints_header].strip()
    print( template.format(Name=name, Email=email, Constraint=constraint) )









