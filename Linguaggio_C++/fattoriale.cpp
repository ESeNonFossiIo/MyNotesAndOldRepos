#include <iostream>

long long int permutazioni(int num){
    long long int f = 1;
    int i = 2;
    for( i=2; i<=num ; i++)
        f *= i;
    return f;
}

int main(){
    int i = 2;
    for(i=2;i<=20;i++)
	   std::cout << "   " << i << "!\t= " <<  permutazioni(i) << std::endl;
	return 0;
}