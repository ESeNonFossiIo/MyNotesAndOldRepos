/*
*	Semplice programma che legge gli argomenti
*	passati nella linea di comando e li stampa
*	a video
*/

#include <stdio.h>
#include <iostream>

int main(int argc, char* argv[])
{
int i;
if(argc < 2)
{
std::cout << "Per eseguire il programma bisogna inserire due argomenti" << std::endl;
std::cout << "Ripetere l’operazione" << std::endl;
exit(0);
}


for(i = 1; i < argc; i++)
{
printf("Argomento %d è %sn \n", i, argv[i]);
}

return (0);

}