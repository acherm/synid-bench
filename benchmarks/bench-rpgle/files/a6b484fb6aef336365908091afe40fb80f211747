     H nomain
      * ************************************************************ *
      * SPVTCR: Programa de Servicio.                                *
      *         Tarjetas de Credito.                                 *
      * ------------------------------------------------------------ *
      * Alvarez Fernando                     23-Ene-2014             *
      * ************************************************************ *
      * Modificaciones:                                              *
      * NWN 11/03/2019 - Se agrega nuevo archivo GNTTC9.             *
      *                  Se agrega procedimiento SPVTCR_chkTarjCredito
      * JSN 26/03/2019 - Se agrega procedimiento                     *
      *                  _fechaVencimientoTcr                        *
      *                  _getGnhdtc                                  *
      *                  _getDesbloqueadas                           *
      *                  _setDesbloqueo                              *
      *                  _updFechaVencimiento                        *
      *                  _getNombre                                  *
      * JSN 22/06/2021 - Se agrega el procedimiento _enmascararNumero*
      * ************************************************************ *
     Fgnttc1    if   e           k disk    usropn
     Fgnhdtc    uf a e           k disk    usropn
     Fgnttc9    if   e           k disk    usropn

      *--- Copy H -------------------------------------------------- *

     D/copy './qcpybooks/spvtcr_h.rpgle'

      * --------------------------------------------------- *
      * Setea error global
      * --------------------------------------------------- *
     D setError        pr
     D  ErrN                         10i 0 const
     D  ErrM                         80a   const

     D ErrN            s             10i 0
     D ErrM            s             80a
      * --------------------------------------------------- *
     D Initialized     s              1N

      * --------------------------------------------------- *
      * Valida Fechas
      * --------------------------------------------------- *
     D valFecha        pr             1n
     D  fecha                         6  0 const
     D  mes                           2  0
     D  aÑo                           4  0

     D fecha           s              6  0

      *--- PR Externos --------------------------------------------- *

      *--- Definicion de Procedimiento ----------------------------- *
      * ------------------------------------------------------------ *
      * SPVTCR_chkEmpresa(): Valida Codigo de Empresa Emisora        *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVTCR_chkEmpresa...
     P                 B                   export
     D SPVTCR_chkEmpresa...
     D                 pi              n
     D   peCtcu                       3  0 const

      /free

       SPVTCR_inz();

       chain peCtcu gnttc1;

       if not %found;
         setError( SPVTCR_EMINE
                 : 'Codigo de Empresa Emisora Inexistente' );
         return *Off;
       else;
         if t1bloq <> 'N';
           setError( SPVTCR_EMBLO
                   : 'Codigo de Empresa Emisora Bloqueado' );
           return *Off;
         endif;
       endif;

       return *On;

      /end-free

     P SPVTCR_chkEmpresa...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_getCantDigitos(): Obtiene Cantidad de Digitos de      *
      *                          Tarjeta de Credito                  *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *                                                              *
      * Retorna: Cantidad de Digitos / 0 En caso de Error            *
      * ------------------------------------------------------------ *

     P SPVTCR_getCantDigitos...
     P                 B                   export
     D SPVTCR_getCantDigitos...
     D                 pi             2  0
     D   peCtcu                       3  0 const

      /free

       SPVTCR_inz();

       chain peCtcu gnttc1;

       select;
         when not %found;
           setError( SPVTCR_EMINE
                  : 'Codigo de Empresa Emisora Inexistente' );
           return 0;
         when t1bloq <> 'N';
           setError( SPVTCR_EMBLO
                   : 'Codigo de Empresa Emisora Bloqueado' );
           return t1cdnt;
         other;
           return t1cdnt;
       endsl;

      /end-free

     P SPVTCR_getCantDigitos...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_getMascTc(): Obtiene Mascara de Tarjeta de Credito    *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *                                                              *
      * Retorna: Mascara / 0 En caso de Error                        *
      * ------------------------------------------------------------ *

     P SPVTCR_getMascTc...
     P                 B                   export
     D SPVTCR_getMascTc...
     D                 pi            25
     D   peCtcu                       3  0 const

      /free

       SPVTCR_inz();

       chain peCtcu gnttc1;

       select;
         when not %found;
           SetError( SPVTCR_EMINE
                   : 'Codigo de Empresa Emisora Inexistente' );
           return *Blanks;
         when t1bloq <> 'N';
           SetError( SPVTCR_EMBLO
                   : 'Codigo de Empresa Emisora Bloqueado' );
           return t1ment;
         other;
           return t1ment;
       endsl;

      /end-free

     P SPVTCR_getMascTc...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_getNroTcEdit(): Obtiene Numerp de Tarjeta de Credito  *
      *                        en Formato                            *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *                                                              *
      * Retorna: Numeroo Editado / 0 En caso de Error                *
      * ------------------------------------------------------------ *

     P SPVTCR_getNroTcEdit...
     P                 B                   export
     D SPVTCR_getNroTcEdit...
     D                 pi            20  0
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const

     D  @@ment         s             25                                         PAR350
     D                 ds                                                       PAR350
     D  p@0170                 1     70                                         PAR350
     D  p@0120                 1     20                                         PAR350
     D  p@2145                21     45                                         PAR350
     D  p@4670                46     70                                         PAR350
     D p@46701         s             20  0                                      PAR350

      /free

       SPVTCR_inz();

       @@ment = SPVTCR_getMascTc ( peCtcu );

       if @@ment = *Blanks;
         return *Zeros;
       endif;

      /end-free

     C                   movel     peNrtc        p@0120                                    || PAR35
     C                   eval      p@2145 = @@ment                                         || PAR35
     C                   call      'SPEDI1'                                                || PAR35
     C                   parm                    p@0170                                    || PAR35
     C                   move      p@4670        p@46701                                   || PAR35
     C                   return    p@46701                                                 || PAR35

     P SPVTCR_getNroTcEdit...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_chkNoCero(): Valida Numero de Tarjeta de Credito <>0  *
      *                                                              *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVTCR_chkNoCero...
     P                 B                   export
     D SPVTCR_chkNoCero...
     D                 pi              n
     D   peNrtc                      20  0 const

      /free

       SPVTCR_inz();

       if peNrtc = *zeros;
         setError( SPVTCR_NROCE
                 : 'Numero de Tarjeta de Credito en Cero' );
         return *Off;
       else;
         return *On;
       endif;

      /end-free

     P SPVTCR_chkNoCero...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_chk1erNro(): Valida Primer Numero de Tarjeta de       *
      *                       Credito <> 0                           *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVTCR_chk1erNro...
     P                 B                   export
     D SPVTCR_chk1erNro...
     D                 pi              n
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const

     D  p@0120         s             20
     D  wr1            s              1    dim(20)                              TRABAJO          PAR
     D  x              s              9  0                                      |Indice wrk.   PAR35
     D  @@cdnt         s              2  0                                      |Indice wrk.   PAR35

      /free

       SPVTCR_inz();

       @@cdnt = SPVTCR_getCantDigitos ( peCtcu );

       if @@cdnt = *zeros;
         return *Off;
       endif;

      /end-free

     C                   movel     peNrtc        p@0120                                    || PAR35
     C                   movea     p@0120        wr1                                       || PAR35
     C                   eval      x = @@cdnt - 1                                          || PAR35
     C                   eval      x = 20 - x                                              || PAR35

      /free

3b   if wr1(x) = '0';
         setError( SPVTCR_PNROC
                 : 'Primer Numero de Tarjeta de Credito en Cero' );
         return *Off;
       else;
         return *On;
       endif;

      /end-free

     P SPVTCR_chk1erNro...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_chkNroTcr(): Valida Numero de Tarjeta de Credito      *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVTCR_chkNroTcr...
     P                 B                   export
     D SPVTCR_chkNroTcr...
     D                 pi              n
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const

     D @@Nrtc          s             20  0

      /free

       SPVTCR_inz();

       if not SPVTCR_chkNoCero ( peNrtc );
         return *Off;
       endif;

       @@Nrtc = SPVTCR_getNroTcEdit ( peCtcu
                                    : peNrtc );
       if @@nrtc = *Zeros;
         return *Off;
       endif;

       if not SPVTCR_chk1erNro ( peCtcu
                               : peNrtc );
         return *Off;
       endif;

       return *On;

      /end-free

     P SPVTCR_chkNroTcr...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_chkTcrAse(): Valida si Existe Tarjeta de Credito      *
      *                                                              *
      *     peAsen   (input)   Codigo de Asegurado                   *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVTCR_chkTcrAsen...
     P                 B                   export
     D SPVTCR_chkTcrAsen...
     D                 pi              n
     D   peAsen                       7  0 const
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const

     D k1ydtc          ds                  likerec(g1hdtc:*key)

      /free

       SPVTCR_inz();

       k1ydtc.dfnrdf = peAsen;
       k1ydtc.dfctcu = peCtcu;
       k1ydtc.dfnrtc = peNrtc;
       chain %kds(k1ydtc) gnhdtc;

       select;
         when not %found;
           setError( SPVTCR_TCIAS
                   : 'No Existe Tarjeta de Credito para Asegurado' );
           return *Off;
         when dfbloq <> 'N' and dfbloq <> 'R';
           setError( SPVTCR_TCBAS
                   : 'Tarjeta de Credito Bloqueada para Asegurado' );
           return *Off;
         other;
           return *On;
       endsl;

      /end-free

     P SPVTCR_chkTcrAsen...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_chkTcr(): Valida Tarjeta de Credito                   *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVTCR_chkTcr...
     P                 B                   export
     D SPVTCR_chkTcr...
     D                 pi              n
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const

      /free

       SPVTCR_inz();

       if not SPVTCR_chkEmpresa ( peCtcu );
         return *Off;
       endif;

       if not SPVTCR_chkNroTcr ( peCtcu
                               : peNrtc );
         return *Off;
       endif;

       return *On;

      /end-free

     P SPVTCR_chkTcr...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_setTcr(): Graba Tarjeta de Credito                    *
      *                                                              *
      *     peAsen   (input)   Codigo de Asegurado                   *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *     peFitc   (input)   Fecha Inicio Tarjeta de Credito(MMAAAA)*
      *     peFftc   (input)   Fecha Fin Tarjeta de Credito   (MMAAAA)*
      *     peUser   (input)   Usuario                               *
      *     peVali   (input)   Marca si Debe Validar Datos Recibidos *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVTCR_setTcr...
     P                 B                   export
     D SPVTCR_setTcr...
     D                 pi              n
     D   peAsen                       7  0 const
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const
     D   peFitc                       6  0 const
     D   peFFtc                       6  0 const
     D   peUser                      10    const
     D   peVali                       1n   options(*omit:*nopass)

     D @@vali          s              1n
     D @@feim          s              2  0
     D @@feia          s              4  0
     D @@fefm          s              2  0
     D @@fefa          s              4  0

     D k1ydtc          ds                  likerec(g1hdtc:*key)

      /free

       SPVTCR_inz();

       k1ydtc.dfnrdf = peAsen;
       k1ydtc.dfctcu = peCtcu;
       k1ydtc.dfnrtc = peNrtc;
       setll %kds(k1ydtc) gnhdtc;

       if %equal;
         return *Off;
       endif;

       if %parms >= 7 and %addr(peVali) <> *NULL;
          @@Vali = peVali;
       else;
          @@Vali = *Off;
       endif;

       if @@vali;
         if not SPVTCR_chkEmpresa ( peCtcu );
           return *Off;
         endif;

         if not SPVTCR_chkNroTcr ( peCtcu
                                 : peNrtc );
           return *Off;
         endif;
       endif;

       if SPVTCR_chkTcrAsen ( peAsen
                            : peCtcu
                            : peNrtc );
         setError( SPVTCR_TCEAS
                 : 'Ya Existe Tarjeta de Credito para Asegurado' );
         return *Off;
       endif;

       //if peFitc > peFftc;
       //  setError( SPVTCR_FTCIM
       //          : 'Fecha de Inicio debe ser Menor a la de Fin' );
       //  return *Off;
       //endif;

       valFecha ( peFitc
                : @@feim
                : @@feia );

       valFecha ( peFftc
                : @@fefm
                : @@fefa );

       dfnrdf = peAsen;
       dfctcu = peCtcu;
       dfnrtc = peNrtc;
       dffita = @@feia;
       dffitm = @@feim;
       dfffta = @@fefa;
       dffftm = @@fefm;
       dfgrab = *Blanks;
       dfbloq = 'N';
       dffbta = *zeros;
       dffbtm = *zeros;
       dffbtd = *zeros;
       dfuser = peUser;

       write g1hdtc;
       return *On;

      /end-free

     P SPVTCR_setTcr...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_setBloqTc(): Bloquea Tarjeta de Credito               *
      *                                                              *
      *     peAsen   (input)   Codigo de Asegurado                   *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *     peUser   (input)   Usuario                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVTCR_setBloqTc...
     P                 B                   export
     D SPVTCR_setBloqTc...
     D                 pi              n
     D   peAsen                       7  0 const
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const
     D   peUser                      10    const

     D k1ydtc          ds                  likerec(g1hdtc:*key)

      /free

       SPVTCR_inz();

       k1ydtc.dfnrdf = peAsen;
       k1ydtc.dfctcu = peCtcu;
       k1ydtc.dfnrtc = peNrtc;
       chain %kds(k1ydtc) gnhdtc;

       if not %found;
         setError( SPVTCR_TCIAS
                 : 'No Existe Tarjeta de Credito para Asegurado' );
         return *Off;
       else;
         dffbta = *year;
         dffbtm = *month;
         dffbtd = *day;
         dfuser = peUser;
         dfbloq = 'F';
         update g1hdtc;
         return *On;
       endif;

      /end-free

     P SPVTCR_setBloqTc...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_getNroTcPant(): Obtiene Numero de Tarjeta de Credito  *
      *                        para mostrar en pantalla              *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *                                                              *
      * Retorna: Numero Editado / 0 En caso de Error                 *
      * ------------------------------------------------------------ *

     P SPVTCR_getNroTcPant...
     P                 B                   export
     D SPVTCR_getNroTcPant...
     D                 pi            25
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const

     D                 ds                                                       PAR350
     D  p@0170                 1     70                                         PAR350
     D  p@0120                 1     20                                         PAR350
     D  p@2145                21     45                                         PAR350
     D  p@4670                46     70                                         PAR350

      /free

       SPVTCR_inz();

       p@2145 = SPVTCR_getMascTc ( peCtcu );

       if p@2145 = *Blanks;
         return *Zeros;
       endif;

      /end-free

     C                   movel     peNrtc        p@0120                                    || PAR35
     C                   call      'SPEDI1'                                                || PAR35
     C                   parm                    p@0170                                    || PAR35
     C                   return    p@4670                                                  || PAR35

     P SPVTCR_getNroTcPant...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_inz(): Inicializa módulo.                             *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     P SPVTCR_inz      B                   export
     D SPVTCR_inz      pi

      /free

       if (initialized);
          return;
       endif;

       if not %open(gnttc1);
         open gnttc1;
       endif;

       if not %open(gnhdtc);
         open gnhdtc;
       endif;

       if not %open(gnttc9);
         open gnttc9;
       endif;


       initialized = *ON;

       return;
      /end-free

     P SPVTCR_inz      E

      * ------------------------------------------------------------ *
      * SPVTCR_End(): Finaliza módulo.                               *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     P SPVTCR_end      B                   export
     D SPVTCR_end      pi

      /free

       close *all;
       initialized = *OFF;

       return;

      /end-free

     P SPVTCR_end      E

      * ------------------------------------------------------------ *
      * SPVTCR_chkTarjCredito: Valida Tarjeta de Credito.            *
      *                                                              *
      *        Input :                                               *
      *                peCtcu  -  Código TC                          *
      *                peNrtc  -  Número TC                          *
      *                                                              *
      * Retorna: 0 OK                                                *
      *                                                              *
      *         -1 Empresa inválida                                  *
      *         -2 Cantidad de Dígitos Inválida                      *
      *         -3 Primer dígito significativo 0                     *
      *         -4 Primer dígito segun tabla GNTTC9                  *
      * -------------------------------------------------------------*
     P SPVTCR_chkTarjCredito...
     P                 B                   Export
     D SPVTCR_chkTarjCredito...
     D                 pi            10i 0
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const


     D   k1ytc9        ds                  likerec( g1ttc9  : *key )

     D SPEDI1          pr                  ExtPgm('SPEDI1')
     D  peNrtc                       70a
     D                 ds
     D @nrtc                         20  0
     D @nrtc1                         1  0 dim(20) overlay(@nrtc:1)

     D c70             s             70a
     D nro             s             20a
     D nro_ed          s             25a
     D @@prid          s              1  0
     D x               s             10i 0
     D y               s             10i 0
     D cd              s             10i 0

      /free

       SPVTCR_inz();

       chain peCtcu gnttc1;
       if not %found;
          return -1;
       endif;

       c70  = %editc(peNrtc:'X');
       nro  = %editc(peNrtc:'X');

       %subst(c70:21) = t1ment;
       SPEDI1( c70 );

       nro_ed = %subst(c70:46);

       y = 0;
       for x = 1 to 25;
           if %subst(nro_ed:x:1) = '0' or
              %subst(nro_ed:x:1) = '1' or
              %subst(nro_ed:x:1) = '2' or
              %subst(nro_ed:x:1) = '3' or
              %subst(nro_ed:x:1) = '4' or
              %subst(nro_ed:x:1) = '5' or
              %subst(nro_ed:x:1) = '6' or
              %subst(nro_ed:x:1) = '7' or
              %subst(nro_ed:x:1) = '8' or
              %subst(nro_ed:x:1) = '9';
              y += 1;
           endif;
       endfor;

       if y <> t1cdnt;
          return -2;
       endif;

       cd = t1cdnt - 1;
       cd = 20 - cd;
       if %subst(nro:cd:1) = '0';
          return -2;
       endif;

       @nrtc = peNrtc;

       x = 0;
       for x = 1 to 20;
           if @nrtc1(x) >=1 and @nrtc1(x) <= 9;
              @@prid = @nrtc1(x);
               leave;
              else;
           endif;
       endfor;

       k1ytc9.t9ctcu = peCtcu;
       k1ytc9.t9prid = @@prid;
       chain %kds( k1ytc9 : 2 ) gnttc9;
       if not %found;
          return -4;
       endif;

       return 0;

      /end-free

     P SPVTCR_chkTarjCredito...
     P                 E
      * ------------------------------------------------------------ *
      * SPVTCR_error(): Retorna el último error del service program  *
      *                                                              *
      *     peEnbr   (output)  Número de error (opcional)            *
      *                                                              *
      * Retorna: Mensaje de error.                                   *
      * ------------------------------------------------------------ *

     P SPVTCR_error    B                   export
     D SPVTCR_error    pi            80a
     D   peEnbr                      10i 0 options(*nopass:*omit)

      /free

       if %parms >= 1 and %addr(peEnbr) <> *NULL;
          peEnbr = ErrN;
       endif;

       return ErrM;

      /end-free

     P SPVTCR_error    E

      * ------------------------------------------------------------ *
      * valFecha(): Valida Fecha                                     *
      *                                                              *
      *     peFech   (input)   Fecha                                 *
      *     peFecm   (input)   Mes                                   *
      *     peFeca   (input)   Año                                   *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *

     P valFecha        B
     D valFecha        pi             1n
     D  peFech                        6  0 const
     D  peFecm                        2  0
     D  peFeca                        4  0

     D                 ds
     D  t@0106                01     06  0
     D  t@0102                01     02  0
     D  t@0306                03     06  0
     D                 ds
     D  p@fdma                01     08  0
     D  p@fdia                01     02  0
     D  p@fmes                03     04  0
     D  p@faÑo                05     08  0
     D p@fech          ds
     D  p@flap                01     05  0
     D  p@ffec                06     13  0

     C                   eval      t@0106 = peFech                              ||
     C                   if        t@0102 = *zeros
     C                   movel     01            t@0102
     C                   eval      p@fdma = t@0106
     C                   else
     C                   eval      p@fdma = t@0106
     C                   movel     01            p@fdia
     C                   endif
     C                   eval      p@flap = *zeros                              ||
     C                   eval      p@ffec = p@fdma                              ||
     C                   call      'SPFECH'                                     ||
     C                   parm                    p@fech                         ||
2b C                   if        p@flap = *zeros                              |||
     C                   eval      peFecm = *zeros
     C                   eval      peFeca = *zeros
     C                   return    *off                                         |||
2x C                   else                                                   ||/
     C                   eval      p@fdma = p@ffec                              |||
     C                   eval      peFeca = p@faÑo
     C                   eval      peFecm = p@fmes
     C                   return    *on
2e C                   endif                                                  ||

     P valFecha...
     P                 E
      * ------------------------------------------------------------ *
      * setError(): Setea último error y mensaje.                    *
      *                                                              *
      *     peErrn   (input)   Número de error a setear.             *
      *     peErrm   (input)   Texto del mensaje.                    *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *

     P setError        B
     D setError        pi
     D  peErrn                       10i 0 const
     D  peErrm                       80a   const

      /free

       ErrN = peErrn;
       ErrM = peErrm;

      /end-free

     P setError...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_fechaVencimientoTcr: Retorna fecha de Vencimiento de  *
      *                             la Tarjeta de Credito            *
      *                                                              *
      *     peAsen   (input)   Codigo de Asegurado                   *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *     peFfta   (output)  Año de Vencimiento                    *
      *     peFftm   (output)  Mes de Vencimiento                    *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     P SPVTCR_fechaVencimientoTcr...
     P                 B                   export
     D SPVTCR_fechaVencimientoTcr...
     D                 pi              n
     D   peAsen                       7  0 const
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const
     D   peFfta                       4  0
     D   peFftm                       2  0

     D k1ydtc          ds                  likerec(g1hdtc:*key)

      /free

       SPVTCR_inz();

       k1ydtc.dfnrdf = peAsen;
       k1ydtc.dfctcu = peCtcu;
       k1ydtc.dfnrtc = peNrtc;
       chain(n) %kds(k1ydtc:3) gnhdtc;

       if not %found;
         setError( SPVTCR_TCIAS
                 : 'No Existe Tarjeta de Credito para Asegurado' );
         return *Off;
       else;
         peFfta = dfFfta;
         peFftm = dfFftm;
       endif;

       return *on;

      /end-free

     P SPVTCR_fechaVencimientoTcr...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_getGnhdtc : Retorna Tarjetas de un Asegurado          *
      *                                                              *
      *     peNrdf   ( input  ) Asegurado                            *
      *     peCtcu   ( input  ) Empresa Emisora           (opcional) *
      *     peNrtc   ( input  ) Numero de Tarjeta         (opcional) *
      *     peDsTc   ( output ) Esrtuctura de Tarjetas    (opcional) *
      *     peDsTcC  ( output ) Cantidad de Tarjetas      (opcional) *
      *                                                              *
      * Retorna: *on = Si coincide le Clave / *off = Si no coincide  *
      * ------------------------------------------------------------ *
     P SPVTCR_getGnhdtc...
     P                 B                   export
     D SPVTCR_getGnhdtc...
     D                 pi              n
     D   peNrdf                       7  0 const
     D   peCtcu                       3  0 options( *nopass : *omit )const
     D   peNrtc                      20  0 options( *nopass : *omit )const
     D   peDsTc                            options( *nopass : *omit )
     D                                     likeds ( dsGnhdtc_t ) dim( 99 )
     D   peDsTcC                     10i 0 options( *nopass : *omit )

     D   k1ydtc        ds                  likerec( g1hdtc : *key   )
     D   @@DsITc       ds                  likerec( g1hdtc : *input )
     D   @@DsTc        ds                  likeds ( dsGnhdtc_t ) dim( 99 )
     D   @@DsTcC       s             10i 0

      /free

       SPVTCR_inz();

       clear @@DsTc;
       clear @@DsTcC;

       k1ydtc.dfnrdf = peNrdf;

       if %parms >= 2;
         Select;
           when %addr( peCtcu ) <> *null and
                %addr( peNrtc ) <> *null;

                k1ydtc.dfctcu = peCtcu;
                k1ydtc.dfnrtc = peNrtc;
                setll %kds( k1ydtc : 3 ) gnhdtc;
                reade(n) %kds( k1ydtc : 3 ) gnhdtc @@DsITc;
                dow not %eof( gnhdtc );
                  @@DsTcC += 1;
                  eval-corr @@DsTc( @@DsTcC ) = @@DsITc;
               reade(n) %kds( k1ydtc : 3 ) gnhdtc @@DsITc;
              enddo;
           when %addr( peCtcu ) <> *null and
                %addr( peNrtc ) =  *null;

                k1ydtc.dfctcu = peCtcu;
                setll %kds( k1ydtc : 2 ) gnhdtc;
                reade(n) %kds( k1ydtc : 2 ) gnhdtc @@DsITc;
                dow not %eof( gnhdtc );
                  @@DsTcC += 1;
                  eval-corr @@DsTc( @@DsTcC ) = @@DsITc;
               reade(n) %kds( k1ydtc : 2 ) gnhdtc @@DsITc;
              enddo;
          other;
                setll %kds( k1ydtc : 1 ) gnhdtc;
                reade(n) %kds( k1ydtc : 1 ) gnhdtc @@DsITc;
                dow not %eof( gnhdtc );
                  @@DsTcC += 1;
                  eval-corr @@DsTc( @@DsTcC ) = @@DsITc;
               reade(n) %kds( k1ydtc : 1 ) gnhdtc @@DsITc;
              enddo;
          endsl;
       else;
            setll %kds( k1ydtc : 1 ) gnhdtc;
            reade(n) %kds( k1ydtc : 1 ) gnhdtc @@DsITc;
            dow not %eof( gnhdtc );
              @@DsTcC += 1;
              eval-corr @@DsTc( @@DsTcC ) = @@DsITc;
           reade(n) %kds( k1ydtc : 1 ) gnhdtc @@DsITc;
          enddo;
       endif;

       if %addr( peDsTc ) <> *null;
         eval-corr peDsTc = @@DsTc;
       endif;

       if %addr( peDsTc ) <> *null;
         peDsTcC = @@DsTcC;
       endif;

       if @@DsTcC = 0;
          return *off;
       endif;

       return *on;

      /end-free

     P SPVTCR_getGnhdtc...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_getDesbloqueadas: Retornas Tarjetas Habilitadas para  *
      *                          un asegurado                        *
      *     peNrdf   ( input  ) Asegurado                            *
      *     peDsTc   ( output ) Esrtuctura de Tarjetas               *
      *     peDsTcC  ( output ) Cantidad de Tarjetas                 *
      *                                                              *
      * Retorna: *on = Si coincide le Clave / *off = Si no coincide  *
      * ------------------------------------------------------------ *
     P SPVTCR_getDesbloqueadas...
     P                 B                   export
     D SPVTCR_getDesbloqueadas...
     D                 pi              n
     D   peNrdf                       7  0 const
     D   peDsTc                            likeds ( dsGnhdtc_t ) dim( 99 )
     D   peDsTcC                     10i 0

     D   x             s             10i 0
     D   @@DsTc        ds                  likeds ( dsGnhdtc_t ) dim( 99 )
     D   @@DsTcC       s             10i 0
      /free

       SPVTCR_inz();

       clear @@DsTc;
       clear @@DsTcC;
       clear peDsTc;
       clear peDsTcC;
       if not SPVTCR_getGnhdtc( peNrdf
                              : *omit
                              : *omit
                              : @@DsTc
                              : @@DsTcC );

         return *off;
       endif;

       for x = 1 to @@DsTcC;
         if @@DsTc( x ).dfbloq <> 'F' and
            @@DsTc( x ).dfbloq <> 'T';
            peDsTcC +=1;
            eval-corr peDsTc(peDsTcC) = @@DsTc(x);
         endif;
       endfor;

       if peDsTcC = 0;
         return *off;
       endif;

       return *on;

      /end-free

     P SPVTCR_getDesbloqueadas...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_setDesbloqueo: Desbloquea Tarjeta del asegurado       *
      *                                                              *
      *     peNrdf   ( input  ) Asegurado                            *
      *     peCtcu   ( input  ) Empresa Emisora                      *
      *     peNrtc   ( input  ) Numero de Tarjeta                    *
      *     peUser   ( input  ) Usuario                              *
      *                                                              *
      * Retorna: *on = Si desbloqueo / *off = No debloqueo           *
      * ------------------------------------------------------------ *
     P SPVTCR_setDesbloqueo...
     P                 B                   export
     D SPVTCR_setDesbloqueo...
     D                 pi              n
     D   peNrdf                       7  0 const
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const
     D   peUser                      10    const

     D k1ydtc          ds                  likerec(g1hdtc:*key)

      /free

       SPVTCR_inz();

       k1ydtc.dfnrdf = peNrdf;
       k1ydtc.dfctcu = peCtcu;
       k1ydtc.dfnrtc = peNrtc;
       chain %kds( k1ydtc : 3 ) gnhdtc;
       if not %found( gnhdtc );
         setError( SPVTCR_TCIAS
                 : 'No Existe Tarjeta de Credito para Asegurado' );
         return *off;
       else;
         dfbloq = 'N';
         dfuser = peUser;
         update g1hdtc;
         return *on;
       endif;

      /end-free

     P SPVTCR_setDesbloqueo...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_updFechaVencimiento: Actualiza fecha de Vencimiento   *
      *                             de la Tarjeta de Credito         *
      *                                                              *
      *     peAsen   (input)   Codigo de Asegurado                   *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Numero de Tarjeta de Credito          *
      *     peFfta   (input)   Año de Vencimiento                    *
      *     peFftm   (input)   Mes de Vencimiento                    *
      *     peUser   (input)   Usuario                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     P SPVTCR_updFechaVencimiento...
     P                 B                   export
     D SPVTCR_updFechaVencimiento...
     D                 pi              n
     D   peAsen                       7  0 const
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const
     D   peFfta                       4  0 const
     D   peFftm                       2  0 const
     D   peUser                      10    const

     D k1ydtc          ds                  likerec(g1hdtc:*key)

      /free

       SPVTCR_inz();

       k1ydtc.dfnrdf = peAsen;
       k1ydtc.dfctcu = peCtcu;
       k1ydtc.dfnrtc = peNrtc;
       chain %kds(k1ydtc:3) gnhdtc;
       if not %found;
         setError( SPVTCR_TCIAS
                 : 'No Existe Tarjeta de Credito para Asegurado' );
         return *Off;
       else;
         dfFfta = peFfta;
         dfFftm = peFftm;
         dfuser = peUser;
         update g1hdtc;
       endif;

       return *on;

      /end-free

     P SPVTCR_updFechaVencimiento...
     P                 E

      * ------------------------------------------------------------ *
      * SPVTCR_getNombre: Retorna Nombre de Tarjeta Credito          *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     P SPVTCR_getNombre...
     P                 B                   export
     D SPVTCR_getNombre...
     D                 pi            40
     D   peCtcu                       3  0 const

     D @@Nomb          s             40a

      /free

       SPVTCR_inz();

       clear @@Nomb;

       chain peCtcu gnttc1;
       if not %found;
         setError( SPVTCR_EMINE
                 : 'Codigo de Empresa Emisora Inexistente' );
         return *blanks;
       endif;

       @@Nomb = SVPDAF_getNombre( t1Nrdf );

       return @@Nomb;

      /end-free

     P SPVTCR_getNombre...
     P                 E

      * ------------------------------------------------------------ *
      * SVPTCR_enmascararNumero: Retorna Numero con mascara          *
      *                                                              *
      *     peCtcu   (input)   Codigo de Empresa Emisora             *
      *     peNrtc   (input)   Número de Tarjeta                     *
      *     peCara   (input)   Caracter a usar                       *
      *     peCant   (input)   Cantidad de Nros. visibles            *
      *                                                              *
      * Retorna: Número con mascara                                  *
      * ------------------------------------------------------------ *
     P SPVTCR_enmascararNumero...
     P                 B                   export
     D SPVTCR_enmascararNumero...
     D                 pi            20
     D   peCtcu                       3  0 const
     D   peNrtc                      20  0 const
     D   peCara                       1    const
     D   peCant                      20  0 const

     D SPEDI1          pr                  ExtPgm('SPEDI1')
     D  peNrtc                       70a

     D i               s             10i 0
     D x               s             10i 0
     D c70             s             70a
     D nro_ed          s             20a

      /free

       SPVTCR_inz();

       chain peCtcu gnttc1;
       if not %found;
          return *blanks;
       endif;

       c70 = %editc(peNrtc:'X');
       %subst(c70:21) = t1ment;
       SPEDI1( c70 );

       nro_ed = %subst(c70:52);

       i = 0;
       for x = 20 downto 1;
         if %subst(nro_ed:x:1) <> ' ';
           i += 1;
           if i > peCant;
             %subst(nro_ed:x:1) = peCara;
           endif;
         endif;
       endfor;

       return nro_ed;

      /end-free

     P SPVTCR_enmascararNumero...
     P                 E

