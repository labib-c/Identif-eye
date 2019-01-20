import requests

subscription_key = "39f85cf12c644292a3dcd910ee8e61ea"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

def detect_face(image):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/detect'

	headers['Content-Type'] = 'application/json'
	json = {'url': image}

	params = {
		'returnFaceId': True,
		'returnFaceLandmarks': False,
		'returnFaceAttributes': 'emotion',
	}

	return requests.post(url, headers=headers, params=params, json=json, data=None)


def identify_face(face_ids, person_group_id=None, max_candidates=50, threshold=None):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/identify'
	json = {
		'personGroupId': person_group_id,
		'largePersonGroupId': None,
		'faceIds': face_ids,
		'maxNumOfCandidatesReturned': max_candidates,
		'confidenceThreshold': threshold,
	}

	return requests.post(url, headers=headers, json=json)


def detect_wanted(json_dict_list, threshold):
	# return criminal/not (True/False), confidence, and personId
	if len(json_dict_list) == 0:
		return False, None, None

	for item in json_dict_list:
		if 'candidates' in item:
			if item['candidates']['confidence'] >= threshold:
				return True, item['candidates']['confidence'], item['candidates']['personId']
		else:
			if item['confidence'] >= threshold:
				return True, item['confidence'], item['personId']


	return False, None, None