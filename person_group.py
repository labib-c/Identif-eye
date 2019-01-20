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

def delete(person_group_id):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}'.format(person_group_id)

	return requests.delete(url, headers=headers)


def train(person_group_id):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}/train'.format(person_group_id)
	return requests.post(url, headers=headers)

def trainingStatus(person_group_id):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}/training'.format(person_group_id)
	return requests.get(url, headers=headers)

def test_person(image, threshold, group_name='group1'):
	Ids = [face.detect_face(image).json()[0]['faceId']]

	candidates = face.identify_face(Ids, group_name).json()[0].get('candidates')

	for p in candidates:
		print(person.getPerson(group_name, p.get('personId')).json())

	return face.detect_wanted(candidates, threshold)

def main():
	
	# print(create("group1"))
<<<<<<< HEAD

	print(get("group1").content)

	# new_person = person.createPerson("group1", "Martin")
	
=======
	#
	# print(get("group1").content)
	#
	# new_person = person.createPerson("group1", "Labib")
	# new_person2 = person.createPerson('group1', 'Saksham')
>>>>>>> 1e5b4c78cb4667066ddf080f3f897201f204e089
	# person_id = new_person.json().get('personId')
	# person_id2 = new_person2.json().get('personId')

	# '''for testing links:	'''
	# image = 'https://goo.gl/zFdk6i' #Saksham
	# image2 = "https://goo.gl/j4sUip" #Labib
	# image3 = "https://goo.gl/M65gQU" #Labib2
	# image4 = "https://goo.gl/JxWSAK" #Martin
	# image5 = 'https://bit.ly/2sCacna' #Saksham

<<<<<<< HEAD
	# person.addFace(image4, 'group1', person_id)

	# person_2 = person.getPerson("group1", person_id).json()

	# print("debug: ", person_id)


=======

	# person.addFace(image, 'group1', person_id2)
	# person.addFace(image2, 'group1', person_id)
	# person.addFace(image3, 'group1', person_id)
>>>>>>> 1e5b4c78cb4667066ddf080f3f897201f204e089

	# Ids = [ face.detect_face(image5).json()[0]['faceId'] ]
	# print(Ids, "\n")
	#
	# print(train("group1"))
	# print(trainingStatus("group1"))
	# candidates = face.identify_face(Ids, "group1").json()[0].get('candidates')
	#
	# print(candidates, "\n")
	#
	# for p in candidates:
	# 	print(person.getPerson("group1", p.get('personId')).json())
	#
	# print('\n')
	# print(face.detect_wanted(candidates, 0.4))

	goodguy_path = 'https://bit.ly/2sCacna'
	print(test_person(goodguy_path, 0.4))


if __name__ == '__main__':
	main()