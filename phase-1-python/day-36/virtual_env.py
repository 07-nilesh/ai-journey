# We tell Python to use its built-in 'venv' tool to create our isolated box named 'my_ai_project'
# WHY: This actually creates a new folder on your computer that will hold all our specific tools
#1.python -m venv my_ai_project

# We must turn ON the isolated box before we start installing things
# WHY: If we don't activate it, our computer will still install things into the messy global folder
# (Note: This is the Windows command. On Mac/Linux, it is: source my_ai_project/bin/activate)
#2.my_ai_project\Scripts\activate

# Now we install a tool (like pandas) inside our active, isolated box
# WHY: Because the environment is activated, pandas goes ONLY into 'my_ai_project', keeping the global computer clean
#3.pip install pandas

# After we're done, we can turn OFF the isolated box
# WHY: This returns us to our normal computer environment, where we can work on other projects
#4.deactivate

# If we want to see what tools we have inside our isolated box, we can ask pip to list them
# WHY: This helps us keep track of what we've installed in our project environment
#5. pip list

# If we want to share our project with someone else, we can create a 'requirements.txt' file that lists all the tools we used
# WHY: This makes it super easy for others to replicate our project setup without manually installing each tool 
#6. pip freeze > requirements.txt

# If someone else wants to set up the same project environment, they can use the 'requirements.txt' file to install all the same tools with one command
# WHY: This makes it super easy for others to replicate our project setup without manually installing each tool
#7. pip install -r requirements.txt

# If we want to remove the isolated box and all its tools, we can simply delete the 'my_ai_project' folder
# WHY: This is the easiest way to clean up everything related to that project without affecting our global computer environment
#8. rm -rf my_ai_project (Mac/Linux) or rmdir /s my_ai_project (Windows)

# this will look for pandas in the global environment and will fail if it's not installed globally, 
# which is why we use virtual environments to keep our project dependencies organized and separate from the global Python installation.
#If you never installed pandas globally, Python will crash and give you a ModuleNotFoundError: No module named 'pandas'.
#9. python -c "import pandas"

# If we want to see all the tools we have installed in our global Python environment, we can ask pip to list them without activating any virtual environment
# WHY: This helps us keep track of what we've installed globally, which is separate from our
# 10. pip freeze

# summary:
# 1. Create a virtual environment: python -m venv my_ai_project
# 2. Activate the virtual environment: my_ai_project\Scripts\activate (Windows) or source my_ai_project/bin/activate (Mac/Linux)
# 3. Install packages inside the virtual environment: pip install pandas
# 4. Deactivate the virtual environment when done: deactivate
# 5. List installed packages in the virtual environment: pip list
# 6. Create a requirements.txt file: pip freeze > requirements.txt
# 7. Install packages from requirements.txt: pip install -r requirements.txt
# 8. Remove the virtual environment: rm -rf my_ai_project (Mac/Linux) or rmdir /s my_ai_project (Windows)
# 9. Test if a package is installed globally: python -c "import pandas"
# 10. List globally installed packages: pip freeze

