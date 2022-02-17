# Driving School System
Driving School System app in Django(Python).

# Features
- Material design based UI.
- Login and Signup functionality.
- Customers can book class based on availability.
- See the booking history and edit order from the dashboard.

# Technology Used
 - HTML/CSS
 - [Materialize CSS](archives.materializecss.com/0.100.2)
 - Javascript( particularly AJAX, DOM)
 - Git
 - Django
# How to run the project
 - clone the repository. `git clone https://github.com/omarsolieman/ClassManagement`
 - Move to newly created git directory as `cd ClassManagement`
 - Install virtualenv as `pip3 install virtualenv`
 - Activate the newly created virtual environement `bookingApp\Scripts\activate`
 - Install all the dependencies as `pip install -r requirements.txt`
 - Traverse to the room_slot **main** directory as `cd class_slot` (This is the place where all source file are kept).
 - Start the development Server as `python manage.py runserver`
 - Visit `localhost:8000` in your browser to view the site live.
 - To deactivate virtual environment anytime use `deactivate`
# Features of the project
 - Fully responsive website(for both mobile and larger screens) based on google material design.
 - Login/Signup/Logout feature for both Student and Tutor.
 - Custom dashboard for both Student and Tutor.
 - Facility to add, delete, update rooms by Tutor.
 - Tutor can see the details of user that has booked one of his classes.
 - Student can cancel the class booking.
 - Contact form support for every visitor of website.
 - Admin have access to all the functionality listed above.

#Necessary Edits
- Models are in room_slot/booking/models.py
- also edit room_slot/api/serializers.py
 
