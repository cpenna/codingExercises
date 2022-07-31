function birthday(date) {
    // This function should receive a date YYYY-MM-DD
    // and return the day of the week you were born.
    validDate = /\d{4}-[0-1][0-9]-[0-3][0-9]/

    if (validDate.test(date)) {
        let dateArray = date.split("-") //  Splits date into array
        let actualDate = new Date(dateArray[0], dateArray[1] - 1, dateArray[2]).getDay()

        switch(actualDate) {
            case 0:
                weekDay = "Sunday"
                break;
            case 1:
                weekDay = "Monday"
                break;
            case 2:
                weekDay = "Tuesday"
                break;
            case 3:
                weekDay = "Wednesday"
                break;
            case 4:
                weekDay = "Thursday"
                break;
            case 5:
                weekDay = "Friday"
                break;
            default:
                weekDay = "Saturday"
        }

        console.log("You were born on : " + weekDay)
    } else {
        console.log("Please provide your birth day in the following format YYYY-MM-DD")
    }
}

birthday("1986-01-14")