# We tell Conda to create a new steel container named 'ai_env' AND we pack Python 3.11 inside it
# WHY: Conda manages the Python version itself, unlike venv which just uses whatever Python you used to run the command
# 1. conda create -n ai_env python=3.11

# We step inside our new steel container
# WHY: So any tools we install next go into this specific container, not the global computer
# 2. conda activate ai_env

# We install a heavy math tool like NumPy using conda instead of pip
# WHY: Conda will automatically figure out and install any complex C++ dependencies NumPy needs in the background
# 3. conda install numpy

# If we want to see what tools we have inside our Conda container, we can ask conda to list them
# WHY: This helps us keep track of what we've installed in our project environment
# 4. conda list

# If we want to share our project with someone else, we can create an 'environment.yml' file that lists all the tools we used   
# WHY: This makes it super easy for others to replicate our project setup without manually installing each tool
# 5. conda env export > environment.yml

# If someone else wants to set up the same project environment, they can use the 'environment.yml' file to create a new Conda environment with all the same tools
# WHY: This makes it super easy for others to replicate our project setup without manually installing each
# 6. conda env create -f environment.yml

# If we want to remove the Conda environment and all its tools, we can simply delete the 'ai_env' environment
# WHY: This is the easiest way to clean up everything related to that project without affecting our
# global computer environment
# 7. conda remove -n ai_env --all
# conda remove -n ai_env 

# 8. conda deactivate (This will step us out of the Conda environment and back to our normal computer environment)

#Conda has a built-in "Solver" (that LibMamba thing). 
# Before it installs anything, it acts like a strict manager. 
# It looked at your request and said: "Wait a minute. Numpy 2.4.4 mathematically requires Python 3.11 or higher. 
# You are asking for Python 2.7. I refuse to let you break this steel box!" This solver is why data scientists trust Conda for massive, complex AI projects.
# It prevents you from accidentally destroying your own setup.
# 9.conda install python=2.7 numpy=2.4.4

# If you want to clone an existing Conda environment (like making a copy of your steel box), you can use the 'conda create --clone' command
# WHY: This is super useful if you want to experiment with changes without risking your original environment    
# 10. conda create --name clone_env --clone ai_env

# Summary:
# 1. Create a Conda environment: conda create -n ai_env python=3.11
# 2. Activate the Conda environment: conda activate ai_env
# 3. Install packages using Conda: conda install numpy
# 4. List installed packages in the Conda environment: conda list
# 5. Export environment to a file: conda env export > environment.yml
# 6. Create a new environment from the file: conda env create -f environment.yml
# 7. Remove the Conda environment: conda remove -n ai_env --all
# 8. Deactivate the Conda environment: conda deactivate
# 9. Test package compatibility: conda install python=2.7 numpy=2.4.4
# 10. Clone an existing Conda environment: conda create --name clone_env --clone ai_env



