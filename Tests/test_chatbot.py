import unittest
import json
from chatbot import app

class ChatbotTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        # Test the root endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the TravelBot API", response.data)

    def test_chat_with_weather_intent(self):
        # Test the /chat endpoint with a weather-related query
        response = self.app.post('/chat', json={"message": "What's the weather in London?"})
        data = json.loads(response.data)
        self.assertIn("response", data)
        self.assertTrue(data["response"])  # Check if response is not empty
        self.assertIn("The weather in", data["response"])  # Check if response contains weather information

    def test_chat_with_invalid_city_weather_intent(self):
        # Test the /chat endpoint with an invalid city name
        response = self.app.post('/chat', json={"message": "What's the weather in InvalidCityName?"})
        data = json.loads(response.data)
        self.assertIn("response", data)
        self.assertEqual(data["response"], "Sorry, I couldn't retrieve the weather information. Please try again.")

    def test_chat_without_weather_intent(self):
        # Test the /chat endpoint with a non-weather-related query
        response = self.app.post('/chat', json={"message": "Tell me a joke"})
        data = json.loads(response.data)
        self.assertIn("response", data)
        self.assertTrue(data["response"])  # Check if response is not empty

if __name__ == '__main__':
    unittest.main()
