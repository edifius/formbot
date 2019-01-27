## story 001 - emergency
* initiate_call
    - utter_greet
* confirm
  - utter_emergency
  > more_help

## story 001 - not emergency
* initiate_call
    - utter_greet
* deny
    - utter_ask_name
* caller_info{"caller_first_name": null}
    - slot{"caller_first_name": null}
    - utter_greet_how_is_caller_doing
* greet_feeling
> how_to_help

## story 001 - not emergency
* initiate_call
    - utter_greet
* deny
    - utter_ask_name
* caller_info{"caller_first_name": "jonathan"}
    - slot{"caller_first_name": "jonathan"}
    - utter_greet_how_is_caller_doing
* greet_feeling
> how_to_help

## story 001 - not emergency
* initiate_call
    - utter_greet
* deny
    - utter_ask_name
* caller_info{"caller_first_name": null}
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
* caller_info{"caller_first_name": "billy"}
    - slot{"caller_first_name": "billy"}
    - utter_greet_how_is_caller_doing
* inform_greet_with_question
    - utter_greet_how_are_you
> how_to_help

## story 004 - greet
* greet
  - utter_greet2

## story 003 - goodbye
* goodbye
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

## story 039 - how to help
> how_to_help
    - utter_how_to_help

## story 039 - end call
> more_help
    - utter_more_help
* deny
    - action_end_call

## story 040 - more help needed
> more_help
    - utter_more_help

## story 054 - more help needed - confirm
> more_help
    - utter_more_help
* confirm
    - utter_more_help2
