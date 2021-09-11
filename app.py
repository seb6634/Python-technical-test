
import emoji 

from util.api import retrieve_json_data, APIRequestError, get_emoji_name, UnknownOSError

try:
    json_content = retrieve_json_data()

except APIRequestError as e:
    print(e)

else:
    user_name = json_content['username']
    user_mail = json_content['email']
    user_agent = json_content['user_agent']

    try :
        emoji_name = get_emoji_name(user_agent)

    except UnknownOSError:
        emoji_name = None

    if emoji_name is not None:
        emoji_value = emoji.emojize(emoji_name)
        print(f"L'adresse email de l'utilisateur {user_name} est {user_mail}. Il utilise le système d'exploitation {emoji_value}.") 

    else:
        print(f"L'adresse email de l'utilisateur {user_name} est {user_mail}.") 






