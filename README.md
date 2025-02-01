# Multilingual FAQ System

A Django-based FAQ system with automatic translation support and caching.

## Features

- Multilingual FAQ management (English, Hindi, Bengali)
- Automatic translation using Google Translate
- Redis caching for improved performance
- RESTful API with language support
- Admin interface with WYSIWYG editor
- Docker support for easy deployment

## Installation

1. Clone the repository:
```bash
git clone https://Nitish-Biswas/FAQ_project.git
cd FAQ_project
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Start Redis server:
```bash
# Ubuntu/Debian
sudo service redis-server start

# macOS
brew services start redis
```

8. Run development server:
```bash
python manage.py runserver
```

## API Usage

### List FAQs
```bash
# Get FAQs in English
GET /api/faqs/

# Get FAQs in Hindi
GET /api/faqs/?lang=hi

# Get FAQs in Bengali
GET /api/faqs/?lang=bn
```

### Create FAQ
```bash
POST /api/faqs/
Content-Type: application/json

{
    "question": "What is this service?",
    "answer": "This is a multilingual FAQ system."
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Commit Message Guidelines

We follow conventional commits:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Adding or modifying tests
- `chore:` Maintenance tasks

## Development

### Running Tests
```bash
pytest
```

