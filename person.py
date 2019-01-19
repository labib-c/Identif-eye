import requests

subscription_key = "39f85cf12c644292a3dcd910ee8e61ea"

def createPerson(person_group_id, name, user_data=None):
    """Create a new person in a specified person group. A newly created person
    have no registered face, you can call `person.add_face` to add faces to the
    person.
    Args:
        person_group_id: Specifying the person group containing the target
            person.
        name: Display name of the target person. The maximum length is 128.
        user_data: Optional parameter. User-specified data about the face list
            for any purpose. The maximum length is 1KB.
    Returns:
        A new `person_id` created.
    """
    url = 'https://canadacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/{}/persons'.format(person_group_id)

    headers = {'Ocp-Apim-Subscription-Key': subscription_key }

    json = {
        'name': name,
        'userData': user_data,
    }

    return requests.post(url, json=json, headers=headers)