     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
      * ************************************************************ *
      * WSRLR1: QUOM Versión 2                                       *
      *         Libro rubricado de operaciones en XML                *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *03-May-2021            *
      * ------------------------------------------------------------ *
      * SGF 08/07/21: NRDO con editc X                               *
      * ************************************************************ *
     Fpahlro    if   e           k disk
     Fsehni201  if   e           k disk
     Fpahec1    if   e           k disk
     Fpaher0    if   e           k disk
     Fpahec0    if   e           k disk
     Fpahev1    if   e           k disk
     Fgnhdaf    if   e           k disk
     Fgntloc02  if   e           k disk
     Fset001    if   e           k disk    prefix(t_)
     Fset100    if   e           k disk    prefix(t100_)

      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/GETSYSV_H.rpgle'

     D uri             s            512a
     D url             s           3000a   varying
     D Data            s            512a
     D empr            s              1a
     D sucu            s              2a
     D nivt            s              1a
     D nivc            s              5a
     D nit1            s              1a
     D niv1            s              5a
     D fema            s              4a
     D femm            s              2a
     D quin            s              1a

     D @care           s             10i 0
     D @tiou           s              1  0
     D @tiso           s              1a
     D @nrdo           s             11  0
     D @copo           s              5  0 dim(99999)
     D @ccop           s              5i 0
     D peResp          s             10i 0
     D fecha           s             10
     D x               s             10i 0
     D sumaAsegurada   s             15  2
     D peQuin          s              1  0

     D PsDs           sds                  qualified
     D  this                         10a   overlay(PsDs:1)
     D  JobName                      10a   overlay(PsDs:244)
     D  JobUser                      10a   overlay(PsDs:254)
     D  JobNbr                        6  0 overlay(PsDs:264)

     D k1hlro          ds                  likerec(p1hlro:*key)
     D k1hni2          ds                  likerec(s1hni201 : *key)
     D k1hec1          ds                  likerec(p1hec1   : *key)
     D k1yec0          ds                  likerec(p1hec0   : *key)

     D proNi2          ds                  likerec(s1hni201 : *input)
     D orgNi2          ds                  likerec(s1hni201 : *input)
     D RegEc1          ds                  likerec(p1hec1   : *input)

     D rc              s              1n

      /free

       *inlr = *on;

       rc  = REST_getUri( psds.this : uri );
       if rc = *off;
         REST_writeHeader( 204
                         : *omit
                         : *omit
                         : 'RPG0001'
                         : 40
                         : 'Error al parsear URL'
                         : 'Error al parsear URL' );
         REST_end();
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
       fema = REST_getNextPart(url);
       femm = REST_getNextPart(url);
       quin = REST_getNextPart(url);

       k1hni2.n2empr = Empr;
       k1hni2.n2sucu = Sucu;
       k1hni2.n2nivt = %dec(nivt:1:0);
       k1hni2.n2nivc = %dec(nivc:5:0);
       chain %kds(k1hni2) sehni201 proNi2;
       if not %found;
          return;
       endif;

       if rtvSysName() <> 'POWER7';
          proNi2.n2matr = 1;
       endif;

       monitor;
          peQuin = %dec(quin:1:0);
        on-error;
          peQuin = 0;
       endmon;

       if proNi2.dftiso = 98;
          @tiso = '1';
        else;
          @tiso = '2';
       endif;

       k1hlro.d0empr = empr;
       k1hlro.d0sucu = sucu;
       k1hlro.d0nivt = %dec(nivt:1:0);
       k1hlro.ronivc = %dec(nivc:5:0);
       k1hlro.d0fema = %dec(fema:4:0);
       k1hlro.d0femm = %dec(femm:2:0);
       if peQuin = 1 or peQuin = 2;
         k1hlro.roquin = peQuin;
         setll %kds( k1hlro : 7 ) pahlro;
         reade %kds( k1hlro : 7 ) pahlro;
       else;                            // Todo el mes
         setll %kds( k1hLro : 6 ) pahlro;
         reade %kds( k1hlro : 6 ) pahlro;
       endif;
       dow not %eof;
           @care += 1;
           if peQuin = 1 Or peQuin = 2;
             reade %kds( k1hlro : 7 ) pahlro;
           else;
             reade %kds( k1hlro : 6 ) pahlro;
           endif;
       enddo;

       REST_writeHeader();
       data = '<?xml version="1.0" encoding="utf-8"?>'
            + '<SSN>'
            + '<Cabecera>'
            + '<Productor TipoPersona="'
            + @tiso
            + '" Matricula="'
            + %trim(%char(proNi2.n2matr))
            + '" />'
            + ' <CantidadRegistros>'
            + %trim(%char(@care))
            + '</CantidadRegistros>'
            + '</Cabecera>'
            + '<Detalle>';
       REST_write(data);

       // --------------------------------------------------
       // Procesa el detalle de operaciones
       // --------------------------------------------------
       if peQuin = 1 Or peQuin = 2;
         setll %kds(k1hlro:7) pahlro;
         reade %kds(k1hlro:7) pahlro;
       else;
         setll %kds(k1hlro:6) pahlro;
         reade %kds(k1hlro:6) pahlro;
       endif;

       dow not %eof;
           k1hec1.c1empr = d0empr;
           k1hec1.c1sucu = d0sucu;
           k1hec1.c1arcd = d0arcd;
           k1hec1.c1spol = d0spol;
           k1hec1.c1sspo = d0sspo;
           chain %kds(k1hec1) pahec1 RegEc1;
           if %found;
              chain RegEc1.c1asen gnhdaf;
              if %scan('&':dfnomb) <> 0;
                 dfnomb = %scanrpl( '&' : '&amp;' : dfnomb);
              endif;
              data = '<Registro>'
                   + '<FechaRegistro>'
                   + %editc(RegEc1.c1fema:'X')
                   + '-'
                   + %editc(RegEc1.c1femm:'X')
                   + '-'
                   + %editc(RegEc1.c1femd:'X')
                   + '</FechaRegistro>'
                   + '<Asegurados>';
              REST_write(Data);

              data = '<Asegurado TipoAsegurado="1" TipoDoc="';
              REST_write(Data);
              @nrdo = 0;
              if dftiso = 98;
                 select;
                  when dftido = 1;
                       data = '7"';
                       @nrdo = dfnrdo;
                  when dftido = 2;
                       data = '6"';
                       @nrdo = dfnrdo;
                  when dftido = 3;
                       data = '3"';
                       @nrdo = dfnrdo;
                  when dftido = 4;
                       data = '1"';
                       @nrdo = dfnrdo;
                  when dftido = 5;
                       data = '5"';
                       @nrdo = dfnrdo;
                  when dftido = 99;
                       data = '1"';
                       @nrdo = dfnrdo;
                  other;
                       if %check('0123456789':dfcuit) <> 0;
                          dfcuit = *all'0';
                       endif;
                       if %dec(dfcuit:11:0) <> 0 or dfnjub <> 0;
                          data = '2"';
                          if %dec(dfcuit:11:0) <> 0;
                             @nrdo = %dec(dfcuit:11:0);
                           else;
                             @nrdo = dfnjub;
                          endif;
                       endif;
                 endsl;
               else;
                 if %check('0123456789':dfcuit) <> 0;
                    dfcuit = *all'0';
                 endif;
                 if %dec(dfcuit:11:0) <> 0 or dfnjub <> 0;
                    data = '2"';
                 endif;
                 if dftiso = 81;
                    data = '2"';
                 endif;
                 @nrdo = %dec(dfcuit:11:0);
              endif;
              data = %trim(data)
                   + ' NroDoc="';
              REST_write(Data);

              data = %trim(%editc(@nrdo:'X'))
                   + '" Nombre="'
                   + %trim(dfnomb)
                   + '" />';
              REST_write(Data);

              data = '</Asegurados>';
              REST_write(Data);

              data = '<CPAProponente>'
                   + %trim(%char(dfcopo))
                   + '</CPAProponente>';
              REST_write(Data);

              chain (dfcopo:dfcops) gntloc02;
              if not %found;
                 prprod = *blanks;
                 loloca = *blanks;
              endif;
              data = '<ObsProponente>'
                   + 'P:' + %trim(prprod)
                   + ' L:' + %trim(loloca)
                   + ' D:' + %trim(dfdomi)
                   + '</ObsProponente>';
              REST_write(Data);

              @copo(*) = 0;
              @ccop    = 0;
              setll %kds(k1hec1:5) paher0;
              reade %kds(k1hec1:5) paher0;
              dow not %eof;
                  if %lookup(r0copo:@copo) = 0;
                     @copo(%lookup(0:@copo)) = r0copo;
                     @ccop += 1;
                  endif;
               reade %kds(k1hec1:5) paher0;
              enddo;
              if %lookup( dfcopo : @copo ) = 0;
                 @ccop += 1;
                 @copo(%lookup(0:@copo)) = dfcopo;
              endif;

              data = '<CPACantidad>'
                   + %trim(%char(@ccop))
                   + '</CPACantidad>';
              REST_write(Data);

              data = '<CodigosPostales>';
              REST_write(Data);
              for x = 1 to 99999;
                  if @copo(x) <> 0;
                     data = '<CPA>'
                          + %trim(%char(@copo(x)))
                          + '</CPA>';
                     REST_write(Data);
                   else;
                     leave;
                  endif;
              endfor;
              data = '</CodigosPostales><CiaID>0335</CiaID>';
              REST_write(Data);

              data = '<Organizador TipoPersona="';
              REST_write(Data);

              k1hni2.n2nivt = 3;
              k1hni2.n2nivc = RegEc1.c1niv3;
              chain %kds(k1hni2) sehni201 orgNi2;
              if not %found;
                 orgNi2 = proNi2;
              endif;
              if orgNi2.dftiso = 98;
                 @tiso = '1';
               else;
                 @tiso = '2';
              endif;
              if rtvSysName() <> 'POWER7';
                 orgNi2.n2matr = 1;
              endif;
              data = @tiso
                   + '" Matricula="'
                   + %trim(%char(orgNi2.n2matr))
                   + '" />';
              REST_write(Data);

              chain d0rama set001;
              if not %found;
                 t_t@ramd = *blanks;
              endif;

              data = '<BienAsegurado>'
                   + %trim(t_t@ramd)
                   + '</BienAsegurado>';
              REST_write(Data);

              if d0rama = 12;
                 t_t@rasu = 60;
              endif;
              data = '<Ramo>'
                   + %trim(%char(t_t@rasu))
                   + '</Ramo>';
              REST_write(Data);

              sumaAsegurada = getSumaAsegurada( d0empr
                                              : d0sucu
                                              : d0arcd
                                              : d0spol
                                              : d0sspo
                                              : d0rama
                                              : d0arse
                                              : d0oper
                                              : RegEc1.c1mone
                                              : RegEc1.c1suas );
              if ( sumaAsegurada = *Zeros );
                data = '<SumaAsegurada>0,00</SumaAsegurada>';
                REST_write(Data);
              else;
                data = '<SumaAsegurada>'
                     + %trim(%editw(sumaAsegurada:'             ,  -'))
                     + '</SumaAsegurada>';
                REST_write(Data);
              endif;

              data = '<SumaAseguradaTipo>1</SumaAseguradaTipo>';
              REST_write(Data);

              fecha = %editc(RegEc1.c1fvoa:'X') + '-'
                    + %editc(RegEc1.c1fvom:'X') + '-'
                    + %editc(RegEc1.c1fvod:'X');
              if fecha = '9999-99-99';
                k1yec0.c0empr = regEc1.c1empr;
                k1yec0.c0sucu = regEc1.c1sucu;
                k1yec0.c0arcd = regEc1.c1arcd;
                k1yec0.c0spol = regEc1.c1spol;
                chain %kds ( k1yec0 ) pahec0;
                if %found;
                  fecha = %editc( c0fhfa : 'X' ) + '-'
                        + %editc( c0fhfm : 'X' ) + '-'
                        + %editc( c0fhfd : 'X' );
                endif;
              endif;

              data = '<CoberturaFechaDesde>'
                   + %editc(RegEc1.c1fioa:'X')   + '-'
                   + %editc(RegEc1.c1fiom:'X')   + '-'
                   + %editc(RegEc1.c1fiod:'X')
                   + '</CoberturaFechaDesde>'
                   + '<CoberturaFechaHasta>'
                   + %trim( fecha )
                   + '</CoberturaFechaHasta>';
              REST_write(Data);

              @tiou = RegEc1.c1tiou;
              if RegEc1.c1tiou = 5;
                 @tiou = 3;
              endif;
              data = '<TipoOperacion>'
                   + %trim(%char(@tiou))
                   + '</TipoOperacion>';
              REST_write(Data);

              if @tiou <> 1;
                data = '<Poliza>'
                     + %trim(%char(d0poli))
                     + '</Poliza>';
                REST_write(Data);
              endif;

              data = '<Flota>0</Flota>';
              REST_write(Data);

              data = '<TipoContacto>1</TipoContacto>';
              REST_write(Data);

              data = '</Registro>';
              REST_write(Data);

           endif;

        if peQuin = 1 Or peQuin = 2;
          reade %kds(k1hlro:7) pahlro;
        else;
          reade %kds(k1hlro:6) pahlro;
        endif;

       enddo;

       data = '</Detalle></SSN>';
       REST_write(Data);

       return;

      /end-free

      * ------------------------------------------------------------ *
      * getSumaAsegurada() Retorna suma aseguradas                   *
      *                                                              *
      *     peEmpr (input)  Empresa                                  *
      *     peSucu (input)  Sucursal                                 *
      *     peArcd (input)  Articulo                                 *
      *     peSpol (input)  SuperPoliza                              *
      *     peSspo (input)  Suplemento                               *
      *     peRama (input)  Rama                                     *
      *     peArse (input)  Arse                                     *
      *     peOper (input)  Operacion                                *
      *     peMone (input)  Moneda                                   *
      *     peSuas (input)  Suma Asegurada EC1                       *
      *                                                              *
      * retorna: Suma Asegurada                                      *
      * ------------------------------------------------------------ *
     P getSumaAsegurada...
     P                 B
     D getSumaAsegurada...
     D                 pi            15  2
     D  peEmpr                        1    const
     D  peSucu                        2    const
     D  peArcd                        6  0 const
     D  peSpol                        9  0 const
     D  peSspo                        3  0 const
     D  peRama                        2  0 const
     D  peArse                        2  0 const
     D  peOper                        7  0 const
     D  peMone                        2    const
     D  peSuas                       13  0 const

     D todo223         s               n

     D k1hev1          ds                  likerec( p1hev1 : *key)
     D k1t100          ds                  likerec( s1t100 : *key)

       if peRama <> 89;
         return peSuas;
       endif;

       if peSspo <> *Zeros;
         return peSuas;
       endif;

       todo223 = *On;
       k1hev1.v1empr = peEmpr;
       k1hev1.v1sucu = peSucu;
       k1hev1.v1arcd = peArcd;
       k1hev1.v1spol = peSpol;
       k1hev1.v1sspo = peSspo;
       k1hev1.v1rama = peRama;
       k1hev1.v1arse = peArse;
       k1hev1.v1oper = peOper;
       setll %kds( k1hev1 : 8) pahev1;
       reade %kds( k1hev1 : 8) pahev1;
       dow not %eof( pahev1 );
         if v1xpro <> 223;
           todo223 = *Off;
           leave;
         endif;
         reade %kds( k1hev1 : 8) pahev1;
       enddo;

       if todo223;
         k1t100.t100_t@rama = peRama;
         k1t100.t100_t@xpro = 223;
         k1t100.t100_t@mone = peMone;
         chain %kds( k1t100 : 3 ) set100;
         if %found;
           return t100_t@sac1;
         endif;
       endif;

       return peSuas;

     P getSumaAsegurada...
     P                 E

      /define GETSYSV_LOAD_PROCEDURE
      /copy './qcpybooks/GETSYSV_H.rpgle'


