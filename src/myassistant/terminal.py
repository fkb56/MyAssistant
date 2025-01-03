from pick import pick
from myassistant.supabase_client import Supabase
from myassistant.chatbot import main

supabase = Supabase().get_client()

supabase.auth.sign_in_with_password({"email": "fkcb@live.fr", "password": "azerty"})

user = supabase.auth.get_user().user

def get_model(provider):
    models = supabase.table('models').select("name").eq('provider', provider).execute()
    data = []
    for model in models.data:
        data.append(model['name'])
    return data

def get_api_key(provider):
    print(f"Veuillez entrer votre clé API {provider}")
    api_key = input(f"Entrez votre clé API {provider}: ")
    return api_key

title = 'Please choose your provider: '
options = ['OpenAi', 'Anthropic', 'HuggingFace', 'Ollama']
option, index = pick(options, title)

if option == 'OpenAi':
    print(f'Vous avez choisi {option}')
    if supabase.table('users').select("open_ai_api_key").eq('id', user.id).execute().data[0]['open_ai_api_key'] is None:
        supabase.table('users').update({'open_ai_api_key': get_api_key(option)}).eq('id', user.id).execute()
        pass
    if supabase.table('users').select("default_model_id").eq('id', user.id).execute().data[0]['default_model_id'] is None:
        title = 'Choisissez un modèle '
        model = get_model(option.lower())
        name, index = pick(model, title)
        default_model_id = supabase.table('models').select("id").eq('name', name).execute().data[0]['id']
        supabase.table('users').update({'default_model_id': default_model_id}).eq('id', user.id).execute()
    else:
        main()
# elif option == 'Anthropic':
#     print(f'Vous avez choisi {option}')
#     if supabase.table('users').select("open_ai_api_key").eq('id', user.id).execute().data[0]['open_ai_api_key'] is None:
#         supabase.table('users').update({'open_ai_api_key': get_api_key(option)}).eq('id', user.id).execute()
#         pass
#     if supabase.table('users').select("default_model_id").eq('id', user.id).execute().data[0]['default_model_id'] is None:
#         title = 'Choisissez un modèle '
#         model = get_model(option.lower())
#         name, index = pick(model, title)
#         default_model_id = supabase.table('models').select("id").eq('name', name).execute().data[0]['id']
#         supabase.table('users').update({'default_model_id': default_model_id}).eq('id', user.id).execute()
#     else:
#         main()
# elif option == 'HuggingFace':
#     print(f'Vous avez choisi {option}')
#     if supabase.table('users').select("open_ai_api_key").eq('id', user.id).execute().data[0]['open_ai_api_key'] is None:
#         supabase.table('users').update({'open_ai_api_key': get_api_key(option)}).eq('id', user.id).execute()
#         pass
#     if supabase.table('users').select("default_model_id").eq('id', user.id).execute().data[0]['default_model_id'] is None:
#         title = 'Choisissez un modèle '
#         model = get_model(option.lower())
#         name, index = pick(model, title)
#         default_model_id = supabase.table('models').select("id").eq('name', name).execute().data[0]['id']
#         supabase.table('users').update({'default_model_id': default_model_id}).eq('id', user.id).execute()
#     else:
#         main()
# elif option == 'Ollama':
#     print(f'Vous avez choisi {option}')
#     if supabase.table('users').select("open_ai_api_key").eq('id', user.id).execute().data[0]['open_ai_api_key'] is None:
#         supabase.table('users').update({'open_ai_api_key': get_api_key(option)}).eq('id', user.id).execute()
#         pass
#     if supabase.table('users').select("default_model_id").eq('id', user.id).execute().data[0]['default_model_id'] is None:
#         title = 'Choisissez un modèle '
#         model = get_model(option.lower())
#         name, index = pick(model, title)
#         default_model_id = supabase.table('models').select("id").eq('name', name).execute().data[0]['id']
#         supabase.table('users').update({'default_model_id': default_model_id}).eq('id', user.id).execute()
#     else:
#         main()
else:
    print('Invalid option')