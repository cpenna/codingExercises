#!/usr/bin/bash
# This should receive date input in format YYYY-MM-DD
# and return the corresponding day of the week

function readDate() {
    echo "Provide your birthday date (YYYY-MM-DD):"
    # Date constructor sample for 1986-01-14
    # date -v1986y -v1m -v14d
    read inputdate

    if [[ -z ${inputdate} ]]; then
        echo "No input provided."
        readDate
    elif [[ ${inputdate} =~ ^[0-2][0-9][0-9][0-9]-[0-2][0-9]-[0-3][0-9]$ ]]; then
        year=`echo $inputdate | cut -d "-" -f 1`
        month=`echo $inputdate | cut -d "-" -f 2`
        day=`echo $inputdate | cut -d "-" -f 3`
        weekDay=`date -v${year}y -v${month}m -v${day}d +%A`

        echo "You were born at weekday: $weekDay"
    else
        echo "Invalid date!"
        readDate
    fi
}

readDate
