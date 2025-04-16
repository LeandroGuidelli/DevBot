from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.interfaces import Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Dict, Any, List

class ActionFornecerSuporte(Action):
    def name(self) -> Text:
        return "action_fornecer_suporte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,  # Certifique-se de que Tracker está sendo passado corretamente
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        problema = next(tracker.get_latest_entity_values("problema"), None)
        if not problema:
            problema = tracker.latest_message.get('text')

        # Fornecer soluções para problemas simples
        if "acessar" in problema or "login" in problema:
            dispatcher.utter_message(text="Verifique se o e-mail e senha estão corretos. Caso tenha esquecido, clique em 'Esqueci minha senha'.")
        elif "mudar" in problema or "plano" in problema:
            dispatcher.utter_message(text="Você pode alterar seu plano nas configurações da sua conta.")
        elif "não funciona" in problema or "aplicativo" in problema or "trava" in problema:
            dispatcher.utter_message(text="Reinstale o aplicativo ou verifique se está atualizado.")
        elif "pedido" in problema or "entregue" in problema:
            dispatcher.utter_message(text="Verifique o status do seu pedido na área do usuário.")
        else:
            # Caso o problema não se encaixe nos exemplos, encaminha para o atendente
            dispatcher.utter_message(text="Não consigo ajudá-lo, irei encaminhar você para um de nossos atendentes.")
            return [SlotSet("problema", "complexo")]

        return []
