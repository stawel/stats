#!/bin/bash

DICT=$2
EXPR="$1"

for s0 in {a..z} 
do 
    for((i=1;i<20;i++))
    do
        prev=s$((i-1))
        pval=${!prev}
        eval s$i=$(echo "$pval" | tr "0-9a-z" "1-9a-z_") 
    done

    S=`eval echo "$EXPR"`
    echo '---'$S
    grep "$S" $DICT
    S=`echo "$S" |rev`
    echo '---'$S
    grep "$S" $DICT
done
