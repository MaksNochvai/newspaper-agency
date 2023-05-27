# newspaper-agency
Newspaper Agency

This project is a web application designed for managing the process of publishing and managing news articles in a newspaper agency. The application provides a user-friendly interface for adding, editing, and deleting articles, as well as managing journalists and editors.

Key Features:
- Add new articles with titles, content, authors, and categories.
- Edit and update existing articles.
- Delete articles that are no longer relevant.
- Manage users, including journalists and editors.
- Search and filter articles by categories, dates, and other parameters.

Technologies Used:
- Python: Programming language for the application's backend logic.
- Django: Web framework for rapid and convenient web development.
- HTML/CSS: Markup and styling languages for creating the web interface.
- PostgreSQL: Database for storing article and user information.

## DB-structure: 
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/a61e3420-482f-40ba-99db-3cb94edec589)

# Test User Credentials

- Username: guest
- Password: guest123

## Login page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/dccc9713-d050-47d6-8ac5-cbf57d223d18)

## Home page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/0c078405-efc5-4e1b-ac20-c5942cce284a)

## Side bar:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/1730f4a6-eed7-47b2-90ad-693033908e57)

## All redactors page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/57470c02-2b83-4768-9bd7-2ca9e73bd246)

## Create redactor page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/b303b2fb-bf35-4f4b-ac29-449889f40bf6)

## Detail redactor page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/0acb047c-215d-4efa-aa9d-0d387bb703c4)

## Update redactor page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/107ecf22-5183-48c3-9914-60f90f1e3048)

## Delete redactor page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/8a9f1b1c-0445-4fe1-9f75-3485bdfa57ec)

## All newspaper page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/e87318ce-a621-4416-ad7a-b28e3463d6c8)

##Create newspaper page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/28fa2971-2a5f-43cd-8eda-a9f75fafc004)

## Detail newspaper page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/0f717d6c-3a00-4f57-b5a5-8aafb4e59d94)

##Update newspaper page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/7bfc405c-d9dd-4a74-98c4-8bb21119d64e)

## Delete newspaper page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/d2e8d35e-7d28-44c9-91ac-beccf718eae3)

## All topic page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/26f4e24f-04bb-4f78-9ddc-a8d5db89edba)

## Update/create topic page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/e7d62b47-9633-42a9-9856-cb73fa18f1d7)
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/75390263-b1f7-41fc-b914-465c2f5a9523)

## Delete topic page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/473b5c0a-3679-4f96-aa44-0b7654319074)

## Logout page:
![image](https://github.com/MaksNochvai/newspaper-agency/assets/123680608/8cef3d54-fa50-4440-bcb7-d57d7e002fe3)

To set up the project locally, follow these steps:

1. Clone the project repository to your computer.
2. Navigate to the project directory.
3. Create a virtual environment for the project: python3 -m venv env
4. Activate the virtual environment:
   - For Windows: .\env\Scripts\activate
   - For macOS/Linux: source env/bin/activate
5. Install the project dependencies: pip install -r requirements.txt
6. Create a .env file in the project root directory and add your secret key and other environment variables. Refer to the .env.sample file for the required variables.
7. Update the database settings in the settings.py file to match your local database configuration.
8. Apply the database migrations: python manage.py migrate
9. Load the test data fixture: python manage.py loaddata test_data.json
10. Create a superuser account for accessing the admin interface: python manage.py createsuperuser
11. Start the development server: python manage.py runserver
12. Access the application in your browser at http://localhost:8000/
