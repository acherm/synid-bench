     H option(*nodebugio:*noshowcpy:*srcstmt)
     H alwnull(*usrctl) dftactgrp(*no)
     H bnddir ( 'HDIILE/HDIBDIR' )
      * ************************************************************ *
      * WSLSPN : WebService                                          *
      *          R torna Inspecciones SpeedWay.                      *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                              *15/12/2015    *
      * ------------------------------------------------------------ *
      *                                                              *
      * ************************************************************ *
     Fpahspwc   if   e           k disk
     Fpahsp2    if   e           k disk
     Fset001    if   e           k disk

      /copy './qcpybooks/svpws_h.rpgle'

     D WSLSPC          pr                  ExtPgm('WSLSPC')
     D   peBase                            likeds(paramBase) const
     D   peCant                      10i 0 const
     D   peRoll                       1a   const
     D   pePosi                            likeds(keyspc_t) const
     D   pePreg                            likeds(keyspc_t)
     D   peUreg                            likeds(keyspc_t)
     D   peLveh                            likeds(pahspwc_t) dim(99)
     D   peLvehC                     10i 0
     D   peMore                        n
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D WSLSPC          pi
     D   peBase                            likeds(paramBase) const
     D   peCant                      10i 0 const
     D   peRoll                       1a   const
     D   pePosi                            likeds(keyspc_t) const
     D   pePreg                            likeds(keyspc_t)
     D   peUreg                            likeds(keyspc_t)
     D   peLveh                            likeds(pahspwc_t) dim(99)
     D   peLvehC                     10i 0
     D   peMore                        n
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D @@Repl          s          65535a
     D @@more          s               n

     D k1hsp2          ds                  likerec(p1hsp2:*key)
     D k1hspwc         ds                  likerec(p1hspwc:*key)

     D finArc          pr              n

     D @@cant          s             10i 0

       *inLr = *On;

       clear peLveh;
       clear peLvehC;
       clear peErro;
       clear peMsgs;

       @@more = *On;

      *- Valido Parametro Forma de Paginado
       if not SVPWS_chkRoll ( peRoll : peMsgs );
         peErro = -1;
         return;
       endif;

      *- Valido Cantidad de Lineas a Retornar
       @@cant = peCant;
       if ( ( peCant <= *Zeros ) or ( peCant > 99 ) );
         @@cant = 99;
       endif;

      * Valido Solicitud
        k1hsp2.swempr = peBase.peEmpr;
        k1hsp2.swsucu = peBase.peSucu;
        k1hsp2.swnivt = peBase.peNivt;
        k1hsp2.swnivc = peBase.peNivc;
        k1hsp2.swrama = pePosi.rama;
        k1hsp2.swsoln = pePosi.soln;
        setll %kds(k1hsp2) pahsp2;
        if not %equal;
           %subst(@@repl:1:7) = %trim(%char(pePosi.soln));
           %subst(@@repl:8:1) = %char(peBase.peNivt);
           %subst(@@repl:9:5) = %trim(%char(peBase.peNivc));
           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'SPW0001'
                        : peMsgs
                        : %trim(@@repl)
                        : %len(%trim(@@repl)) );
           peErro = -1;
           return;
        endif;

      *- Posicionamiento en archivo
       exsr posArc;

      * Retrocedo si es paginado 'R'
       exsr retPag;

       exsr leeArc;

       if ( not finArc );
         exsr priReg;
       endif;

       dow ( ( not finArc ) and ( peLvehC < @@cant ) );

         peLvehC += 1;

         peLveh(peLvehC).wcrama = wcrama;
         chain wcrama set001;
         if %found;
            peLveh(peLvehC).wcramd = t@ramd;
          else;
            peLveh(peLvehC).wcramd = *blanks;
         endif;
         peLveh(peLvehC).wcpoli = wcpoli;
         peLveh(peLvehC).wcsoln = wcsoln;
         peLveh(peLvehC).wcpoco = wcpoco;
         peLveh(peLvehC).wcvhmd = wcvhmd;
         peLveh(peLvehC).wcvhdm = wcvhdm;
         peLveh(peLvehC).wcvhds = wcvhds;
         peLveh(peLvehC).wcvhan = %trim(%char(wcvhan));
         peLveh(peLvehC).wccobl = wccobl;
         peLveh(peLvehC).wcvhvu = wcvhvu;
         peLveh(peLvehC).wcnmat = wcnmat;
         peLveh(peLvehC).wcmoto = wcmoto;
         peLveh(peLvehC).wcchas = wcchas;
         peLveh(peLvehC).wcscta = wcscta;
         peLveh(peLvehC).wccobd = wccobd;
         peLveh(peLvehC).wcrast = wcrast;
         peLveh(peLvehC).wceras = wceras;

         exsr UltReg;

         exsr leeArc;

       enddo;

       select;
         when ( peRoll = 'R' );
           peMore = @@more;
         when %eof ( pahspwc );
           peMore = *Off;
         other;
           peMore = *On;
       endsl;

       return;

      *- Rutina de Posicionamiento de Archivo. Segun pePosi, peRoll
       begsr posArc;

         k1hspwc.wcrama = pePosi.rama;
         k1hspwc.wcpoli = pePosi.poli;
         k1hspwc.wcsoln = pePosi.soln;
         k1hspwc.wcpoco = pePosi.poco;

         if ( peRoll = 'F' );
            setgt %kds ( k1hspwc ) pahspwc;
         else;
            setll %kds ( k1hspwc ) pahspwc;
         endif;

       endsr;

      *- Rutina de Lectura para Adelante
       begsr leeArc;

         reade %kds(k1hspwc:3) pahspwc;

       endsr;

      *- Rutina de Lectura para Atras en caso de Paginado "F"
       begsr retArc;

         readpe %kds(k1hspwc:3) pahspwc;

       endsr;

      *- Rutina de Posicionamiento en Comienzo de Archivo
       begsr priArc;

         setll %kds(k1hspwc:3) pahspwc;

       endsr;

      *- Rutina de Posicionamiento en Comienzo de Archivo
       begsr retPag;

       if ( peRoll = 'R' );
         exsr retArc;
         dow ( ( not finArc ) and ( @@cant > 0 ) );
           @@cant -= 1;
           exsr retArc;
         enddo;
         if finArc;
           @@more = *Off;
           exsr priArc;
         endif;
         @@cant = peCant;
         if (@@cant <= 0 or @@cant > 99);
            @@cant = 99;
         endif;
       endif;

       endsr;

      *- Rutina que graba el Primer Registro
       begsr priReg;

         pePreg.rama = wcrama;
         pePreg.soln = wcsoln;
         pePreg.poli = wcpoli;
         pePreg.poco = wcpoco;

       endsr;

      *- Rutina que graba el Ultimo Registro
       begsr ultReg;

         peUreg.rama = wcrama;
         peUreg.soln = wcsoln;
         peUreg.poli = wcpoli;
         peUreg.poco = wcpoco;

       endsr;

      *- Rutina que determina si es Fin de Archivo
     P finArc          B
     D finArc          pi              n

       return %eof ( pahspwc );

     P finArc          E
