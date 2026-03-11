Tableau API at EPFL
========================

This repository goal is to help you connect to the EPFL datasources available through the tableau API.

Setup on Noto
-------------

1. Login in [noto.epfl.ch](https://noto.epfl.ch).
2. Open a terminal (File > New > Terminal)
3. Create a new virtual environment called tableau_api and activate it.
    ```shell
    my_venvs_create tableau_api
    my_venvs_activate tableau_api
    ```
4. Install the requirements
    ```shell
    pip install -r requirements.txt
    ```
5. Create a new kernel called "tableau_api" and displayed as "Tableau API":
    ```shell
    my_kernels_create tableau_api "Tableau API"
    my_venvs_deactivate
    ```
6. Reload the page.

Setup locally
------------
1. Install python3 and the venv module.

    On an Ubuntu/Debian system it is done with:
    ```bash
    sudo apt-get install python3 python3-venv
    ```
2. create a new virtual environment and activate it:
    ```shell
    python -m venv tableau_api
    source tableau_api/bin/activate
    ```
3. Install the requirements
    ```shell
    pip install -r requirements.txt
    ```
