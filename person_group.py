import requests, person, face


subscription_key = "39f85cf12c644292a3dcd910ee8e61ea"
headers = {'Ocp-Apim-Subscription-Key': subscription_key }

def create(person_group_id, name=None, user_data=None):
	name = name or person_group_id
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}'.format(person_group_id)

	json = {
		'name': name,
		'userData': user_data,
	}

	return requests.put(url, json=json, headers=headers)

def get(person_group_id):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}'.format(person_group_id)

	return requests.get(url, headers=headers)

def train(person_group_id):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}/train'.format(person_group_id)
	return requests.post(url, headers=headers)

def trainingStatus(person_group_id):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}/training'.format(person_group_id)
	return requests.get(url, headers=headers)

def main():
	
	# print(create("group1"))

	print(get("group1").content)

	new_person = person.createPerson("group1", "saksham")
	
	person_id = new_person.json().get('personId')

	image = 'https://goo.gl/zFdk6i'

	person.addFace(image, 'group1', person_id)

	person_2 = person.getPerson("group1", person_id).json()

	# print("debug: ", person_2)

	print(face.detect_face(image))

if __name__ == '__main__':
	main()