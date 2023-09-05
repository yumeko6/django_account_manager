from mimesis.enums import TimestampFormat
from mimesis.locales import Locale
from mimesis.keys import maybe
from mimesis.schema import Field, Schema


field = Field(locale=Locale.RU)

schema = Schema(
    schema=lambda: {
        "model": "employees.employee",
        "pk": field('increment'),
        "fields": {
            "lastname": field('last_name'),
            "firstname": field('name'),
            "middlename": field('name'),
            "position": field('occupation'),
            "email": field('email'),
            "phone": field('phone_number', mask='##########'),
            "extension": field('integer_number', start=100, end=200),
            'author': '1',
            'pub_date': field('timestamp', fmt=TimestampFormat.RFC_3339),
            'change_date': field('timestamp', fmt=TimestampFormat.RFC_3339),
            'is_fired': 'False'
        }
    },
    iterations=200
)

schema2 = Schema(
    schema=lambda: {
        "model": "resources.resource",
        "pk": field('increment'),
        "fields": {
            "title": field('company'),
            "author": '1',
            "url": field('url'),
            'pub_date': field('timestamp', fmt=TimestampFormat.RFC_3339),
            'change_date': field('timestamp', fmt=TimestampFormat.RFC_3339),
            'note': field('quote')
        }
    },
    iterations=20
)

#schema.to_json(file_path='data.json')
schema2.to_json(file_path='data2.json')
