     H option(*nodebugio:*noshowcpy:*srcstmt)
     H alwnull(*usrctl) dftactgrp(*no)
     H bnddir ( 'HDIILE/HDIBDIR' )
      * ************************************************************ *
      * WSLRED  : Tareas generales.                                  *
      *           WebService - Retorna Rango de Edades               *
      * ------------------------------------------------------------ *
      * Alvarez Fernando                               *23-Dic-2015  *
      * ------------------------------------------------------------ *
      * Modificaciones:                                              *
      * ************************************************************ *

      /copy './qcpybooks/svpws_h.rpgle'

     D WSLRED          pr                  ExtPgm('WSLRED')
     D   peEdad                            likeds(edades_t) dim(9)
     D   peEdadC                     10i 0
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D WSLRED          pi
     D   peEdad                            likeds(edades_t) dim(9)
     D   peEdadC                     10i 0
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

       *inLr = *On;

       clear peEdad;
       clear peMsgs;

       peEdadC = 3;
       peErro  = *Zeros;

       peEdad( 1 ).codi = 1;
       peEdad( 1 ).mini = *Zeros;
       peEdad( 1 ).maxi = 14;
       peEdad( 1 ).desc = 'Menores de 15 Años';

       peEdad( 2 ).codi = 2;
       peEdad( 2 ).mini = 15;
       peEdad( 2 ).maxi = 64;
       peEdad( 2 ).desc = 'De 15 a 64 Años';

       peEdad( 3 ).codi = 3;
       peEdad( 3 ).mini = 65;
       peEdad( 3 ).maxi = 99;
       peEdad( 3 ).desc = 'Mayores de 64 Años';

       return;
