# Engineering-Test-Risk-Analytics
Engineering Test Risk Analytics
### Steps to run the Script
- create a virtual environment using virtualenv *[environment name]* and then activate it.
    example-- `vitualenv env`
               `.\env\Scripts\activate`
            
- install all the dependencies from requirement.txt using `pip install -r requirement.txt` in your virtual environment
- Once installed, drop the csv file in `Engineering Test Files` folder.
- Run the Script using `python -m src.main.py file_name` ex- `python -m src.main.py Engineering Test Files`
- **Output** : new csv file will get saved in `Engineering Test Files/Output` folder with the name **combined.csv**


**TESTING** : run  `python -m  pytest  Test/combined_csv_test.py`
