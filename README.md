# Mock AMS Booklet

Just a collection of python scripts to generate LaTeX files for Mock AMS 2018's booklet. Ideally this will be run with the following commands.


## Short Description 

```bash
python3 gen_abstracts.py > abstracts.tex
python3 gen_schedule.py > schedule.csv
python3 schedule_to_tex.py > schedule.tex
python3 conflicts.py > out/conflicts.txt

pdflatex -output-directory out abstracts
pdflatex -output-directory out schedule
```
`code snippets.py` should be run just in a terminal, and is used to get first and last names primarily. I'll clean this up eventually to make it more user friendly.

The only real input file is `submissions.csv` which holds title, abstracts, constraints, etc. Whoever is organizing the conference has to come up with a schedule.

## Longer Description

To generate the booklet, run the following bash commands using python3

1. List all conflicts in an easy-to-read text file.
```
python3 conflicts.py >> out/conflicts.txt
```
This should be helpful when making the schedule, which I ended up doing on a coffee table.

2. Read the abstracts in from a CSV file and format in LaTeX, pass into PDFLaTeX:
```
python3 gen_abstracts.py >>> abstracts.tex
pdflatex abstracts.tex -output-directory
```

3. At this point I want to have a shell of schedule file with just the following columns: day, event, email, full name, title. Use `gen_schedule.py` to fill in columns with start times and stop times for every talk. Then use `schedule_to_tex.py` to generate a LaTeX tile which can then be passed into PDFLaTeX.
```
python3 gen_schedule.py
python3 schedule_to_tex.py >> schedule.tex
pdflatex -output-directory out schedule.tex
```
