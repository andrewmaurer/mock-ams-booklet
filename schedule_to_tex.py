import pandas as pd
import os

schedule = pd.read_csv("schedule.csv")

email_header = "Email"
name_header = "Full Name"
title_header = "Title of your Mock AMS talk."
abstract_header = "Abstract of your Mock AMS talk."
day_header = 'Day'
event_header = 'Event'
email_header = 'Email'
start_header = 'Start'
stop_header = 'Stop'
readable_start_header = 'Readable Start'
readable_stop_header = 'Readable Stop'

# Contributed Talks

print(r"""
\documentclass[oneside]{amsart}

\usepackage{amsthm,amssymb,amsmath}
\usepackage[margin=1in]{geometry}

\usepackage{draftwatermark}
\SetWatermarkScale{4.0}

\begin{document}

%\title{Mock AMS Schedule}
%\date{July 26-27, 2018}
%\author{University of Georgia Department of Mathematics}
%\maketitle

\pagenumbering{gobble}

\section*{\textbf{Thursday}}

\begin{itemize}
\setlength\itemsep{1em}
""")

talk_template = "\\item {Start} -- {Stop}: {Title} \\\\ \\vspace{{-1.5em}} \\begin{{flushright}}\\textit{{ {Name} }}\\end{{flushright}}"

coffee_template ="""
\\end{{itemize}}
\\section*{{\\textit{{Coffee Break}}}}
\\vspace{{0.5em}}
\\begin{{itemize}}
\\setlength\\itemsep{{1em}}
"""

lunch_template = """
\\end{{itemize}}
\\section*{{\\textit{{Lunch Break}}}}
\\vspace{{0.5em}}
\\begin{{itemize}}
\\setlength\\itemsep{{1em}}
"""

remarks_template = "\\item {Start} -- {Stop}: Opening Remarks"

templates = {
'remarks':remarks_template,
'coffee':coffee_template,
'talk':talk_template,
'lunch':lunch_template
}

def print_day(day_num):
    for index, row in schedule[schedule[day_header] == day_num].iterrows():
        event = row[event_header]
        name = row[name_header]
        title = row[title_header]
        start = row[readable_start_header]
        stop = row[readable_stop_header]
        print(templates[event].format(Title=title, Name=name, Start=start, Stop=stop ))

print_day(1)

print(r"""
\end{itemize}

\newpage
\section*{\textbf{Friday}}

\begin{itemize}
\setlength\itemsep{1em}
""")

print_day(2)



print(r"""
\end{itemize}
\end{document}
""")



