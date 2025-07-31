import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)

    response_text = response.text
    response_json = response.json()

    emotion_predictons = response_json.get('emotionPredictions', [])
    emotions, *rest = emotion_predictons

    if emotion_predictons and emotions:
        emotions_scores = emotions.get('emotion')
        dominant_emotion = max(emotions_scores, key=emotions_scores.get)
        dominant_emotion_score = emotions_scores.get(dominant_emotion)



    return emotions_scores, { 'message': f'Dominant emotion is {dominant_emotion} with score of {dominant_emotion_score}'}
