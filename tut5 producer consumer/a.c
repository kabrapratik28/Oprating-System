//gcc a.c -l pthread
#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>
#include<string.h>
void *s; 
pthread_t pth , cth ; 
sem_t empty , full ; 
void *prod() ; 
void *consu() ; 
char s1[10] , s2[10] , buf[10] ;
int main()
{
sem_init(&empty, 0, 1);
sem_init(&full, 0, 0);
pthread_create(&pth,NULL,prod,NULL);
pthread_create(&cth,NULL,consu,NULL);
pthread_join(pth,&s);
pthread_join(cth,&s);
sem_destroy(&empty);
sem_destroy(&full);
return 0 ; 
}


void *prod()
{
while(1)
{
printf("Enter String\n");
scanf("%s",s1) ;
   sem_wait(&empty);
   strcpy(buf,s1);
   sem_post(&full);
}
pthread_exit(&s) ; 
}

void *consu()
{

while(1)
{
   sem_wait(&full);
   strcpy(s2,buf);
   sem_post(&empty);
   printf("%s\n",s2) ; 
}
pthread_exit(&s) ; 
}

/* OUTPUT
student@vit-OptiPlex-360:~/Desktop$ ./a.out
Enter String
pratik
Enter String
pratik
kabara
Enter String
kabara
shrikant
Enter String
shrikant

*/
