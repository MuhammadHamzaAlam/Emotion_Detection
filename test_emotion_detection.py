from EmotionDetection.emotion_detection import emotion_detector
import unittest

class Test_Emotion_Detector(unittest.TestCase):
    def tester(self):
         result_1 = emotion_detector("I am glad this happened")
         self.assertEqual(result_1["Dominant"] , "joy")

         result_2 = emotion_detector("I am really mad about this")
         self.assertEqual(result_1["Dominant"] , "anger")         

         result_3 = emotion_detector("I feel disgusted just hearing about this")
         self.assertEqual(result_1["Dominant"] , "disgust")        

         result_4 = emotion_detector("I am so sad about this")
         self.assertEqual(result_1["Dominant"] , "sadness")   

         result_5 = emotion_detector("I I am really afraid that this will happen")
         self.assertEqual(result_1["Dominant"] , "fear")  

unittest.main() 
