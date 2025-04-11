# University Information System

This project is a Django-based university information system that handles event management, professor and staff profiles, and registration for events. The project aims to provide easy access to event details, professor information, and other university-related content.

## Project Structure

Here is an overview of the key components:

```
config/               # Django settings and configuration
events/               # Event management, event registration, and related services
professor_staff/      # Professor and staff profiles, work experiences, and related services
association/          # Student associations, including profiles and logos
shahid/               # Martyr (Shohada) profiles with related details
frontend/             # Frontend templates and static files
home/                 # Home page and main navigation
static/               # Static files (CSS, images, JavaScript)
templates/            # Base and shared HTML templates
media/                # Media files (profiles, event images, logos)

```

### Detailed Explanation:

- **config/**: Contains the settings, including `base.py`, `development.py`, and `production.py`, as well as URL and WSGI configurations.
  
- **events/**: Manages event creation, registration, and listing. It includes the necessary templates, models, and views for handling events. The `populate_date` management command is available to pre-fill dates.
  
- **professor_staff/**: Handles professor and staff profiles, including their educational background, work experience, and teaching courses. Templates are available for viewing detailed and list views of professors and staff members.
  
- **association/**: Manages student associations, including their profile information, logos, and a list of available associations. Templates for viewing association details and listings are included.
  
- **shahid/**: Manages martyr (Shohada) profiles with information such as their life story, birth and martyrdom dates, and images. The QR code generation for each martyr is also handled here.
  
- **frontend/**: Contains the frontend HTML for the home page.
  
- **home/**: Manages the home page view and its template.
  
- **static/**: Contains static assets such as CSS, JavaScript, and images.
  
- **templates/**: Contains shared HTML templates, including the base layout (`base.html`) and email templates.
  
- **media/**: Stores uploaded media, such as profile images, association logos, event images, and martyr profiles.


### Features

- **Event Management**: Create, edit, and register for events. Each event has a title, description, location, and schedule date.
- **Professor and Staff Profiles**: Profiles with detailed information such as work experience and academic background.
- **Registration Forms**: Event registration forms with custom validations.
- **Student Associations**: Browse student associations with their respective logos and profile details.
- **Admin Panel**: Manage events, professors, and staff through Django's admin interface.
- **Martyr Profiles (Shohada)**: Access detailed martyr information with QR code support.
- **Farsi Localization**: Supports Farsi with RTL layout for users.

## Technologies

- **Django**: Backend framework.
- **SQLite**: Default database (can be switched to PostgreSQL for production).
- **Docker**: Optional containerization support via `Dockerfile` and `docker-compose.yml`.


## 🛠 Installation & Running the Project

1. **Clone the repository**:
   ```bash
   git clone http://github.com/md5502/Tj-uni-info.git
   cd Tj-uni-info
   ```

2. **Create and activate a virtual environment**:

   ### On Linux/macOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   ### On Windows (Command Prompt):
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

   ### On Windows (PowerShell):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:

   - Copy the sample environment file:
     ```bash
     cp .env-sample .env  # Use 'copy .env-sample .env' on Windows
     ```

   - Edit the `.env` file and add your configuration:

     ```env
     SECRET_KEY=your_secret_key
     DEBUG=True
     DJANGO_SETTINGS_MODULE=config.settings.development
     ```

     > ✅ **Important:** Make sure to add `DJANGO_SETTINGS_MODULE=config.settings.development` in your `.env` file. This ensures you don’t need to manually pass `--settings` when running management commands.

5. **Auto-load `.env` variables (recommended)**:

   This project uses [`python-dotenv`](https://pypi.org/project/python-dotenv/) or similar tools. Make sure your `manage.py` and `wsgi.py` contain this snippet at the top (already included in the repo):

   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

   This line loads all environment variables from `.env` automatically.

6. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**:
   Just use:
   ```bash
   python manage.py runserver
   ```

   No need to pass `--settings=...` anymore!

9. **Access the application**:
   - Frontend: [http://localhost:8000](http://localhost:8000)
   - Admin Panel: [http://localhost:8000/admin](http://localhost:8000/admin)


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

