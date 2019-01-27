# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

import os
from twilio.rest import Client

#account_sid = os.environ["TWILIO_ACCOUNT_SID"]

account_sid = "AC8dd7c3947acb406b1dddd6a4bfeedc89"
auth_token = "2BF75A7799C79BCA152D423526132D14"

clientTwilio = Client(account_sid, auth_token)

class EmergencyForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "action_emergency_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["caller_first_name", "caller_callback_number",
                "caller_message"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"caller_first_name": self.from_entity(entity="caller_first_name",
                                            intent="inform"),

                "caller_callback_number": self.from_entity(entity="caller_callback_number",
                                            intent="phone_number"),

                "caller_message": self.from_text()}

#    @staticmethod
#    def is_int(string: Text) -> bool:
#        """Check if a string is an integer"""
#        try:
#            int(string)
#            return True
#        except ValueError:
#            return False


    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        clientTwilio.messages.create(
                to="+16194837869",
                from_="+16194837869",
                body="Congrats!"
        )
        # utter submit template
        dispatcher.utter_template('utter_confirm_message', tracker)
        return []
