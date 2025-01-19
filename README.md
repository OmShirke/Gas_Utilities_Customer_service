# Gas Utility Service

This is a web application built using Django, designed for managing and tracking customer service requests in a gas utility company. The platform allows users to submit requests, track their status, and get responses from customer service representatives.


## Setup Instructions

### Prerequisites:
- Python 3.8 or higher
- Django 5.1.5
- PostgreSQL (or your preferred database)

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/OmShirke/Gas_Utilities_Customer_service
   ```
2. Navigate to the project directory:
   ```bash
   cd yourproject
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the database:
   - Create a `.env` file with your environment variables:
     ```plaintext
     DATABASE_URL=your_database_url
     ```
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Admin Access:
- Create a superuser to access the admin panel:
  ```bash
  python manage.py createsuperuser
  ```
- You can now access the admin panel at `http://127.0.0.1:8000/admin/`.

- **Submit a Service Request**:
  - Go to the "Submit Request" page and fill in your details (name, email, request type, and description).
  - After submission, you can track the status of your request.

- **Track a Service Request**:
  - Go to the "Track Request" page, where you can view the status of your submitted requests.
  - Only logged-in users can see their requests.

- **Admin View**:
  - Admins can log in to the admin panel and view all requests submitted by users.
  - Admins can respond to requests by updating the status and adding responses.
