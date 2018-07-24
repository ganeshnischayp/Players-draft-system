#!/bin/bash
filename='1.txt'
cat $filename | while read LINE
do
    echo $LINE
    p=$LINE
    echo "1-indbat...2-indbowl...3-indar...4-intbat...5-intbowl...6-intar...7-locbat...8-locbowl...9-locar...10-wk"
    read c
    if[$c == 1];then
        cat $p >> indbat.txt
    elif[$c == 2];then
        cat $p >> indbowl.txt
    elif[$c == 3];then
        cat $p >> indar.txt
    elif[$c == 4];then
        cat $p >> intbat.txt
    elif[$c == 5];then
        cat $p >> intbowl.txt
    elif[$c == 6];then
        cat $p >> intar.txt
    elif[$c == 7];then
        cat $p >> dombat.txt
    elif[$c == 8];then
        cat $p >> dombowl.txt
    elif[$c == 9];then
        cat $p >> domar.txt
    elif[$c == 10];then
        cat $p >> wk.txt
    fi
done