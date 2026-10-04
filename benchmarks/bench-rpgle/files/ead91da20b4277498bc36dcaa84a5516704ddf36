     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
     H alwnull(*usrctl)
      * ************************************************************ *
      * WSRPAN: QUOM Versión 2                                       *
      *         Lista pólizs anteriores.                             *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *06-May-2022            *
      * ------------------------------------------------------------ *
      *                                                              *
      * ************************************************************ *
     Fpahec0    if   e           k disk
     Fpahed0    if   e           k disk
     Fpahec1    if   e           k disk

      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/spvspo_h.rpgle'
      /copy './qcpybooks/svpint_h.rpgle'

     D uri             s            512a
     D url             s           3000a   varying
     D empr            s              1a
     D sucu            s              2a
     D nivt            s              1a
     D nivc            s              5a
     D nit1            s              1a
     D niv1            s              5a
     D arcd            s              6a
     D spol            s              9a
     D rama            s              2a
     D arse            s              2a
     D oper            s              7a
     D poli            s              7a

     D peArcd          s              6  0
     D peSpol          s              9  0
     D @@repl          s          65535a
     D rc              s              1n
     D peErro          s             10i 0
     D x               s             10i 0
     D fecha           s              8  0
     D file            s            256a
     D cab_actual      s              5  0
     D cab_anterior    s              5  0
     D peCade          s              5  0 dim(9)

     D peMsgs          ds                  likeds(paramMsgs)
     D peBase          ds                  likeds(paramBase)
     D p2Base          ds                  likeds(paramBase)

     D k1hec0          ds                  likerec(p1hec0:*key)
     D k1hed0          ds                  likerec(p1hed0:*key)
     D k1hec1          ds                  likerec(p1hec1:*key)

     D anteriores      ds                  qualified dim(99)
     D  arcd                          6  0
     D  spol                          9  0

     D PsDs           sds                  qualified
     D  this                         10a   overlay(PsDs:1)

      /free

       *inlr = *on;

       if REST_getUri( psds.this : uri ) = *off;
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
       arcd = REST_getNextPart(url);
       spol = REST_getNextPart(url);
       rama = REST_getNextPart(url);
       arse = REST_getNextPart(url);
       oper = REST_getNextPart(url);
       poli = REST_getNextPart(url);

       if SVPREST_chkBase(empr:sucu:nivt:nivc:nit1:niv1:peMsgs) = *off;
          REST_writeHeader( 400
                          : *omit
                          : *omit
                          : peMsgs.peMsid
                          : peMsgs.peMsev
                          : peMsgs.peMsg1
                          : peMsgs.peMsg2 );
          REST_end();
          SVPREST_end();
          close *all;
          return;
       endif;

       peBase.peEmpr = empr;
       peBase.peSucu = sucu;
       peBase.peNivt = %dec(nivt:1:0);
       peBase.peNivc = %dec(nivc:5:0);
       peBase.peNit1 = %dec(nit1:1:0);
       peBase.peNiv1 = %dec(niv1:5:0);

       COWLOG_logcon( psds.this : peBase );

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

       //
       // Busco el cabecera, ya que sólo voy a dejar que se puedan
       // bajar los endosos donde el cabecera coincida
       //
       cab_actual = 0;
       if not SVPINT_getCadena( peBase.peEmpr
                              : peBase.peSucu
                              : peBase.peNivt
                              : peBase.peNivc
                              : peCade        );
          cab_actual = peCade(9);
       endif;

       exsr $anteriores;

       k1hed0.d0empr = empr;
       k1hed0.d0sucu = sucu;

       REST_writeHeader();
       REST_writeEncoding();

       REST_startArray( 'polizasAnteriores' );

       for x = 1 to %elem(anteriores);
           if anteriores(x).spol <> 0;
              k1hed0.d0arcd = anteriores(x).arcd;
              k1hed0.d0spol = anteriores(x).spol;
              setgt  %kds(k1hed0:4) pahed0;
              readpe %kds(k1hed0:4) pahed0;
              dow not %eof;
                  k1hec1.c1empr = d0empr;
                  k1hec1.c1sucu = d0sucu;
                  k1hec1.c1arcd = d0arcd;
                  k1hec1.c1spol = d0spol;
                  k1hec1.c1sspo = d0sspo;
                  chain %kds(k1hec1) pahec1;
                  if %found;
                     exsr $response;
                  endif;
               readpe %kds(k1hed0:4) pahed0;
              enddo;
           endif;
       endfor;

       REST_endArray( 'polizasAnteriores');

       close *all;

       return;

       begsr $anteriores;
        clear anteriores;
        x = 0;
        k1hec0.c0empr = empr;
        k1hec0.c0sucu = sucu;
        k1hec0.c0arcd = peArcd;
        k1hec0.c0spol = peSpol;
        dou c0spoa <= 0 or c0spoa = 999999999;
            chain %kds(k1hec0:4) pahec0;
            if not %found;
               leavesr;
            endif;
            if c0spoa <= 0 or c0spoa = 999999999;
               leavesr;
            endif;
            x += 1;
            anteriores(x).arcd = c0arcd;
            anteriores(x).spol = c0spoa;
            k1hec0.c0spol = c0spoa;
        enddo;
       endsr;

       begsr $response;
        exsr $control_base;
        if (cab_actual   =  cab_anterior) and
           (cab_actual   <> 0           ) and
           (cab_anterior <> 0           ) and
        REST_startArray('polizaAnterior');
         REST_writeXmlLine( 'rama'             : %char(d0rama) );
         REST_writeXmlLine( 'poliza'           : %char(d0poli) );
         REST_writeXmlLine( 'suplPoliza'       : %char(d0suop) );
         REST_writeXmlLine( 'articulo'         : %char(d0arcd) );
         REST_writeXmlLine( 'suplSuperpoliza'  : %char(d0sspo) );
         REST_writeXmlLine( 'tipo'             : 'Versión Completa' );
         file = 'POLIZA_'
              + %editc(d0arcd:'X')
              + '_'
              + %editc(d0spol:'X')
              + '_'
              + %editc(d0sspo:'X')
              + '_'
              + %editc(d0rama:'X')
              + '_'
              + %editc(d0poli:'X')
              + '_'
              + %editc(d0suop:'X')
              + '.pdf';
         REST_writeXmlLine( 'documento'        : %trim(file) );
         fecha = (d0fioa * 10000)
               + (d0fiom *   100)
               +  d0fiod;
         REST_writeXmlLine( 'vigenciaDesde'
                          : SVPREST_editFecha( fecha )       );
         fecha = (d0fhfa * 10000)
               + (d0fhfm *   100)
               +  d0fhfd;
         REST_writeXmlLine( 'vigenciaHasta'
                          : SVPREST_editFecha( fecha )       );
         REST_writeXmlLine( 'fechaEmision'
                          : SVPREST_editFecha( SPVSPO_getFecEmi( d0empr
                                                               : d0sucu
                                                               : d0arcd
                                                               : d0spol)));
        REST_endArray('polizaAnterior');
        endif;
       endsr;

       begsr $control_base;
        cab_anterior = 0;
        if not SVPINT_getCadena( c1empr
                               : c1sucu
                               : c1nivt
                               : c1nivc
                               : peCade  );
           cab_anterior = peCade(9);
        endif;
       endsr;

      /end-free
