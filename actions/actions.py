# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from scripts.joke import print_joke
import asyncio
import nest_asyncio

class ActionTellJoke(Action):

    def name(self) -> Text:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        joke = ""
        try:
            entityVal = tracker.latest_message['entities'][0]['value']
        except:
            entityVal = ""
        # entityVal = tracker.get_latest_entity_values('str')
        # entityVal = tracker.get_slot("joke_type")
        print(type(entityVal))
        print(entityVal)
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        nest_asyncio.apply()
        joke = asyncio.run(print_joke(entityVal))
        dispatcher.utter_message(text=joke)

        return []
