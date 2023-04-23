from consts.const import URL, SCHEMA

FILTER_BY_NAME_URL = URL + SCHEMA + '/name/Fido'

FILTER_BY_NAME = {
    "results": [
      {
        "breed": "Bulldog",
        "color": "White",
        "name": "Fido"
      }
    ]
}

FILTER_BY_BREED_URL = URL + SCHEMA + '/breed/Bulldog'

FILTER_BY_BREED = {
  "results": [
    {
      "breed": "Bulldog",
      "color": "Black",
      "name": "Hund"
    },
    {
      "breed": "Bulldog",
      "color": "White",
      "name": "Fido"
    }
  ]
}


FILTER_BY_COLOR_URL = URL + SCHEMA + '/color/White'

FILTER_BY_COLOR = {
    "results": [
      {
        "breed": "Shepard",
        "color": "White",
        "name": "Chien"
      },
      {
        "breed": "Bulldog",
        "color": "White",
        "name": "Fido"
      }
    ]
}
