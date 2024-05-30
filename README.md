# Description

This submission formed the basis of CSE304: PYTHON PROGRAMMING WITH WEB FRAMEWORKS end semester examinations conducted in February 2022.

# Problem

An owner of a working women hostel is interested in developing a Django application
The application should maintain details of hostel members. The Manager needs to have
a database with the following details:
Aadhar Number, Name, Age, Residential Address, Native Place, Mobile Number. A web framework should be developed to perform the following operations:

- A method to add member details into the database.
- Given a mobile number, a method to display details of a particular person in a
  web page
- A method to display the current occupant details in a web page

# Hostel Management App using Django

This application maintains details of hostel members.
The database contains details like
Aadhar Number, Name, Age, Residential Address, Native Place, Mobile Number.

It has methods to  
a. A method to add member details into the database.
b. Given a mobile number, a method to display details of a particular person in a
web page
c. A method to display the current occupant details in a web page

There are five html files
createnew,home,index,search, userdata which are rendered by a view upon request from user

The homepage contains links to each of those methods

Forms are used to create the objects of Hostel members class
It can also be created using django administration site

The credentials for the admin site
Username :python
Password :python

To search an occupant based on mobile number, a form is used of only one IntegerField
It compares with the existing objects of the Model class and returns it if there is a match.
