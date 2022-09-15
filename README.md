# Engineering-Test-Risk-Analytics
Engineering Test Risk Analytics
### Steps to run the Script
- create a virtual environment using virtualenv *[environment name]* and then activate it.
    example-- `vitualenv env`
               `.\env\Scripts\activate`
            
- install all the dependencies from requirement.txt using `pip install -r requirement.txt` in your virtual environment
- Once installed, for example- drop the csv file in `Engineering Test Files` folder and use this folder when asked.
- Run the Script using `python -m src.main.py` ex- `python -m src.main.py` then enter the folder name
- **Output** : new csv file will get saved in Output folder for example `Engineering Test Files/Output` folder with the name **combined.csv**


**TESTING** : run  `python -m  pytest  Test/combined_csv_test.py`
