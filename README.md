# crud-project

## Brief
The objective of this project was to develop a fully functional CRUD application with use of the tools and concepts that we have covered up to this point. These tools and concepts are:


    Project Management
    Python Fundamentals
    Python Testing
    Git
    Basic Linux
    Python Web Development
    Continuous Integration
    Cloud Fundamentals
    Databases

## Requirements
The requirements of the project were the following:


    A Trello board (or equivalent Kanban board tech) with full expansion on user stories, use cases and tasks needed to complete the project. It could also provide a record of any issues or risks that you faced creating your project.
    A relational database used to store data persistently for the project, this database needs to have at least 2 tables in it, to demonstrate your understanding, you are also required to model a relationship.
    Clear Documentation from a design phase describing the architecture you will use for you project as well as a detailed Risk Assessment.
    A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on your Kanban Board
    Fully designed test suites for the application you are creating, as well as automated tests for validation of the application. You must provide high test coverage in your backend and provide consistent reports and evidence to support a TDD approach.
    A functioning front-end website and integrated API's, using Flask.
    Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

## Project Aprroach:
My project is all about users reviewing albums for others to read. This meant that it had to do all of the following:

    Create and add a review of an Album
    It must show the following on the front end:
        Album Title
        Album Artist
        Genre of the Album
        The Review itself
        Rating of the Album
    View and update reviews
    Delete reviews

# ERD

## Plan
Below is my plan for my ERD. This database will be hosted on a Google Cloud Platform SQL instance using MySQL. This will allow the user to create, read, update and delete reviews. These tables have a one to many relationship, as albums are allowed multiple reviews, however not every album wants the review.

![ERD](https://i.imgur.com/gV9vsv7.png)

# CI Pipeline
The CI Pipeline used for the development can be seen below
![CI Pipeline](https://i.imgur.com/vGqE0zW.png)

# Project Trackng
For the project I used GitHubs inbuilt project tracker as a planning tool, as well as to host my user stories. Below is a screenshot of my project board
![Trello Board](https://i.imgur.com/jPacOKT.png)

# Testing
Testing of this app was done using pytest. When checking the coverage, it seemed that the apps total coverage combined was around 83%, with the one test managing to cover 66% and the other covering 100%. Testing helped me make sure that my app was doing what was intending, and throwing errors when I expected it to.
![Test Cov](https://i.imgur.com/NcK1JPC.png)

# Deployment
This app was deployed for testing with use in Jenkins, a CI Server. Jenkins was installed onto a GCP instance, which allowed me to login and test the app using the inbuilt testing features.
![Jenkins](https://i.imgur.com/hTOpNro.png)
The app was also deployed via Gunicorn, this takes it out of development and puts it into a real, user ready production environment.
![Gunicorn](https://i.imgur.com/GBhk1cE.png)
# Risk Asessment
I have thought of different risks for my risk assessment, as shown below. I made a matrix that identified risks, mitigators and what the objective of the mitigator was, along with a likelihood and impact of the risk based on how it would affect the app or user.
![Risk Asessment](https://i.imgur.com/pmlH8ND.png)

# Technlogies Used
 
    Database: GCP SQL Server
    Programming language: Python
    Framework: Flask
    Deployment: Gunicorn
    CI Server: Jenkins
    Test Reporting: Pytest, Selenium
    VCS: Git
    Project Tracking: GitHub
    Live Environment: GCP
# Future Improvements
Future improvements for this project would be focused on adding features to the project. This would include the following:

    Allow users to add their own albums, complete with genre and artist
    Add a fully functioning filter, to make sure that expletives etc can be cut out
    A feature that allows people to say if a review was helpful or not

