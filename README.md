# codeAlpha_Project_Management_Tool
# ProjectFlow – Project Management Tool

> A full-stack collaborative project management platform inspired by tools like Trello and Asana.

---

## Internship Task

**Program:** Artificial Intelligence Tasks & Instructions  
**Organization:** CodeAlpha  
**Task:** Task 3 – Project Management Tool  
**Project Type:** Full-Stack Web Application  
**Backend:** Django  
**Frontend:** HTML, CSS, JavaScript  
**Database:** SQLite  
**Programming Language:** Python  
**Real-Time Communication:** Django Channels + WebSockets

---

## 1. Project Overview

ProjectFlow is a collaborative project management web application designed to help users organize projects, create tasks, assign work, and communicate through task comments.

The system provides a centralized workspace where users can manage their projects and track tasks efficiently.

The application is inspired by popular project management platforms such as:

- Trello
- Asana

The main objective of this project is to implement a complete full-stack application with authentication, project management, task management, comments, and optional real-time communication.

---

## 2. Main Objectives

The main objectives of ProjectFlow are:

- User registration and authentication
- Secure login and logout
- Create group projects
- Add project members
- Create and manage tasks
- Assign tasks to users
- Track task status
- Set task priority
- Add task due dates
- Comment within tasks
- Communicate with project members
- Display project boards
- Manage projects from a dashboard
- Provide an admin panel
- Support real-time updates using WebSockets
- Provide notifications for project activities

---

## 3. Core Features

### Authentication

Users can:

- Register a new account
- Login using username and password
- Logout securely
- Access protected pages only after authentication

### Registration Flow

```text
New User
    ↓
Registration Page
    ↓
Enter User Information
    ↓
Form Validation
    ↓
Account Created
    ↓
Login Page
```

### Login Flow

```text
Login
    ↓
Authentication
    ↓
Session Created
    ↓
Dashboard
```

Unauthenticated users are redirected to the login page when accessing protected pages.

---

## 4. User Dashboard

After successful login, users are redirected to the dashboard.

The dashboard provides an overview of the user's projects.

Users can:

- View existing projects
- Create new projects
- Open project boards
- Access assigned tasks
- Navigate to project details
- Logout from the system

### Dashboard Flow

```text
User Login
    ↓
Authentication
    ↓
Dashboard
    ↓
View Projects
    ↓
Create / Open Project
```

---

## 5. Project Management

Users can create collaborative projects.

Each project contains information such as:

- Project name
- Project description
- Project owner
- Project members
- Creation date
- Updated date

### Create Project Flow

```text
Dashboard
    ↓
Create Project
    ↓
Enter Project Information
    ↓
Form Validation
    ↓
Project Created
    ↓
Project Owner Added as Member
    ↓
Project Board
```

The project creator automatically becomes the project owner and is also added as a project member.

---

## 6. Project Board

The project board is the main workspace for managing project tasks.

It displays tasks in an organized structure.

A typical board can contain:

```text
Project Board
      ↓
┌───────────────┬───────────────┬───────────────┐
│    TODO       │  IN PROGRESS  │    DONE       │
├───────────────┼───────────────┼───────────────┤
│ Task 1        │ Task 3        │ Task 5        │
│ Task 2        │ Task 4        │ Task 6        │
└───────────────┴───────────────┴───────────────┘
```

This makes it easier to understand the current state of project work.

---

## 7. Task Management

Project members can create tasks inside a project.

A task can contain:

- Task title
- Task description
- Assigned user
- Task status
- Task priority
- Due date
- Project
- Creation date
- Updated date

### Task Creation Flow

```text
Project Board
    ↓
Create Task
    ↓
Enter Task Information
    ↓
Select Assignee
    ↓
Select Priority
    ↓
Select Status
    ↓
Set Due Date
    ↓
Save Task
    ↓
Task Appears on Project Board
```

---

## 8. Task Status

Tasks can have different statuses.

Example:

- TODO
- IN PROGRESS
- DONE

The status helps users understand the current progress of each task.

```text
TODO
  ↓
IN PROGRESS
  ↓
DONE
```

---

## 9. Task Priority

Tasks can be organized according to priority.

Example priorities:

- Low
- Medium
- High

This helps team members identify important tasks.

```text
Low
  ↓
Medium
  ↓
High
```

---

## 10. Task Assignment

Project members can be assigned to specific tasks.

Example:

```text
Project
    ↓
Task
    ↓
Select Team Member
    ↓
Assign Task
    ↓
Member Can Work on Task
```

Task assignment helps distribute project responsibilities among team members.

---

## 11. Task Details

Each task has a dedicated task detail page.

The task detail page can display:

- Task title
- Description
- Assigned user
- Status
- Priority
- Due date
- Project information
- Comments
- Comment form

### Task Detail Flow

```text
Project Board
    ↓
Click Task
    ↓
Task Detail Page
    ↓
View Task Information
    ↓
Read Comments
    ↓
Add Comment
```

---

## 12. Comments and Communication

Users can communicate inside individual tasks through comments.

A comment contains:

- Comment author
- Comment text
- Related task
- Created date

### Comment Flow

```text
Task Detail
    ↓
Write Comment
    ↓
Submit Comment
    ↓
Comment Saved
    ↓
Comment Displayed
```

This allows team members to discuss task-related information without leaving the project.

---

## 13. Notifications

ProjectFlow can provide notifications for important project activities.

Possible notification events include:

- New task assignment
- New project membership
- New comment
- Task status changes
- Important project updates

Example:

```text
Project Activity
      ↓
Event Generated
      ↓
Notification Created
      ↓
User Receives Notification
```

---

## 14. Real-Time Updates

The project can use Django Channels and WebSockets for real-time communication.

WebSockets allow the server to communicate with connected clients without requiring a full page refresh.

### WebSocket Concept

```text
User A
   ↓
WebSocket Connection
   ↓
Django Channels
   ↓
Server
   ↓
Project Group
   ↓
User B
```

For example, when a new task or comment is created, connected users can receive updates in real time.

---

## 15. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Database |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| JavaScript | Frontend interaction |
| Django Channels | WebSocket support |
| Daphne | ASGI server |
| WebSockets | Real-time communication |
| Django Authentication | User authentication |

---

## 16. Project Architecture

ProjectFlow follows a Django-based application architecture.

```text
User
  ↓
Browser
  ↓
HTML / CSS / JavaScript
  ↓
Django URLs
  ↓
Django Views
  ↓
Forms / Models
  ↓
SQLite Database
```

For real-time communication:

```text
Browser
  ↓
WebSocket
  ↓
Django Channels
  ↓
Consumer
  ↓
Database / Event
  ↓
Connected Users
```

---


```

---

## 17. Django Applications

The project is divided into multiple Django apps.

### accounts

Responsible for:

- User registration
- User login
- User logout
- Authentication
- Dashboard access

### projects

Responsible for:

- Project creation
- Project details
- Project members
- Project ownership
- Project board

### tasks

Responsible for:

- Task creation
- Task assignment
- Task status
- Task priority
- Due dates
- Task details

### comments

Responsible for:

- Task comments
- User communication
- Comment creation
- Comment display

---

## 18. Database Models

The main database entities are:

```text
User
  ↓
Project
  ↓
Task
  ↓
Comment
```

A project can have multiple members.

```text
User
  ↓
Many-to-Many
  ↓
Project
```

A project can contain multiple tasks.

```text
Project
  ↓
One-to-Many
  ↓
Task
```

A task can contain multiple comments.

```text
Task
  ↓
One-to-Many
  ↓
Comment
```

---

## 19. Authentication System

ProjectFlow uses Django's built-in authentication system.

Authentication provides:

- User login
- User logout
- Password hashing
- Session management
- Login protection
- User permissions

Protected views use Django authentication mechanisms to prevent unauthorized access.

---

## 20. Forms and Validation

Django Forms are used to process user input.

Forms are used for:

- Registration
- Login
- Project creation
- Task creation
- Comment creation

The form system helps validate submitted data before storing it in the database.

```text
User Input
    ↓
Django Form
    ↓
Validation
    ↓
Valid Data
    ↓
Database
```

If validation fails:

```text
User Input
    ↓
Form Validation
    ↓
Invalid Data
    ↓
Error Message
    ↓
Form Displayed Again
```

---

## 21. URL Routing

The application uses Django URL routing.

Main routes include:

```text
/
    ↓
Home

/accounts/
    ↓
Authentication

/projects/
    ↓
Project Management

/tasks/
    ↓
Task Management

/comments/
    ↓
Comment Management

/admin/
    ↓
Django Admin Panel
```

---

## 22. Admin Panel

Django's built-in admin panel is available for administrative management.

Admin users can manage:

- Users
- Projects
- Tasks
- Comments
- Notifications

Admin URL:

```text
/admin/
```

A superuser can be created using:

```bash
python manage.py createsuperuser
```

---

## 23. Installation Requirements

Before running the project, make sure Python is installed.

Recommended environment:

```text
Python 3.10+
Django 5.2+
SQLite
```

For real-time features:

```text
Channels
Daphne
```

---

## 24. Create Virtual Environment

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

After activation, the terminal should display:

```text
(venv)
```

---

## 25. Install Required Packages

Install Django:

```bash
pip install django
```

Install Channels:

```bash
pip install channels
```

Install Daphne:

```bash
pip install daphne
```

Or install everything together:

```bash
pip install django channels daphne
```

Check Django:

```bash
python -m django --version
```

Check installed packages:

```bash
pip list
```

---

## 26. Database Setup

After creating or updating models, generate migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Check migration status:

```bash
python manage.py showmigrations
```

Check the complete Django project:

```bash
python manage.py check
```

---

## 27. Create Admin User

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Django will ask for:

```text
Username:
Email address:
Password:
Password (again):
```

Use your own username and email.

The password must be entered exactly the same during both password prompts.

---

## 28. Run Development Server

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the development server:

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

Login page:

```text
http://127.0.0.1:8000/accounts/login/
```

---

## 29. Development Workflow

The recommended development workflow is:

```text
Create Virtual Environment
    ↓
Activate Virtual Environment
    ↓
Install Dependencies
    ↓
Create Django Project
    ↓
Create Django Apps
    ↓
Configure settings.py
    ↓
Create Models
    ↓
Create Forms
    ↓
Create Views
    ↓
Configure URLs
    ↓
Create Templates
    ↓
Add CSS
    ↓
Add JavaScript
    ↓
Create Migrations
    ↓
Apply Migrations
    ↓
Run System Check
    ↓
Run Development Server
    ↓
Test Application
```

---

## 30. Application User Flow

The complete user flow is:

```text
Start Application
    ↓
Home Page
    ↓
Login / Register
    ↓
Authentication
    ↓
Dashboard
    ↓
Create Project
    ↓
Project Board
    ↓
Create Task
    ↓
Assign Task
    ↓
Update Task Status
    ↓
Open Task Details
    ↓
Add Comment
    ↓
Team Communication
    ↓
Project Completed
```

---

## 31. Project Collaboration Flow

Multiple users can collaborate on a project.

```text
Project Owner
      ↓
Create Project
      ↓
Add Members
      ↓
Create Tasks
      ↓
Assign Tasks
      ↓
Team Members Work
      ↓
Update Task Status
      ↓
Comment on Tasks
      ↓
Track Project Progress
```

---

## 32. Task Lifecycle

A task normally follows this lifecycle:

```text
Task Created
    ↓
Task Assigned
    ↓
TODO
    ↓
IN PROGRESS
    ↓
DONE
```

If a task needs additional work, it can move back:

```text
DONE
  ↓
IN PROGRESS
```

---

## 33. Error Checking Commands

Use these commands when debugging the project.

### Django System Check

```bash
python manage.py check
```

### Deployment Check

```bash
python manage.py check --deploy
```

### Check Pending Migrations

```bash
python manage.py makemigrations --check --dry-run
```

### View Migrations

```bash
python manage.py showmigrations
```

### Check Installed Django

```bash
python -m django --version
```

### Check Python

```bash
python --version
```

### Check Pip

```bash
pip --version
```

### Check Installed Packages

```bash
pip list
```

---

## 34. Common Problems and Solutions

### Problem 1 – Django Not Found

Error:

```text
ModuleNotFoundError: No module named 'django'
```

Solution:

```bash
source venv/bin/activate
pip install django
```

Then verify:

```bash
python -m django --version
```

---

### Problem 2 – Server Not Running

If the browser shows:

```text
ERR_CONNECTION_REFUSED
```

make sure the Django development server is running:

```bash
python manage.py runserver
```

Keep the terminal running while accessing the website.

---

### Problem 3 – Migration Problems

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

Then check:

```bash
python manage.py showmigrations
```

---

### Problem 4 – URL NoReverseMatch

If Django shows:

```text
NoReverseMatch
```

check:

- URL name
- URL pattern
- Namespace
- Required URL parameters
- Template `{% url %}` values

For example:

```django
{% url 'create_task' project.id %}
```

requires a valid project ID.

---

### Problem 5 – Virtual Environment Not Activated

If Django suddenly cannot be found, activate the environment:

```bash
source venv/bin/activate
```

The terminal should show:

```text
(venv)
```

Then run:

```bash
python manage.py check
```

---

## 35. Frontend

The frontend uses:

- HTML5
- CSS3
- JavaScript

The templates provide the application interface.

Main templates:

```text
base.html
    ↓
login.html
register.html
dashboard.html
project.html
task_detail.html
```

The `base.html` template provides common elements such as:

- Navigation
- Branding
- User links
- Common layout

---

## 36. JavaScript

JavaScript is used for client-side interaction.

Possible functionality includes:

- Confirm actions
- Dynamic UI updates
- Notifications
- WebSocket connection
- Real-time messages
- Interactive task updates
- UI feedback

---

## 37. Static Files

Static files are organized as:

```text
static/
    ↓
css/
    ↓
style.css

static/
    ↓
js/
    ↓
main.js
```

CSS controls the visual design.

JavaScript controls browser-side interaction.

---

## 38. Security

The application uses Django security features such as:

- Password hashing
- CSRF protection
- Session authentication
- Login-required views
- Form validation
- Django ORM
- Permission checking

For production deployment, additional security settings should be configured.

---

## 39. Development vs Production

This project is primarily designed for development and internship demonstration.

Development settings may include:

```python
DEBUG = True
```

For production, security configuration should be improved, including:

- `DEBUG = False`
- Proper `ALLOWED_HOSTS`
- Secure secret key
- HTTPS
- Secure cookies
- HSTS
- Production database
- Proper static file configuration

---

## 40. Testing Checklist

Before submitting the project, test the following:

```text
[ ] Registration works
[ ] Login works
[ ] Logout works
[ ] Dashboard opens
[ ] Project creation works
[ ] Project details open
[ ] Project members work
[ ] Task creation works
[ ] Task assignment works
[ ] Task status works
[ ] Task priority works
[ ] Due date works
[ ] Task details open
[ ] Comments work
[ ] Notifications work
[ ] WebSocket functionality works
[ ] Admin panel works
[ ] Database migrations are applied
[ ] No Django system-check errors
[ ] Static files load correctly
```

---

## 41. Important Django Commands

### Start Project

```bash
django-admin startproject project_management
```

### Create Apps

```bash
python manage.py startapp accounts
python manage.py startapp projects
python manage.py startapp tasks
python manage.py startapp comments
```

### Create Migrations

```bash
python manage.py makemigrations
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

### Check Project

```bash
python manage.py check
```

---

## 42. Project Architecture Summary

```text
                    PROJECTFLOW
                         ↓
              Project Management System
                         ↓
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
    Accounts          Projects          Tasks
        ↓                ↓                ↓
 Authentication     Project Board     Task Cards
        ↓                ↓                ↓
   Users/Login       Members          Assignment
                                         ↓
                                      Status
                                         ↓
                                      Priority
                                         ↓
                                      Due Date
                                         ↓
                                      Comments
```

---

## 43. Real-Time Architecture

When WebSockets are enabled:

```text
                    Browser
                       ↓
                 WebSocket
                       ↓
              Django Channels
                       ↓
                   Consumer
                       ↓
                Project Group
                  ↓       ↓
                 User A  User B
                  ↓       ↓
               Real-Time Updates
```

This allows connected users to receive project updates without manually refreshing the page.

---

## 44. Learning Concepts Used

This project demonstrates several important concepts.

### Python

- Variables
- Functions
- Classes
- Modules
- Object-Oriented Programming
- Exception handling

### Django

- Django project structure
- Django apps
- Models
- Views
- Templates
- URLs
- Forms
- Authentication
- ORM
- Migrations
- Admin panel
- Static files
- Middleware

### Database

- SQLite
- ForeignKey
- ManyToManyField
- Database relationships
- CRUD operations

### Frontend

- HTML
- CSS
- JavaScript
- Forms
- DOM interaction

### Advanced Concepts

- Django Channels
- ASGI
- WebSockets
- Real-time updates
- Notifications
- Collaborative applications

---

## 45. CRUD Operations

ProjectFlow implements CRUD concepts.

### Create

```text
Create Project
Create Task
Create Comment
```

### Read

```text
View Projects
View Tasks
View Comments
```

### Update

```text
Update Task Status
Update Task Information
```

### Delete

```text
Delete Project
Delete Task
Delete Comment
```

CRUD means:

```text
C → Create
R → Read
U → Update
D → Delete
```

---

## 46. Advantages of ProjectFlow

ProjectFlow provides:

- Centralized project management
- Better team collaboration
- Task assignment
- Progress tracking
- Task communication
- Organized project boards
- User authentication
- Real-time communication support
- Simple and responsive interface

---

## 47. Future Improvements

The application can be extended with:

- Drag-and-drop task cards
- Calendar view
- Email notifications
- File attachments
- Task search
- Task filtering
- Project analytics
- Progress charts
- User profile pages
- Dark mode
- Mobile responsive improvements
- Advanced permissions
- REST API
- PostgreSQL
- Cloud deployment
- Redis-based WebSocket channel layer

---

## 48. Possible Production Architecture

For a production version:

```text
User
  ↓
Frontend
  ↓
Nginx
  ↓
Django / Daphne
  ↓
Django Channels
  ↓
Redis
  ↓
PostgreSQL
```

This architecture would provide better scalability than the development setup.

---

## 49. Expected Result

After successful implementation, ProjectFlow should provide a complete workflow:

```text
Register
    ↓
Login
    ↓
Dashboard
    ↓
Create Project
    ↓
Add Members
    ↓
Create Tasks
    ↓
Assign Tasks
    ↓
Update Status
    ↓
Open Task
    ↓
Comment
    ↓
Collaborate
    ↓
Track Progress
    ↓
Complete Project
```

---

## 50. Project Goal

The primary goal of this internship project is to demonstrate practical knowledge of full-stack web development using Django.

The project combines:

```text
Python
   +
Django
   +
SQLite
   +
HTML
   +
CSS
   +
JavaScript
   +
Authentication
   +
Project Management
   +
Task Management
   +
Comments
   +
WebSockets
```

into a single collaborative application.

---

## 51. Conclusion

ProjectFlow is a full-stack project management application designed to simplify team collaboration and project tracking.

It demonstrates how a real-world web application can be developed using Django and modern web technologies.

The application provides the core features required by the internship task:

```text
Group Projects
    ↓
Project Boards
    ↓
Task Cards
    ↓
Task Assignment
    ↓
Task Status
    ↓
Comments
    ↓
Team Communication
    ↓
Notifications
    ↓
Real-Time Updates
```

Through this project, practical experience is gained in Django development, database management, authentication, CRUD operations, frontend development, project architecture, and real-time communication.

---

## Internship Information

**Program:** Artificial Intelligence Tasks & Instructions  
**Organization:** CodeAlpha  
**Task:** Task 3 – Project Management Tool  
**Project:** ProjectFlow  
**Type:** Full-Stack Web Application  
**Backend:** Django  
**Frontend:** HTML, CSS, JavaScript  
**Database:** SQLite  
**Language:** Python  
**Real-Time:** Django Channels + WebSockets

---

## Author

**Mohan Khadka**

Project developed as part of the **CodeAlpha Internship Program**.

---

## Project Status

**Status:** Completed / Under Development

The project can be further enhanced with advanced collaboration, notification, analytics, API, and deployment features.

---

## License

This project is developed for educational and internship purposes.


