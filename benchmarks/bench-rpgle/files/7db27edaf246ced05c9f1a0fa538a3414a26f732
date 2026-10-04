     H option(*srcstmt:*noshowcpy:*nodebugio) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
      * ************************************************************ *
      * WSRAGB: Portal de Autogestión de Asegurados.                 *
      *         Anular o Arrepentimiento.                            *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *19-May-2021            *
      * ------------------------------------------------------------ *
      *                                                              *
      * ************************************************************ *
     Fpahaag    if   e           k disk
     Fpahag4    if a e           k disk
     Fpahtan    if a e           k disk
     Fpahec0    if   e           k disk
     Fset915    uf a e           k disk

      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/wsstruc_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/svppol_h.rpgle'
      /copy './qcpybooks/spvspo_h.rpgle'

      * ------------------------------------------------------------ *
      * URL y URI
      * ------------------------------------------------------------ *
     D uri             s            512a
     D url             s           3000a   varying

      * ------------------------------------------------------------ *
      * Parámetros de URL
      * ------------------------------------------------------------ *
     D empr            s              1a
     D sucu            s              2a
     D tdoc            s              2a
     D ndoc            s             11a
     D arcd            s              6a
     D spol            s              9a
     D rama            s              2a
     D arse            s              2a
     D oper            s              7a
     D poli            s              7a
     D tipo            s              1a
     D cmot            s              2a
     D ntel            s             20a

     D peTdoc          s              2  0
     D peNdoc          s             11  0
     D peArcd          s              6  0
     D peSpol          s              9  0
     D peRama          s              2  0
     D peArse          s              2  0
     D peOper          s              7  0
     D pePoli          s              7  0
     D peTnum          s              2a   inz('AA')
     D @@fecn          s              8  0
     D @@horn          s              6  0
     D peCade          s              5  0 dim(9)

     D x               s             10i 0
     D peRepl          s          65535a
     D rc              s              1n
     D LogData         s          65535a   varying
     D peMsgs          ds                  likeds(paramMsgs)
     D peErro          s             10i 0

     D k1hag4          ds                  likerec(p1hag4:*key)
     D k1hec0          ds                  likerec(p1hec0:*key)
     D k1t915          ds                  likerec(s1t915:*key)
     D k1htan          ds                  likerec(p1htan:*key)

     D psds           sds                  qualified
     D  this                         10a   overlay(psds:1)
     D  curusr                       10a   overlay(psds:358)

      /free

       *inlr = *on;

       REST_getUri( psds.this : uri );
       url = %trim(uri);

       empr = REST_getNextPart(url);
       sucu = REST_getNextPart(url);
       tdoc = REST_getNextPart(url);
       ndoc = REST_getNextPart(url);
       arcd = REST_getNextPart(url);
       spol = REST_getNextPart(url);
       rama = REST_getNextPart(url);
       arse = REST_getNextPart(url);
       oper = REST_getNextPart(url);
       poli = REST_getNextPart(url);
       tipo = REST_getNextPart(url);
       cmot = REST_getNextPart(url);
       ntel = REST_getNextPart(url);

       if SVPREST_chkCliente( empr
                            : sucu
                            : tdoc
                            : ndoc
                            : peMsgs ) = *Off;
          exsr logError;
          REST_writeHeader( 204
                          : *omit
                          : *omit
                          : peMsgs.peMsid
                          : peMsgs.peMsev
                          : peMsgs.peMsg1
                          : peMsgs.peMsg2 );
          exsr wrtError;
          REST_end();
          SVPREST_end();
          close *all;
          return;
       endif;

       if SVPREST_chkPolizaCliente( empr
                                  : sucu
                                  : arcd
                                  : spol
                                  : rama
                                  : poli
                                  : tdoc
                                  : ndoc
                                  : peMsgs ) = *off;
          exsr logError;
          REST_writeHeader( 204
                          : *omit
                          : *omit
                          : peMsgs.peMsid
                          : peMsgs.peMsev
                          : peMsgs.peMsg1
                          : peMsgs.peMsg2 );
          exsr wrtError;
          REST_end();
          SVPREST_end();
          close *all;
          return;
       endif;

       monitor;
         peTdoc = %dec(tdoc:2:0);
        on-error;
         peTdoc = 0;
       endmon;

       monitor;
         peNdoc = %dec(ndoc:11:0);
        on-error;
         peNdoc = 0;
       endmon;

       monitor;
         peArcd = %dec(arcd:6:0);
        on-error;
         peArcd = 0;
       endmon;

       monitor;
         peSpol = %dec(spol:9:0);
        on-error;
         peSpol = 0;
       endmon;

       monitor;
         peRama = %dec(rama:2:0);
        on-error;
         peRama = 0;
       endmon;

       monitor;
         peArse = %dec(arse:2:0);
        on-error;
         peArse = 0;
       endmon;

       monitor;
         peOper = %dec(oper:7:0);
        on-error;
         peOper = 0;
       endmon;

       monitor;
         pePoli = %dec(poli:7:0);
        on-error;
         pePoli = 0;
       endmon;

       rc = COWLOG_logConAutoGestion( empr
                                    : sucu
                                    : peTdoc
                                    : peNdoc
                                    : psds.this);

       //
       // Tipo debe ser:
       // "A" = Anular
       // "R" = Arrepentimiento
       //
       if tipo <> 'A' and tipo <> 'R';
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'AAG0011'
                       : peMsgs    );
          exsr logError;
          REST_writeHeader( 204
                          : *omit
                          : *omit
                          : peMsgs.peMsid
                          : peMsgs.peMsev
                          : peMsgs.peMsg1
                          : peMsgs.peMsg2 );
          exsr wrtError;
          REST_end();
          SVPREST_end();
          close *all;
          return;
       endif;

       //
       // Debe estar vigente
       //
       k1hec0.c0empr = empr;
       k1hec0.c0sucu = sucu;
       k1hec0.c0arcd = peArcd;
       k1hec0.c0spol = peSpol;
       chain %kds(k1hec0) pahec0;
       if %found;
          if c0econ <> '0';
             SVPWS_getMsgs( '*LIBL'
                          : 'WSVMSG'
                          : 'AAG0012'
                          : peMsgs    );
             exsr logError;
             REST_writeHeader( 204
                             : *omit
                             : *omit
                             : peMsgs.peMsid
                             : peMsgs.peMsev
                             : peMsgs.peMsg1
                             : peMsgs.peMsg2 );
             exsr wrtError;
             REST_end();
             SVPREST_end();
             close *all;
             return;
          endif;
       endif;

       //
       // Debe haber sido emitda por Autogestion
       //
       if (SVPPOL_permiteAnular( empr
                               : sucu
                               : peArcd
                               : peSpol
                               : peRama
                               : peArse
                               : peOper
                               : pePoli  ) = *off and tipo = 'A')
          or
          (SVPPOL_permiteArrepentir( empr
                                   : sucu
                                   : peArcd
                                   : peSpol
                                   : peRama
                                   : peArse
                                   : peOper
                                   : pePoli ) = *off and tipo = 'R')
          or
          SVPPOL_AnulacionEnProceso( empr
                                   : sucu
                                   : peArcd
                                   : peSpol
                                   : peRama
                                   : peArse
                                   : peOper
                                   : pePoli  );
             SVPWS_getMsgs( '*LIBL'
                          : 'WSVMSG'
                          : 'AAG0013'
                          : peMsgs    );
             exsr logError;
             REST_writeHeader( 204
                             : *omit
                             : *omit
                             : peMsgs.peMsid
                             : peMsgs.peMsev
                             : peMsgs.peMsg1
                             : peMsgs.peMsg2 );
             exsr wrtError;
             REST_end();
             SVPREST_end();
             close *all;
             return;
       endif;

       k1hag4.g4empr = empr;
       k1hag4.g4sucu = sucu;
       k1hag4.g4arcd = peArcd;
       k1hag4.g4spol = peSpol;
       k1hag4.g4rama = peRama;
       k1hag4.g4arse = peArse;
       k1hag4.g4oper = peOper;
       k1hag4.g4poli = pePoli;
       k1hag4.g4endo = 0;
       setll %kds(k1hag4:9) pahag4;
       if not %equal;
          k1t915.t@empr = empr;
          k1t915.t@sucu = sucu;
          k1t915.t@tnum = peTnum;
          setgt  %kds(k1t915) set915;
          readpe %kds(k1t915) set915;
          if not %eof;
             t@nres += 1;
             update s1t915;
           else;
             t@empr = empr;
             t@sucu = sucu;
             t@tnum = peTnum;
             t@nres  = 1;
             write s1t915;
          endif;
          g4empr = empr;
          g4sucu = sucu;
          g4arcd = peArcd;
          g4spol = peSpol;
          g4rama = peRama;
          g4arse = peArse;
          g4oper = peOper;
          g4poli = pePoli;
          g4mar1 = tipo;
          g4usr1 = psds.curusr;
          g4fec1 = %dec(%date():*iso);
          g4tim1 = %dec(%time():*iso);
          // Envio a PAS
          g4mar2 = '0';
          g4usr2 = *blanks;
          g4fec2 = 0;
          g4tim2 = 0;
          // Envio a Asegurado
          g4mar3 = '0';
          g4usr3 = *blanks;
          g4fec3 = 0;
          g4tim3 = 0;
          // Envio a usuario interno
          g4mar4 = '0';
          g4usr4 = *blanks;
          g4fec4 = 0;
          g4tim4 = 0;
          g4mar5 = '0';
          g4mar6 = '0';
          g4mar7 = '0';
          g4mar8 = '0';
          g4mar9 = '0';
          g4mar0 = '0';
          @@fecn = %dec(%date():*iso);
          @@horn = %dec(%time():*iso);
          if g4mar1 = 'A';
             g4nres = 'ASAN-'
                    + %editc(t@nres:'X')
                    + '-'
                    + %editc(@@fecn:'X')
                    + %editc(@@horn:'X');
           else;
             g4nres = 'ASAR-'
                    + %editc(t@nres:'X')
                    + '-'
                    + %editc(@@fecn:'X')
                    + %editc(@@horn:'X');
          endif;
          monitor;
             g4cmot = %dec(cmot:2:0);
           on-error;
             g4cmot = 0;
          endmon;
          g4ntel = ntel;
          write p1hag4;
          exsr $interm;
          exsr logSuccess;
       endif;

       REST_writeHeader();
       REST_writeEncoding();

       REST_startArray( 'anularArrepentimiento' );

        REST_writeXmlLine( 'status'    : 'OK'   );
        REST_writeXmlLine( 'idTramite' : g4nres );

       REST_endArray( 'anularArrepentimiento' );

       return;

       begsr logError;
        LogData = %trim(url)
                + '<br>'
                + 'peErro: ' + %trim(%char(peErro))
                + '<br>'
                + 'peMsid: ' + %trim(peMsgs.peMsid)
                + '<br>'
                + 'peMsg1: ' + %trim(peMsgs.peMsg1)
                + '<br>'
                + 'peMsg2: ' + %trim(peMsgs.peMsg2)
                + '<br>';
        COWLOG_pgmLog( psds.this : LogData );
       endsr;

       begsr logSuccess;
        LogData = %trim(url)
                + '<br>'
                + 'Se ha grabado correctamente registro en PAHAG4<br>';
        COWLOG_pgmLog( psds.this : LogData );
       endsr;

       begsr wrtError;
        REST_startArray( 'anularArrepentimiento' );
         REST_writeXmlLine( 'status'    : 'ERROR');
         REST_writeXmlLine( 'idTramite' : ' '    );
        REST_endArray( 'anularArrepentimiento' );
       endsr;

       begsr $interm;
        if SPVSPO_getCadenaComercial( g4empr
                                    : g4sucu
                                    : g4arcd
                                    : g4spol
                                    : peCade
                                    : *omit  );
           for x = 1 to 8;
               if peCade(x) <> 0;
                  k1htan.anempr = g4empr;
                  k1htan.ansucu = g4sucu;
                  k1htan.annivt = x;
                  k1htan.annivc = peCade(x);
                  k1htan.anarcd = g4arcd;
                  k1htan.anspol = g4spol;
                  k1htan.anrama = g4rama;
                  k1htan.anarse = g4arse;
                  k1htan.anoper = g4oper;
                  k1htan.anpoli = g4poli;
                  k1htan.anendo = g4endo;
                  setll %kds(k1htan) pahtan;
                  if not %equal;
                     anempr = g4empr;
                     ansucu = g4sucu;
                     annivt = x;
                     annivc = peCade(x);
                     anarcd = g4arcd;
                     anspol = g4spol;
                     anrama = g4rama;
                     anarse = g4arse;
                     anoper = g4oper;
                     anpoli = g4poli;
                     anendo = g4endo;
                     annres = g4nres;
                     anmar1 = '0';
                     anmar2 = '0';
                     anmar3 = '0';
                     anmar4 = '0';
                     anmar5 = '0';
                     anmar6 = '0';
                     anmar7 = '0';
                     anmar8 = '0';
                     anmar9 = '0';
                     anmar0 = '0';
                     anusr1 = psds.curusr;
                     anfec1 = %dec(%date():*iso);
                     antim1 = %dec(%time():*iso);
                     write p1htan;
                  endif;
               endif;
           endfor;
        endif;
       endsr;

      /end-free

