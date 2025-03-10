# Django LeetCode Clone

A web application that replicates core functionality of LeetCode, built with Django. This platform allows users to browse, solve, and track progress on coding problems across various categories.

## Features

- **Problem Library**: Browse all problems with filtering by category, difficulty, and search
- **User Authentication**: Track your solved problems and progress
- **Study Plans**: Follow structured learning paths
- **Company-specific Problems**: View problems by company for interview preparation
- **Problem Detail View**: View problem description, examples, and submit solutions
- **User Progress Tracking**: Track completion status across problems

## Installation

### Prerequisites
- Python 3.11+
- Django 5.1.6+

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/leetcode_clone.git
cd leetcode_clone
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Populate the database with sample data:
```bash
python manage.py populate_data
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application at http://127.0.0.1:8000/

## Project Structure

```
leetcode_clone/
├── leetcode_clone/      # Project settings
├── problems/            # Main app directory
│   ├── management/      # Custom management commands
│   ├── migrations/      # Database migrations
│   ├── templates/       # HTML templates
│   ├── templatetags/    # Custom template tags
│   ├── admin.py         # Admin interface
│   ├── apps.py          # App configuration
│   ├── models.py        # Database models
│   ├── tests.py         # Test cases
│   ├── urls.py          # URL routing
│   └── views.py         # Views and controllers
├── db.sqlite3           # SQLite database
├── manage.py            # Django command-line utility
└── requirements.txt     # Project dependencies
```

## Models

- **Problem**: Core problem details, including title, description, examples
- **Category**: Problem categories (Array, String, Hash Table, etc.)
- **Difficulty**: Problem difficulty levels (Easy, Medium, Hard)
- **UserProblem**: Tracks user progress on specific problems
- **Company**: Companies that frequently ask certain problems
- **StudyPlan**: Curated problem sets for structured learning
- **UserStudyPlan**: Tracks user progress on study plans

## Development

### Adding New Problems

1. Use the Django Admin interface at http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Navigate to Problems > Add
4. Fill in the required fields and save

### Creating Custom Management Commands

You can add more commands like `populate_data` in the `problems/management/commands/` directory.

## Technologies Used

- **Django**: Web framework
- **SQLite**: Database
- **Tailwind CSS**: UI styling
- **Font Awesome**: Icons

## License

[MIT License](LICENSE)