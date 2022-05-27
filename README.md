# Django - Ubuntu Debian 20.02
This is a Django Course, with snippets from Jose Portilla's Course in Udemy

Virtual Environments are important in Django installations. They assist the user to keep up with Packages updates in Django. I have used Conda as a virtual environment (venv) in this course.
Install conda by sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
Then Update by: conda update --all
Create a virtual environment by: conda create --name MyEnv django
This will install all libraries and django instance
Then activate by: conda activate myEnv
Deactivate by: conda deactivate myEnv

List all venv by: conda env list
