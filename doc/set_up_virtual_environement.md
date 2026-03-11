How to set up the virtual environment
-----------------------------

1. Install python3 and the venv module

    On an Ubuntu/Debian system it is done with:
    ```bash
   sudo apt-get install python3 python3-venv
    ```
2. In the directory of the project to access the data, create a new virtual environment and activate it.
    
    For a virtual environment called "vizql_venv", on a linux system, it is done with: 
    ```bash
   python3 -m venv vizql_venv
   source vizql_venv/bin/activate
    ```
   
3. Install the requirements:
    ```bash
   pip3 install -r requirements
    ```