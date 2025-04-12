# Oxford Consultants Website

Repository for Oxford Consultants website: [oxfordconsultantsgh.com](https://oxfordconsultantsgh.com)

## Overview

This is a Django-based static website hosted on GitHub Pages. The site uses a SQLite database for development and content management, while the static files are generated using Django Distill and published to the `/docs` directory for GitHub Pages hosting.

## Requirements

- Python 3.8+
- Git
- Pipenv (for dependency management)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/oxfordconsultantsgh.git
cd oxfordconsultantsgh
```

### 2. Set Up Virtual Environment

This project uses Pipenv to manage dependencies. To set up your environment:

```bash
# Install Pipenv if you don't have it
pip install pipenv

# Create virtual environment and install dependencies
pipenv install

# Activate the virtual environment
pipenv shell
```

### 3. Database Setup

The site uses SQLite for the database. Initialize it with:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Follow the prompts to create an admin user that you can use to access the Django admin interface.

## Development

### Running the Development Server

```bash
python manage.py runserver
```

Access the site at http://127.0.0.1:8000/ and the admin interface at http://127.0.0.1:8000/admin/

### Making Changes

1. Edit your Django templates, views, and models as needed
2. Update content through the Django admin interface
3. Test your changes in the development environment

## Deployment

The site is deployed on GitHub Pages from the `/docs` directory. To update the deployment:

### 1. Generate Static Files

```bash
# Collect static files from all apps into the static directory
python manage.py collectstatic

# Generate static site with Django Distill
python manage.py distill-local docs --force
```

These commands will:
- Collect all static files into the static directory
- Create static HTML files for all site pages
- Copy CSS, JavaScript, and media files to the `/docs` directory
- Generate the necessary files for GitHub Pages

### 2. Preserving CNAME for GitHub Pages

To maintain your custom domain configuration, use the `post_distill.sh` script:

```bash
# Make the script executable (first time only)
chmod +x post_distill.sh

# Run the script
./post_distill.sh
```

This script automatically:
- Runs the distill command with collectstatic
- Creates/preserves the CNAME file with your domain

Remember to commit the updated CNAME file along with other changes.

### 3. Commit and Push Changes

```bash
git add .
git commit -m "Update static site content"
git push origin main
```

### 4. GitHub Pages Deployment

The site will automatically be deployed from the `/docs` directory in the main branch. No additional build steps are required on GitHub.

## Common Django Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Generate static files with verbose output to see all URLs being processed
python manage.py distill-local docs --force -v 3

# Generate static files with parallel rendering (faster for large sites)
python manage.py distill-local docs --force --parallel-render 4

# Generate static files with automatic collectstatic
python manage.py distill-local docs --force --collectstatic
```

## File Structure

```
oxfordconsultantsgh/
├── docs/                 # Generated static site (for GitHub Pages)
├── frontend/             # Frontend assets and templates
├── oxfordconsultants/    # Django project settings
├── .gitignore            # Git ignore file
├── .python-version       # Python version specification
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
├── Pipfile               # Pipenv dependencies
└── Pipfile.lock          # Locked dependencies
```

## Troubleshooting

### Static Files Not Updating
If changes to static files aren't reflected after running the distill command:
1. Clear your browser cache
2. Ensure you're using the `--force` flag with distill
3. Check that all static files are properly collected

### Database Changes
Remember that this is a static site - database changes need to be made in development and then the static site must be regenerated and redeployed.