#include <iostream>
#include <fstream> //header necessario per ifstream!

using namespace std;

int main() {
    system("clear");
    ifstream f("righe.txt"); //nome del file da aprire, si può mettere anche il percorso (es C:\\file.txt)
    string s;

    if(!f) {
        cout <<"Il file non esiste!";
        return -1;
    }

    while(f.good()) //fino a quando c'è qualcosa da leggere ..
    {
        getline(f, s); //legge tutta la riga dal file e la mette nella variabile s
        cout<<s<<endl;
    }
    f.close(); //chiude il file

    return 0;
}