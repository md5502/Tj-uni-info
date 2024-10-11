# University Information System

This project is a Django-based university information system that handles event management, professor and staff profiles, and registration for events. The project aims to provide easy access to event details, professor information, and other university-related content.

## Project Structure

Here is an overview of the key components:

```
config/               # Django settings and configuration
events/               # Event management application
home/                 # Main landing page app
professor_staff/      # Professor and staff profiles app
static/               # Static files (CSS, JS, Images)
templates/            # HTML templates for the project
media/                # Uploaded media (profile pictures, event images)
manage.py             # Django management command utility
requirements.txt      # Python dependencies
.env                  # Environment variables (not committed to version control)
.env-sample           # Sample .env file to demonstrate required environment variables
```

### Features

- **Event Management**: Create, edit, and register for events. Each event has a title, description, location, and schedule date.
- **Professor and Staff Profiles**: Profiles with detailed information such as work experience and academic background.
- **Registration Forms**: Event registration forms with custom validations.
- **Admin Panel**: Manage events, professors, and staff through Django's admin interface.
- **Farsi Localization**: Supports Farsi with RTL layout for users.

## Installation

1. **Clone the repository**:
   ```bash
   git clone http://github.com/md5502/Tj-uni-info.git
   cd Tj-uni-info
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   - Copy `.env-sample` to `.env`:
     ```bash
     cp .env-sample .env
     ```

   - Open `.env` and configure the necessary values:
     ```bash
     SECRET_KEY=your_secret_key
     DEBUG=True
     ```

   **Note**: The `.env-sample` file is provided to demonstrate what environment variables are required. You should not commit the `.env` file to version control as it contains sensitive information such as the `SECRET_KEY`.

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for accessing the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the app**:
   - Open [http://localhost:8000](http://localhost:8000) in your browser.
   - Admin panel is available at [http://localhost:8000/admin](http://localhost:8000/admin).

## .env and .env-sample

- **.env**: This file stores environment variables such as the Django settings module, secret keys, and any other sensitive configuration. This file is ignored by Git to keep sensitive information private. You need to create your own `.env` file by copying the provided `.env-sample`.

- **.env-sample**: This is a sample file that lists all the required environment variables but without actual values. Use it as a reference to create your own `.env` file. Never commit your actual `.env` file to version control to avoid exposing sensitive data.

Example content of `.env-sample`:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
```

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature/bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes.
4. Ensure all tests pass.
5. Submit a pull request.

### Setting Up a Development Environment

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure the project passes linting and tests:
   ```bash
   ruff check .
   python manage.py test
   ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, feel free to contact me at [m.baniasadi.d@gmail.com](mailto:m.baniasadi.d@gmail.com).