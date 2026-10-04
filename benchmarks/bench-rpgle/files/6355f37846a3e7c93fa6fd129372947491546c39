     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
      * Ruta de directorio de enlace de SERVICES PROGRAMS
     H bnddir('HDIILE/HDIBDIR')
     H alwnull(*usrctl)
      * ************************************************************ *
      * WSSFRA  BPM  Versión 1                                      *
      *         Retorna Indicadores de Fraude                        *
      * Método: GET                                                  *
      * Parám.recibir URL: Empresa, Sucursal, Rama, Póliza, Componen_*
      *                    te, Fecha de Ocurrencia.                  *
      *          Objetivo: Retornar un ARRAY de indicadores de fraude*
      *                    para mostrar                              *
      *                                                              *
      * ------------------------------------------------------------ *
      * David Tilatti                        *14 Oct-2021            *
      * ------------------------------------------------------------ *
      * Modificaciones:                                              *
      *                                                              *
      * ************************************************************ *
      *--- Definiciones DB ----------------------------------------- *
     Fpahet9    if   e           k disk
     Fpaher0    if   e           k disk
     Fpahev0    if   e           k disk

      *--- Copy H -------------------------------------------------- *
      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/spvveh_h.rpgle'
      /copy './qcpybooks/svpdes_h.rpgle'
      // -- Utilizados validaciones           ----------------//
      /copy './qcpybooks/svpemp_h.rpgle'
      /copy './qcpybooks/svpsuc_h.rpgle'
      /copy './qcpybooks/svpval_h.rpgle'
      /copy './qcpybooks/svppol_h.rpgle'
      /copy './qcpybooks/spvspo_h.rpgle'
      // -- llamada programas                 ----------------//
      // Retorna indicadores de fraude
     D SPFRAU          pr                  extpgm('SPFRAU')
     D  peEmpr                        1a
     D  peSucu                        2a
     D  peRama                        2  0
     D  pePoli                        7  0
     D  pePoco                        4  0
     D  peFsin                        8  0
     D  peErro                        1N
     D  peIemi                        1a
     D  peIvig                        1a
     D  peIitm                        1a
     D  peIsum                        1a
     D  peIcob                        1a
     D  peIcuo                        1a
     D  peIcvpag                      1a
     D  peIave                        1a

      // -- Definiciones                      ----------------//
     D uri             s            512a
     D url             s           3000a   varying
     D rc              s              1n
      // -- Fechas
     D @@Fsini         s               d   datfmt(*eur)
     D @@Fvige         s               d   datfmt(*eur)
      // @@Feditada      s             10
      // -- Informacion para xml
     D @@item          s             30a   inz(*blanks)
     D @@Suma          s             30a   inz(*blanks)
     D @@Cobertura     s             30a   inz(*blanks)
     D @@fvigdes       s              8  0
     D @@fvighas       s              8  0

      * Definiciones variables y array para utilizacion SVP
     D @@repl          s          65535a
     D peMsgs          ds                  likeds(paramMsgs)
     D @@DsD0          ds                  likeds ( dsPahed0_t ) dim( 999 )
     D @@DsD0C         s             10i 0

      * Parametros de llamada
     D empr            s              1a                                         Empresa URL
     D sucu            s              2a                                         Sucursal URL
     D rama            s              2a                                         Rama URL
     D poli            s              7a                                         Poliza URL
     D poco            s              6a                                         Componenete URL
     D fsin            s              8a                                         Fecha de Sinies.URL
      * Parametros de llamada Numericos
     D peRama          s              2  0
     D pePoli          s              7  0
     D pePoco          s              4  0
     D peFsin          s              8  0
     D peArcd          s              6  0
     D peSpol          s              9  0
      *
     D @error          s              1N
     D peIemi          s              1a
     D peIvig          s              1a
     D peIitm          s              1a
     D peIsum          s              1a
     D peIcob          s              1a
     D peIcuo          s              1a
     D peIcvpag        s              1a
     D peIave          s              1a
      * Claves
     D k1het9          ds                  likerec(p1het9:*key)
     D k1her0          ds                  likerec(p1her0:*key)
     D k1hev0          ds                  likerec(p1hev0:*key)

     D psds           sds                  qualified
     D  this                         10a   overlay(psds:1)

       // ------      Cuerpo Principal       ------------------//

      /free

       *inlr = *on;

       // Recuperar la URL desde donde se lo llamo
       rc  = REST_getUri( psds.this : uri );

       // Error en la llamada al servicio
       if rc = *off;
          REST_writeHeader( 400
                          : *omit
                          : *omit
                          : 'RPG0001'
                          : 40
                          : 'Error al parsear URL'
                          : 'Error al parsear URL' );
          REST_end();
       // Cierro BD vuelvo al llamador y evito resto de proceso
          close *all;
          return;
       endif;

       //  Mueve la URI a URL eliminado blancos
       url = %trim(uri);

       //  Obtengo los parámetros tipo string de la URL
       empr = REST_getNextPart(url);
       sucu = REST_getNextPart(url);
       rama = REST_getNextPart(url);
       poli = REST_getNextPart(url);
       poco = REST_getNextPart(url);
       fsin = REST_getNextPart(url);

       //  Paso a numerico por longitud, monitoreo en caso de error pone valor en 0
       monitor;
          peRama = %dec(rama:2:0);
       on-error;
          peRama = 0;
       endmon;

       monitor;
          pePoli = %dec(poli:7:0);
       on-error;
          pePoli = 0;
       endmon;

       monitor;
          pePoco = %dec(Poco:4:0);
       on-error;
          pePoco = 0;
       endmon;

       monitor;
          peFsin = %dec(Fsin:8:0);
       on-error;
          pePoco = 0;
       endmon;
       //      ** VALIDACIONES  **

       //1) Valido existencia de Empresa
       if SVPEMP_getDatosDeEmpresa( empr : *omit ) = *off;

       // Envio Mensaje de Error COW*
          @@repl = empr;
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'COW0113'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'COW0113'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       //2) Valido existencia de Sucursal
       if SVPSUC_getDatosDeSucursal( empr : sucu : *omit ) = *off;

       // Envio Mensaje de Error COW*
          %subst(@@repl:1:2) = sucu;
          %subst(@@repl:3:1) = empr;
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'COW0114'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'COW0114'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       //3) Valido existencia de Rama
       if SVPVAL_rama( peRama ) = *off;

       // Envio Mensaje de Error RAM*
          @@repl = rama;
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'RAM0001'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'RAM0001'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2  );
          REST_end();
          close *all;
          return;
       endif;

       //4) Valido existencia de Poliza
       clear @@DsD0;
       clear @@DsD0C;
       if SVPPOL_getPoliza( empr
                          : sucu
                          : peRama
                          : pePoli
                          : *omit
                          : *omit
                          : *omit
                          : *omit
                          : *omit
                          : *omit
                          : @@DsD0
                          : @@DsD0C  ) = *off;
          %subst(@@repl:1:2) = rama;
          %subst(@@repl:3:7) = poli;

       // Envio Mensaje de Error POL*
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'POL0009'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'POL0009'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2  );
          REST_end();
          close *all;
          return;
       endif;

       //5) Valido Existencia del Componente

       // Automoviles en paheT9  T9EMPR, T9SUCU, T9ARCD, T9SPOL, T9RAMA, T9ARSE, T9OPER Y T9POCO
       k1het9.t9empr = empr;
       k1het9.t9sucu = sucu;
       k1het9.t9arcd = SVPPOL_getArticulo(empr :sucu :peRama :pePoli );
       eval peArcd = k1het9.t9arcd;
       k1het9.t9spol = SVPPOL_getSuperPoliza(empr :sucu :peRama :pePoli );
       eval peSpol = k1het9.t9spol;
       k1het9.t9rama = peRama;
       clear @@DsD0;
       clear @@DsD0C;
       rc = SVPPOL_getPolizadesdeSuperPoliza( empr
                                              : sucu
                                              : k1het9.t9arcd
                                              : k1het9.t9spol
                                              : *omit
                                              : *omit
                                              : *omit
                                              : *omit
                                              : *omit
                                              : @@DsD0
                                              : @@DsD0C );
       if rc;
         k1het9.t9arse = @@DsD0( @@DsD0C ).d0arse;
         k1het9.t9oper = @@DsD0( @@DsD0C ).d0oper;
         k1het9.t9poco = pePoco;
       endif;
       // Chequeo si es poliza Riezgos Varios PAHER0
       setll %kds(k1het9:8) pahet9;
       if not %equal( pahet9 );

         // Riezgos Varios paher0
         // R0EMPR, R0SUCU, R0ARCD, R0SPOL, R0SSPO, R0RAMA, R0ARSE, R0OPER,  R0POCO,  R0SUOP
         k1her0.r0empr = empr;
         k1her0.r0sucu = sucu;
         k1her0.r0arcd = SVPPOL_getArticulo(empr :sucu :peRama :pePoli );
         eval peArcd = k1her0.r0arcd;
         k1her0.r0spol = SVPPOL_getSuperPoliza(empr :sucu :peRama :pePoli );
         eval peSpol = k1her0.r0spol;
         k1her0.r0sspo = SVPPOL_getUltimoSuopFacturacion( empr
                                                        : sucu
                                                        : peRama
                                                        : pePoli
                                                        : k1her0.r0sspo);
         k1her0.r0rama = peRama;
         clear @@DsD0;
         clear @@DsD0C;
         rc = SVPPOL_getPolizadesdeSuperPoliza( empr
                                                : sucu
                                                : k1her0.r0arcd
                                                : k1her0.r0spol
                                                : *omit
                                                : *omit
                                                : *omit
                                                : *omit
                                                : *omit
                                                : @@DsD0
                                                : @@DsD0C );
         if rc;
           k1her0.r0arse = @@DsD0( @@DsD0C ).d0arse;
           k1her0.r0oper = @@DsD0( @@DsD0C ).d0oper;
           k1her0.r0poco = pePoco;
           k1her0.r0suop = @@DsD0( @@DsD0C ).d0suop;
         endif;
         // Chequeo si es poliza Riezgos Varios PAHER0
         setll %kds(k1her0:10) paher0;
           if not %equal( paher0 );

           // Polizas Vida pahev0
           // V0EMPR, V0SUCU, V0ARCD, V0SPOL,  V0RAMA, V0ARSE, V0OPER, V0POCO,  V0PACO
           k1hev0.v0empr = empr;
           k1hev0.v0sucu = sucu;
           k1hev0.v0arcd = SVPPOL_getArticulo(empr :sucu :peRama :pePoli );
           eval peArcd = k1hev0.v0arcd;
           k1hev0.v0spol = SVPPOL_getSuperPoliza(empr :sucu :peRama :pePoli );
           eval peSpol = k1hev0.v0spol;
           k1hev0.v0rama = peRama;
           clear @@DsD0;
           clear @@DsD0C;
           rc = SVPPOL_getPolizadesdeSuperPoliza( empr
                                                  : sucu
                                                  : k1hev0.v0arcd
                                                  : k1hev0.v0spol
                                                  : *omit
                                                  : *omit
                                                  : *omit
                                                  : *omit
                                                  : *omit
                                                  : @@DsD0
                                                  : @@DsD0C );
           if rc;
             k1hev0.v0arse = @@DsD0( @@DsD0C ).d0arse;
             k1hev0.v0oper = @@DsD0( @@DsD0C ).d0oper;
             k1hev0.v0poco = pePoco;
           // de Donde SAco el codigo de parentesco ??????? PACO
             k1hev0.v0paco = 1;
           endif;
           // Chequeo si es poliza Vida PAHEV0
           setll %kds(k1hev0:9) pahev0;
             if not %equal( pahev0 );

             // No Existe el Componente en ninguna poliza, Envio error y retorno al llamador
             %subst(@@repl:1:4) = %char(pePoco);
             %subst(@@repl:5:2) = %char(peRama);
             %subst(@@repl:7:7) = %char(pePoli);
          // Envio Mensaje de Error BIE
             SVPWS_getMsgs( '*LIBL'
                          : 'WSVMSG'
                          : 'BIE0001'
                          : peMsgs
                          : %trim(@@repl)
                          : %len(%trim(@@repl)) );
             rc = REST_writeHeader( 400
                                  : *omit
                                  : *omit
                                  : 'BIE0001'
                                  : peMsgs.peMsev
                                  : peMsgs.peMsg1
                                  : peMsgs.peMsg2  );
             REST_end();
             close *all;
             return;
             endif;
           endif;
         endif;

       //
       // Armo respuesta con indidcadores de Fraude
       // LLamo SPFRAU
         eval @error = *off;
         SPFRAU(empr: sucu: peRama: pePoli: pePoco: peFsin
                : @error : peIemi :peIvig :peIitm
                : peIsum: peIcob: peIcuo: peIcvpag: peIave);

       // Arma XML
       REST_writeHeader();
       REST_writeEncoding();

       REST_startArray( 'indicadoresFraude' );
         REST_startArray( 'indicadores' );

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '1' );
             REST_writeXmlLine( 'descripcion'
                              : 'Fecha de siniestro cercana a la emisión de +
                                 la póliza.' );
             if peIemi ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '2' );
             REST_writeXmlLine( 'descripcion'
                              : 'Fecha de siniestro cercana al inicio de vig+
                                 encia de una póliza nueva.' );
             if peIvig ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '3' );
             REST_writeXmlLine( 'descripcion'
                              : 'Fecha de siniestro cercana a un cambio en las +
                                condiciones de la póliza: Inclusión de ítem.');
             if peIitm ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '4' );
             REST_writeXmlLine( 'descripcion'
                              : 'Fecha de siniestro cercana a un cambio en l+
                                as condiciones de la póliza: Aumento de suma +
                                asegurada.');
             if peIsum ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '5' );
             REST_writeXmlLine( 'descripcion'
                              : 'Fecha de siniestro cercana a la emision de +
                                 as condiciones de la póliza: Cambio de cobe+
                                 rtura.');
             if peIcob ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '6' );
             REST_writeXmlLine( 'descripcion'
                              : 'Fecha de siniestro posterior a pago de cuot+
                                 a vencida.' );
             if peIcuo ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '7' );
             REST_writeXmlLine( 'descripcion'
                              : 'Productor con convenio de pago');
             if peIcvpag ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '8' );
             REST_writeXmlLine( 'descripcion'
                              : 'Vehículo con carta de daños.');
             if peIave ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

           // Calculo fecha de siniestro en comparacion a fin de vigencia ????
           // Paso fechas a formato euro
           monitor;
           @@Fsini = %date( peFsin: *iso);
            on-error;
           @@Fsini = %date(00010101:*iso);
           endmon;
           // Obtengo fechas de vigencia
           SPVSPO_getFecvig( Empr
                           : Sucu
                           : peArcd
                           : peSpol
                           : @@Fvigdes
                           : @@Fvighas );
           monitor;
           @@Fvige = %date( @@Fvighas : *iso);
            on-error;
            @@Fvige =  %date(00010101 :*iso);
           endmon;

           // Obtengo diferencia de dias
           eval peIemi = '0';
           if %diff(@@Fvige: @@Fsini: *d) > -30 and
              %diff(@@Fvige: @@Fsini: *d) < 30;
             eval peIemi = '1';
           endif;

           // Invierto y le doy edicion a la fecha
           //@@Feditada = SVPREST_editFecha (@@Fvighas);

           REST_startArray( 'indicador' );
             REST_writeXmlLine( 'codigo' : '9' );
             REST_writeXmlLine( 'descripcion'
                              : 'Fecha de siniestro cercana a fin de vigenci+
                              a de la póliza.');
             if peIemi ='1';
             REST_writeXmlLine( 'valor' : 'VERDADERO' );
             else;
             REST_writeXmlLine( 'valor' : 'FALSO' );
             endif;
           REST_endArray( 'indicador' );

         REST_endArray( 'indicadores' );
       REST_endArray( 'indicadoresFraude' );

       REST_end();
       close *all;

