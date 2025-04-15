import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBuscarLivro(Action):
    def name(self) -> Text:
        return "action_buscar_livro"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        titulo = tracker.get_slot('titulo_livro')
        autor = tracker.get_slot('nome_autor')
        assunto = tracker.get_slot('assunto_livro')

        if titulo:
            query = f"https://openlibrary.org/search.json?title={titulo}"
        elif autor:
            query = f"https://openlibrary.org/search.json?author={autor}"
        elif assunto:
            query = f"https://openlibrary.org/search.json?subject={assunto}"
        else:
            dispatcher.utter_message(text="Não consegui identificar sua busca.")
            return []

        response = requests.get(query).json()

        if response['docs']:
            livro = response['docs'][0]
            titulo_resultado = livro.get('title', 'Título não encontrado')
            autor_resultado = livro.get('author_name', ['Autor desconhecido'])[0]
            dispatcher.utter_message(
                text=f"Encontrei: *{titulo_resultado}* de {autor_resultado}."
            )
        else:
            dispatcher.utter_message(text="Não encontrei nenhum livro com esses critérios.")

        return []
