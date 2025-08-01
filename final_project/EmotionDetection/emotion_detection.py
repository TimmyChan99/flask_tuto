import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)

    if response.status_code == 200:
        response_text = response.text
        response_json = response.json()

        emotion_predictions = response_json.get('emotionPredictions', [])
        emotions, *rest = emotion_predictions

        if emotion_predictions and emotions:
            emotions_scores = emotions.get('emotion')
            dominant_emotion = max(emotions_scores, key=emotions_scores.get)
            
            return { **emotions_scores, 'dominant_emotion': dominant_emotion }
    
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
