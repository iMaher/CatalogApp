# Item Catalog App
This web app is a project for the Udacity Full Stack Nanodegree Course.

## About the project

This project will display list of items within a variety of categories and description of each item.Also provide the users who are already registered to add, edit, and delete items in each categories once they login to the app.  

# How to run the app?

**Note: Before you start run the application there are some requirements need to be done as listed bellow **

## System Requirement and Configuration
You will need to install the following applications
* Install [Vagrant](https://www.vagrantup.com/)
* Install [VirtualBox](https://www.virtualbox.org/)
* Clone [FSND VM](https://github.com/udacity/fullstack-nanodegree-vm)
* Add catalog app project inside vagrant folder

### run the project
1. Open Terminal
2. Run vagrant 'vagrant up'  
`$ vagrant up`
3. Enter remote to vagrant as ssh  
`$ vagrant ssh`
4. Run "database_setup.py" to setup and create the database  
`$ python database_setup.py`
5. Run "lotsofdata.py" to insert all the data to database  `$ python lotsofdata.py`
6. run "project.py" to start using the project  `$ python project.py`
7. open your browser and go to http://localhost:8000
8. enjoy

## JSON endpoint
to access JSON file go to http://localhost:8000/catalog.json
