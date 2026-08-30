
"""Emotion detection module."""

import json

import requests


def emotion_detector(text_to_analyze):
    """Analyze the emotions in the given text."""

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    header = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    my_obj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        json=my_obj,
        headers=header,
        timeout=30
    )

    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "Emotions": emotions,
            "Dominant": dominant_emotion
        }

    emotions = None
    dominant_emotion = None

    return {
        "Emotions": emotions,
        "Dominant": dominant_emotion
    }

