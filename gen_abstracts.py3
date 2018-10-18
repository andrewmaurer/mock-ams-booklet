import pandas as pd
import os

contributed = pd.read_csv("submissions.csv")

email_header = "Username"
name_header = "Full Name"
giving_talk_header = "Will You give a talk at this year's Mock AMS?"
no_talk_header = "If If you answered \"no\", please explain."
constraints_header = "Do you have any scheduling constraints?"
yes_constraints_header = "If you answered \"yes\", please explain."
title_header = "Title of your Mock AMS talk."
abstract_header = "Abstract of your Mock AMS talk."
content_header = "How would you describe the content of your talk?"

# Contributed Talks

print(r"""
\documentclass[oneside]{amsart}

\usepackage{amsthm,amssymb,amsmath}
\usepackage[margin=1in]{geometry}

\usepackage{draftwatermark}
\SetWatermarkScale{4}

\begin{document}

\title[Mock AMS]{Mock AMS Conference \\ Abstracts}
\date{July 26-27, 2018}
\author{University of Georgia \\ Department of Mathematics}
\maketitle
\noindent\rule{\textwidth}{0.4pt}
\vspace{0.5em}
""")

template = """\\filbreak
\\hspace{{-20pt}}\\textbf{{ \\textbf{{ {Title} }} }} \\vspace{{0.5em}}\\\\
{Abstract} \\vspace{{-1em}}\\\\
\\begin{{flushright}} \\textit{{ {Name} }} \\vspace{{0.5em}} \\end{{flushright}}
\\rule{{\\textwidth}}{{0.4pt}}
\\vspace{{0.5em}}
"""

for index, row in contributed.iterrows():
    name = row[name_header].strip()
    email = row[email_header].strip()
    title = row[title_header].strip()
    abstract = row[abstract_header].strip()
    print(template.format(Abstract=abstract, Title=title, Name=name, Email=email ))



print(r"""
\end{document}
""")



