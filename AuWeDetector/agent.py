from uagents import Agent, Context
import json

from AuWeDetector.agents.config import EMAIL, PASSWORD, INTERVAL
from AuWeDetector.agents.utils import fetch_temperature
from AuWeDetector.agents.mail import Mail

# Create a weather agent instance
weather = Agent(name="weather", seed="weather seed")

# Create a Mail instance for sending emails
mail = Mail(EMAIL, PASSWORD)


@weather.on_event("start")
async def start(ctx: Context) -> None:
    """
    Event handler called when the Weather Agent starts.

    Args:
        ctx (Context): The agent context.

    Returns:
        None
    """
    print("Weather Agent Started")


@weather.on_interval(period=INTERVAL)
async def data_cleaner_and_sender(ctx: Context) -> None:
    """
    Event handler for data cleaning and email sending at regular intervals.

    Args:
        ctx (Context): The agent context.

    Returns:
        None
    """

    # Read data from the data.json file
    with open('data.json', 'r') as openfile:
        data = json.load(openfile)

    if not data:
        return

    email = data["email"]

    for location in data["location"]:
        min_alert = max_alert = False

        temp = fetch_temperature(city=location["name"])

        assert temp, "Cannot find temperature"

        if temp < location["min-temp"]: # When the Temperature is less than minimum Temperature
            res = f"""The Temperature in {location["name"]} ventured below the minimum temperature 🥶.
            Current Temperature: {temp}°C
            Expected Temperature range: {location["min-temp"]}°C - {location["max-temp"]}°C
            """
            min_alert = True
        elif temp > location["max-temp"]: # When the Temperature is more than maximum Temperature
            res = f"""The Temperature in {location["name"]} is scorching beyond the maximum temperature ☀.
            Current Temperature: {temp}°C
            Expected Temperature range: {location["min-temp"]}°C - {location["max-temp"]}°C
            """
            max_alert = True
        else: # When the Temperature is in the specified range
            res = f"Everything looks good!"

        weather._logger.info(res)

        if max_alert or min_alert:
            mail.send(email, res)

            weather._logger.info("Email Sent Successfully")
