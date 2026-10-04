     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
     H alwnull(*usrctl)
      * ************************************************************ *
      * WSPTRE : Terminar Reclamo                                    *
      * ------------------------------------------------------------ *
      * Nestor Nelson                        18/11/2021              *
      * ------------------------------------------------------------ *
      * Modificación:                                                *
      *                                                              *
      * ************************************************************ *

      /copy './qcpybooks/svpemp_h.rpgle'
      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/svprvs_h.rpgle'
      /copy './qcpybooks/sinest_h.rpgle'
      /copy './qcpybooks/svpsin_h.rpgle'
      /copy './qcpybooks/svpsi1_h.rpgle'
      /copy './qcpybooks/svpsuc_h.rpgle'
      /copy './qcpybooks/svptab_h.rpgle'

     D request         ds                  likeds(wsptre_t)
     D buffer          s           5000a
     D options         s            100a
     D rc1             s             10i 0
     D penmro          s              7p 0
     D @@repl          s          65535a
     D path            s            256a   varying
     D pevalu          s           1024a
     D peMsgs          ds                  likeds(paramMsgs)
     d peMsgf          s              6a
     d peIdms          s              7a

     d WSPVST          pr                  ExtPgm('WSPVST')
     d  peEmpr                        1a   const
     d  peSucu                        2a   const
     d  peRama                        2  0 const
     d  peSini                        7  0 const
     d  peNops                        7  0 const
     d  peMsgf                        6a
     d  peIdms                        7a

      /free

       *inlr = *on;

       // Inicio

        options = 'path=terminarReclamo +
                   allowmissing=yes allowextra=yes case=any';

        REST_getEnvVar('REQUEST_METHOD':peValu);

        if %trim(peValu) <> 'POST';
           REST_writeHeader( 405
                           : *omit
                           : *omit
                           : *omit
                           : *omit
                           : *omit  );
           REST_end();
           SVPREST_end();
           return;
        endif;

       // Lectura y Parseo

          if REST_getEnvVar('WSPTRE_BODY' : peValu );
             buffer = peValu;
             Qp0zDltEnv('WSPTRE_BODY');
           else;
          rc1= REST_readStdInput( %addr(buffer): %len(buffer) );
          endif;

       // BUFFER =  '<terminarReclamo>' +
       //           '<empresa>A</empresa>' +
       //           '<sucursal>CA</sucursal>'+
       //           '<rama>3</rama>'+
       //           '<siniestro>670067</siniestro>'+
       //           '<nroOperStro>424622</nroOperStro>' +
       //           '<reclamo>1</reclamo>' +
       //           '</terminarReclamo>' ;



        monitor;
          xml-into request %xml(buffer : options);
        on-error;
          @@repl = 'wsptre_t';
          SVPWS_getMsgs( '*LIBL'
                      : 'WSVMSG'
                       : 'RPG0001'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          REST_writeHeader( 400
                          : *omit
                          : *omit
                          : 'RPG0001'
                          : peMsgs.peMsev
                          : peMsgs.peMsg1
                          : peMsgs.peMsg2 );
          REST_end();
          SVPREST_end();
          return;
        endmon;

       // -------------------------------------------------------
       // Control sobre los parámetros de entrada enviados
       // -------------------------------------------------------

           wspvst( request.empresa
                 : request.sucursal
                 : %dec(request.rama:2:0)
                 : %dec(request.siniestro:7:0)
                 : %dec(request.nroOperStro:7:0)
                 : peMsgf
                 : peIdms) ;

           if peMsgf <> *blanks ;

             rc1 = SVPWS_getMsgs( '*LIBL'
                              : peMsgf
                              : peIdms
                              : peMsgs
                              : *omit
                              : *omit );

             REST_writeHeader( 400
                             : *omit
                             : *omit
                             : peIdms
                             : peMsgs.peMsev
                             : peMsgs.peMsg1
                             : peMsgs.peMsg2 );

             REST_end();

             SVPREST_end();

             return;

           endif;

       // --------------------------------------------------------------
       // Controlo que las no tenga reservas activas sobre ese reclamo
       // --------------------------------------------------------------

       //if SVPSIN_getRvaXReclamo( request.empresa
       //                        : request.sucursal
       //                        : request.rama
       //                        : request.siniestro
       //                        : request.nroOperStro
       //                        : request.reclamo ) <> *zeros ;
       //
       //    rc1 = SVPWS_getMsgs( '*LIBL'
       //                       : 'WSVMSG'
       //                       : 'SIN1006'
       //                       : peMsgs
       //                       : *omit
       //                       : *omit );
       //
       //    REST_writeHeader( 400
       //                    : *omit
       //                    : *omit
       //                    : 'SIN1006'
       //                    : peMsgs.peMsev
       //                    : peMsgs.peMsg1
          //                 : peMsgs.peMsg2 );
          //
          // REST_end();
          //
          // SVPREST_end();
          //
          // return;
       //endif;

       // --------------------------------------------------------------
       // Llamo a programa que controla que no tenga siniestro en juicio
       // --------------------------------------------------------------

spv    if SVPSIN_chkStroEnJuicio( request.empresa
spv                             : request.sucursal
spv                             : request.rama
spv                             : request.siniestro
spv                             : request.nroOperStro ) = *on;

          SVPWS_getMsgs( '*LIBL'
                      : 'WSVMSG'
                       : 'SIN1005'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );

             REST_writeHeader( 400
                             : *omit
                             : *omit
                             : 'SIN1005'
                             : peMsgs.peMsev
                             : peMsgs.peMsg1
                             : peMsgs.peMsg2 );
             REST_end();

             SVPREST_end();

             return;
       endif;

       // --------------------------------------------------------------
       // Llamo a programa que controle que el siniestro este habilitado
       // --------------------------------------------------------------

       if SVPSIN_chkSinModificable( request.empresa
                                  : request.sucursal
                                  : request.rama
                                  : request.nroOperStro ) = *on;


       // --------------------------------------------------------------
       // Llamo a programa que Termine el Reclamo
       // --------------------------------------------------------------

         if  SVPSIN_terminarBenefXReclamo( request.empresa
                                         : request.sucursal
                                         : request.rama
                                         : request.siniestro
                                         : request.nroOperStro
                                         : request.reclamo ) = *on ;

         endif;
       endif;



       REST_writeHeader( 201
                       : *omit
                       : *omit
                       : *omit
                       : *omit
                       : *omit
                       : *omit );


       return;
