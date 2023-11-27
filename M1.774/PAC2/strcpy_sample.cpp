#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char* argv[]) {
    // Crear un array de caràcters de destinació
    char destinacio[20];

    // Crear una cadena d'origen
    const char* origen = argv[1];

    // Utilitzar strcpy per copiar la cadena d'origen a l'array de destinació
    strcpy(destinacio, origen);

    // Imprimir el resultat
    cout << "Cadena de destinació: " << destinacio << endl;

    return 0;
}
