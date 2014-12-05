#include <iostream>
#include <string>


int main()
{
    int lenght;
    std::string parola;
	std::cin >> parola;
    lenght = sizeof(parola)/sizeof(parola[0]);
    std::cout << "|" << parola <<"|"<< parola.length();
	return 0;
}