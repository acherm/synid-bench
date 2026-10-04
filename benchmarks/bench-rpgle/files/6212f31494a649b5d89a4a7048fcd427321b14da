     H option(*nodebugio:*noshowcpy:*srcstmt)
     H actgrp(*new) dftactgrp(*no)
     H bnddir ('HDIILE/HDIBDIR')
      * ************************************************************ *
      * PLQWEB32:WebService                                          *
      *          Preliquidación Web                                  *
      *          Wrapper para _listarCuotasMarcadas()                *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                         *07-Nov-2011        *
      * ************************************************************ *
     Fpahcd5    if   e           k disk
     Fgntmon    if   e           k disk

      /copy './qcpybooks/plqweb_h.rpgle'

     D PLQWEB32        pr                  ExtPgm('PLQWEB32')
     D   peBase                            likeds(paramBase) const
     D   peCant                      10i 0 const
     D   peRoll                       1    const
     D   pePosi                            likeds(keycmar_t) const
     D   pePreg                            likeds(keycmar_t)
     D   peUreg                            likeds(keycmar_t)
     D   peLdet                            likeds(listcma2_t) dim(99)
     D   peLdetC                     10i 0
     D   peMore                        n
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D PLQWEB32        pi
     D   peBase                            likeds(paramBase) const
     D   peCant                      10i 0 const
     D   peRoll                       1    const
     D   pePosi                            likeds(keycmar_t) const
     D   pePreg                            likeds(keycmar_t)
     D   peUreg                            likeds(keycmar_t)
     D   peLdet                            likeds(listcma2_t) dim(99)
     D   peLdetC                     10i 0
     D   peMore                        n
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D k1hcd5          ds                  likerec(p1hcd5:*key)
     D peLde2          ds                  likeds(listcmar_t) dim(99)
     D peLde2C         s             10i 0
     D x               s             10i 0

      /free

       *inlr = *on;

       PLQWEB_listarCuotasMarcadas( peBase
                                  : peCant
                                  : peRoll
                                  : pePosi
                                  : pePreg
                                  : peUreg
                                  : peLde2
                                  : peLde2C
                                  : peMore
                                  : peErro
                                  : peMsgs );

       peLdetC = peLde2C;
       for x = 1 to peLde2C;
           eval-corr peLdet(x) = peLde2(x);
           k1hcd5.d5empr = peBase.peEmpr;
           k1hcd5.d5sucu = peBase.peSucu;
           k1hcd5.d5arcd = peLde2(x).arcd;
           k1hcd5.d5spol = peLde2(x).spol;
           k1hcd5.d5sspo = peLde2(x).sspo;
           k1hcd5.d5rama = peLde2(x).rama;
           k1hcd5.d5arse = peLde2(x).arse;
           k1hcd5.d5oper = peLde2(x).oper;
           k1hcd5.d5suop = peLde2(x).suop;
           k1hcd5.d5nrcu = peLde2(x).nrcu;
           k1hcd5.d5nrsc = peLde2(x).nrsc;
           peLdet(x).como = *blanks;
           peLdet(x).nmoc = *blanks;
           peLdet(x).nmol = *blanks;
           peLdet(x).imc2 = *zeros;
           chain %kds(k1hcd5) pahcd5;
           if %found;
              chain d5mone gntmon;
              if %found;
                 if momoeq <> 'AU';
                    peLdet(x).como = d5mone;
                    peLdet(x).nmoc = monmoc;
                    peLdet(x).nmol = monmol;
                    peLdet(x).imc2 = d5imcu;
                 endif;
              endif;
           endif;
       endfor;

       return;

      /end-free
