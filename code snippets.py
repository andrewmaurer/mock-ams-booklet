# Split names into first and last, for alphebetizing the booklet.

import pandas as pd

submissions = pd.read_csv('submissions.csv')
names = submissions['Full Name']

first = [name.split()[0] for name in names]
last = [name.split()[1] for name in names]

submissions['First Name'] = first
submissions['Last Name'] = last

submissions.to_csv('submissions2.csv')



