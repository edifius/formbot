## story 001 - emergency
* initiate_call
    - utter_greet
* confirm
    - utter_emergency
    - action_emergency_form
    - form{"name": "action_emergency_form"}
    - form{"name": null}
* confirm
    - utter_message_sent
> more_help

## story 002 - emergency
* initiate_call
    - utter_greet
* confirm
    - utter_emergency
> emergency

## story 003 - emergency checkpoint
> emergency
    - action_emergency_form
    - form{"name": "action_emergency_form"}
    - slot{"requested_slot": "caller_first_name"}
* form: inform{"caller_first_name": "joe"}
    - form: action_emergency_form
    - slot{"caller_first_name": "joe"}
    - slot{"requested_slot": "caller_last_name"}
* form: inform{"caller_last_name": "humphrey"}
    - form: action_emergency_form
    - slot{"caller_last_name": "humphrey"}
    - slot{"requested_slot": "caller_callback_number"}
* form: phone_number{"caller_callback_number": "7708778901"}
    - form: action_emergency_form
    - slot{"caller_callback_number": "7708778901"}
    - slot{"requested_slot": "caller_message"}
* form: inform{"caller_message": "my son needs an earlier pickup"}
    - slot{"caller_message": "my son needs an earlier pickup"}
    - form: action_emergency_form
    - slot{"caller_message": "my son needs an earlier pickup"}
    - form{"name": null}
    - slot{"requested_slot": null}
* confirm
    - utter_message_sent
> more_help

* initiate_call
    - utter_greet
* confirm
    - utter_emergency
    - action_emergency_form
    - form{"name": "action_emergency_form"}
    - slot{"requested_slot": "caller_first_name"}
* form: inform{"caller_first_name": "joe"}
    - form: action_emergency_form
    - slot{"caller_first_name": "joe"}
    - slot{"requested_slot": "caller_last_name"}
* form: inform{"caller_last_name": "humphrey"}
    - form: action_emergency_form
    - slot{"caller_last_name": "humphrey"}
    - slot{"requested_slot": "caller_callback_number"}
* form: phone_number{"caller_callback_number": "7708778901"}
    - form: action_emergency_form
    - slot{"caller_callback_number": "7708778901"}
    - slot{"requested_slot": "caller_message"}
* form: inform{"caller_message": "my son needs an earlier pickup"}
    - slot{"caller_message": "my son needs an earlier pickup"}
    - form: action_emergency_form
    - slot{"caller_message": "my son needs an earlier pickup"}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_wrong_message_info
    - action_deactivate_form
    - form{"name": null}
> emergency

## story 001 - not emergency
* initiate_call
    - utter_greet
* deny
    - utter_ask_name
* inform{"caller_first_name": null}
    - slot{"caller_first_name": null}
    - utter_greet_how_is_caller_doing
* greet_feeling
> how_to_help

## story 001 - not emergency
* initiate_call
    - utter_greet
* deny
    - utter_ask_name
* inform{"caller_first_name": "jonathan"}
    - slot{"caller_first_name": "jonathan"}
    - utter_greet_how_is_caller_doing
* greet_feeling
> how_to_help

## story 001 - not emergency
* initiate_call
    - utter_greet
* deny
    - utter_ask_name
* inform{"caller_first_name": null}
    - slot{"caller_first_name": null}
    - utter_greet_how_is_caller_doing
* inform_greet_with_question
    - utter_greet_how_are_you
> how_to_help

## story 001 - not emergency
* initiate_call
    - utter_greet
* deny
    - utter_ask_name
* inform{"caller_first_name": "billy"}
    - slot{"caller_first_name": "billy"}
    - utter_greet_how_is_caller_doing
* inform_greet_with_question
    - utter_greet_how_are_you
> how_to_help

## story 002 - emergency
* emergency
    - utter_emergency
> emergency

## story 004 - greet
* greet
  - utter_greet2

## story 003 - goodbye
* goodbye
    - utter_goodbye
    - action_end_call

## story 008 - pickup_location
* pickup_location
    - utter_pickup_location
    - utter_question_answered
* confirm
> more_help

## story 008 - pickup_location
* pickup_location
    - utter_pickup_location
    - utter_question_answered
* deny
  - utter_still_learning

## story 010 - ages
* ages
    - utter_ages
    - utter_question_answered
* confirm
> more_help

## story 010 - ages
* ages
    - utter_ages
    - utter_question_answered
* deny
  - utter_still_learning

## story 012 - dropff_location
* dropff_location
    - utter_dropff_location
    - utter_question_answered
* confirm
> more_help

## story 012 - dropff_location
* dropff_location
    - utter_dropff_location
    - utter_question_answered
* deny
    - utter_still_learning

## story 014 - payment_tracks
* payment_tracks
    - utter_payment_tracks
    - utter_question_answered
* confirm
> more_help

## story 014 - payment_tracks
* payment_tracks
    - utter_payment_tracks
    - utter_question_answered
* deny
    - utter_still_learning

## story 016 - riders
* riders
    - utter_riders
    - utter_question_answered
* confirm
> more_help

## story 016 - riders
* riders
    - utter_riders
    - utter_question_answered
* deny
    - utter_still_learning

## story 018 - driver
* driver
    - utter_driver
    - utter_question_answered
* confirm
> more_help

## story 018 - driver
* driver
    - utter_driver
    - utter_question_answered
* deny
    - utter_still_learning

## story 020 - sickdays
* sickdays
    - utter_sickdays
    - utter_question_answered
* confirm
> more_help

## story 020 - sickdays
* sickdays
    - utter_sickdays
    - utter_question_answered
* deny
    - utter_still_learning

## story 022 - discount
* discount
    - utter_discount
    - utter_question_answered
* confirm
> more_help

## story 022 - discount
* discount
    - utter_discount
    - utter_question_answered
* deny
    - utter_still_learning

## story 024 - other_routes
* other_routes
    - utter_other_routes
    - utter_question_answered
* confirm
> more_help

## story 024 - other_routes
* other_routes
    - utter_other_routes
    - utter_question_answered
* deny
    - utter_still_learning

## story 026 - reservations
* reservations
    - utter_reservations
    - utter_question_answered
* confirm
> more_help

## story 026 - reservations
* reservations
    - utter_reservations
    - utter_question_answered
* deny
    - utter_still_learning

## story 026 - service cost
* service_cost
    - utter_service_cost
    - utter_question_answered
* confirm
> more_help

## story 026 - service cost
* service_cost
    - utter_service_cost
    - utter_question_answered
* deny
    - utter_still_learning

## story 028 - payments
* payments
    - utter_payments
    - utter_question_answered
* confirm
> more_help

## story 028 - payments
* payments
    - utter_payments
    - utter_question_answered
* deny
    - utter_still_learning

## story 030 - deposit
* deposit
    - utter_deposit
    - utter_question_answered
* confirm
> more_help

## story 030 - deposit
* deposit
    - utter_deposit
    - utter_question_answered
* deny
    - utter_still_learning

## story 032 - kinder_child
* kinder_child
    - utter_kinder_child
    - utter_question_answered
* confirm
> more_help

## story 032 - kinder_child
* kinder_child
    - utter_kinder_child
    - utter_question_answered
* deny
    - utter_still_learning

## story 034 - daily_rate
* daily_rate
    - utter_daily_rate
    - utter_question_answered
* confirm
> more_help

## story 034 - daily_rate
* daily_rate
    - utter_daily_rate
    - utter_question_answered
* deny
    - utter_still_learning

## story 036 - transportation_times
* transportation_times
    - utter_transportation_times
    - utter_question_answered
* confirm
> more_help

## story 036 - transportation_times
* transportation_times
    - utter_transportation_times
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - older_child
* older_child
    - utter_older_child
    - utter_question_answered
* confirm
> more_help

## story 038 - older_child
* older_child
    - utter_older_child
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - registration
* registration
    - utter_registration
    - utter_question_answered
* confirm
> more_help

## story 038 - registration
* registration
    - utter_registration
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - driver_presence
* driver_presence
    - utter_driver_presence
    - utter_question_answered
* confirm
> more_help

## story 038 - driver_presence
* driver_presence
    - utter_driver_presence
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - military_discounts
* military_discounts
    - utter_military_discounts
    - utter_question_answered
* confirm
> more_help

## story 038 - military_discounts
* military_discounts
    - utter_military_discounts
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - service_breaks
* service_breaks
    - utter_service_breaks
    - utter_question_answered
* confirm
> more_help

## story 038 - service_breaks
* service_breaks
    - utter_service_breaks
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - cancellation_policy
* cancellation_policy
    - utter_cancellation_policy
    - utter_question_answered
* confirm
> more_help

## story 038 - cancellation_policy
* cancellation_policy
    - utter_cancellation_policy
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - service_drivers
* service_drivers
    - utter_service_drivers
    - utter_question_answered
* confirm
> more_help

## story 038 - service_drivers
* service_drivers
    - utter_service_drivers
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - gps_tracking
* gps_tracking
    - utter_gps_tracking
    - utter_question_answered
* confirm
> more_help

## story 038 - gps_tracking
* gps_tracking
    - utter_gps_tracking
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - service_app
* service_app
    - utter_service_app
    - utter_question_answered
* confirm
> more_help

## story 038 - service_app
* service_app
    - utter_service_app
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - service_vehicles
* service_vehicles
    - utter_service_vehicles
    - utter_question_answered
* confirm
> more_help

## story 038 - service_vehicles
* service_vehicles
    - utter_service_vehicles
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - our_drivers
* our_drivers
    - utter_our_drivers
    - utter_question_answered
* confirm
> more_help

## story 038 - our_drivers
* our_drivers
    - utter_our_drivers
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - advanced_booking
* advanced_booking
    - utter_advanced_booking
    - utter_question_answered
* confirm
> more_help

## story 038 - advanced_booking
* advanced_booking
    - utter_advanced_booking
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - service_hours
* service_hours
    - utter_service_hours
    - utter_question_answered
* confirm
> more_help

## story 038 - service_hours
* service_hours
    - utter_service_hours
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - service_areas
* service_areas
    - utter_service_areas
    - utter_question_answered
* confirm
> more_help

## story 038 - service_areas
* service_areas
    - utter_service_areas
    - utter_question_answered
* deny
    - utter_still_learning

## story 038 - pickup_tomorrow
* pickup_tomorrow
    - utter_pickup_tomorrow
    - utter_question_answered
* confirm
> more_help

## story 038 - pickup_tomorrow
* pickup_tomorrow
    - utter_pickup_tomorrow
    - utter_question_answered
* deny
    - utter_still_learning

## story 039 - how to help
> how_to_help
    - utter_how_to_help

## story 039 - end call
> more_help
    - utter_more_help
* deny
    - utter_goodbye
    - action_end_call

## story 040 - more help needed
> more_help
    - utter_more_help

## story 054 - more help needed - confirm
> more_help
    - utter_more_help
* confirm
    - utter_more_help2
## Generated Story 6807429880061983787
* initiate_call
    - utter_greet
* deny
    - utter_ask_name
* inform{"caller_first_name": "joe"}
    - utter_greet_how_is_caller_doing
* greet_feeling
    - utter_how_to_help
* discount
    - utter_discount
    - utter_question_answered
* confirm
    - utter_more_help
* ages
    - utter_ages
    - utter_question_answered
* deny
    - utter_still_learning
* ages
    - utter_ages
    - utter_question_answered
* confirm
    - utter_more_help
* emergency
    - utter_emergency
    - action_emergency_form
    - form{"name": "action_emergency_form"}
    - slot{"requested_slot": "caller_first_name"}
* form: inform{"caller_first_name": "joe"}
    - form: action_emergency_form
    - slot{"caller_first_name": "joe"}
    - slot{"requested_slot": "caller_last_name"}
* form: inform{"caller_last_name": "humphrey"}
    - form: action_emergency_form
    - slot{"caller_last_name": "humphrey"}
    - slot{"requested_slot": "caller_callback_number"}
* form: phone_number{"caller_callback_number": "7705467892"}
    - form: action_emergency_form
    - slot{"caller_callback_number": "7705467892"}
    - slot{"requested_slot": "caller_message"}
* form: inform{"caller_message": "it's raining. please hurry."}
    - form: action_emergency_form
    - slot{"caller_message": "it's raining. please hurry."}
    - form{"name": null}
    - slot{"requested_slot": null}
* confirm
    - utter_message_sent
    - utter_more_help
* ages
    - utter_ages
    - utter_question_answered
* confirm
    - utter_more_help
* goodbye
    - utter_goodbye
    - action_end_call
## Generated Story 4768347756522452267
* initiate_call
    - utter_greet
* confirm
    - utter_emergency
    - action_emergency_form
    - form{"name": "action_emergency_form"}
    - slot{"requested_slot": "caller_first_name"}
* form: inform{"caller_first_name": "joe"}
    - form: action_emergency_form
    - slot{"caller_first_name": "joe"}
    - slot{"requested_slot": "caller_last_name"}
* form: inform{"caller_last_name": "humphrey"}
    - form: action_emergency_form
    - slot{"caller_last_name": "humphrey"}
    - slot{"requested_slot": "caller_callback_number"}
* form: phone_number{"caller_callback_number": "7079345678"}
    - form: action_emergency_form
    - slot{"caller_callback_number": "7079345678"}
    - slot{"requested_slot": "caller_message"}
* form: inform{"caller_message": "i need to cancel my ride"}
    - form: action_emergency_form
    - slot{"caller_message": "i need to cancel my ride"}
    - form{"name": null}
    - slot{"requested_slot": null}
* confirm
    - utter_message_sent
    - utter_more_help
* deny
    - utter_goodbye
    - action_end_call

