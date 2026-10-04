*SRCMBRTXT:Imágenes de cheques - Prueba acceso via

/*    /COPY LE00525/TO10US,TOS1RR1RI                         */

CALL START
CALL CONNECTION
EXIT
/*-------------------------------------------------------------------*/
START:
/*-------------------------------------------------------------------*/
ADDRESS COMMAND
SYSNME="39.0.1.5"
USUARIO='anonymous'
CLAVE='anonymous'
RETURN
/*-------------------------------------------------------------------*/
CONNECTION:
/*-------------------------------------------------------------------*/
"DLTOVR *ALL       "
"DLTF  QTEMP/RESULT"
"CRTPF QTEMP/RESULT RCDLEN(80)"
"DLTF  QTEMP/SCRIPT"
"CRTPF QTEMP/SCRIPT RCDLEN(200)"
"OVRDBF STDOUT QTEMP/SCRIPT SECURE(*YES)"
SAY USUARIO CLAVE
SAY "quit"
"DLTOVR *ALL"
"OVRDBF INPUT  QTEMP/SCRIPT"
"OVRDBF STDOUT QTEMP/RESULT"
"FTP RMTSYS(&SYSNME) PORT(28)"
"DLTOVR *ALL"
RETURN
/*ENDREXSRC*/
