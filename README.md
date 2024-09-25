# Nutrition and Workout Tracker

This Python project tracks your exercises and logs them into a Google Sheets document using the Nutritionix API to calculate exercise metrics and Sheety API to store the data.

## Features

- Automatically tracks exercises based on your input.
- Uses the Nutritionix API to estimate exercise duration and calories burned.
- Logs exercise details like date, time, exercise name, duration, and calories burned into a Google Sheet using Sheety API.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Requests Library](https://pypi.org/project/requests/)

## APIs Used

1. **Nutritionix API**: To estimate exercise duration, calories, and other details.
2. **Sheety API**: To log workouts into a Google Sheets document.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ahmed00faraz/nutrition-workout-tracker.git
   cd nutrition-workout-tracker
   ```

2. **Install required dependencies:**

   Make sure to install the `requests` library if you haven't already:

   ```bash
   pip install requests
   ```

3. **Create accounts and get API keys:**

   - **Nutritionix API**: Create an account and get your `NUTRITION_APP_ID` and `NUTRITION_API_KEY` from the [Nutritionix Developer Portal](https://developer.nutritionix.com/).
   - **Sheety API**: Create a Google Sheets document and use the [Sheety API](https://sheety.co/) to convert it into an API endpoint.

4. **Set environment variables:**

   Create environment variables for your API credentials. You can do this in your terminal, `.bash_profile`, or directly in your code (for simplicity).

   ```bash
   export USERNAME="your_sheety_username"
   export PASSWORD="your_sheety_password"
   export NUTRITION_APP_ID="your_nutritionix_app_id"
   export NUTRITION_API_KEY="your_nutritionix_api_key"
   ```

   Replace the above placeholders with your actual credentials.

## Usage

1. **Run the script:**

   ```bash
   python workout_tracker.py
   ```

2. **Input your exercises:**

   The script will prompt you to enter the exercises you performed. You can type something like:

   ```
   Tell me which exercises you did: Ran for 30 minutes and lifted weights for 20 minutes
   ```

3. **Logging the workout:**

   - The script will call the Nutritionix API to analyze your exercises and get details like calories burned and exercise duration.
   - It will then log the results into a Google Sheet via the Sheety API.

## Example Output

Example logged data in your Google Sheet:

| Date       | Time     | Exercise       | Duration (min) | Calories |
|------------|----------|----------------|----------------|----------|
| 22/09/2024 | 15:30:45 | Running         | 30             | 300      |
| 22/09/2024 | 15:30:45 | Weightlifting   | 20             | 150      |

## Contributing

Feel free to open issues or submit pull requests if you want to enhance the functionality or add new features.
