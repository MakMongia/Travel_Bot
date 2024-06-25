import unittest
from chatbot import get_weather

class WeatherAPITestCase(unittest.TestCase):

    def test_get_weather_valid_city(self):
        # Test the get_weather function with a valid city name
        city = "London"
        weather_data = get_weather(city)
        self.assertIsNotNone(weather_data)
        self.assertIn("temperature", weather_data)
        self.assertIn("description", weather_data)
        self.assertIn("city", weather_data)
        self.assertEqual(weather_data["city"], city)

    def test_get_weather_invalid_city(self):
        # Test the get_weather function with an invalid city name
        city = "InvalidCityName"
        weather_data = get_weather(city)
        self.assertIsNone(weather_data)

if __name__ == '__main__':
    unittest.main()
