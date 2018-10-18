# Mock AMS Booklet

Just a collection of python scripts to generate LaTeX files for Mock AMS 2018's booklet. Ideally this will be run with the following commands.

```bash
python3 gen_abstracts.py3 > abstracts.tex
python3 gen_schedule.py3 > schedule.csv
python3 schedule_to_tex.py > schedule.tex
python3 conflicts.py3 > conflicts.txt

pdflatex abstracts
pdflatex schedule
```
`code snippets.py` should be run just in a terminal, and is used to get first and last names primarily. I'll clean this up eventually to make it more user friendly.

The only real input file is `submissions.csv` which holds title, abstracts, constraints, etc.
