# JOUR479T: Building Newsroom-Wide Tools with Artificial Intelligence

_By Apurva Mahajan_ | University of Maryland, College Park

This repository contains the code and materials for JOUR479T, a student-initiated course taught at the University of Maryland during the spring 2026 semester. 

## Terminal commands to know

### Creating a virtual environment
A virtual environment, or venv, is a separate workspace within your project where you can install packages and dependencies without having to install them globally on your entire computer. A venv is kind of like a sandbox where anything you install doesn't touch the rest of your computer.

Whenever we want to run a Python script or install packages, we typically want to be in a venv before doing so.

To create a virtual Python environment in your project folder, run the following in your terminal. This names our venv `.venv`.
```bash
python3 -m venv .venv
```

Then, to activate/initialize your virtual environment, run:
```bash
source .venv/bin/activate
```
### Installing requirements 
Before you can run some of the code in the Python notebooks and scripts in this repository, you need to install the required libraries. You theoretically could do this one by one, but luckily, we've got a `requirements.txt` file that lists all the libraries we will need!

To install the libraries in `requirements.txt`, run the following in your terminal:
```bash
pip install -r requirements.txt
```
You wont need this for this class really, but for future reference, if you want to turn all of the packages and dependencies you've installed in your venv into a `requirements.txt` file, run:
```bash
pip freeze > requirements.txt
```
This will only work if you have all the packages you want in the `requirements.txt` already installed in your virtual environment.

### Working with Git
When working in codespaces, if we want to push changes to GitHub so other people can see them, we need to run certain commands in the terminal.

To **pull new changes** from the main branch of the repository you've forked, run:
```bash
git pull
```

After you've made changes to your code and you're ready to send those to GitHub, run the following in the order they're in:

1. `git add` tells your computer you're staging changes to Git. The `.` tells it "we want to add EVERYTHING that we've changed."
    ```bash
    git add .
    ```
2. `git commit` commits these changes, which basically means it acts as a snapshot of your project at this point in time. Commit saves your changes to your local machine.
    ```bash
    git commit -m "your commit message here"
    ```
3. `git push` is the part that actually sends your changes to GitHub and makes the newest iteration of your files visible on GitHub. Depending on what your branch is called, you might have either `main` or `master`, but these are functionally identical. 

    To know which one to run, look at the left hand side of your terminal. You'll see something like this (but with your own GitHub username):

    ```bash
    @amahaja25 ➜ /workspaces/jour_479t (main) $
    ```
    Look at what is in that parentheses. If it's main, run:

    ```bash
    git push origin main
    ```
    Alternatively, if you see ```(master)``` then run this:

    ```bash
    git push origin master
    ```
### Running python scripts 

When you run `python3 [insert script name here].py`, you are executing the code in that script. For example, if I run:

```bash
python3 app.py
```

or
```bash
python app.py
```
I am telling my computer to excecute all of the code in the file named `app.py`. If there's some bad code or something is weird with my script, I will get an error thrown in my terminal that allows me to troubleshoot.

Make sure you understand where your file is stored. If my `app.py` file isn't in the root of my folder (`/`) and is instead stored in another directory, like `week12`, running `python app.py` won't work, because my computer won't be able to find `jour_479t/app.py`. 

I'd instead need to specify where my script is located, e.g.:

```bash
python week12/app.py
```