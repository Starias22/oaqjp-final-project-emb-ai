import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test  case for joy dominance
        dominant_emotion_1=emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(dominant_emotion_1,"joy")

        # Test  case for anger dominance
        dominant_emotion_2=emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(dominant_emotion_2,"anger")

        # Test  case for disgust dominance
        dominant_emotion_3=emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(dominant_emotion_3,"disgust")

        # Test  case for sadness dominance
        dominant_emotion_4=emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(dominant_emotion_4,"sadness")

        # Test  case for fear dominance
        dominant_emotion_5=emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(dominant_emotion_5,"fear")
        
if __name__=="__main__":
    unittest.main()

