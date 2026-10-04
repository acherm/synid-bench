     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
      * ************************************************************ *
      * WSRAGV: Portal de Autogestión de Asegurados.                 *
      *         Verifica si un tipo/nro de doc es asegurado.         *
      *         RM#01148 Generar servicio REST lista de pólizas      *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *26-Jul-2017            *
      * ------------------------------------------------------------ *
      * Modificaciones:                                              *
      *                                                              *
      * ************************************************************ *

      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'

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

     D peMsgs          ds                  likeds(paramMsgs)

     D psds           sds                  qualified
     D  this                         10a   overlay(psds:1)

     D @@repl          s          65535a
     D @@Tdoc          s              2  0
     D @@Ndoc          s             11  0
     D rc              s               n

     d lda             ds                  qualified dtaara(*lda)
     d   empr                         1a   overlay(lda:401)
     d   sucu                         2a   overlay(lda:402)

      /free

       *inlr = *on;

       REST_getUri( psds.this : uri );
       url = %trim(uri);

       empr = REST_getNextPart(url);
       sucu = REST_getNextPart(url);
       tdoc = REST_getNextPart(url);
       ndoc = REST_getNextPart(url);

       in lda;
       lda.empr = empr;
       lda.sucu = sucu;
       out lda;

       if SVPREST_chkCliente( empr : sucu : tdoc : ndoc : peMsgs );
          REST_writeHeader();
          REST_writeEncoding();
          REST_writeXmlLine('result' : 'OK' );
        else;
          REST_writeHeader( 204
                          : *omit
                          : *omit
                          : peMsgs.peMsid
                          : peMsgs.peMsev
                          : peMsgs.peMsg1
                          : peMsgs.peMsg2 );
       endif;

       monitor;
         @@Tdoc = %dec(tdoc:2:0);
       on-error;
         @@Tdoc = 0;
       endmon;

       monitor;
         @@Ndoc = %dec(ndoc:11:0);
       on-error;
         @@Ndoc = 0;
       endmon;

       rc = COWLOG_logConAutoGestion( empr
                                    : sucu
                                    : @@Tdoc
                                    : @@Ndoc
                                    : psds.this);

       REST_end();

       return;

      /end-free

