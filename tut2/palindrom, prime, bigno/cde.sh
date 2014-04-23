#PALINDROM
read a
lena=${#a}
i=1
j=$lena
while [ $i -le $lena ] 
do
    o=`echo $a | cut -c $i`
    q=`echo $a | cut -c $j`
   
    if [ $o != $q ]
    then
	echo "NOTPALINDROM"
	exit
    fi
    i=`expr $i + 1`
    j=`expr $j - 1`
done

echo "PALINDROM"