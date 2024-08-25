''' This is the servr file, the entry point of application.
It handle client requests for detecting emotion in texts
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app=Flask("Emotion Detector")
@app.route("/emotionDetector")
def detect_emotion():
    """ This is the core function of our web application.
     It allow clients to enter text and perform emotion detection task.
     """
    text_to_analyze=request.args.get("textToAnalyze")
    emotions=emotion_detector(text_to_analyze)
    dominant_emotion=emotions['dominant_emotion']
    if dominant_emotion is None:
        return "<b>Invalid text! Please try again!</b>"
    return f"For the given statement, the system response is {emotions}.\
    The dominant emotion is <b>{dominant_emotion}</b>."
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
