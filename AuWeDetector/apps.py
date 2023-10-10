import json
import threading
from django.apps import AppConfig
from AuWeDetector.agent import weather

class AuwedetectorConfig(AppConfig):
    """
    Configuration class for the AuWeDetector app.

    Attributes:
        default_auto_field (str): The default auto field for database models.
        name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AuWeDetector'

    def ready(self) -> None:
        """
        Method called when the application is ready.

        This method is automatically executed when the Django application is fully loaded.
        It initializes the data.json file and starts a separate thread to run the weather data agent.

        Returns:
            None
        """
        # Initialize the data.json file with an empty JSON object
        with open("data.json", "w") as f:
            json.dump({}, f, indent=4)

        # Start a separate thread to run the weather data agent
        threading.Thread(target=weather.run).start()
