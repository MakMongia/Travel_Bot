
## Requirements
- Python 3.x
- Flask
- ChatterBot
- Requests
- PyYAML
- Unittest

## Installation Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/MakMongia/Travel_Bot
    cd TravelBot
    ```

2. **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Run the Flask app**:
    ```bash
    python app.py
    ```
    The server usually starts on `http://127.0.0.1:5000/`.

2. **Interact with the chatbot**:
    - Use a tool like Postman to send POST requests to the `/chat` endpoint.
    - Example request:
        ```json
        {
          "message": "How's the weather in London?"
        }
        ```

## Testing
1. **Run the unit tests**:
    ```bash
    python -m unittest discover -s tests
    ```

## Theoretical and Operational Information
### Starting a chatbot
ChatterBot was introduced by chatbot. It is trained with NLU data and information defined in YAML files in the `data` folder.

### Weather Call
The `get_weather` function interfaces with the OpenWeatherMap API to retrieve a 5-day weather forecast. This API processes the response and sorts the weather information.

### Flask integration
Flask is used to create an API endpoint for interaction with a chatbot. The `/chat` endpoint handles user input, determines whether the input requests weather information, and responds accordingly.

### Training Information
YAML files (`nlu.yml` and `stories.yml`) are used to structure training data for shapes and stories, allowing for easy and customizable updates.

### Error handling
Advanced error handling has been implemented to ensure that the chatbot handles incorrect information and API failures gracefully.

### Examine
Unit tests are written to verify the chatbot’s functionality and the reproducible weather. These tests included situations including valid and illegal city names, weather-related questions, and non-weather-related questions.

## Reflections and lessons learned
- **Challenges**: Integrating API calls and chatbot generic responses.
- **Lesson Learned**: Test-driven improvement programs help identify and fix problems early and makes it easier for future enhancement of the project and development.

## Author
Developed by [Mayank Mongia]

## Contact
For any questions or suggestions, please contact [102905592@student.swin.edu.au].
