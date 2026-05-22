## Yahtzee Assignment

**All coding for this assignment must be completed within CodeSpaces, i.e. you should not code a solution elsewhere and paste the code into CodeSpaces**

Please download and complete the GenAI Declaration document and submit to ELE with your final submission files.

Should you have any issues or queries about GitHub or working in CodeSpaces please contact the module organiser for additional support on using it.

### TASK

Follow the instructions provided in the *Coding Yahtzee* PDF file.

To check your functions are working as you write them you can add code to the `run_checks.py` file to verify the functions behave as expected, by running it using the following terminal command:

```
python run_checks.py
```

Your codespace files save automatically as you work on the local machine. However they are not permenantly saved unless they are saved back to GitHub.

To save your work to GitHub see the instructions below. You should do this regularly (e.g. at least at the end of every coding session). 

#### Saving to GitHub

After completing the exercises please run the following commands in the terminal.

These lines will save your code in three stages:
 - modified files are staged to specify which changes will be commited;
 - staged changes are committed to the local git code repository (on the CodeSpace machine)
 - changes are pushed to the remote master copy of the code repository on GitHub website

```
git add .
git commit -m "finished assignment"
git push
```

It is a good habit to commit and push your files
 everytime you have made a significant change. 
 
In this case you can change the commit message, e.g. 

```
git commit -m "completed part1"
```

To check your work has been saved you can run the line of code below in the terminal to get the web address of the repository in GitHub. Goto the repository and check the code files have the changes you have made.

```
git config --get remote.origin.url
```
