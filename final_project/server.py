from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze:
        result = emotion_detector('happy')

        return f"""
        For the given statement, the system response is 
        'anger': {result.get('anger')}, 
        'disgust': {result.get('disgust')}, 
        'fear': {result.get('fear')}, 
        'joy': {result.get('joy')} and 
        'sadness': {result.get('sadness')}. 
        The dominant emotion is {result.get('dominant_emotion')}. 
        """
    
    return render_template('index.html')
    

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
