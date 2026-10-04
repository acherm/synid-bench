     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
     H alwnull(*usrctl)
      * ************************************************************ *
      * WSRPOL: QUOM Versión 2                                       *
      *         Lista de pólizas por intermediario                   *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *26-May-2017            *
      * ------------------------------------------------------------ *
      * EXT 18-07-18 - Nuevo tag <isAnulada>, <estaVigente> y        *
      *                <tieneCoberturaFinanciera>                    *
      * GIO 20-07-18 - Se recompila por cambio en pahpol01           *
      * NWN 31-08-18 - Nuevo tag <saldoPendiente>                    *
      * ERC 27-05-21 - Se controla que las Polizas no esten anuladas *
      *                ni renovadas.                                 *
      * JSN 02-06-21 - Se agrega filtro a las polizas AP y RC si se  *
      *                encuentra relacionada con Robo                *
      * SGF 02/09/2021: Si anualidad supera maximo de dias, no se    *
      *                 muestra.                                     *
      *                                                              *
      * ************************************************************ *
     Fpahpol01  if   e           k disk
     Fgntemp    if   e           k disk
     Fgntsuc    if   e           k disk
     Fset901    if   e           k disk
     Fpahed004  if   e           k disk
     Fsehase01  if   e           k disk
     Fgntmon    if   e           k disk
     Fsehni201  if   e           k disk    prefix(n2:2)
     Fgnhdaf    if   e           k disk
     Fgnttdo    if   e           k disk
     Fset123    if   e           k disk

      /copy './qcpybooks/cowgrai_h.rpgle'
      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/spvspo_h.rpgle'

     D GSWEB037        pr                  ExtPgm('GSWEB037')
     D  peEmpr                        1a   const
     D  peSucu                        2a   const
     D  peRama                        2  0 const
     D  peTiou                        1  0 const
     D  peStou                        2  0 const
     D  peDsop                       20a

     D WSPCSP          pr                  ExtPgm('WSPCSP')
     D   peBase                            likeds(paramBase) const
     D   peRama                       2  0 const
     D   pePoli                       7  0 const
     D   peFech                        d   const
     D   peCast                      10i 0
     D   peCasp                      10i 0
     D   peCass                      10i 0
     D   peCasi                      10i 0
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     DPAR310X3         pr                  extpgm('PAR310X3')
     D                                1a   const
     D                                4  0
     D                                2  0
     D                                2  0

     DDXP021           pr                  extpgm('DXP021')
     D                                1    Const
     D                                2    Const
     D                                6  0 Const
     D                                9  0 Const
     D                                4  0 Const
     D                                2  0 Const
     D                                2  0 Const
     D                                1
     D                                3

     D SPVIG2          pr                  extpgm('SPVIG2')
     D                                6  0 const
     D                                9  0 const
     D                                2  0 const
     D                                2  0 const
     D                                7  0 const
     D                                8  0 const
     D                                8  0 const
     D                                1
     D                                3  0
     D                                3  0
     D                                3    const

     D SPCOBFIN        pr                  extpgm('SPCOBFIN')
     D                                1    const
     D                                2    const
     D                                6  0 const
     D                                9  0 const
     D                                8  0 const
     D                                1    const
     D                                 n
     D                                3    const

     Dspsald           pr                  extpgm('SPSALD')
     D  peArcd                        6  0
     D  peSpol                        9  0
     D  peRama                        2  0
     D  @@aÑo                         4  0
     D  @@mes                         2  0
     D  @@dia                         2  0
     D  @@sald                       15  2
     D  @@impr                        2
     D  @@fpgm                        3    const

     D uri             s            512a
     D empr            s              1a
     D sucu            s              2a
     D nivt            s              1a
     D nivc            s              5a
     D nit1            s              1a
     D niv1            s              5a
     D desd            s              8a
     D hast            s              8a
     D desde           s             10a
     D hasta           s             10a
     D prim            s             30a
     D prem            s             30a
     D @@datd          s             20a
     D @@repl          s          65535a
     D @@dsop          s             20a
     D url             s           3000a   varying
     D rc              s              1n
     D @@nrdo          s             11  0
     D @@tiou          s              1  0
     D @@stou          s              2  0
     D desdn           s              8  0
     D hastn           s              8  0
     D c               s             10i 0
     D peCast          s             10i 0
     D peCasp          s             10i 0
     D peCass          s             10i 0
     D peCasi          s             10i 0
     D rc2             s             10i 0
     D fecha           s             10d
     D @mostrar        s              1n
     D @@hoy           s             10d
     D dif             s              5  0

     D CRLF            c                   x'0d25'

     D peBase          ds                  likeds(paramBase)
     D peMsgs          ds                  likeds(paramMsgs)
     D peErro          s             10i 0
     D k1hpol          ds                  likerec(p1hpol:*key)
     D k1hed0          ds                  likerec(p1hed004:*key)
     D k1hni2          ds                  likerec(s1hni201:*key)

     D @@d             s              2  0
     D @@m             s              2  0
     D @@a             s              4  0
     D @@fech          s              8  0
     D @@anul          s              1
     D @@vige          s               n
     D @@cobf          s               n
     D endpgm          s              3
     D anulada         s              1
     D cobfina         s              1
     D vigente         s              1
     D vigeSspo        s              3  0
     D vigeSuop        s              3  0
     D @@fpgm          s              3    inz('   ')
     D @@ano           s              4  0
     D @@mes           s              2  0
     D @@dia           s              2  0
     D @@impr          s              2
     D @1sald          s             15  2
     D peNctw          s              7  0
     D trelacion       s               n
     D grupoRama       s              1a

     D PsDs           sds                  qualified
     D  this                         10a   overlay(PsDs:1)

     D                 ds                  inz
     D  @@sald                01     15  2
     D  @@ente                01     13  0
     D  @@deci                14     15  0

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
       desde= REST_getNextPart(url);
       hasta= REST_getNextPart(url);

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

       desd = %subst(desde:1:4)
            + %subst(desde:6:2)
            + %subst(desde:9:2);

       hast = %subst(hasta:1:4)
            + %subst(hasta:6:2)
            + %subst(hasta:9:2);

       if %check( '0123456789' : %trim(desd) ) <> 0;
          rc2 = SVPWS_getMsgs( '*LIBL'
                             : 'WSVMSG'
                             : 'GEN0001'
                             : peMsgs    );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'GEN0001'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       desdn = %dec(desd:8:0);
       monitor;
          fecha = %date( desdn : *iso);
        on-error;
          rc2 = SVPWS_getMsgs( '*LIBL'
                             : 'WSVMSG'
                             : 'GEN0001'
                             : peMsgs    );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'GEN0001'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endmon;

       if %check( '0123456789' : %trim(hast) ) <> 0;
          rc2 = SVPWS_getMsgs( '*LIBL'
                             : 'WSVMSG'
                             : 'GEN0002'
                             : peMsgs   );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'GEN0002'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       hastn = %dec(hast:8:0);
       monitor;
          fecha = %date( hastn : *iso);
        on-error;
          rc2 = SVPWS_getMsgs( '*LIBL'
                             : 'WSVMSG'
                             : 'GEN0002'
                             : peMsgs    );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'GEN0002'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endmon;

       if hastn < desdn;
          rc2 = SVPWS_getMsgs( '*LIBL'
                             : 'WSVMSG'
                             : 'GEN0003'
                             : peMsgs    );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'GEN0003'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       clear @@fech;
       PAR310X3 ( empr : @@a : @@m : @@d );
       @@fech = (@@a * 10000) + (@@m * 100) + @@d;
       @@hoy  = %date(@@fech:*iso);

       k1hpol.poempr = empr;
       k1hpol.posucu = sucu;
       k1hpol.ponivt = %dec( nivt : 1 : 0 );
       k1hpol.ponivc = %dec( nivc : 5 : 0 );
       k1hpol.poanua = %date( desdn : *iso );

       peBase.peEmpr = empr;
       peBase.peSucu = sucu;
       peBase.peNivt = %dec(nivt:1:0);
       peBase.peNivc = %dec(nivc:5:0);
       peBase.peNit1 = %dec(nit1:1:0);
       peBase.peNiv1 = %dec(niv1:5:0);

       COWLOG_logcon('WSRPAV':peBase);

       rc = REST_writeHeader();
       if rc = *off;
          return;
       endif;

       rc = REST_writeEncoding();
       rc = REST_writeXmlLine( 'polizas' : '*BEG');
       if rc = *off;
          return;
       endif;

       c = 0;

       setll %kds(k1hpol:5) pahpol01;
       reade %kds(k1hpol:4) pahpol01;
       dow not %eof;

           exsr $anualidad;

           if @mostrar;
           clear grupoRama;
           clear peNctw;
           Trelacion = *off;

           grupoRama = SVPWS_getGrupoRama( poRama );
           if grupoRama = 'V' or grupoRama = 'W'; // Vida / RC
             peNctw = COWGRAI_getNroCotiXSpol( peBase : poArcd : poSpol );
             select;
               when grupoRama = 'V';
                 Trelacion = COWGRAI_chkRelacionAP( peBase
                                                  : peNctw );
               when grupoRama = 'W';
                 Trelacion = COWGRAI_chkRelacionRC( peBase
                                                  : peNctw );
             endsl;
           endif;

           if %dec(poanua:*iso) >= desdn and %dec(poanua:*iso) <= hastn
              and not spvspo_chkanuladav2(poempr
                                         :posucu
                                         :poarcd
                                         :pospol
                                         :*omit)

              and spvspo_chkspolrenovada(poempr
                                        :posucu
                                        :poarcd
                                        :pospol) =0

              and not Trelacion;

              k1hed0.d0empr = poempr;
              k1hed0.d0sucu = posucu;
              k1hed0.d0rama = porama;
              k1hed0.d0poli = popoli;
              setgt %kds(k1hed0:4) pahed004;
              readpe %kds(k1hed0:4) pahed004;
              if %eof;
                 @@tiou = potiou;
                 @@stou = postou;
               else;
                 @@tiou = d0tiou;
                 @@stou = d0stou;
              endif;
              GSWEB037( poempr
                      : posucu
                      : porama
                      : @@tiou
                      : @@stou
                      : @@dsop );

              chain pomone gntmon;
              if not %found;
                 monmoc = *blanks;
              endif;

              chain poasen gnhdaf;
              if not %found;
                 dfnomb = *blanks;
                 dftido = 0;
                 dfnrdo = 0;
                 dfcuit = *all'0';
                 dfnjub = 0;
                 dftiso = 0;
              endif;

              @@datd = *blanks;
              @@nrdo = 0;
              select;
               when dftiso = 98;
                    chain dftido gnttdo;
                    if not %found;
                       gndatd = *blanks;
                    endif;
                    @@datd = gndatd;
                    if dfnrdo > 0;
                       @@nrdo = dfnrdo;
                     else;
                       if dfcuit <> *all'0' and dfcuit <> *blanks;
                          monitor;
                            @@nrdo = %dec(dfcuit:11:0);
                           on-error;
                            @@nrdo = 0;
                            @@datd = *blanks;
                          endmon;
                        else;
                          @@nrdo = dfnjub;
                       endif;
                    endif;
               other;
                    if dfcuit <> *all'0' and dfcuit <> *blanks;
                       @@datd = 'CUIT';
                       monitor;
                         @@nrdo = %dec(dfcuit:11:0);
                        on-error;
                         @@datd = *blanks;
                         @@nrdo = *zeros;
                       endmon;
                    endif;
              endsl;

              k1hni2.n2empr = poempr;
              k1hni2.n2sucu = posucu;
              k1hni2.n2nivt = 1;
              k1hni2.n2nivc = ponivc1;
              chain %kds(k1hni2:4) sehni201;
              if not %found;
                 n2nomb = *blanks;
              endif;

              WSPCSP( peBase
                    : porama
                    : popoli
                    : %date
                    : peCast
                    : peCasp
                    : peCass
                    : peCasi
                    : peErro
                    : peMsgs );

              prim = %editw( poprim : '                 .  -' );
              prem = %editw( poprem : '                 .  -' );

              c += 1;

              REST_writeXmlLine( 'poliza ' : '*BEG' );
               REST_writeXmlLine( 'articulo'           : %trim(%char(poarcd)) );
               REST_writeXmlLine( 'superpoliza'        : %trim(%char(pospol)) );
               REST_writeXmlLine( 'rama'               : %trim(%char(porama)) );
            REST_writeXmlLine( 'nroPoliza'          : %trim(%char(popoli)) );
               REST_writeXmlLine( 'arse'               : %trim(%char(poarse)) );
               REST_writeXmlLine( 'operacion'          : %trim(%char(pooper)) );
               REST_writeXmlLine( 'certificado'        : %trim(%char(pocert)) );
               REST_writeXmlLine( 'tipoOperacion'      : %trim(@@dsop)        );
            REST_writeXmlLine( 'codigoAsegurado'    : %trim(%char(poasen)) );
               REST_writeXmlLine( 'nombreAsegurado'    : %trim(dfnomb)        );
               REST_writeXmlLine( 'tipoDocAsegurado'   : %trim(@@datd)        );
               REST_writeXmlLine( 'numeroDocAsegurado' : %trim(%char(@@nrdo)) );
               REST_writeXmlLine( 'codigoProductor' : %trim(%char(ponivc1))   );
               REST_writeXmlLine( 'nombreProductor' : %trim(n2nomb)           );
               REST_writeXmlLine( 'fechaEmision'  : %trim(%char(pofemi:*iso)) );
               REST_writeXmlLine( 'fechaVigDesd'  : %trim(%char(pofdes:*iso)) );
               REST_writeXmlLine( 'fechaVigHast'  : %trim(%char(pofhas:*iso)) );
               REST_writeXmlLine( 'moneda'               : %trim(monmoc)      );
               REST_writeXmlLine( 'prima'                : %trim(prim)        );
               REST_writeXmlLine( 'premio'               : %trim(prem)        );
               REST_writeXmlLine( 'patente'              : %trim(popatente)   );
               REST_writeXmlLine( 'cantidadSiniestros' : %trim(%char(peCasi)) );
               REST_writeXmlLine( 'embarcacion'        : %trim(poemcn)      );
               anulada = 'N';
               callp DXP021( empr
                           : sucu
                           : poarcd
                           : pospol
                           : @@a
                           : @@m
                           : @@d
                           : @@anul
                           : endpgm );
               if ( @@anul = 'A' );
                 anulada = 'S';
               endif;
               REST_writeXmlLine( 'isAnulada' : anulada );

               vigente = 'N';
               SPVIG2( poarcd
                     : pospol
                     : porama
                     : poarse
                     : pooper
                     : @@fech
                     : @@fech
                     : @@vige
                     : vigeSspo
                     : vigeSuop
                     : *blanks );
               if @@vige;
                 vigente = 'S';
               endif;
               REST_writeXmlLine( 'estaVigente' : vigente );

               cobFina = 'N';
               SPCOBFIN( poempr
                       : posucu
                       : poarcd
                       : pospol
                       : @@fech
                       : 'P'
                       : @@cobf
                       : *blanks );
               if @@cobf;
                 cobFina = 'S';
               endif;
               REST_writeXmlLine( 'tieneCoberturaFinanciera' : cobFina );

         @@sald = 0 ;
         @1sald = 0 ;
         @@impr = ' ';

         spsald  ( poarcd
                 : pospol
                 : porama
                 : @@a
                 : @@m
                 : @@d
                 : @1sald
                 : @@impr
                 : *blanks);

         @@sald = @1sald;

         if @@deci <> 0;
            @@deci = 0;
         endif;

               REST_writeXmlLine( 'saldoPendiente'
                                : svprest_editImporte(@@sald) );

              REST_writeXmlLine( 'poliza ' : '*END' );

           endif;

        endif; // @mostrar

        reade %kds(k1hpol:4) pahpol01;
       enddo;

       REST_writeXmlLine( 'cantidad' : %trim(%char(c)) );
       REST_writeXmlLine( 'polizas' : '*END' );

       close *all;

       return;

       begsr $anualidad;
        @mostrar = *on;
        chain porama set123;
        dif = %diff(poanua:@@hoy:*d);
        if dif > t@ldee;
           @mostrar = *off;
        endif;
       endsr;

