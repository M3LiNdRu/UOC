#include <iostream>
#include <syslog.h>
using namespace std;

int main() {

    string userFormat;
    
    // Inicialització de la funció syslog
    openlog("my_program", LOG_PID | LOG_CONS, LOG_USER);

    cout << "Introdueix el missatge de registre: ";
    getline(cin, userFormat);

    //L'usuari proporciona el missatge de registre sense validar
    syslog(LOG_INFO, userFormat.c_str());

    // Tancament de la funció syslog
    closelog();

    return 0;
}