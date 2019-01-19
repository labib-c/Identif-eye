import requests
import person

subscription_key = "39f85cf12c644292a3dcd910ee8e61ea"

def createGroup(groupName):
	face_api_url = "https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/"+groupName

	

	params = {
		"name": groupName,
		"userData": "user-provided data attached to the person group."
	}

	response = requests.put(face_api_url, params=params, headers=headers)
	faces = response.json()
	print (faces)

def create(person_group_id, name=None, user_data=None):
	name = name or person_group_id
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}'.format(person_group_id)

	headers = {'Ocp-Apim-Subscription-Key': subscription_key }

	json = {
		'name': name,
		'userData': user_data,
	}

	return requests.put(url, json=json, headers=headers)

def get(person_group_id):
	url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}'.format(person_group_id)

	headers = {'Ocp-Apim-Subscription-Key': subscription_key }

	return requests.get(url, headers=headers)

def main():
	# print(create("group1"))
	print(get("group1").content)


if __name__ == '__main__':
	main()