#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void pausa(int);

int main(){
  char command[50];
  strcpy(command, "clear" );
  system(command);

  pausa(3);
  int j = 0;
  for(j = 1; j <= 10; j++){
      printf("%i Hello world\n", j);
    }
  pausa(3);

  return(0);
}

void pausa(int a){
  int j = 0;
  for(j = 1; j <= a; j++){
      printf("\n");
    }
}
