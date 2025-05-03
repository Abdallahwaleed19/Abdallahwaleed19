# Library Management System

A modern web-based library management system built with Flask and SQLAlchemy.

## Features

- User Management (Admin, Librarian, Customer)
- Book Management
- Library Card System
- Borrowing and Returns
- Book Sales
- Multiple Library Branches
- Notifications System
- Profile Management
- Search Functionality

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd library-management-system
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-email-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

5. Initialize the database:
```bash
python init_db.py
```

## Running the Application

1. Start the Flask development server:
```bash
flask run
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Default Admin Account

After initializing the database, you can log in with these credentials:
- Email: admin@library.com
- Password: admin123

## Project Structure

```
library_management_system/
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── uploads/
├── templates/
│   ├── base.html
│   ├── index.html
│   └── ...
├── app.py
├── models.py
├── config.py
├── init_db.py
└── requirements.txt
```

## Testing

Run the tests using pytest:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. 