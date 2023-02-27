## Python check (powershell)
    python
    python --version
## Git check
    git
    git --version
## Data import from https using "wget" (cmd)
    wget -P <local location> <https: address>

    wget -P /DATA_Download https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv

**Todo**: Need to work out where the data is stored when using wget -P

    C:\Users\shara\ML_Projects>cd DATA_Download

    C:\Users\shara\ML_Projects\DATA_Download>wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv

## Data dump into MongoDB
    refer: "data_dump.py"
    create: requirements.txt
            packages: pymongo, pandas. json
            pip install -r requirements.txt
*Use **"r"** to convert from normal string to raw string*
    DATA_FILE_PATH = r"C:\Users\shara\ML_Projects\DATA_Download\aps_failure_training_set1.csv" 
    
##Github commit
    Select the working folder and Goto SOURCE CONTROL --> Initialize Repository --> 
    Then the main* branch will appear at bottom left corner.

    Create new Github repository. (APS_Sensor_Project)
        - Public
        - Add .gitignore template to python
    
    git remote -v (list all origin available)
    git remote remove origin (removes all origin available)
    
    create a new origin
        git remote add origin <#URL: of the repository APS_Sensor_Project>
        get remote -v (lists the newly created origin available)
            origin  https://github.com/sharathprakash81/APS_Sensor_Project.git (fetch)
            origin  https://github.com/sharathprakash81/APS_Sensor_Project.git (push)

## notebook for EDA, .gitignore and .env files


##setup.py 
    first file --> Source code as a library format!    (distribution of code)
    create requirements.txt file --> with "-e ." (HYPHEN_DOT_E)
    running pip install -r requirements.txt
             --> will install all the packages
             --> installation will happen in sensor folder as it has (__init__.py file added manually)
            --> will create a folder sensor.egg-info with all source packages
This is required for all projects as standard procedure
    

## Training Pipeline with the following components

![](notebook\Training_Pipeline.jpg)

**Artifact** (model/document) is output generatored by the training pipeline
**Configuration** is input for the training pipeline
**Entity** is an light weight persistence domain object.(I/O structure)
**utils** helper functions

##Folder structure:

![](notebook\project_prep_1.JPG)

#####
