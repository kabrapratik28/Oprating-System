//gcc readerwriter.c -l pthread

#include<stdio.h>
#include<pthread.h>

void *s ;
int a =1 ; 

pthread_t rth ; 
pthread_t wth ; 

pthread_mutex_t m ; 

void * read()
{
  while(1)
    {
      pthread_mutex_lock(&m);
      printf("reader %d",a);
      pthread_mutex_unlock(&m);
      sleep(1) ; 
    }
  pthread_exit(&s);
}

void * write()
{
while(1)
    {
      pthread_mutex_lock(&m);
      printf("writter %d",++a);
      pthread_mutex_unlock(&m);
      sleep(1) ; 
    }
  pthread_exit(&s);

}

int main()
{
  pthread_mutex_init(&m,0);
  pthread_create(&wth,NULL,write,NULL);
  pthread_create(&rth,NULL,read,NULL);
  
  pthread_join(rth,&s);
  pthread_join(wth,&s);

  return 0 ; 

}
