import re
import datetime

def birthday(date, language = "en"):
    # This function should receive a date YYYY-MM-DD
    # User can inform language by providing a second param.
    # br: Brazilian Portuguese, se: Swedish, default English if not provided.
    # and return the day of the week you were born.
    validDate = "\d{4}-[0-1][0-9]-[0-3][0-9]"

    if (re.search(validDate, date)):

        dateSplit = date.split("-")
        actualDate = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
        weekDaysTranslation = {
            "br": {
                "0": "Domingo",
                "1": "Segunda-feira",
                "2": "Terça-feira",
                "3": "Quarta-feira",
                "4": "Quinta-feira",
                "5": "Sexta-feira",
                "6": "Sábado"
            },
            "se": {
                "0": "söndag",
                "1": "måndag",
                "2": "tisdag",
                "3": "onsdag",
                "4": "torsdag",
                "5": "fredag",
                "6": "lördag"
            }
        }

        if language in weekDaysTranslation:
            weekDay = weekDaysTranslation[language][str(actualDate.strftime("%w"))]
            print(weekDay)
        else:
            weekDay = actualDate.strftime("%A")
            print(weekDay)

    else:
        print("Please provide your birth day in the following format YYYY-MM-DD")


birthday("1986-03-14", "br")