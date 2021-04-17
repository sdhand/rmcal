#!/bin/bash

ical=""
cd $(dirname $0)
./rmcal.py $ical > Calendar.tex
pdflatex Calendar.tex
