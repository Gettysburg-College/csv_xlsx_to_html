# Transcription: CSV/XLSX to HTML Format

# About CSV/XLSX to HTML project

Get student information (rows) from files and convert into html. The program will generate a html file. For staffs at Gettysburg College who work with dotCMS system, we can copy source code from that file and paste it into the dotCMS editing page, especially for editing Dean's Honor List and Dean's Commendation List.

---

### Table of content
1. [Model](#Model)
2. [Codebase](#Codebase)
3. [Files format](#Files-format)
4. [How to run the package](#How-to-run-the-package)

---

## Model:

<img src="./doc/model.jpg" width=500/>

---

## Codebase:

  * Data folder:
    * `file_name.csv` or `file_name.xlsx`: the files that need to be convert into html. Data is stored as a table following [our format](#Files-format).
  * Doc folder:
    * `model.jpg`: the structure of this program as a UML graph.
  * Output folder:
    * `output_file.html`: the output file of this program.
  * Tool folder:
    * `table.py`:contains object-oriented class `Table`. Each `Table` object is a class year cohort including:
      * `table_id`: each table will have only one unique id
      * `table_name`: name of table
      * `rows`: each row is a student with information stored as Dictionary
    * `reader.py`: contains object-oriented class `Reader` needed to pass parameter: data file path as `str`. This class reads data from `.csv` or `.xlsx` file and store data in each class each as `rows` in `Table` object.
    * `page.py`: contains object-oriented class `Page` needed to pass parameter: a `Reader` object. This class contains skeleton structure for HTML file.
  * `main.py`: the main file to run this program.
  * `requirements.txt`: contains required libraries and their version. Follow [How to run the package](#How-to-run-the-package) section to know how to use this file.

---

## Files format

Table format: 
- Column name (1st row): Last-Name, First-Name, Middle-Name, Exp-Grad.
- Students are listed in order from Seniors, Juniors, Sophomores, and First Years.
* Note: check files `\data\Deans Commendation List.csv` or `\data\Deans Commendation List.xlsx` for examples.

|  Last-Name  |  First-Name  |  Middle-Name  |   Exp-Grad  |
|  ---------  |  ----------  |  -----------  |   --------  |
| Seniors     |              |               |             |
| stud's last | stud's first | stud's middle | Exp Grad yr |
|             |              |               |             |
| Juniors     |              |               |             |
| stud's last | stud's first | stud's middle | Exp Grad yr |
|             |              |               |             |
| Sophomores  |              |               |             |
| stud's last | stud's first | stud's middle | Exp Grad yr |
|             |              |               |             |
| First Years |              |               |             |
| stud's last | stud's first | stud's middle | Exp Grad yr |
|             |              |               |             |


File location:
- All files should be put in `data` folder.

---

## How to run the package

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
    # python3 main.py <data_file> <output_file>
    
    # For example:
    
    python3 main.py "./data/Deans Commendation List.csv" "./output/commendation.html"
    ```
    The html file can be found in `output` folder.

  * Note: You can change `pip3` to `pip` and `python3` to `python` if possible.
  * Note: command `./data/Deans Commendation List.csv` can be changed based on your file name.



