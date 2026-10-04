
     H option(*srcstmt:*noshowcpy:*nodebugio) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
     H alwnull(*usrctl)

      * ************************************************************ *
      * WSRCVA: Mobile.                                              *
      *         AUTOS - Lista de Certificados Varios.                *
      * ------------------------------------------------------------ *
      * Luis R. Gómez                        *22-Ene-2018            *
      * ------------------------------------------------------------ *
      * Modificiones:                                                *
      * SGF 08/08/2019: Fecha Hasta en Mercosur es igual a tarjeta.  *
      * SGF 23/08/2019: Vuelvo atrás SGF 08/08/2019.                 *
      * SGF 19/07/2021: Redmine 10249. Definido por Juan Beraldi: si *
      *                 un vehículo está de baja, se muestra pero la *
      *                 fecha hasta es la fecha de baja del auto y no*
      *                 la de póliza.                                *
      *                                                              *
      * ************************************************************ *

     Fpahet993  if   e           k disk    rename( p1het9 : p1het993 )
     Fpahet9    if   e           k disk
     Fpahec0    if   e           k disk

      * Parametros de entrada ---------------------------------- *
     D moto            s             25a
     D poli            s              7a
     D ncel            s             20a
     D mail            s             50a
     D fnac            s             10a
     D tusr            s             10a
     D nomb            s             40a
     D empr            s              1a
     D sucu            s              2a
     D arcd            s              6a
     D spol            s              9a
     D arse            s              2a
     D rama            s              2a
     D oper            s              7a

      * Claves -------------------------------------------------- *
     D k1y993          ds                  likerec( p1het993 : *key )
     D k1yec0          ds                  likerec( p1hec0   : *key )
     D k1yet9          ds                  likerec( p1het9   : *key )

      * Variables ----------------------------------------------- *
     D uri             s            512a
     D url             s           3000a   varying
     D reg             ds                  likeds(regex_t)
     D match           ds                  likeds(regmatch_t)
     D wrepl           s          65535a
     D pattern         s             25a   varying
     D regerro         s          65535a
     D x               s             10i 0
     D @@valsys        s            512
     D @@cval          s             10a
     D @@empr          s              1
     D @@sucu          s              2
     D @@rama          s              2  0
     D @@DsMob         ds                  likeds( DsPahmob_t )
     D @@nomb          s             40a
     D @@fnac          s              8a
     D @1fnac          s              8  0
     D @@tusr          s             10
     D @@fhoy          s              8  0

     D                 ds
     D @@femi                 01     08  0
     D @@a                    01     04  0
     D @@m                    05     06  0
     D @@d                    07     08  0

     D tmpfec          s             10d
     D pefpgm          s              3
     D @@MS            s            512
     D @@nivt          s              1  0
     D @@nivc          s              5  0
     D @@DsTl          ds                  likeds ( DsTelPublic_t ) dim( 100 )
     D @@DsTlC         s             10i 0
     D @@mail          ds                  likeds(Mailaddr_t) dim(100)
     D @@mailC         s             10i 0

      * Banderas...
     D peVig2          s               n   inz('1')
     D fnac_valida     s               n   inz('1')
     D estado          s               n
     D procesa         s               n   inz('0')
     D rc              s               n
     D primera         s               n   inz('1')

      * Datos Output...
     D EmpAse          s             50
     D Pais            s             50
     D NomAse          s             50
     D Poliza          s             50
     D NumCer          s             50
     D Domici          s             50
     D Fvigen          s             50
     D Marca           s             15
     D Modelo          s             15
     D Submodelo       s             10
     D Anio            s             50
     D Matricula       s             50
     D Chasis          s             50
     D Paises          s             50
     D Ciudad          s             50
     D Fecha           s             50
     D Tipo            s             50
     D Fdesd           s             50
     D Fhast           s             50
     D Asiste          s             50
     D Interm          s             50
     D DesTel          s             50
     D DesMail         s             50
     D @@fbaj          s              8  0

      * Constantes  --------------------------------------------- *
     D min             c                   const('abcdefghijklmnñopqrstuvwxyz-
     D                                     áéíóúàèìòùäëïöü')
     D may             c                   const('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ-
     D                                     ÁÉÍÓÚÀÈÌÒÙÄËÏÖÜ')
      * Estructuras --------------------------------------------- *
     D peMsgs          ds                  likeds( paramMsgs )
     D peBase          ds                  likeds( paramBase )
     D meses           s             20a   dim(12) ctdata perrcd(1)

      * Vectores ------------------------------------------------ *
     D @@cade          s              5  0 dim(9)

      * Informacion de Sistema ---------------------------------- *
     D psds           sds                  qualified
     D  this                         10a   overlay( psds : 1 )

     D Local           ds                  dtaara(*lda) qualified
     D  empr                          1a   overlay(Local:401)
     D  sucu                          2a   overlay(Local:*next)

      * Procedimientos ------------------------------------------ *

     DPAR310X3         pr                  extpgm('PAR310X3')
     D                                1a   const
     D                                4  0
     D                                2  0
     D                                2  0

     DSPVIG3           pr                  extpgm('SPVIG3')
     D  t9arcd                        6  0
     D  t9spol                        9  0
     D  t9rama                        2  0
     D  t9arse                        2  0
     D  t9oper                        7  0
     D  t9poco                        4  0
     D  t9fvig                        8  0
     D  t9femi                        8  0
     D  estado                        1n
     D  t9sspo                        3  0
     D  t9suop                        3  0
     D  pefpgm                        3
     D  peVig2                        1n   options(*nopass) const

     D Poliza_Vigente...
     D                 pr              n
     D getDatosFormateados...
     D                 pr
      // Log de llamadas...
     D WSLOG           pr                  extpgm('WSLOG')
     D   MS                         512

      // Procedimiento para debug...
     D sleep           pr            10u 0 extproc('sleep')
     D  secs                         10u 0 value

      * Copy's -------------------------------------------------- *
      /copy './qcpybooks/svpmob_h.rpgle'
      /copy './qcpybooks/svpemp_h.rpgle'
      /copy './qcpybooks/svpdes_h.rpgle'
      /copy './qcpybooks/svpdaf_h.rpgle'
      /copy './qcpybooks/svpint_h.rpgle'

      /copy './qcpybooks/regex_h.rpgle'
      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/svpws_h.rpgle'
      /copy './qcpybooks/svpvls_h.rpgle'
      /copy './qcpybooks/spvveh_h.rpgle'
      /copy './qcpybooks/mail_h.rpgle'
      /copy './qcpybooks/spvveh_h.rpgle'
      /copy './qcpybooks/spvspo_h.rpgle'
      /copy './qcpybooks/svpase_h.rpgle'
      /copy './qcpybooks/svpvls_h.rpgle'

      /free
        *inlr = *on;

        rc  = REST_getUri( psds.this : uri );
        if rc = *off;
           return;
        endif;
        url = %trim( uri );

        // ------------------------------------------
        // Obtener los parámetros de la URL
        // ------------------------------------------
        moto = REST_getNextPart(url);
        poli = REST_getNextPart(url);
        ncel = REST_getNextPart(url);
        mail = REST_getNextPart(url);
        fnac = REST_getNextPart(url);
        tusr = REST_getNextPart(url);
        nomb = REST_getNextPart(url);
        empr = REST_getNextPart(url);
        sucu = REST_getNextPart(url);
        arcd = REST_getNextPart(url);
        spol = REST_getNextPart(url);
        rama = REST_getNextPart(url);
        arse = REST_getNextPart(url);
        oper = REST_getNextPart(url);
        nomb = %scanrpl( '|' : '/' : nomb );

        @@nomb = %xlate( min : may : nomb );
        @@tusr = %xlate( min : may : tusr );
        @@fnac = %subst(fnac:1:4)
               + %subst(fnac:6:2)
               + %subst(fnac:9:2);
        if @@fnac <> *blanks;
          monitor;
            @1fnac = %dec(@@fnac:8:0);
            tmpfec = %date(@1fnac:*iso);
          on-error;
            fnac_valida = *off;
            @1fnac = 0;
          endmon;
        endif;

        @@empr = %xlate( min : may : empr );
        @@sucu = %xlate( min : may : sucu );

        // Datos de Auditoria...
        clear @@DsMob;
        @@DsMob.obempr = @@empr;
        @@DsMob.obsucu = @@sucu;
        @@DsMob.obpoli = poli;
        @@DsMob.obmoto = moto;
        @@DsMob.obncel = ncel;
        @@DsMob.obmail = mail;
        @@DsMob.obfnac = @1fnac;
        @@DsMob.obtusr = tusr;
        @@DsMob.obnomb = @@nomb;
        @@DsMob.obfech = %char(%timestamp());
        @@DsMob.obresu = '0';
        @@DsMob.obempr = empr;
        @@DsMob.obsucu = sucu;

        // Valida Parámetros de entrada...

        // Motor...
        if not SPVVEH_CheckMotor ( moto );

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0039'
                        : peMsgs );

           // Auditoria...
           @@DsMob.obresu = '1';
           @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
           SVPMOB_setAuditoria( @@DsMob );

           // Respuesta Rest - Cabecera...
           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'MOB0001'
                        :  peMsgs );

           rc = REST_writeHeader( 204
                                : *omit
                                : *omit
                                : peMsgs.peMsid
                                : peMsgs.peMsev
                                : peMsgs.peMsg1
                                : peMsgs.peMsg2 );

           REST_end();
           close *all;
           return;
        endif;

        if %checkr(' ':moto) <= 3;
           %subst(wrepl:1:6) = 'Motor';
           %subst(wrepl:7:1) = '4';
           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0135'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl)) );

           // Auditoria...
           @@DsMob.obresu = '1';
           @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
           SVPMOB_setAuditoria( @@DsMob );

           // Respuesta Rest - Cabecera...
           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'MOB0001'
                        :  peMsgs );

           rc = REST_writeHeader( 204
                                : *omit
                                : *omit
                                : peMsgs.peMsid
                                : peMsgs.peMsev
                                : peMsgs.peMsg1
                                : peMsgs.peMsg2 );

           REST_end();
           close *all;
           return;
         endif;

         if %check( '0123456789' : %subst(%trim(moto): 1: 1)) <> 0 and
            %check( min          : %subst(%trim(moto): 1: 1)) <> 0 and
            %checkr( may          : %subst(%trim(moto): 1: 1))<> 0;
            x = 1;
         endif;

         if x <> *zeros;
            %subst(wrepl:1:6) = 'Motor';
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'COW0136'
                         : peMsgs
                         : %trim(wrepl)
                         : %len(%trim(wrepl)) );
            // Auditoria...
            @@DsMob.obresu = '1';
            @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
            SVPMOB_setAuditoria( @@DsMob );

            // Respuesta Rest - Cabecera...
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'MOB0001'
                         :  peMsgs );

            rc = REST_writeHeader( 204
                                 : *omit
                                 : *omit
                                 : peMsgs.peMsid
                                 : peMsgs.peMsev
                                 : peMsgs.peMsg1
                                 : peMsgs.peMsg2 );

            REST_end();
            close *all;
            return;

         endif;

         // Poliza...
         if %check( '0123456789' : %trim(poli) ) <> 0;
            %subst(wrepl:1:2) = %char(@@rama) ;
            %subst(wrepl:3:7) = poli;
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'POL0009'
                         : peMsgs
                         : %trim(wrepl)
                         : %len(%trim(wrepl)) );
            // Auditoria...
            @@DsMob.obresu = '1';
            @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
            SVPMOB_setAuditoria( @@DsMob );

            // Respuesta Rest - Cabecera...
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'MOB0001'
                         :  peMsgs );

            rc = REST_writeHeader( 204
                                 : *omit
                                 : *omit
                                 : peMsgs.peMsid
                                 : peMsgs.peMsev
                                 : peMsgs.peMsg1
                                 : peMsgs.peMsg2 );

            REST_end();
            close *all;
            return;
         endif;

         // Número de Celular...
         if ncel = *blank or %trim(ncel) = *all'0';
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'MOB0002'
                         : peMsgs
                         : %trim(wrepl)
                         : %len(%trim(wrepl)) );
            // Auditoria...
            @@DsMob.obresu = '1';
            @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
            SVPMOB_setAuditoria( @@DsMob );

            // Respuesta Rest - Cabecera...
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'MOB0001'
                         :  peMsgs );

            rc = REST_writeHeader( 204
                                 : *omit
                                 : *omit
                                 : peMsgs.peMsid
                                 : peMsgs.peMsev
                                 : peMsgs.peMsg1
                                 : peMsgs.peMsg2 );

            REST_end();
            close *all;
            return;
         endif;

         // Mail...
       //if mail <> *blanks;
         //if MAIL_isValid( %trim(mail) ) = *OFF;
         //
         // SVPWS_getMsgs( '*LIBL'
         //              : 'WSVMSG'
         //              : 'MOB0006'
         //              : peMsgs
         //              : %trim(wrepl)
         //              : %len(%trim(wrepl)) );
         // // Auditoria...
         // @@DsMob.obresu = '1';
         // @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
         // SVPMOB_setAuditoria( @@DsMob );
         //
         // // Respuesta Rest - Cabecera...
         // // SVPWS_getMsgs( '*LIBL'
         // //           : 'WSVMSG'
         // //           : 'MOB0001'
         // //           :  peMsgs );
         //
         // rc = REST_writeHeader( 204
         //                      : *omit
         //                      : *omit
         //                      : peMsgs.peMsid
         //                      : peMsgs.peMsev
         //                      : peMsgs.peMsg1
         //                      : peMsgs.peMsg2 );
         // REST_end();
         // close *all;
         // return;
         //endif;
       //endif;

         // Tipo de usuario...
         if %trim(@@tusr) <> 'PRINCIPAL' AND
            %trim(@@tusr) <> 'SECUNDARIO';
            wrepl = 'Debe ser Principal o Secundario';
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'MOB0003'
                         : peMsgs
                         : %trim(wrepl)
                         : %len(%trim(wrepl)) );
            // Auditoria...
            @@DsMob.obresu = '1';
            @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
            SVPMOB_setAuditoria( @@DsMob );

            // Respuesta Rest - Cabecera...
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'MOB0001'
                         :  peMsgs );

            rc = REST_writeHeader( 204
                                 : *omit
                                 : *omit
                                 : peMsgs.peMsid
                                 : peMsgs.peMsev
                                 : peMsgs.peMsg1
                                 : peMsgs.peMsg2 );
            REST_end();
            close *all;
            return;
        endif;

        // Si Usuario es Secundario debe enviar nombre y apellido...
        if %trim(@@tusr) = 'SECUNDARIO' and
                 nomb  = *blanks;

          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'MOB0004'
                       : peMsgs
                       : %trim(wrepl)
                       : %len(%trim(wrepl)) );
          // Auditoria...
          @@DsMob.obresu = '1';
          @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
          SVPMOB_setAuditoria( @@DsMob );

          // Respuesta Rest - Cabecera...
          //SVPWS_getMsgs( '*LIBL'
          //             : 'WSVMSG'
          //             : 'MOB0001'
          //             :  peMsgs );

          rc = REST_writeHeader( 204
                               : *omit
                               : *omit
                               : peMsgs.peMsid
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
        endif;

        // Fecha de nacimiento...
        if not fnac_valida;

          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'MOB0005'
                       : peMsgs
                       : %trim(wrepl)
                       : %len(%trim(wrepl)) );
          // Auditoria...
          @@DsMob.obresu = '1';
          @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
          SVPMOB_setAuditoria( @@DsMob );

          // Respuesta Rest - Cabecera...
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'MOB0001'
                       :  peMsgs );

          rc = REST_writeHeader( 204
                               : *omit
                               : *omit
                               : peMsgs.peMsid
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
        endif;

       // PAR310X3( empr: @@a : @@m : @@d );
       // @@fhoy = (@@a * 10000) + (@@m * 100) + @@d;

        // Busca Polizas Vigentes...

        k1y993.t9empr = @@empr;
        k1y993.t9sucu = @@sucu;
        k1y993.t9moto = moto;
        k1y993.t9poli = %dec(poli:7:0);
        chain %kds( k1y993 : 4 ) pahet993;
        if not %found( pahet993 );
          %subst(wrepl:1:7) = poli;
          %subst(wrepl:8)   = %trim(moto);

          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'POL0013'
                       : peMsgs
                       : %trim(wrepl)
                       : %len(%trim(wrepl)) );
          // Auditoria...
          @@DsMob.obresu = '1';
          @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
          SVPMOB_setAuditoria( @@DsMob );

          // Respuesta Rest - Cabecera...
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'MOB0001'
                         :  peMsgs );

          rc = REST_writeHeader( 204
                               : *omit
                               : *omit
                               : peMsgs.peMsid
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
        endif;

        // Poliza Vigente...
        procesa = *on;

        if not procesa;
          wrepl = %trim(moto);
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'MOB0007'
                       : peMsgs
                       : %trim(wrepl)
                       : %len(%trim(wrepl)) );
          // Auditoria...
          @@DsMob.obresu = '1';
          @@DsMob.obobse = '(' + peMsgs.peMsid + ') ' + peMsgs.peMsg1;
          SVPMOB_setAuditoria( @@DsMob );

          // Respuesta Rest - Cabecera...
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'MOB0001'
                       :  peMsgs );

          rc = REST_writeHeader( 204
                               : *omit
                               : *omit
                               : peMsgs.peMsid
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );

          REST_end();
          close *all;
          return;

        endif;

        // Si llegamos a este punto...Estamos bien...

        k1yet9.t9empr = empr;
        k1yet9.t9sucu = sucu;
        k1yet9.t9arcd = %dec(arcd:6:0);
        k1yet9.t9spol = %dec(spol:9:0);
        k1yet9.t9rama = %dec(rama:2:0);
        k1yet9.t9arse = %dec(arse:2:0);
        k1yet9.t9oper = %dec(oper:7:0);
        setll %kds( k1yet9 : 7 ) pahet9;
        reade %kds( k1yet9 : 7 ) pahet9;
        dow not %eof( pahet9 );
           getDatosFormateados();
           REST_writeXmlLine( 'Certificados' : '*BEG' );
             REST_writeXmlLine( 'DatosMercosur'     : '*BEG' );
               REST_writeXmlLine( 'Aseguradora'     : %trim(EmpAse));
               REST_writeXmlLine( 'Pais'            : %trim(Pais  ));
               REST_writeXmlLine( 'Asegurado'       : %trim(NomAse));
               REST_writeXmlLine( 'PolizaNro'       : %trim(Poliza));
               REST_writeXmlLine( 'CertificadoNro'  : %trim(NumCer));
               REST_writeXmlLine( 'Domicilio'       : %trim(Domici));
               REST_writeXmlLine( 'Vigencia'        : %trim(Fvigen));
               REST_writeXmlLine( 'Marca'           : %trim(marca ));
               REST_writeXmlLine( 'Modelo'          : %trim(modelo));
               REST_writeXmlLine( 'Anio'            : %trim(Anio  ));
               REST_writeXmlLine( 'Matricula'       : %trim(t9nmat));
               REST_writeXmlLine( 'Motor'           : %trim(t9moto));
               REST_writeXmlLine( 'Chasis'          : %trim(t9chas));
               REST_writeXmlLine( 'Paises'          : %trim(Paises));
               REST_writeXmlLine( 'Ciudad'          : %trim(Ciudad));
               REST_writeXmlLine( 'Fecha'           : %trim(Fecha ));
             REST_writeXmlLine( 'DatosMercosur' : '*END' );

             REST_writeXmlLine( 'TarjetaCirculacion' : '*BEG' );
               REST_writeXmlLine( 'Asegurado'       : %trim(NomAse));
               REST_writeXmlLine( 'PolizaNro'       : %trim(Poliza));
               REST_writeXmlLine( 'Tipo'            : %trim(Tipo  ));
               REST_writeXmlLine( 'Desde'           : %trim(Fdesd ));
               REST_writeXmlLine( 'Hasta'           : %trim(Fhast ));
               REST_writeXmlLine( 'Anio'            : %trim(Anio  ));
               REST_writeXmlLine( 'Asistencia'      : %trim(Asiste));
               REST_writeXmlLine( 'Marca'           : %trim(Marca ));
               REST_writeXmlLine( 'Carroceria'      : %trim(t9chas));
               REST_writeXmlLine( 'Motor'           : %trim(t9moto));
             REST_writeXmlLine( 'TarjetaCirculacion' : '*END' );

           REST_writeXmlLine( 'Certificados' : '*END' );

         reade %kds( k1yet9 : 7 ) pahet9;
        enddo;

        SVPMOB_setAuditoria( @@DsMob );

        rc = SVPMOB_setDataq ( @@empr : @@sucu : @@DsMob.obfech );

        REST_end();
        close *all;

        return;

      /end-free

      * ------------------------------------------------------- *
      * getDatosFormateados(): Retorna datos formateados        *
      *                                                         *
      * ------------------------------------------------------- *
     P getDatosFormateados...
     P                 B                   export
     D getDatosFormateados...
     D                 pi

     D @@asen          s              7  0
     D @@ivig          s              8  0
     D @@fvig          s              8  0
     D @@loca          s             25
     D @@copo          s              5  0
     D @@cops          s              1  0

      /free

         @@asen = SPVSPO_getAsen ( t9empr
                                 : t9sucu
                                 : t9arcd
                                 : t9spol
                                 : t9sspo );

         SPVSPO_getFecVig ( t9empr : t9sucu : t9arcd : t9spol
                          : @@ivig : @@fvig );

         tmpfec = %date(%editc( @@ivig : 'X' ) : *iso0);
         @@ivig = %int(%char(tmpfec : *eur0));

         tmpfec = %date(%editc( @@fvig : 'X' ) : *iso0 );

         @@fvig = %int(%char( tmpfec : *eur0 ) );
         SPVVEH_GetDescripcion ( t9vhmc : t9vhmo : t9vhcs
                               : marca : modelo : submodelo );

         SVPDAF_getLocalidad( @@asen : @@copo : @@cops : @@loca );

         EmpAse = %xlate( min : may : SVPEMP_getNombre( @@empr ) );
         Pais   = %xlate( min : may : SVPEMP_getPais( @@empr ) );
         NomAse = %xlate( min : may : t9nmer );
         Poliza = %editw( t9poli : '    . 0 ');
         NumCer = %editw( t9cert : ' .   .   .0 ');
         Domici = %xlate( min : may : SVPDAF_getDomicilio( @@asen ) );
         Anio   = %editw( t9vhaÑ : '   0 ');
         if SVPVLS_getValSys( 'HPAISMESUR':*omit :@@ValSys );
           Paises = %trim( @@ValSys );
         endif;
         Ciudad = %xlate( min : may : @@loca );
         @@femi = SPVSPO_getFecEmi( t9empr :t9sucu :t9arcd :t9spol );
         Fecha  = %editc( @@d : 'X' ) + ' de '
                  + %trim(meses( @@m )) + ' del '
                  + %editc( @@a : 'X' );

         Tipo   = SVPDES_getTipoDeVehiculo( t9vhct );
         Fdesd  = %editw( @@ivig : '0  /  /    ');

         //
         // Si está dado de baja, poner como hasta la fecha de baja
         //
         if t9aegn <> 0;
             @@fbaj = (t9aegn * 10000)
                    + (t9megn *   100)
                    +  t9degn;
             tmpfec = %date(%editc( @@fbaj : 'X' ) : *iso0);
             @@fbaj = %int(%char(tmpfec : *eur0));
             Fhast  = %editw( @@fbaj : '0  /  /    ');
             Fvigen = %editw( @@ivig : '0  /  /    ') + ' ' +
                      %editw( @@fbaj : '0  /  /    ');
          else;
            Fvigen = %editw( @@ivig : '0  /  /    ') + ' ' +
                     %editw( @@fvig : '0  /  /    ');
            Fhast  = %editw( @@fvig : '0  /  /    ');
         endif;


         if ( t9vhca = 1 ) or ( t9vhca = 4 ) or ( t9vhca = 5 );
           Asiste = 'SI';
         else;
           Asiste = 'NO';
         endif;

         // Datos de Productor...
         if primera;
            primera = *off;
            Interm = SPVSPO_getProductor( @@empr
                                        : @@sucu
                                        : t9arcd
                                        : t9spol
                                        : t9sspo
                                        : @@nivt
                                        : @@nivc );
            if @@nivt <> 1;
              SVPINT_GetCadena( @@empr
                              : @@sucu
                              : @@nivt
                              : @@nivc
                              : @@cade );
              @@nivt = 1;
              @@nivc = @@cade(1);
              clear Interm;
              Interm = SPVSPO_getProductor( @@empr
                                          : @@sucu
                                          : t9arcd
                                          : t9spol
                                          : t9sspo
                                          : @@nivt
                                          : @@nivc );
            endif;
            rc = SVPINT_getTelefonosWeb( @@empr
                                       : @@sucu
                                       : @@nivt
                                       : @@nivc
                                       : @@DsTl
                                       : @@DsTlC );
            clear @@mail;
            clear @@mailC;
            rc = SVPINT_getMailWeb( @@empr
                                  : @@sucu
                                  : @@nivt
                                  : @@nivc
                                  : @@mail
                                  : @@mailC );
         endif;
       return;
      /end-free
     P getDatosFormateados...
     P                 E
**
Enero
Febrero
Marzo
Abril
Mayo
Junio
Julio
Agosto
Septiembre
Octubre
Noviembre
Diciembre
