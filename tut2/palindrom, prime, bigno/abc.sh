#max number
read a
d=${#a}
l=1
k=10
temp=0
temp2=0 
while [ $l -le $d ]
do
    temp2=`expr $a % $k`
    echo $temp2
    if [ $temp2 -ge $temp ]
    then
	temp=$temp2
    fi
    a=`expr $a / $k`
    l=`expr $l + 1`
done

echo "$temp"
