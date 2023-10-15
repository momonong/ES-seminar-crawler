# Seminar Notification Crawler

This project is designed to periodically check for session changes on the NCKU ES Seminar website. When a session change is detected, it automatically sends a notification to a specified LINE account.

## Set up

**Copy .env and fill in the appropriate values:**  
PREVIOUS_VALUE: The value of the session from the last check.  
LINE_NOTIFY_TOKEN: Your LINE Notify API token.

**Install the required Python packages:**  
poetry install

## Usage

**Run manually:**  
poetry run python main.py

**Schedule with cron for periodic execution:**  
Add the following line to your crontab to run the script every hour:  
*/20 * * * * cd </path/to/project_dir> && </path/to/poetry> run python </path/to/project_dir/main.py>

## Notes
**Ensure you have permission from the website to periodically scrape its content.**  
Avoid excessively frequent scraping to prevent unnecessary load on the server.
