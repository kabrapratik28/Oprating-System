read a
d=${#a} 
temp=0
c=1
while [ $c -le $d ]
do
	temp2=`expr $a % 10`
	a=`echo $a | rev | cut -c 2- | rev`
	#echo $temp2
	#echo $a
	
	if [ $temp2 -gt $temp ]
	then
   		temp=$temp2
	fi
	c=`expr $c + 1`
done


echo $temp
