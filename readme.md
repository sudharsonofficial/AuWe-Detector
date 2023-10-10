# AuWeDetector - Automatic Weather Detection

**AuWeDetector** is a Django-based web application that automatically detects and alerts users about weather conditions in specific locations. It allows users to add cities and set temperature thresholds, and the application will send email alerts when the weather conditions fall outside the specified range.

## Features

- User-friendly web interface.
- Add multiple cities and set temperature alerts.
- Real-time weather data retrieval.
- Email notifications for temperature alerts.
- Flexible configuration through a simple Django app.

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/yourusername/AuWeDetector.git
   ```

2. Create a virtual environment (recommended) and activate it:

   ```
   python3 -m venv auwedetector-venv
   source auwedetector-venv/bin/activate
   ```

3. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Configure the application by setting up your email and API keys in `AuWeDetector/agents/config.py`.

5. Run database migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Visit the homepage at `http://localhost:8000`.
2. Click on "Add City" to specify a location and temperature thresholds.
3. The application will periodically check the weather conditions for added cities and send email alerts if needed.

## Contributing

We welcome contributions from the community! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Commit your changes with clear and concise messages.
5. Push your changes to your fork.
6. Create a pull request to merge your changes into the main repository.


## Contact

For questions, suggestions, or feedback, please contact us at [your.email@example.com](mailto:your.email@example.com).

---

Thank you for choosing **AuWeDetector**! We hope you find this application helpful for staying informed about weather conditions in your desired locations. Enjoy using it!
