let media = (myArray) => {

    let sumTotal = 0

    myArray.forEach((n) => { sumTotal += n })

    return sumTotal / myArray.length
}

console.log(media([0, 5, 10, 15, 20]))