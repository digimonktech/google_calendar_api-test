from build_service import build_service


def create_new_event():
    service = build_service()
    event = {
        'summary': 'Google I/O 2021',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2021-10-09T09:00:00-07:00',
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': '2021-10-09T17:00:00-07:00',
            'timeZone': 'Asia/Kolkata',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':
    create_new_event()
