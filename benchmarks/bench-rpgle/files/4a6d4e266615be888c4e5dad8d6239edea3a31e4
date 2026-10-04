     H option(*nodebugio:*srcstmt)
     H alwnull(*usrctl) dftactgrp(*no)
     H bnddir ( 'HDIILE/HDIBDIR' )

      * ************************************************************ *
      * WSLVHN  : Tareas generales.                                  *
      *           WebService - Retorna carta de daños vehiculo.      *
      *                                                              *
      * ------------------------------------------------------------ *
      * Norberto Franqueira                            *23-Abr-2015  *
      * ------------------------------------------------------------ *
      * SGF 11/05/2015: Tomo todos desde archivos GAUS.              *
      *                                                              *
      * ************************************************************ *
     Fset001    if   e           k disk    prefix(tr:2)
     Fpahet504  if   e           k disk
     Fpahet995  if   e           k disk
     Fset025    if   e           k disk

      /copy './qcpybooks/svpws_h.rpgle'

     D WSLVHN          pr                  ExtPgm('WSLVHN')
     D   peBase                            likeds(paramBase) const
     D   peRama                       2  0 const
     D   pePoli                       7  0 const
     D   peSpol                       9  0 const
     D   pePoco                       4  0 const
     D   peNveh                            likeds(pahaut5_t) dim(100)
     D   peNvehC                     10i 0
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D WSLVHN          pi
     D   peBase                            likeds(paramBase) const
     D   peRama                       2  0 const
     D   pePoli                       7  0 const
     D   peSpol                       9  0 const
     D   pePoco                       4  0 const
     D   peNveh                            likeds(pahaut5_t) dim(100)
     D   peNvehC                     10i 0
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D k1het9          ds                  likerec(p1het9 : *key)
     D k1het5          ds                  likerec(p1het5 : *key)

     D dsIn            ds                  likerec(p1het5)
     D dsOut           ds                  likerec(p1het5)

     D respue          s          65536
     D longm           s             10i 0
     D poco6           s              6  0
     D leyo            s              1N

       *inLr = *On;

       peNvehC = *Zeros;
       peErro  = *Zeros;
         leyo  = *off;

       clear peNveh;
       clear peMsgs;

       if not SVPWS_chkParmBase ( peBase : peMsgs );
         peErro = -1;
         return;
       endif;

       chain (peRama) set001;
       if %found( set001 ) and trrame <> 4;
          %subst(respue:1:2) = %editc(peRama:'X');
          %subst(respue:3:7) = %trim(%char(pePoli));
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'POL0003'
                       : peMsgs
                       : respue
                       : 9 );
         peErro = -1;
         return;
       endif;

       k1het9.t9empr = peBase.peEmpr;
       k1het9.t9sucu = peBase.peSucu;
       k1het9.t9rama = peRama;
       k1het9.t9poli = pePoli;
       k1het9.t9spol = peSpol;
       k1het9.t9poco = pePoco;
       chain %kds(k1het9:6) pahet995;
       if not %found;
          poco6  = pePoco;
          %subst(respue:1:6) = %trim(%char(poco6));
          %subst(respue:7:2) = %editc(peRama:'X');
          %subst(respue:9:7) = %trim(%char(pePoli));
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'BIE0001'
                       : peMsgs
                       : respue
                       : %len(%trim(respue)) );
         peErro = -1;
         return;
       endif;

       k1het5.t5empr = peBase.peEmpr;
       k1het5.t5sucu = peBase.peSucu;
       k1het5.t5rama = peRama;
       k1het5.t5poli = pePoli;
       k1het5.t5poco = pePoco;

       setll %kds(k1het5:5) pahet504;
       reade %kds(k1het5:5) pahet504 dsIn;
       dow ( not %eof ( pahet504) ) and ( peNvehC < 100 );

           if not leyo;
              leyo = *on;
            else;

               if dsIn.t5cdaÑ <> dsOut.t5cdaÑ;
                  peNvehC += 1;
                  peNveh(peNvehC).aucdan = dsOut.t5cdaÑ;
                  chain dsOut.t5cdaÑ set025;
                  if %found;
                     peNveh(peNvehC).auddan = t@ddaÑ;
                  endif;
                  peNveh(peNvehC).audanl = dsOut.t5daÑl;
                  peNveh(peNvehC).auedan = dsOut.t5edaÑ;
                  select;
                    when dsOut.t5edaÑ = '0';
                     peNveh(peNvehC).auedda = 'NO REPARADO';
                    when dsOut.t5edaÑ = '1';
                     peNveh(peNvehC).auedda = 'REPARADO';
                    when dsOut.t5edaÑ = '9';
                     peNveh(peNvehC).auedda = 'BAJA';
                  endsl;
               endif;

           endif;

           dsOut = dsIn;

       reade %kds(k1het5:5) pahet504 dsIn;

       enddo;


       if leyo and %eof(pahet504);
          peNvehC += 1;
          peNveh(peNvehC).aucdan = dsOut.t5cdaÑ;
          chain dsOut.t5cdaÑ set025;
          if %found;
             peNveh(peNvehC).auddan = t@ddaÑ;
          endif;
          peNveh(peNvehC).audanl = dsOut.t5daÑl;
          peNveh(peNvehC).auedan = dsOut.t5edaÑ;
          select;
            when dsOut.t5edaÑ = '0';
                 peNveh(peNvehC).auedda = 'NO REPARADO';
            when dsOut.t5edaÑ = '1';
                 peNveh(peNvehC).auedda = 'REPARADO';
            when dsOut.t5edaÑ = '9';
                 peNveh(peNvehC).auedda = 'BAJA';
          endsl;
       endif;

       return;
