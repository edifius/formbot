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

        return ["caller_first_name", "caller_last_name", "caller_callback_number",
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

                "caller_last_name": self.from_entity(entity="caller_last_name",
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

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
#        for slot, value in slot_values.items():
#            if slot == 'cuisine':
#                if value.lower() not in self.cuisine_db():
#                    dispatcher.utter_template('utter_wrong_cuisine', tracker)
#                    # validation failed, set slot to None
#                    slot_values[slot] = None

#            elif slot == 'num_people':
#                if not self.is_int(value) or int(value) <= 0:
#                    dispatcher.utter_template('utter_wrong_num_people',
#                                              tracker)
                    # validation failed, set slot to None
#                    slot_values[slot] = None

#            elif slot == 'outdoor_seating':
#                if isinstance(value, str):
#                    if 'out' in value:
                        # convert "out..." to True
#                        slot_values[slot] = True
#                    elif 'in' in value:
                        # convert "in..." to False
#                        slot_values[slot] = False
#                    else:
#                        dispatcher.utter_template('utter_wrong_outdoor_seating',
#                                                  tracker)
                        # validation failed, set slot to None
#                        slot_values[slot] = None

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        clientTwilio.messages.create(
                to="+17708456280",
                from_="+17708456280",
                body="Congrats, Perla!"
        )
        # utter submit template
        dispatcher.utter_template('utter_confirm_message', tracker)
        return []
