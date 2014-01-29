FILE="/home/pratik/Desktop/out"

#echo "abc" >> $FILE
echo "1.Insert 2.Delete 3.Update 4.Display 5.Search"
read option
case "$option" in
   1) 
	echo "Id"
	read idd 
	echo "Name"
	read name 
	echo "Designation"
	read desig 
	echo "Salary"
	read sal
	echo "$idd\t$name\t$desig\t$sal" >> $FILE
   ;;
   2)  
	read number
	grep "^$number" $FILE > out1
	if [ $? -ne 0 ]
	then
	  echo "Record Not Found"  
	else
	grep -v "^$number" $FILE > out1
	`cat out1 > $FILE`
	`rm out1`
	fi
   ;;
   3)
  	read number
	grep "^$number" $FILE
	if [ $? -ne 0 ]
	then
	  echo "Record Not Found"  
	else
	    grep -v "^$number" $FILE > out1
	    `cat out1 > $FILE`
	    `rm out1`
	     #echo "Id"
             #read idd 
	    echo "Name"
	    read name 
	    echo "Designation"
	    read desig 
	    echo "Salary"
	    read sal
	    echo "$number\t$name\t$desig\t$sal" >> $FILE
	fi
   ;;
   4)
	echo "id name designation salary\n"
	cat $FILE
   ;;
   5)
	read number 
  	grep "^$number" $FILE
	if [ $? -ne 0 ]
	then
	  echo "Record Not Found"  
	fi
   ;;
esac

