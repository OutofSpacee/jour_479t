# JOUR479T 

_By Apurva Mahajan_ | University of Maryland, College Park

This repository contains the code and materials for _JOUR479T: Building Newsroom-Wide Tools with Artificial Intelligence_, a student-initiated course taught at the University of Maryland during the spring 2026 semester. 

## Terminal commands to know

### Creating a virtual environment
A virtual environment, or venv, is 

To create a virtual Python environment in your project folder, run the following in your terminal.
```bash
python3 -m venv .venv
```

Then, to initialize your virtual environment, run:
```bash
source .venv/bin/activate
```
### Installing requirements 
Before you can run some of the code in the Python notebooks and scripts in this repository, you need to install the required libraries. You theoretically could do this one by one, but luckily, we've got a `requirements.txt` file that lists all the libraries we will need!

To install the libraries in `requirements.txt`, run the following in your terminal:
```bash
pip install -r requirements.txt
```

### Working with Git
When working in codespaces, if we want to push changes to GitHub so other people can see them, we need to run certain commands in the terminal.

To **pull new changes** from the main branch of the repository you've forked, run:
```bash
git pull
```

After you've made changes to your code and you're ready to send those to GitHub, run the following in the order they're in:

`git add` tells your computer you're staging changes to Git. The `.` tells it "we want to add EVERYTHING that we've changed."
```bash
git add .
```
`git commit` commits these changes, which basically means it acts as a snapshot of your project at this point in time. Commit saves your changes to your local machine.
```bash
git commit -m "your commit message here"
```
`git push` is the part that actually sends your changes to GitHub and makes the newest iteration of your files visible on GitHub.
```bash
git push origin main
```
or
```bash
git push origin master
```
### Working with app.py

```bash
python3 app.py
```

e.g. 

```bash
python3 week12/app.py
```s