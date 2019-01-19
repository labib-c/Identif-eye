import requests

def detect_face(image, local=False):
    url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/detect'
    headers = None
    data = None
    json = None
    if not local:
        headers = {'Content-Type': 'application/json'}
        json = {'url': image}
    else:
        headers = {'Content-Type': 'application/octet-stream'}
        data = open(image, 'rb').read()

    params = {
        'returnFaceId': True,
        'returnFaceLandmarks': False,
        'returnFaceAttributes': 'emotion',
    }

    return requests.post(url, headers=headers, params=params, json=json, data=data)


def identify_face(face_ids, person_group_id=None, max_candidates=50, threshold=None):
    url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/identify'
    json = {
        'personGroupId': person_group_id,
        'largePersonGroupId': None,
        'faceIds': face_ids,
        'maxNumOfCandidatesReturned': max_candidates,
        'confidenceThreshold': threshold,
    }

    return requests.post(url, json=json)
