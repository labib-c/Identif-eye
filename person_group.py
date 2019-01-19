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

	# print(get("group1").content)

	# new_person = person.createPerson("group1", "Martin")
	
	# person_id = new_person.json().get('personId')

	image = 'https://goo.gl/zFdk6i' #Saksham
	image2 = "https://goo.gl/j4sUip" #Labib
	image3 = "https://goo.gl/M65gQU" #Labib2
	image4 = "https://goo.gl/JxWSAK" #Martin


	# person.addFace(image4, 'group1', person_id)

	# person_2 = person.getPerson("group1", person_id).json()

	# print("debug: ", person_id)



	Ids = [ face.detect_face(image4).json()[0]['faceId'] ]
	print(Ids, "\n")

	# print(train("group1"))
	# print(trainingStatus("group1"))
	candidates = face.identify_face(Ids, "group1").json()[0].get('candidates')

	print(candidates, "\n")

	for p in candidates:
			# print(p.get('personId'))
			print(person.getPerson("group1", p.get('personId')).json())


if __name__ == '__main__':
	main()