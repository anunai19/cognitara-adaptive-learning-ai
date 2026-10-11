
import unittest
from pathlib import Path
import sys

sys.path.insert(
    0, str(Path(__file__).resolve().parent.parent / "ai")
)

from recommend import recommend_intervention


class TestRecommendations(unittest.TestCase):

    def test_low_score(self):
        result = recommend_intervention(20)
        self.assertIn("visual explanation", result)

    def test_medium_score(self):
        result = recommend_intervention(50)
        self.assertIn("step-by-step", result)

    def test_high_score(self):
        result = recommend_intervention(80)
        self.assertIn("advanced", result)


if __name__ == "__main__":
    unittest.main()
  
