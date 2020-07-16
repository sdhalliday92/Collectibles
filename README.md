# **Collectibles App**

## **Resources**
- Trello - https://trello.com/b/KdnuhFZX/collectibles-week-5-project
- Website - http://35.214.92.246

### **Contents**
- Brief
  * Minimum Requirements
- Functionality
- Data
- Tech Stack
- CI Pipeline
- Front End Design
- Risk Assessment
- Difficulties
- Future Improvements
- Authors

### **Brief**
The brief for this project was "To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training".
This meant building an app that could take input from a user in order to create, read, update and delete data in a database while also making this visible to the user via the app itself.

#### **Minimum Requirements**
- A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
- It could also provide a record of any issues or risks that you faced
creating your project.
- A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
- Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
- A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board
- Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
- A functioning front-end website and integrated API's, using Flask.
- Code fully integrated into a Version Control System using the
- Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

### **Functionality**
To satisfy the brief I designed an app that would allow users to create a list of collectibles that they owned.
The users stories that satisfied the brief were:
- As a User, I would like to have a function that allows me to CREATE/ADD to the database.
- As a User, I would like to have a function that allows me to READ the database.
- As a User, I would like to have a function that allows me to UPDATE the database.
- As a User, I would like to have a function that allows me to DELETE from the database.

The below images show all the user stories created for this app as well as the layout and flow of the AGILE cycle that was implemented throughout.

IMAGE

### **Data**
It is important to outline what data will be included in the database and how it will all relate. The entity relationship diagram (ERD) below shows this.

IMAGE

The ERD shows the relationship between the Collectibles and Users tables.

### **Tech Stack**
The below tech stack was implemented for this project.
- GCP SQL Server
- GCP Virtual Machine
- Trello
- Python
- Flask
- Git
- Jenkins

### **CI Pipeline**
The below image shows the flow of the app and how the tech stack is used in the Continuous Integration (CI) Pipeline.

IMAGE

### **Front End Design**
The front end design of the app is very basic and is made to be functional.
The apps URL will take the user to the Home page.

IMAGE?
IMAGE?
IMAGE?

### **Risk Assessment**

IMAGE

### **Difficulties**
The main difficulties encountered were ones of my own making, pieces of code missing or references not answered.
With my own incompetance aside other issues involved design. My initial designs for the appearance and operation of the app were far more difficult to employ than I anticipated. Things such as drop down menus and images were put aside and changed to allow easier functionality.

### **Future Improvements**
- To allow social media integration to allow the sharing of users lists
- To improve the pages design, include images and more colour

### **Author**
Scott Halliday
