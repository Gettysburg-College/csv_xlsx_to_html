# Transcription: CSV/XLSX to HTML Format

* Model:
  <img src="./doc/model.jpg" width=500/>
  


# Running
To get html of Commendation List:
```
python main.py "./data/Deans Commendation List.csv" "./output/commendation.html"
```

To get html of Honor List:
```
python main.py "./data/Deans Honor List.csv" "./output/honor.html"
```

# Files

Table format: 
- Column name (1st row): Last-Name, First-Name, Middle-Name, Exp-Grad.
- Students are listed in order from Seniors, Juniors, Sophomores, and First Years.
* Note: check files `\data\Deans Commendation List.csv` or `\data\Deans Commendation List.xlsx` for examples.

File location:
- All files should be put in `data` folder.

# How to run the package
1. Requirements:
  - Python 3

2. Run this in bash:
  - Install related python library:
  ```
  pip3 install -r ./requirements.txt
  ```
  - Run the main file from the package:
    - To get html of Commendation List:
    ```
    python3 main.py "./data/Deans Commendation List.csv" "./output/commendation.html"
    ```
    - To get html of Honor List:
    ```
    python3 main.py "./data/Deans Honor List.csv" "./output/honor.html"
    ```
    The html file can be found in `output` folder.

  * Note: You can change `pip3` to `pip` and `python3` to `python` if possible.
  * Note: command `./data/Deans Commendation List.csv` can be changed based on your file name.



