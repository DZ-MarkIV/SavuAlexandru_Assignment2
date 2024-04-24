Simple Python application showcasing user access with authentication through an SQL Database.
App created using Visual Studio 2019, MySQL Server, MySQL Workbench, and Python 3.12.3.

Application UI has been creating using the Tkinter module.

Features:
  - Connection to a MySQL database using the mysql.connector module.
  - Log in page where users can either log in or create an account.
  - 3 levels of user power: Normal user, Administrator, and Root.
  - Administrators can create a Normal user as well as delete them, but they cannot delete other Administrators.
  - Root can create Normal Users, Administrators as well as delete both of them. The Root user cannot be deleted.

Under constant analysis from Sonarqube.
