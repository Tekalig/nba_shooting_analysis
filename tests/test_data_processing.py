import unittest
import pandas as pd
from src.data_processing import preprocess_data

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        """Set up a sample dataframe for testing."""
        self.sample_data = pd.DataFrame({
            'X': [1, 2, 3],
            'Y': [4, 5, 6],
            'SCORE': ['MADE', 'MISSED', 'MADE']
        })

    def test_preprocess_data(self):
        """Test if preprocessing adds the correct columns."""
        processed_data = preprocess_data(self.sample_data)
        self.assertIn('SHOT_ATTEMPTED', processed_data.columns)
        self.assertIn('SHOT_MADE', processed_data.columns)
        self.assertIn('DISTANCE', processed_data.columns)

        # Check SHOT_ATTEMPTED column
        self.assertTrue((processed_data['SHOT_ATTEMPTED'] == 1).all())

        # Check SHOT_MADE column
        self.assertListEqual(processed_data['SHOT_MADE'].tolist(), [1, 0, 1])

        # Check DISTANCE calculation
        expected_distances = [4.1231, 5.3852, 6.7082]  # Approximate values
        self.assertTrue(
            all(abs(a - b) < 0.0001 for a, b in zip(processed_data['DISTANCE'], expected_distances))
        )

if __name__ == "__main__":
    unittest.main()