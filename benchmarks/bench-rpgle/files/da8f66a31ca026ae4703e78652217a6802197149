     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
     H alwnull(*usrctl)
      * ************************************************************ *
      * WSRDIA: Producción Por Artículos                             *
      *         Producción diaria por servicio rest (acumulada)      *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *27-Mar-2018            *
      * ------------------------------------------------------------ *
      *                                                              *
      * ************************************************************ *
     Fpahec105  if   e           k disk
     Fpahed0    if   e           k disk
     Fpahed3    if   e           k disk
     Fset001    if   e           k disk

      /copy './qcpybooks/rest_h.rpgle'

     D fech            s             10a
     D empr            s              1a
     D sucu            s              2a
     D aÑo             s              4a
     D mes             s              2a
     D dia             s              2a
     D aÑon            s              4  0
     D mesn            s              2  0
     D dian            s              2  0
     D femi            s              8  0
     D fem2            s              8  0
     D uri             s            512a
     D url             s           3000a   varying
     D x               s              5i 0
     D rc              s              1n

     D ramaDisplay     s             30a
     D panu            s             30a
     D pare            s             30a
     D paep            s             30a
     D paen            s             30a
     D pane            s             30a
     D prex            s             30a
     D comi            s             30a
     D pr              s              5  2
     D @pr             s             10a
     D cp              s              5  2
     D @cp             s             10a
     D @@prex          s             15  2

     D k1hec1          ds                  likerec(p1hec105:*key)
     D k1hed0          ds                  likerec(p1hed0:*key)
     D k1hed3          ds                  likerec(p1hed3:*key)

      * ------------------------------------------------------------ *
      * Para acumular por día                                        *
      * ------------------------------------------------------------ *
     D diario          ds                  qualified dim(100) inz
     D  rama                          2  0
     D  ramd                         20a
     D  ramb                          5a
     D  disp                         50a
     D  canu                         10i 0
     D  panu                         15  2
     D  care                         10i 0
     D  pare                         15  2
     D  caep                         10i 0
     D  paep                         15  2
     D  caen                         10i 0
     D  paen                         15  2
     D  cane                         10i 0
     D  pane                         15  2
     D  reca                         15  2
     D  comi                         15  2

     D PsDs           sds                  qualified
     D  this                         10a   overlay(PsDs:1)

      /free

       *inlr = *on;

       rc  = REST_getUri( psds.this : uri );
       url = %trim(uri);

       // ------------------------------------------
       // Obtener los parámetros de la URL
       // ------------------------------------------
       empr = REST_getNextPart(url);
       sucu = REST_getNextPart(url);
       fech = REST_getNextPart(url);

       aÑo  = %subst(fech:1:4);
       mes  = %subst(fech:6:2);
       dia  = %subst(fech:9:2);
       aÑon = %dec(aÑo:4:0);
       mesn = %dec(mes:2:0);
       dian = %dec(dia:2:0);
       femi = (aÑon * 10000) + (mesn * 100) + dian;
       fem2 = (aÑon * 10000) + (mesn * 100) + 1;

       diario(100).rama = -1;
       diario(100).disp = 'Totales: ';

       k1hec1.c1empr = empr;
       k1hec1.c1sucu = sucu;
       k1hec1.c1femi = fem2;

       setll %kds(k1hec1:3) pahec105;
       reade %kds(k1hec1:2) pahec105;
       dow not %eof;

           if c1femi <= femi;
              k1hed0.d0empr = c1empr;
              k1hed0.d0sucu = c1sucu;
              k1hed0.d0arcd = c1arcd;
              k1hed0.d0spol = c1spol;
              k1hed0.d0sspo = c1sspo;
              setll %kds(k1hed0:5) pahed0;
              reade %kds(k1hed0:5) pahed0;
              dow not %eof;

                  if d0come <= 0;
                     d0come = 1;
                  endif;

                  d0prim *= d0come;
                  d0bpri *= d0come;
                  d0dere *= d0come;
                  d0read *= d0come;
                  d0refi *= d0come;

                     diario(d0rama).rama = d0rama;
                     chain d0rama set001;
                     if not %found;
                        t@ramd = *blanks;
                        t@ramb = *blanks;
                     endif;
                     diario(d0rama).ramd = t@ramd;
                     diario(d0rama).ramb = t@ramb;
                     diario(d0rama).disp = %editc(d0rama:'X')
                                         + ' '
                                         + %trim(t@ramb);
                     select;
                      when d0tiou = 1;
                           diario(d0rama).canu += 1;
                           diario(d0rama).panu += d0prim - d0bpri;
                           diario(100).panu    += d0prim - d0bpri;
                           diario(100).canu    += 1;
                      when d0tiou = 2;
                           diario(d0rama).care += 1;
                           diario(d0rama).pare += d0prim - d0bpri;
                           diario(100).care += 1;
                           diario(100).pare += d0prim - d0bpri;
                      when (d0tiou = 3 and d0prim >= 0) or
                           (d0tiou = 5);
                           diario(d0rama).caep += 1;
                           diario(d0rama).paep += d0prim - d0bpri;
                           diario(100).caep += 1;
                           diario(100).paep += d0prim - d0bpri;
                      when (d0tiou = 3 and d0prim < 0) or
                           (d0tiou = 4);
                           diario(d0rama).caen += 1;
                           diario(d0rama).paen += d0prim - d0bpri;
                           diario(100).caen += 1;
                           diario(100).paen += d0prim - d0bpri;
                     endsl;
                     diario(d0rama).cane += 1;
                     diario(d0rama).pane += d0prim - d0bpri;
                     diario(d0rama).reca += (d0read + d0refi + d0dere);
                     diario(100).cane += 1;
                     diario(100).pane += d0prim - d0bpri;
                     diario(100).reca += (d0read + d0refi + d0dere);
                     k1hed3.d3empr = d0empr;
                     k1hed3.d3sucu = d0sucu;
                     k1hed3.d3arcd = d0arcd;
                     k1hed3.d3spol = d0spol;
                     k1hed3.d3sspo = d0sspo;
                     k1hed3.d3rama = d0rama;
                     k1hed3.d3arse = d0arse;
                     k1hed3.d3oper = d0oper;
                     k1hed3.d3suop = d0suop;
                     setll %kds(k1hed3:9) pahed3;
                     reade %kds(k1hed3:9) pahed3;
                     dow not %eof;
                         d3copr *= d0come;
                         d3ccob *= d0come;
                         d3cfno *= d0come;
                         d3cfnn *= d0come;
                         diario(d0rama).comi += d3copr
                                              + d3ccob
                                              + d3cfno
                                              + d3cfnn;
                         diario(100).comi += d3copr
                                          + d3ccob
                                          + d3cfno
                                          + d3cfnn;
                      reade %kds(k1hed3:9) pahed3;
                     enddo;

               reade %kds(k1hed0:5) pahed0;
              enddo;
           endif;

        reade %kds(k1hec1:2) pahec105;
       enddo;

       REST_writeHeader();
       REST_writeEncoding();

       REST_writeXmlLine( 'produccionDiaria' : '*BEG' );
       REST_writeXmlLine( 'diario' : '*BEG' );

       for x = 1 to 100;
        if diario(x).rama <> 0;
          if x <= 99;
             REST_writeXmlLine( 'linea' : '*BEG' );
           else;
             REST_writeXmlLine( 'diario' : '*END' );
             REST_writeXmlLine( 'total' : '*BEG' );
          endif;
          if diario(x).panu = 0;
             panu = '.00';
           else;
             panu = %editw(diario(x).panu:'           0 .  ');
          endif;
          if diario(x).panu < 0;
             panu = '-' + %trim(panu);
          endif;
          if diario(x).pare = 0;
             pare = '.00';
           else;
             pare = %editw(diario(x).pare:'           0 .  ');
          endif;
          if diario(x).pare < 0;
             pare = '-' + %trim(pare);
          endif;
          if diario(x).paep = 0;
             paep = '.00';
           else;
             paep = %editw(diario(x).paep:'           0 .  ');
          endif;
          if diario(x).paep < 0;
             paep = '-' + %trim(paep);
          endif;
          if diario(x).paen = 0;
             paen = '.00';
           else;
             paen = %editw(diario(x).paen:'           0 .  ');
          endif;
          if diario(x).paen < 0;
             paen = '-' + %trim(paen);
          endif;
          if diario(x).pane = 0;
             pane = '.00';
           else;
             pane = %editw(diario(x).pane:'           0 .  ');
          endif;
          if diario(x).pane < 0;
             pane = '-' + %trim(pane);
          endif;
          @@prex = diario(x).pane + diario(x).reca;
          if @@prex = 0;
             prex = '.00';
           else;
             prex = %editw(@@prex:'           0 .  ');
          endif;
          if @@prex < 0;
             prex = '-' + %trim(prex);
          endif;
         if diario(x).pane <> 0;
            pr = %dech((diario(x).reca/diario(x).pane)*100:5:2);
            @pr = %editw(pr:' 0 .  ');
          else;
            pr = 0;
            @pr = '.00';
         endif;
         if pr < 0;
            @pr = '-' + %trim(@pr);
         endif;
          if diario(x).comi = 0;
             comi = '.00';
           else;
             comi = %editw(diario(x).comi:'           0 .  ');
          endif;
          if diario(x).comi < 0;
             comi = '-' + %trim(comi);
          endif;

          if diario(x).pane <> 0;
             cp = %dech((diario(x).comi/diario(x).pane)*100:5:2);
             @cp = %editw(cp:' 0 .  ');
           else;
             cp = 0;
             @cp = '.00';
          endif;
         if cp < 0;
            @cp = '-' + %trim(@cp);
         endif;

         REST_writeXmlLine('rama' : %editc(diario(x).rama:'X'));
         REST_writeXmlLine('ramd' : %trim(diario(x).ramd));
         REST_writeXmlLine('ramb' : %trim(diario(x).ramb));
         REST_writeXmlLine('ramaDisplay' : diario(x).disp);
         REST_writeXmlLine('cantidadNuevas': %char(diario(x).canu));
         REST_writeXmlLine('primaNuevas': %trim(panu) );
         REST_writeXmlLine('cantidadRenovaciones': %char(diario(x).care));
         REST_writeXmlLine('primaRenovaciones': %trim(pare) );
         REST_writeXmlLine('cantidadEndPositivos': %char(diario(x).caep));
         REST_writeXmlLine('primaEndPositivos': %trim(paep) );
         REST_writeXmlLine('cantidadEndNegativos': %char(diario(x).caen));
         REST_writeXmlLine('primaEndNegativos': %trim(paen) );
         REST_writeXmlLine('cantidadNeta': %char(diario(x).cane));
         REST_writeXmlLine('primaNeta': %trim(pane) );
         REST_writeXmlLine('porcPrimaMasExtra' : %trim(@pr) );
         REST_writeXmlLine('primaMasExtra' : %trim(prex) );
         REST_writeXmlLine('porcComisiones' : %trim(@cp) );
         REST_writeXmlLine('importeComisiones' : %trim(comi) );

         if x <= 99;
            REST_writeXmlLine( 'linea' : '*END' );
          else;
            REST_writeXmlLine( 'total' : '*END' );
         endif;
        endif;
       endfor;

       REST_writeXmlLine( 'produccionDiaria' : '*END' );

       return;

      /end-free

