#This is a decider, due to my indecisiveness it will help me choose what to do.
#It looks at my file of things to do and using a random number generator and
#awk it will pick something for me to do.

#random number generator
FLOOR=1
CEILING=`awk '{print $1}' $1 | wc -w`
RANGE=$(($CEILING - $FLOOR + 1))
RESULT=$RANDOM
let "RESULT %= $RANGE"
RESULT=$(($RESULT + $FLOOR))

#Using awk I pick the row number using my random number generator and I print
#the line out. The $1 is taking in the file name from the command line.
des=`awk 'FNR == '$RESULT' {print}' $1`

#This prints out the result!
echo $des
