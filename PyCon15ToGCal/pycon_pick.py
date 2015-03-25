# -*- coding: utf-8 -*-
"""
PyCon Pick
----------

Pick events from the schedule of talks and keynotes given at PyCon15.

:copyright: (c) 2015 by Samuel Masuy.
:license: GNU version 2.0, see LICENSE for more details.
"""


def pick_events(events):
    """
    Interface to select PyCon talks and keynotes.
    This let the user choose an event per time slot.
    The user can also skip a time slot, if desired.

    :param events: The list of events by time slot in order.
    :param events: list of lists of dicts.
    :return: The list of events that the user selected.
    :rtype: list of dicts.
    """
    events_picked = []
    date = None
    for time_slot in events:
        if not time_slot:
            continue
        else:
            if time_slot[0]['time_start'].date() != date:
                date = time_slot[0]['time_start'].date()
                print "\n=============================================================="
                print "===============Events on {0}===============".format(
                    time_slot[0]['time_start'].strftime('%A, %B %d, %Y'))
                print "==============================================================\n"

        if len(time_slot) == 1:
            event_to_pick = time_slot[0]
            invalid_user_input = False
            print u"Would you like to attend {0}?".format(event_to_str(event_to_pick))
            while not invalid_user_input:
                choice = raw_input("Press 'y' for yes, 'n' to skip it.  ")
                invalid_user_input = is_choice_valid(choice, ['y', 'n'])
            if choice != 'n':
                events_picked.append(event_to_pick)
        else:
            invalid_user_input = False
            print "Which of the following talk would you like to attend?"
            for index, event in enumerate(time_slot, start=1):
                print u"{0}) {1}".format(index, event_to_str(event))
            while not invalid_user_input:
                choice = raw_input("Press one of the corresponding talk number to select or 'n' to skip it.  ")
                invalid_user_input = is_choice_valid(
                    choice, ['n', range(1, len(time_slot) + 1)])
            if choice != 'n':
                events_picked.append(time_slot[int(choice) - 1])
        print "\n==============================================================\n"

    return events_picked


def is_choice_valid(choice, valid_options):
    """
    Check if an option is choice is valid give a list of options.

    :param choice: One character or integer.
    :type choice: int or str
    :param list valid_options: A list or a list of list containing valid options.
    :return: Choice is in list.
    :rtype: bool
    """
    return choice in (str(v) for subv in valid_options for v in subv)


def event_to_str(event):
    """
    Create a sentence out of an event.

    :param dict event: A PyCon event, can be a talk or a keynote.
    :return: A sentence describing the event.
    :rtype: str
    """
    title = event['title']
    speaker = event['speaker']
    time_start = event['time_start'].strftime('%I:%M%p')
    time_end = event['time_end'].strftime('%I:%M%p')
    track = event['track']
    return u"{title} by {speaker} from {time_start} to {time_end} in {track}".format(
        title=title,
        speaker=speaker,
        time_start=time_start,
        time_end=time_end,
        track=track)
