     H option(*nodebugio:*noshowcpy:*srcstmt)
     H alwnull(*usrctl) dftactgrp(*no)
     H bnddir ( 'HDIILE/HDIBDIR' )

      * ************************************************************ *
      * WSLCYA  : Tareas generales.                                  *
      *           WebService - Retorna clausulas/anexos poliza/endoso*
      * ------------------------------------------------------------ *
      * Norberto Franqueira                            *22-May-2015  *
      * ------------------------------------------------------------ *
      * ************************************************************ *
     Fset620    if   e           k disk
     Fpahec0    if   e           k disk

      /copy './qcpybooks/svpws_h.rpgle'

     D WSLCYA          pr                  ExtPgm('WSLCYA')
     D   peBase                            likeds(paramBase) const
     D   peArcd                       6  0 const
     D   peSpol                       9  0 const
     D   peSspo                       3  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   peOper                       7  0 const
     D   peSuop                       3  0 const
     D   peClax                            likeds(pahcla_t) dim(60)
     D   peClaxC                     10i 0
     D   peAnex                            likeds(pahane_t) dim(60)
     D   peAnexC                     10i 0
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D WSLCYA          pi
     D   peBase                            likeds(paramBase) const
     D   peArcd                       6  0 const
     D   peSpol                       9  0 const
     D   peSspo                       3  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   peOper                       7  0 const
     D   peSuop                       3  0 const
     D   peClax                            likeds(pahcla_t) dim(60)
     D   peClaxC                     10i 0
     D   peAnex                            likeds(pahane_t) dim(60)
     D   peAnexC                     10i 0
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D SPWLIBLC        pr                  ExtPgm('TAATOOL/SPWLIBLC')
     D   peEnto                       1a   const

     D SP0068W         pr                  ExtPgm('SP0068W')
     D  zEmpr                         1a   const
     D  zSucu                         2a   const
     D  zArcd                         6  0 const
     D  zSpol                         9  0 const
     D  zSspo                         3  0 const
     D  zRama                         2  0 const
     D  zArse                         2  0 const
     D  zOper                         7  0 const
     D  zSuop                         3  0 const
     D  zCla                          3a   dim(60)
     D  zClan                         9a   dim(60)
     D  zAnex                         1a   dim(60)

     D i               s             10i 0 inz(*zero)
     D j               s             10i 0 inz(*zero)
     D k               s             10i 0 inz(*zero)
     D l               s             10i 0 inz(*zero)

     D k1hec0          ds                  likerec(p1hec0:*key)

     D  pEmpr          s              1a
     D  pSucu          s              2a
     D  pArcd          s              6  0
     D  pSpol          s              9  0
     D  pSspo          s              3  0
     D  pRama          s              2  0
     D  pArse          s              2  0
     D  pOper          s              7  0
     D  pSuop          s              3  0
     D  pCla           s              3a   dim(60)
     D  pClan          s              9a   dim(60)
     D  pAnex          s              1a   dim(60)
     D @@repl          s          65535a

       *inLr = *On;

       SPWLIBLC('P');

       if not SVPWS_chkParmBase ( peBase : peMsgs );
         peErro = -1;
         return;
       endif;

       setll peArcd set620;
       if not %equal;
          %subst(@@repl:1:6) = %trim(%char(peArcd));
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'ART0001'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl))  );
          peErro = -1;
          return;
       endif;

       k1hec0.c0empr = peBase.peEmpr;
       k1hec0.c0sucu = peBase.peSucu;
       k1hec0.c0arcd = peArcd;
       k1hec0.c0spol = peSpol;
       setll %kds(k1hec0:4) pahec0;
       if not %equal;
          %subst(@@repl:1:6) = %trim(%char(peArcd));
          %subst(@@repl:7:9) = %trim(%char(peSpol));
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'SPO0001'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl))  );
          peErro = -1;
          return;
       endif;

       peClaxC  = *Zeros;
       peAnexC  = *Zeros;
       peErro   = *Zeros;

       clear peClax;
       clear peAnex;
       clear peMsgs;

       pEmpr = peBase.peEmpr;
       pSucu = peBase.peSucu;
       pArcd = peArcd;
       pSpol = peSpol;
       pSspo = peSspo;
       pRama = peRama;
       pArse = peArse;
       pOper = peOper;
       pSuop = peSuop;
       clear pCla;
       clear pClan;
       clear pAnex;

       SP0068W( pEmpr
              : pSucu
              : pArcd
              : pSpol
              : pSspo
              : pRama
              : pArse
              : pOper
              : pSuop
              : pCla
              : pClan
              : pAnex);

       for i = 1 to 60;
           if pCla(i) <> *blanks;
              peClaxC += 1;
              peClax(peClaxC).clau = pCla(i);
              peClax(peClaxC).clan = pClan(i);
           endif;
       endfor;
       for i = 1 to 60;
           if pAnex(i) <> *blanks;
              peAnexC += 1;
              peAnex(peAnexC).anex = pAnex(i);
           endif;
       endfor;

       return;
