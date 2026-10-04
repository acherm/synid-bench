     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
      * ************************************************************ *
      * WSRP11: QUOM Versión 2                                       *
      *         Preliquidación - Listar Cuotas                       *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *21-Jul-2017            *
      * ------------------------------------------------------------ *
      * SGF 09/05/18: Edición de decimales.                          *
      * SGF 20/09/18: Clear de peLcuo.                               *
      *                                                              *
      * ************************************************************ *
     Fpahcd5    if   e           k disk
     Fgntmon    if   e           k disk

      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/plqweb_h.rpgle'

     D PLQWEB25        pr                  ExtPgm('PLQWEB25')
     D  peBase                             likeds(paramBase) const
     D  peCant                       10i 0 const
     D  peRoll                        1    const
     D  pePosi                             likeds(keycmar_t) const
     D  pePreg                             likeds(keycmar_t)
     D  peUreg                             likeds(keycmar_t)
     D  peLdet                             likeds(listcmar_t) dim(99)
     D  peLdetC                      10i 0
     D  peMore                         n
     D  peErro                             like(paramErro)
     D  peMsgs                             likeds(paramMsgs)

     D PLQWEB32        pr                  ExtPgm('PLQWEB32')
     D  peBase                             likeds(paramBase) const
     D  peCant                       10i 0 const
     D  peRoll                        1    const
     D  pePosi                             likeds(keycmar_t) const
     D  pePreg                             likeds(keycmar_t)
     D  peUreg                             likeds(keycmar_t)
     D  peLdet                             likeds(listcma2_t) dim(99)
     D  peLdetC                      10i 0
     D  peMore                         n
     D  peErro                             like(paramErro)
     D  peMsgs                             likeds(paramMsgs)

     D uri             s            512a
     D empr            s              1a
     D sucu            s              2a
     D nivt            s              1a
     D nivc            s              5a
     D nit1            s              1a
     D niv1            s              5a
     D nrpl            s              7a
     D tipo            s              1a
     D @@repl          s          65535a
     D url             s           3000a   varying
     D rc              s              1n
     D rc2             s             10i 0
     D x               s             10i 0
     D peNrpl          s              7  0
     D comi            s             30a
     D imcu            s             30a
     D imc2            s             30a
     D fvto            s             10d

     D CRLF            c                   x'0d25'

     D k1hcd5          ds                  likerec(p1hcd5:*key)
     D peBase          ds                  likeds(paramBase)
     D peMsgs          ds                  likeds(paramMsgs)
     D pePosi          ds                  likeds(keycmar_t)
     D pePreg          ds                  likeds(keycmar_t)
     D peUreg          ds                  likeds(keycmar_t)
     D peLcuo          ds                  likeds(listcmar_t) dim(99)
     D peTodo          ds                  likeds(listcma2_t) dim(99)
     D peLcuoC         s             10i 0
     D peErro          s             10i 0
     D peRoll          s              1a
     D peMore          s              1n

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
       nrpl = REST_getNextPart(url);
       tipo = REST_getNextPart(url);

       if tipo <> 'T' and tipo <> 'M';
          tipo = 'T';
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
          return;
       endif;

       monitor;
          peNrpl = %dec(nrpl:7:0);
        on-error;
          peNrpl = 0;
       endmon;

       clear peBase;
       clear peMsgs;
       clear pePosi;
       clear pePreg;
       clear peUreg;
       peErro = 0;

       peBase.peEmpr = empr;
       peBase.peSucu = sucu;
       peBase.peNivt = %dec(nivt:1:0);
       peBase.peNivc = %dec(nivc:5:0);
       peBase.peNit1 = %dec(nit1:1:0);
       peBase.peNiv1 = %dec(niv1:5:0);

       peRoll = 'I';

       pePosi.nrpl = peNrpl;

       REST_writeHeader();
       REST_writeEncoding();

       REST_writeXmlLine('Cuotas':'*BEG');

       if tipo = 'T';
        dou peMore = *off;
            clear peTodo;
            clear peLcuo;
            PLQWEB25( peBase
                    : 99
                    : peRoll
                    : pePosi
                    : pePreg
                    : peUreg
                    : peLcuo
                    : peLcuoC
                    : peMore
                    : peErro
                    : peMsgs );
            peRoll = 'F';
            pePosi = peUreg;
            eval-corr peTodo = peLcuo;
            if peErro = 0;
               for x = 1 to peLcuoC;
                k1hcd5.d5empr = peBase.peEmpr;
                k1hcd5.d5sucu = peBase.peSucu;
                k1hcd5.d5arcd = peTodo(x).arcd;
                k1hcd5.d5spol = peTodo(x).spol;
                k1hcd5.d5sspo = peTodo(x).sspo;
                k1hcd5.d5rama = peTodo(x).rama;
                k1hcd5.d5arse = peTodo(x).arse;
                k1hcd5.d5oper = peTodo(x).oper;
                k1hcd5.d5suop = peTodo(x).suop;
                k1hcd5.d5nrcu = peTodo(x).nrcu;
                k1hcd5.d5nrsc = peTodo(x).nrsc;
                peTodo(x).como = *blanks;
                peTodo(x).nmoc = *blanks;
                peTodo(x).nmol = *blanks;
                peTodo(x).imc2 = *zeros;
                chain %kds(k1hcd5) pahcd5;
                if %found;
                   chain d5mone gntmon;
                   if %found;
                      if momoeq <> 'AU';
                         peTodo(x).como = d5mone;
                         peTodo(x).nmoc = monmoc;
                         peTodo(x).nmol = monmol;
                         peTodo(x).imc2 = d5imcu;
                      endif;
                   endif;
                endif;

                fvto = %date(peTodo(x).fvto:*iso);
                if peTodo(x).imcu = 0;
                   imcu = '.00';
                 else;
                   imcu = %editw(peTodo(x).imcu:'           0 .  ');
                endif;
                if peTodo(x).imcu < 0;
                   imcu = '-' + %trim(imcu);
                endif;
                if peTodo(x).imc2 = 0;
                   imc2 = '.00';
                 else;
                   imc2 = %editw(peTodo(x).imc2:'           0 .  ');
                endif;
                if peTodo(x).imc2 < 0;
                   imc2 = '-' + %trim(imc2);
                endif;
                if peTodo(x).comi = 0;
                   comi = '.00';
                 else;
                   comi = %editw(peTodo(x).comi:'           0 .  ');
                endif;
                REST_writeXmlLine('cuota':'*BEG');
                REST_writeXmlLine('articulo':%char(peTodo(x).arcd));
                REST_writeXmlLine('superPoliza':%char(peTodo(x).spol));
                REST_writeXmlLine('suplementoSupPol':%char(peTodo(x).sspo));
                REST_writeXmlLine('rama':%char(peTodo(x).rama));
                REST_writeXmlLine('arse':%char(peTodo(x).arse));
                REST_writeXmlLine('operacion':%char(peTodo(x).oper));
                REST_writeXmlLine('suplemento':%char(peTodo(x).suop));
                REST_writeXmlLine('poliza':%char(peTodo(x).poli));
                REST_writeXmlLine('numero':%char(peTodo(x).nrcu));
                REST_writeXmlLine('subCuota':%char(peTodo(x).nrsc));
                REST_writeXmlLine('vencimiento':%char(fvto:*iso));
                REST_writeXmlLine('importePesos':%trim(imcu));
                REST_writeXmlLine('comision':%trim(comi));
                REST_writeXmlLine('codMoneda':peTodo(x).como);
                REST_writeXmlLine('nombreMoneda':peTodo(x).nmol);
                REST_writeXmlLine('abreviaturaMoneda':peTodo(x).nmoc);
                REST_writeXmlLine('importeMonedaExtranjera':imc2);
                REST_writeXmlLine('asegurado':peTodo(x).nomb);
                REST_writeXmlLine('cuota':'*END');
               endfor;
            endif;
            if peMore = *off;
               leave;
            endif;
        enddo;
       endif;

       if tipo = 'M';
        dou peMore = *off;
            clear peTodo;
            clear peLcuo;
            PLQWEB32( peBase
                    : 99
                    : peRoll
                    : pePosi
                    : pePreg
                    : peUreg
                    : peTodo
                    : peLcuoC
                    : peMore
                    : peErro
                    : peMsgs );
            peRoll = 'F';
            pePosi = peUreg;
            if peErro = 0;
               for x = 1 to peLcuoC;
                fvto = %date(peTodo(x).fvto:*iso);
                if peTodo(x).imcu = 0;
                   imcu = '.00';
                 else;
                   imcu = %editw(peTodo(x).imcu:'           0 .  ');
                endif;
                if peTodo(x).imcu < 0;
                   imcu = '-' + %trim(imcu);
                endif;
                if peTodo(x).imc2 = 0;
                   imc2 = '.00';
                 else;
                   imc2 = %editw(peTodo(x).imc2:'           0 .  ');
                endif;
                if peTodo(x).imc2 < 0;
                   imc2 = '-' + %trim(imc2);
                endif;
                if peTodo(x).comi = 0;
                   comi = '.00';
                 else;
                   comi = %editw(peTodo(x).comi:'           0 .  ');
                endif;
                REST_writeXmlLine('cuota':'*BEG');
                REST_writeXmlLine('articulo':%char(peTodo(x).arcd));
                REST_writeXmlLine('superPoliza':%char(peTodo(x).spol));
                REST_writeXmlLine('suplementoSupPol':%char(peTodo(x).sspo));
                REST_writeXmlLine('rama':%char(peTodo(x).rama));
                REST_writeXmlLine('arse':%char(peTodo(x).arse));
                REST_writeXmlLine('operacion':%char(peTodo(x).oper));
                REST_writeXmlLine('suplemento':%char(peTodo(x).suop));
                REST_writeXmlLine('poliza':%char(peTodo(x).poli));
                REST_writeXmlLine('numero':%char(peTodo(x).nrcu));
                REST_writeXmlLine('subCuota':%char(peTodo(x).nrsc));
                REST_writeXmlLine('vencimiento':%char(fvto:*iso));
                REST_writeXmlLine('importePesos':%trim(imcu));
                REST_writeXmlLine('comision':%trim(comi));
                REST_writeXmlLine('codMoneda':peTodo(x).como);
                REST_writeXmlLine('nombreMoneda':peTodo(x).nmol);
                REST_writeXmlLine('abreviaturaMoneda':peTodo(x).nmoc);
                REST_writeXmlLine('importeMonedaExtranjera':imc2);
                REST_writeXmlLine('asegurado':peTodo(x).nomb);
                REST_writeXmlLine('cuota':'*END');
               endfor;
            endif;
            if peMore = *off;
               leave;
            endif;
        enddo;
       endif;

       REST_writeXmlLine('Cuotas':'*END');
       REST_end();

       return;

