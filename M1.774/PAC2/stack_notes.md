
//16 bytes per fila
(gdb) x/20w $sp
0x7fffffffde20: 0xffffdf48      0x00007fff      0x00000000      0x00000002
0x7fffffffde30: 0x55555250      0x00005555      0x55555090      0x00005555
0x7fffffffde40: 0xffffdf40      0x00007fff      0xffffe2bc      0x00007fff
0x7fffffffde50: 0x55555250      0x00005555  |-> 0xf7c30d0a      0x00007fff <-| Adreça de retorn de la funció
0x7fffffffde60: 0xffffdf48      0x00007fff      0x000011bf      0x00000002


$sp: 0x7fffffffde20 -> register $sp points to the top of stack (lowest numerical address)
                    The bottom of stack is a fixed address
$fp: 0x7fffffffde50 -> fixed location within a frame. any compilers use a second
register, FP, for referencing both local variables and parameters because their distances from FP do not change
with PUSHes and POPs. Marca la primera adreça de la pila que coincideix amb l'adreça de retorn de la funcio

Stack frame -> contains the parameters to a function, its local variables, and the data necessary to recover the previous stack frame, 
including the value of the instruction pointer at the time of the function call.

Intel -> stack grows down

2 words = 8 bytes

x/2w 0x7fffffffdf48 -> x "extract" obtenim el valor dins d'una posició de memòria

p &origen -> p "print" imprimim l'adreça de memòria de la variable en qüestió

(gdb) x/20w $sp
0x7fffffffde20: 0xffffdf48      0x00007fff      0x00000000      0x00000002
0x7fffffffde30: 0x6f786941      0x6e757365      0x64616361      0x64616e65
0x7fffffffde40: 0x72616365      0x65746361      0x65647372      0x6473656d
0x7fffffffde50: 0x6e697665      0x72616374 |->  0x65746361      0x00007372 <-| L'adreça de retorn s'ha sobreescrit!!!
0x7fffffffde60: 0xffffdf48      0x00007fff      0x000011bf      0x00000002