from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze=request.args.get("textToAnalyze")
    emotions=emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is {emotions}.\
     The dominant emotion is <b>{emotions['dominant_emotion']}</b>." 

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
