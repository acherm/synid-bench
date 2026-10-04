     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
      * ************************************************************ *
      * WSRPQ1: QUOM Versión 2                                       *
      *         Preliquidación - Nueva Preliquidación                *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *17-Jul-2017            *
      * ------------------------------------------------------------ *
      * SGF 18/07/2020: Agrego parametro para saber si incluye o no  *
      *                 debito automatico.                           *
      *                                                              *
      * ************************************************************ *

      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'

     D PLQWEB1         pr                  ExtPgm('PLQWEB1')
     D   peBase                            likeds(paramBase) const
     D   peNrpl                       7  0
     D   peFhas                       8  0
     D   peDaut                       1a   const
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D uri             s            512a
     D empr            s              1a
     D sucu            s              2a
     D nivt            s              1a
     D nivc            s              5a
     D nit1            s              1a
     D niv1            s              5a
     D daut            s              1a
     D url             s           3000a   varying
     D rc              s              1n
     D peNrpl          s              7  0
     D peFhas          s              8  0
     D peDaut          s              1a
     D peErro          s             10i 0

     D peBase          ds                  likeds(paramBase)
     D peMsgs          ds                  likeds(paramMsgs)

     D PsDs           sds                  qualified
     D  this                         10a   overlay(PsDs:1)

      /free

       *inlr = *on;

       rc  = REST_getUri( psds.this : uri );
       if rc = *off;
          return;
       endif;
       url = %trim(uri);

       // ------------------------------------------
       // Obtener los parámetros de la URL
       // ------------------------------------------
       empr = REST_getNextPart(url);
       sucu = REST_getNextPart(url);
       nivt = REST_getNextPart(url);
       nivc = REST_getNextPart(url);
       nit1 = REST_getNextPart(url);
       niv1 = REST_getNextPart(url);
       daut = REST_getNextPart(url);

       if SVPREST_chkBase(empr:sucu:nivt:nivc:nit1:niv1:peMsgs) = *off;
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : peMsgs.peMsid
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          SVPREST_end();
          return;
       endif;

       clear peBase;
       clear peMsgs;
       peErro  = 0;

       peBase.peEmpr = empr;
       peBase.peSucu = sucu;
       peBase.peNivt = %dec(nivt:1:0);
       peBase.peNivc = %dec(nivc:5:0);
       peBase.peNit1 = %dec(nit1:1:0);
       peBase.peNiv1 = %dec(niv1:5:0);

       peDaut = daut;
       if peDaut <> 'S' and peDaut <> 'N';
          peDaut = 'N';
       endif;

       PLQWEB1( peBase
              : peNrpl
              : peFhas
              : peDaut
              : peErro
              : peMsgs );

       if peErro = -1;
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : peMsgs.peMsid
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
           REST_end();
           return;
       endif;

       REST_writeHeader();
       REST_writeEncoding();

       REST_startArray( 'preliquidacion' );
           REST_writeXmlLine( 'numero'     : %trim(%char(peNrpl)));
           REST_writeXmlLine( 'fechaHasta' : SVPREST_editFecha(peFhas));
       REST_endArray( 'preliquidacion' );

       REST_end();

       return;

