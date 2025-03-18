from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecomendarFilme(Action):
    def name(self) -> Text:
        return "action_recomendar_filme"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Obtém o gênero do slot
        genero = tracker.get_slot("genero")
        
        # Obtém recomendações de filmes
        filmes = self.obter_recomendacoes(genero)
        
        if filmes:
            # Retorna a resposta com recomendações
            dispatcher.utter_message(text=f"Para o gênero {genero}, recomendo: {', '.join(filmes)}.")
        else:
            # Mensagem caso não encontre recomendações
            dispatcher.utter_message(text=f"Desculpe, não encontrei recomendações para o gênero {genero}.")
        
        return []

    def obter_recomendacoes(self, genero: Text) -> List[Text]:
        """ Retorna uma lista de filmes baseada no gênero informado. """
        filmes_por_genero = {
            "comédia": ["Se Beber, Não Case!", "Minha Mãe é Uma Peça", "Deadpool"],
            "ação": ["Mad Max: Estrada da Fúria", "John Wick", "Missão Impossível"],
            "ficção científica": ["Interestelar", "Blade Runner 2049", "Matrix"],
            "drama": ["Um Sonho de Liberdade", "O Poderoso Chefão", "A Lista de Schindler"],
            "suspense": ["Seven - Os Sete Crimes Capitais", "Ilha do Medo", "O Silêncio dos Inocentes"],
            "terror": ["O Iluminado", "Invocação do Mal", "Hereditário"],
            "romance": ["Diário de uma Paixão", "Simplesmente Acontece", "Antes do Amanhecer"],
            "aventura": ["Jurassic Park", "Piratas do Caribe", "O Senhor dos Anéis"],
            "documentário": ["I Am Not Your Negro", "Planeta Terra", "Free Solo"],
            "anime": ["A Viagem de Chihiro", "Your Name", "Akira"]
        }
        
        # Retorna os filmes do gênero informado ou uma lista vazia
        return filmes_por_genero.get(genero.lower(), [])
