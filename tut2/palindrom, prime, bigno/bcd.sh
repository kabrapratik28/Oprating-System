#prime number
read k
l=2
p=0
s=1
flag=0
while [ $l -lt $k ]
do 
    temp=`expr $k % $l`
    if [ $temp -eq $p ]
    then
	flag=1
    fi
    l=`expr $l + 1`
done

if [ $flag -eq $s ]
then
    echo "NOT PRIME"
else
    echo "PRIME"
fi