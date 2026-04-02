Tableau API at EPFL
========================

This repository goal is to help you connect to the EPFL datasources available through the tableau API.

Select the appropriate Notebook
---------------

Several Notebooks are available:
- The [personal_access_token.ipynb](personal_access_token.ipynb) notebook allows to access all the data available to your personal account. It is the preferred option but requires a bit of configuration. 
- The [public_jwt.ipynb](public_jwt.ipynb) notebook allows to access public data with a minimal configuration. 
- The [direct_trust_jwt.ipynb](direct_trust_jwt.ipynb) notebook should only be used if you requested access through a service account to the ISCS-BI team, and a specific configuration has been given to you. 

You can run the appropriate notebook either directly on [noto.epfl.ch](https://noto.epfl.ch) or locally after setting up the chosen system as described below. 

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
6. Reload the webpage.
7. Click on the link corresponding to the appropriate Notebook below to clone the tableau-api repository 
  and open the right notebook directly:
    - [personal_access_token.ipynb](https://noto.epfl.ch/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fepfl-si%2Ftableau_api&urlpath=lab%2Ftree%2Ftableau_api%2Fpersonal_access_token.ipynb&branch=master)
    - [public_jwt.ipynb](https://noto.epfl.ch/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fepfl-si%2Ftableau_api&urlpath=lab%2Ftree%2Ftableau_api%public_jwt.ipynb&branch=master)
    - [direct_trust_jwt.ipynb](https://noto.epfl.ch/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fepfl-si%2Ftableau_api&urlpath=lab%2Ftree%2Ftableau_api%direct_trust_jwt.ipynb&branch=master)


Setup locally
------------
1. Install python3 and the venv module.

    On an Ubuntu/Debian system it is done with:
    ```bash
    sudo apt-get install python3 python3-venv
    ```
2. Clone the tableau-api repository and go into the cloned directory
    ```bash
    git clone https://github.com/epfl-si/tableau_api.git $HOME/tableau_api
    cd $HOME/tableau_api
    ```
3. Create a new virtual environment and activate it:
    ```shell
    python -m venv tableau_api_venv
    source tableau_api_venv/bin/activate
    ```
4. Install the requirements
    ```shell
    pip install -r requirements.txt
    ```

Running locally
-----------------

1. Activate the virtual environment if not done already:
    ```bash
    cd $HOME/tableau_api
    source tableau_api_venv/bin/activate
    ```
2. Start the Notebook Server:
    ```bash
    jupyter notebook 
    ```
3. This will print some information about the notebook server in your terminal, 
    including the URL of the web application (by default, http://localhost:8888).

    It will then open your default web browser to the Notebook Dashboard at this URL.
4. Select the appropriate Notebook in the Notebook Dashboard.