# Django-Python-Machine-Test
Django Python CURD Operations
1)	How did you run the code?
•	Execution via Django Development Server:
o	After setting up the Django project and necessary configurations, I ran the application by using the Django development server. This is typically done with the following command:
	python manage.py makemigrations        #Create migrations for your models: 
	python manage.py migrate                    #Apply to create database tables:

	python manage.py runserver    #TO RUN SERVER
o	This starts the server at http://127.0.0.1:8000/, which I used to access and test the web application locally.

2) How did you run the machine test?
•	Testing via Django Test Framework:
o	I used Django’s built-in testing framework to run the machine test. This involved:
	Writing test cases in a separate file (typically in tests.py).
	Running tests using:
	python manage.py test
	This allowed me to ensure that the models, views, serializers, and other parts of the application worked as expected.
o	Manual Testing (API Endpoint):
	I manually tested the API endpoints using tools like Postman or cURL to simulate requests to the endpoints, ensuring that the database and backend logic responded correctly.


3) DB Design
•	Database Configuration:
o	The database name is store_address, and the table address_client stores the client data. The table schema might look like this:
CREATE TABLE `address_client` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `client_name` VARCHAR(255) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `created_by` VARCHAR(255) NOT NULL
);
o	The Django model that corresponds to this schema is:
from django.db import models
class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    class Meta:
        db_table = 'address_client'  # Ensures the model uses the correct table name
•	Model Relationships:
o	If additional related tables (e.g., for addresses) exist, I would define them using Django's ForeignKey, OneToMany, or ManyToMany relationships. For example:
class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Foreign key to client
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    class Meta:
        db_table = 'address'
