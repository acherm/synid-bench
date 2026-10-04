     H actgrp(*caller) dftactgrp(*no)
     H option(*nodebugio:*srcstmt:*noshowcpy)
     H bnddir('HDIILE/HDIBDIR')
      * ********************************************************** *
      * COW311: Emision Automatica Desde Web                       *
      * ---------------------------------------------------------- *
      * Convierte a "todo RC"                                      *
      * ---------------------------------------------------------- *
      * Sergio Fernandez                    *15-Nov-2016           *
      * ---------------------------------------------------------- *
      * SGF 05/04/2017: Incorporo plan de pago especial desde la   *
      *                 SET6118 cuando es mono rama y es cobranza  *
      *                 por cobrador.                              *
      * SGF 25/04/2017: Me llevo la PTF de 05/04/2017 a COW312 por *
      *                 que los planes especiales no están en web. *
      *                 Esto provoca que cancele la consulta de    *
      *                 cotizaciones web.                          *
      * LRG 15/08/2017: Se recompila por cambios en CTW000:        *
      *                          º Número de Cotización API        *
      *                          º Nombre de Sistema Remoto        *
      *                          º CUIT del productor              *
      * LRG 13/10/2017: Se recompila por cambios en CTW000:        *
      *                          º Nombre de Usuario               *
      * GIO 15/12/2017: Verifica si articulo cambia a combinacion  *
      *                 Articulo-Rama (T@ARCC-T@RAMC) si la Marca  *
      *                 esta habilitada (T@MAR3)                   *
      * EXT 17/01/2019: Se recompila por cambios en CTWET0         *
      * LRG 26/06/2019: Se recompila por cambios en CTW001         *
      * LRG 13/11/2019: Se agrega scoring - CTWET3                 *
      *                                                            *
      * ********************************************************** *
     Fctw000    uf   e           k disk
     Fctweg3    uf a e           k disk
     Fctweg3p   uf a e           k disk
     Fctwetc    uf a e           k disk
     Fctwet0    uf a e           k disk
     Fctwet1    uf a e           k disk
     Fctwet3    uf a e           k disk
     Fctwetc01  if   e           k disk    rename(c1wetc:c1wetc01)
     Fctwet4    uf a e           k disk
     Fctw001    uf a e           k disk
     Fctw001c   uf a e           k disk
     Fctw002    uf a e           k disk
     Fset620    if   e           k disk
     Fset6118   if   e           k disk

     D COW311          pr                  ExtPgm('COW311')
     D  peEmpr                        1a   const
     D  peSucu                        2a   const
     D  peNivt                        1  0 const
     D  peNivc                        5  0 const
     D  peNctw                        7  0 const

     D COW311          pi
     D  peEmpr                        1a   const
     D  peSucu                        2a   const
     D  peNivt                        1  0 const
     D  peNivc                        5  0 const
     D  peNctw                        7  0 const

     D k@wetc          ds                  likerec(c1wetc01:*key)
     D k1w000          ds                  likerec(c1w000:*key)
     D k1wetc          ds                  likerec(c1wetc:*key)
     D k1wet0          ds                  likerec(c1wet0:*key)
     D k1wet1          ds                  likerec(c1wet1:*key)
     D k1wet3          ds                  likerec(c1wet3:*key)
     D k1wet4          ds                  likerec(c1wet4:*key)
     D k1w001          ds                  likerec(c1w001:*key)
     D k1w001c         ds                  likerec(c1w001c:*key)
     D k1w002          ds                  likerec(c1w002:*key)
     D k1weg3          ds                  likerec(c1weg3:*key)
     D k1weg3p         ds                  likerec(c1weg3p:*key)
     D k1t6118         ds                  likerec(s1t6118:*key)

     D inEg3           ds                  likerec(c1weg3:*input)
     D inEg3p          ds                  likerec(c1weg3p:*input)
     D inEtc           ds                  likerec(c1wetc:*input)
     D inEt0           ds                  likerec(c1wet0:*input)
     D inEt1           ds                  likerec(c1wet1:*input)
     D inEt3           ds                  likerec(c1wet3:*input)
     D inEt4           ds                  likerec(c1wet4:*input)
     D in001           ds                  likerec(c1w001:*input)
     D in001c          ds                  likerec(c1w001c:*input)
     D in002           ds                  likerec(c1w002:*input)

     D ouEg3           ds                  likerec(c1weg3:*output)
     D ouEg3p          ds                  likerec(c1weg3p:*output)
     D ouEtc           ds                  likerec(c1wetc:*output)
     D ouEt0           ds                  likerec(c1wet0:*output)
     D ouEt1           ds                  likerec(c1wet1:*output)
     D ouEt3           ds                  likerec(c1wet3:*output)
     D ouEt4           ds                  likerec(c1wet4:*output)
     D ou001           ds                  likerec(c1w001:*output)
     D ou001c          ds                  likerec(c1w001c:*output)
     D ou002           ds                  likerec(c1w002:*output)

     D todoRc          s              1
     D qtyRam          s             10i 0
     D @@Arcd          s              6  0
     D @@Rams          s              2  0
     D @@Arcc          s              6  0
     D @@Ramc          s              2  0

      *--- Copy H -------------------------------------------------- *******
      /copy './qcpybooks/svpweb_h.rpgle'

      /free

       *inlr = *on;

       todoRc = *on;
       qtyRam = 0;

       k1w001.w1empr = peEmpr;
       k1w001.w1sucu = peSucu;
       k1w001.w1nivt = peNivt;
       k1w001.w1nivc = peNivc;
       k1w001.w1nctw = peNctw;
       setll %kds(k1w001:5) ctw001;
       reade %kds(k1w001:5) ctw001;
       dow not %eof;
           qtyRam += 1;
           if qtyRam > 1;
              returN;
           endif;
        reade %kds(k1w001:5) ctw001;
       enddo;

       k1wet0.t0empr = peEmpr;
       k1wet0.t0sucu = peSucu;
       k1wet0.t0nivt = peNivt;
       k1wet0.t0nivc = peNivc;
       k1wet0.t0nctw = peNctw;
       setll %kds(k1wet0:5) ctwet0;
       if not %equal;
          return;
       endif;

       k@wetc.t0empr = peEmpr;
       k@wetc.t0sucu = peSucu;
       k@wetc.t0nivt = peNivt;
       k@wetc.t0nivc = peNivc;
       k@wetc.t0nctw = peNctw;
       setll %kds(k@wetc:5) ctwetc01;
       reade %kds(k@wetc:5) ctwetc01;
       dow not %eof;
           if t0cobl <> 'A';
              return;
           endif;
        reade %kds(k@wetc:5) ctwetc01;
       enddo;


       k1w000.w0empr = peEmpr;
       k1w000.w0sucu = peSucu;
       k1w000.w0nivt = peNivt;
       k1w000.w0nivc = peNivc;
       k1w000.w0nctw = peNctw;
       chain %kds(k1w000:5) ctw000;
       if %found;

          @@arcd = w0arcd;
          clear @@rams;
          clear @@arcc;
          clear @@ramc;
          if not SVPWEB_getConvertirArticuloRamaEmision( peEmpr
                                                       : peSucu
                                                       : @@arcd
                                                       : @@rams
                                                       : @@arcc
                                                       : @@ramc );
             return;
          endif;

          if @@ramc = *zeros;
             @@ramc = @@rams;
          endif;

          w0arcd = @@arcc;

          chain w0arcd set620;
          if not %found;
             t@arno = *blanks;
          endif;
          w0arno = t@arno;

          update c1w000;
       endif;

       k1weg3.g3empr = peEmpr;
       k1weg3.g3sucu = peSucu;
       k1weg3.g3nivt = peNivt;
       k1weg3.g3nivc = peNivc;
       k1weg3.g3nctw = peNctw;
       setll %kds(k1weg3:5) ctweg3;
       reade %kds(k1weg3:5) ctweg3 inEg3;
       dow not %eof;
           if inEg3.g3rama = @@rams;
              delete c1weg3;
              ouEg3 = inEg3;
              ouEg3.g3rama = @@ramc;
              write c1weg3 ouEg3;
           endif;
        reade %kds(k1weg3:5) ctweg3 inEg3;
       enddo;

       setll %kds(k1weg3:5) ctweg3p;
       reade %kds(k1weg3:5) ctweg3p inEg3p;
       dow not %eof;
           if inEg3p.gp3rama = @@rams;
              delete c1weg3p;
              ouEg3p = inEg3p;
              ouEg3p.gp3rama = @@ramc;
              write c1weg3p ouEg3p;
           endif;
        reade %kds(k1weg3:5) ctweg3p inEg3p;
       enddo;

       k1wetc.t0empr = peEmpr;
       k1wetc.t0sucu = peSucu;
       k1wetc.t0nivt = peNivt;
       k1wetc.t0nivc = peNivc;
       k1wetc.t0nctw = peNctw;
       setll %kds(k1wetc:5) ctwetc;
       reade %kds(k1wetc:5) ctwetc inEtc;
       dow not %eof;
           if inEtc.t0rama = @@rams;
              delete c1wetc;
              ouEtc = inEtc;
              ouEtc.t0rama = @@ramc;
              write c1wetc ouEtc;
           endif;
        reade %kds(k1wetc:5) ctwetc inEtc;
       enddo;

       k1wet0.t0empr = peEmpr;
       k1wet0.t0sucu = peSucu;
       k1wet0.t0nivt = peNivt;
       k1wet0.t0nivc = peNivc;
       k1wet0.t0nctw = peNctw;
       setll %kds(k1wet0:5) ctwet0;
       reade %kds(k1wet0:5) ctwet0 inEt0;
       dow not %eof;
           if inEt0.t0rama = @@rams;
              delete c1wet0;
              ouEt0 = inEt0;
              ouEt0.t0rama = @@ramc;
              write c1wet0 ouEt0;
           endif;
        reade %kds(k1wet0:5) ctwet0 inEt0;
       enddo;

       k1wet1.t1empr = peEmpr;
       k1wet1.t1sucu = peSucu;
       k1wet1.t1nivt = peNivt;
       k1wet1.t1nivc = peNivc;
       k1wet1.t1nctw = peNctw;
       setll %kds(k1wet1:5) ctwet1;
       reade %kds(k1wet1:5) ctwet1 inEt1;
       dow not %eof;
           if inEt1.t1rama = @@rams;
              delete c1wet1;
              ouEt1 = inEt1;
              ouEt1.t1rama = @@ramc;
              write c1wet1 ouEt1;
           endif;
        reade %kds(k1wet1:5) ctwet1 inEt1;
       enddo;

       k1wet3.t3empr = peEmpr;
       k1wet3.t3sucu = peSucu;
       k1wet3.t3nivt = peNivt;
       k1wet3.t3nivc = peNivc;
       k1wet3.t3nctw = peNctw;
       setll %kds(k1wet3:5) ctwet3;
       reade %kds(k1wet3:5) ctwet3 inEt3;
       dow not %eof;
           if inEt3.t3rama = @@rams;
              delete c1wet3;
              ouEt3 = inEt3;
              ouEt3.t3rama = @@ramc;
              write c1wet3 ouEt3;
           endif;
        reade %kds(k1wet3:5) ctwet3 inEt3;
       enddo;

       k1wet4.t4empr = peEmpr;
       k1wet4.t4sucu = peSucu;
       k1wet4.t4nivt = peNivt;
       k1wet4.t4nivc = peNivc;
       k1wet4.t4nctw = peNctw;
       setll %kds(k1wet4:5) ctwet4;
       reade %kds(k1wet4:5) ctwet4 inEt4;
       dow not %eof;
           if inEt4.t4rama = @@rams;
              delete c1wet4;
              ouEt4 = inEt4;
              ouEt4.t4rama = @@ramc;
              write c1wet4 ouEt4;
           endif;
        reade %kds(k1wet4:5) ctwet4 inEt4;
       enddo;

       k1w001.w1empr = peEmpr;
       k1w001.w1sucu = peSucu;
       k1w001.w1nivt = peNivt;
       k1w001.w1nivc = peNivc;
       k1w001.w1nctw = peNctw;
       setll %kds(k1w001:5) ctw001;
       reade %kds(k1w001:5) ctw001 in001;
       dow not %eof;
           if in001.w1rama = @@rams;
              delete c1w001;
              ou001 = in001;
              ou001.w1rama = @@ramc;
              write c1w001 ou001;
           endif;
        reade %kds(k1w001:5) ctw001 in001;
       enddo;

       k1w001c.w1empr = peEmpr;
       k1w001c.w1sucu = peSucu;
       k1w001c.w1nivt = peNivt;
       k1w001c.w1nivc = peNivc;
       k1w001c.w1nctw = peNctw;
       setll %kds(k1w001c:5) ctw001c;
       reade %kds(k1w001c:5) ctw001c in001c;
       dow not %eof;
           if in001c.w1rama = @@rams;
              delete c1w001c;
              ou001c = in001c;
              ou001c.w1rama = @@ramc;
              write c1w001c ou001c;
           endif;
        reade %kds(k1w001c:5) ctw001c in001c;
       enddo;

       k1w002.w2empr = peEmpr;
       k1w002.w2sucu = peSucu;
       k1w002.w2nivt = peNivt;
       k1w002.w2nivc = peNivc;
       k1w002.w2nctw = peNctw;
       setll %kds(k1w002:5) ctw002;
       reade %kds(k1w002:5) ctw002 in002;
       dow not %eof;
           if in002.w2rama = @@rams;
              delete c1w002;
              ou002 = in002;
              ou002.w2rama = @@ramc;
              write c1w002 ou002;
           endif;
        reade %kds(k1w002:5) ctw002 in002;
       enddo;


       return;

      /end-free
