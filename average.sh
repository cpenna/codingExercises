#!/usr/bin/bash
numbers=('0' '5' '10' '15' '20')

average() {

    sum=0
    counter=0

    for i in ${numbers[@]};
    do
        ((sum+=i))
        ((counter+=1))
    done

    echo "For numbers list ${numbers[@]} average is $((sum/counter))"
}

average
