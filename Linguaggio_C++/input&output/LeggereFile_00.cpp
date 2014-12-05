/*
  Lettura di un file riga per riga.
*/

#include<stdlib.h>
#include<stdio.h>
#include<cstring>

int main() {
  FILE *fd;
  char buf[200];
  char *res;
    int i = 0;
  char * pch;    


		/* apre il file */
  fd=fopen("righe.txt", "r");
  if( fd==NULL ) {
    perror("Errore in apertura del file");
    exit(1);
  }

system("clear");
		/* legge e stampa ogni riga */
  while(1) {
    res=fgets(buf, 200, fd);
    if( res==NULL )
      break;  
  pch = strstr (res,"using");

    printf("%d \t %s", i, buf);
    if(pch!=NULL){
        printf(" <--  TROVATO!\n");
    }
    i++;
  }
printf("\n\n");

		/* chiude il file */
  fclose(fd);

  return 0;
}