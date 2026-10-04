     H option(*srcstmt) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
     H alwnull(*usrctl)
      * ************************************************************ *
      * WSRPLA: QUOM Versión 2                                       *
      *         Lista planes por productor.                          *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *27-Abr-2020            *
      * ------------------------------------------------------------ *
      * Modificación:                                                *
      *  JSN 18/05/2021 - Se agrega los tags RQAP y RQRC.            *
      * ************************************************************ *
     Fset100    if   e           k disk
     Fset101    if   e           k disk

      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/svpprd_h.rpgle'

     D uri             s            512a
     D empr            s              1a
     D sucu            s              2a
     D nivt            s              1a
     D nivc            s              5a
     D nit1            s              1a
     D niv1            s              5a
     D rama            s              2a
     D arcd            s              6a
     D tipo            s              1a

     D url             s           3000a   varying
     D rc              s              1n
     D peMsgs          ds                  likeds(paramMsgs)
     D peErro          s             10i 0
     D pePlan          ds                  likeds(regPlan_t) dim(999)
     D peArcd          s              6  0
     D peRama          s              2  0
     D peFweb          s              1n
     D x               s             10i 0
     D q               s             10i 0

     D k1y100          ds                  likerec(s1t100:*key)
     D k1t101          ds                  likerec(s1t101:*key)

     D PsDs           sds                  qualified
     D  this                         10a   overlay(PsDs:1)
     D  JobName                      10a   overlay(PsDs:244)
     D  JobUser                      10a   overlay(PsDs:254)
     D  JobNbr                        6  0 overlay(PsDs:264)

      /free

       *inlr = *on;

       rc  = REST_getUri( psds.this : uri );
       if rc = *off;
         REST_writeHeader( 204
                         : *omit
                         : *omit
                         : 'RPG0001'
                         : 40
                         : 'Error al parsear URL'
                         : 'Error al parsear URL' );
         REST_end();
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
       rama = REST_getNextPart(url);
       arcd = REST_getNextPart(url);
       tipo = REST_getNextPart(url);

       if ( tipo <> 'T' and tipo <> 'W' );
          tipo = 'T';
       endif;
       peFweb = *off;
       if tipo = 'W';
          peFweb = *on;
       endif;

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
          close *all;
          return;
       endif;

       monitor;
         peRama = %dec(rama:2:0);
        on-error;
         peRama = 0;
       endmon;

       monitor;
         peArcd = %dec(arcd:6:0);
        on-error;
         peArcd = 0;
       endmon;

       REST_writeHeader();
       REST_writeEncoding();

       REST_startArray( 'planes' );

       q = SVPPRD_planesPorProductor( empr
                                    : sucu
                                    : peRama
                                    : peArcd
                                    : %dec(nivt:1:0)
                                    : %dec(nivc:5:0)
                                    : pePlan
                                    : peFweb         );

       for x = 1 to q;
        REST_startArray( 'plan' );
         REST_writeXmlLine( 'CAGR' : %char(pePlan(x).t@cagr) );
         REST_writeXmlLine( 'CTA1' : pePlan(x).t@cta1        );
         REST_writeXmlLine( 'CTA2' : pePlan(x).t@cta2        );
         REST_writeXmlLine( 'CTAR' : %char(pePlan(x).t@ctar) );
         REST_writeXmlLine( 'PRDL' : pePlan(x).t@prdl        );
         REST_writeXmlLine( 'PRDS' : pePlan(x).t@prds        );
         REST_writeXmlLine( 'XPRO' : %char(pePlan(x).t@xpro) );
         REST_writeXmlLine( 'INCO' : pePlan(x).t@1022        );
         k1t101.t@rama = peRama;
         k1t101.t@ctar = pePlan(x).t@ctar;
         k1t101.t@cta1 = pePlan(x).t@cta1;
         k1t101.t@cta2 = pePlan(x).t@cta2;
         chain %kds(k1t101:4) set101;
         if %found;
            REST_writeXmlLine( 'CTDS' : t@ctds );
          else;
            REST_writeXmlLine( 'CTDS' : *blanks        );
         endif;
         if pePlan(x).t@Mar1 = '1';
           REST_writeXmlLine( 'RQAP' : 'S' );
         else;
           REST_writeXmlLine( 'RQAP' : 'N' );
         endif;

         if pePlan(x).t@Mar2 = '1';
           REST_writeXmlLine( 'RQRC' : 'S' );
         else;
           REST_writeXmlLine( 'RQRC' : 'N' );
         endif;

         k1y100.t@rama = peRama;
         k1y100.t@xpro = pePlan(x).t@xpro;
         k1y100.t@mone = '01';
         chain %kds ( k1y100 : 3 ) set100;
         select;
           when not %found ( set100 );
             REST_writeXmlLine( 'TIDP' : 'E' );
           when t@prem = *Zeros;
             REST_writeXmlLine( 'TIDP' : 'A' );
           other;
             REST_writeXmlLine( 'TIDP' : 'C' );
         endsl;

        REST_endArray( 'plan' );
       endfor;

       REST_endArray( 'planes' );

       return;
