# awk -F "|" -f pratik.awk emp
BEGIN{
    print "id name post money";
}
{
    if ($6 < 5000)
    {
	hr=0.2;
	pr=0.1; 
	total=$6+$6*hr+$6*pr ; 
	print $1,$2,$3,total ;
    }
    else if ($6 >= 5000 && $6 < 6000)
    {
	hr=0.1;
	pr=0.3; 
	total=$6+$6*hr+$6*pr ; 
	print $1,$2,$3,total ;
    }
    else if ($6 >= 6000 && $6 < 7000)
    {
	hr=0.4;
	pr=0.2; 
	total=$6+$6*hr+$6*pr ; 
	print $1,$2,$3,total ;
    }
    else if ($6 >= 7000 && $6 < 8000)
    {
	hr=0.5;
	pr=0.3; 
	total=$6+$6*hr+$6*pr ; 
	print $1,$2,$3,total ;
    }
    else
    {
	hr=0.5;
	pr=0.5; 
	total=$6+$6*hr+$6*pr ; 
	print $1,$2,$3,total ;
    }

}
END{
   
}
