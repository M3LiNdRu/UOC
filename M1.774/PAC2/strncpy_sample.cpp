#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char* argv[]) {
    // Crear un array de caràcters de destinació
    char destinacio[20];

    // Crear una cadena d'origen
    const char* origen = argv[1];

    // Utilitzar strncpy per copiar la cadena d'origen a l'array de destinació de manera segura
    strncpy(destinacio, origen, sizeof(destinacio)-1);
    destinacio[sizeof(destinacio)-1] = '\0';  // Assegurar que la cadena de destinació estigui acabada amb null

    // Imprimir el resultat
    cout << "Cadena de destinació: " << destinacio << endl;

    return 0;
}
