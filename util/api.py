import requests

_URL = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"


def retrieve_json_data(url=_URL):
    try:
        response = requests.get(url)

    except Exception as e:
        raise APIRequestError() from e

    if response.status_code != 200:
        raise APIRequestError('Erreur lors de l\'appel à l\'API, code de retour : {0}'.format(response.status_code))

    return response.json()


class APIRequestError(Exception):
    pass


def get_emoji_name(user_agent):
    user_agent_upper = user_agent.upper()
    os_list = {
        'LINUX': ':penguin:',
        'MACINTOSH': ':red_apple:',
        'WINDOWS': ':window:',
        'COMPATIBLE': ':robot:',
        }
    for os_name, emoji_name in os_list.items():
        if user_agent_upper.find((os_name), 0, 30) >= 0:
            return emoji_name
    
    # OS not found in user-agent
    raise UnknownOSError('OS inconnu dans le user-agent retourné par l\'API : {0}'.format(user_agent))


class UnknownOSError(Exception):
    pass
