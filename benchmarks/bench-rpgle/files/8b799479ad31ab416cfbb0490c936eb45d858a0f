     H nomain
     H option(*nodebugio)
      * ************************************************************ *
      * SVPEPV  :Programa de Servicio.                               *
      *          Validación Diferencia Excesiva EPV                  *
      * ------------------------------------------------------------ *
      * Nestor Nelson                        18-Jul-2014             *
      * ************************************************************ *
      *> IGN: DLTMOD MODULE(QTEMP/&N)                         <*  *
      *> IGN: DLTSRVPGM SRVPGM(*LIBL/&N)                      <*  *
      *> CRTRPGMOD MODULE(QTEMP/&N) -                         <*  *
      *>           SRCFILE(&L/&F) SRCMBR(*MODULE) -           <*  *
      *>           DBGVIEW(&DV)                               <*  *
      *> CRTSRVPGM SRVPGM(&O/&ON) -                           <*  *
      *>           MODULE(QTEMP/&N) -                         <*  *
      *>           EXPORT(*SRCFILE) -                         <*  *
      *>           SRCFILE(HDIILE/QSRVSRC) -                  <*  *
      *> TEXT('Programa de Servicio: Validacion Dif.Exc.EPV') <*  *
      *> IGN: DLTMOD MODULE(QTEMP/&N)                         <*  *
      * ************************************************************ *
      * Modificaciones:                                              *
      * LRG - 30/03/17 - Se corrigecalculo de limites de EPV         *
      *                  dentro del PRC _getlimiteProductor          *
      *                                                              *
      * ************************************************************ *

     fset123    if   e           k disk    usropn
     fset6118   if   e           k disk    usropn
     fset621    if   e           k disk    usropn

      *--- Copy H -------------------------------------------------- *
     D/copy HDIILE/QCPYBOOKS,SVPEPV_H

     D @@finpgm        s              3a
     D @RETORNO        s              1n
     D @@FItm          s              8  0
     D @error          s              1n

      * --------------------------------------------------- *
      * Setea procedimientos globales
      * --------------------------------------------------- *
     D SetError        pr
     D  ErrCode                      10i 0 const
     D  ErrText                      80a   const

     D  Errn           s             10i 0
     D  Errm           s             80a

      * ---- claves
     D k1h123          ds                  likerec(s1t123:*key)
     D k1h6118         ds                  likerec(s1t6118:*key)
     D k1h621          ds                  likerec(s1t621:*key)

      *--- Initialized --------------------------------------------- *

     D Initialized     s              1N   inz(*OFF)

      *--- Definición de Procedimientos----------------------------- *

      * ------------------------------------------------------------ *
      * SVPEPV_GETMINMAX(): Accede a Set123 y retorna los campos     *
      *                     de Puntos de EVP de Aumento y Disminución*
      *                                                              *
      *                                                              *
      *     peRama   (input)   Rama                                  *
      *     pepaed   (output)  Puntos de Aumento.                    *
      *     pepded   (output)  Puntos de Disminución.                *
      *                                                              *
      * Retorna: 0 / -1                                              *
      * ------------------------------------------------------------ *

     P SVPEPV_getMinMax...
     P                 B                   export
     D SVPEPV_getMinMax...
     D                 pi            10i 0
     D   peRama                       2  0 const
     D   pePaep                       2  0
     D   pePdep                       2  0
      *

      /free

       SVPEPV_Inz();

       k1h123.t@Rama = peRama;

         //obtengo Rama

       chain %kds(k1h123:1) set123;
1b     if %found;
          eval pepaep = t@paep;
          eval pepdep = t@pdep;
          return 0;
1e     endif;

       seterror (SVPEPV_RANF
                : 'Parámetros para la rama no encontrados.');
       return -1;

      /end-free

     P SVPEPV_getMinMax...
     P                 E

      * ------------------------------------------------------------ *
      * SVPEPV_LIMITEPRODUCTOR(): Accede a set6118 para el productor *
      *                     /rama y calcula peLmin y peLmax con el   *
      *                     valor por default y los recuperados de   *
      *                     GETMINMAX                                *
      *                                                              *
      *     peEmpr   (input)   Empresa                               *
      *     peSucu   (input)   Sucursal.                             *
      *     peNivt   (input)   Nivel del Intermediario.              *
      *     peNivc   (input)   Código del Intermediario.             *
      *     peRama   (input)   Rama                                  *
      *     peLmin   (output)  Limite Minimo                         *
      *     peLmax   (output)  Limite Maximo                         *
      *                                                              *
      * Retorna: 0 / -1                                              *
      * ------------------------------------------------------------ *

     P SVPEPV_getlimiteProductor...
     P                 B                   export
     D SVPEPV_getlimiteProductor...
     D                 pi            10i 0
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peNivt                       1  0 const
     D   peNivc                       5  0 const
     D   peRama                       2  0 const
     D   peLmin                       5  2
     D   peLmax                       5  2
      *
     D   @ePaep        s              2  0
     D   @ePdep        s              2  0

      /free

       SVPEPV_Inz();

       if SVPEPV_getMinMax(peRama:
                           @epaep:
                           @epdep) = -1;
       seterror (SVPEPV_RSCC
                : 'Rama sin condiciones comerciales.');
       return -1;
       endif;

       k1h6118.t@Empr = peEmpr;
       k1h6118.t@Sucu = peSucu;
       k1h6118.t@Nivt = peNivt;
       k1h6118.t@Nivc = peNivc;
       k1h6118.t@Rama = peRama;

         //obtengo Productor/Rama

       chain %kds(k1h6118:5) set6118;
         if not %found( set6118 );

           seterror (SVPEPV_PRSC
                   : 'Productor/Rama sin comisiones ');
           return -1;
         endif;

         //Obtengo el menor entre EPV vs COM...
         select;
           when t@xrea < t@pdn1;
             peLmin = t@xrea;
           when t@pdn1 < t@xrea;
             peLmin = t@pdn1;
           other;
             peLmin = t@pdn1;
         endsl;

         // Determina si el valor de peLmin es menor o mayor al de EPV...
         // Con eso se realiza el calculo para obtener el mínimo...
         if peLmin > @epdep;
           peLmin = @epdep;
         else;
           peLmin = @epdep - ( @epdep - peLmin );
         endif;

         //Obtengo el menor entre EPV vs COM...
         select;
           when t@xrea > t@pdn1;
             peLmax = t@xrea;
           when t@pdn1 > t@xrea;
             peLmax = t@pdn1;
           other;
             peLmax = t@pdn1;
         endsl;

         // Determina si el valor de peLmax es menor o mayor al de EPV...
         // Con eso se realiza el calculo para obtener el màximo...

         if peLmax + @epaep > 100;
            peLmax = @epaep - ( ( peLmax + @epaep ) - 100 );
         else;
            peLmax  = @epaep;
         endif;

       return 0;

      /end-free

     P SVPEPV_getlimiteProductor...
     P                 E

      * ------------------------------------------------------------ *
      * SVPEPV_GETACCION: Accede a Set621 y recupera campo agregado  *
      *                     en Punto 2.                              *
      *                                                              *
      *     peArcd   (input)   Artículo.                             *
      *     peRama   (input)   Rama.                                 *
      *     peArse   (input)   Artículo/Secuencia.                   *
      *     peAcci   (Output)  Acción.                               *
      *                                                              *
      * Retorna: 0 / -1                                              *
      * ------------------------------------------------------------ *

     P SVPEPV_getAccion...
     P                 B                   export
     D SVPEPV_getAccion...
     D                 pi            10i 0
     D   peArcd                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   peAcci                       1
      *

      /free

       SVPEPV_Inz();

       k1h621.t@Arcd = peArcd;
       k1h621.t@Rama = peRama;
       k1h621.t@Arse = peArse;

       chain %kds(k1h621:3) set621;
1b      if %found;
            eval peAcci = t@mar4;
            return 0;
1e      endif;

       seterror (SVPEPV_ASNF
                : 'No se ha encontrado el Artículo/Secuencia');
        return -1;

      /end-free

     P SVPEPV_getAccion...
     P                 E

      * ------------------------------------------------------------ *
      * SVPEPV_CHKEPVINGRESADA: Usa todos los procedimientos anteri- *
      *                     ores y verifica que la EPV ingresada sea *
      *                     correcta                                 *
      *                                                              *
      *     peEmpr   (input)   Empresa.                              *
      *     peSucu   (input)   Sucursal.                             *
      *     peNivt   (input)   Nivel del Intermediario.              *
      *     peNivc   (input)   Código del Intermediario.             *
      *     peArcd   (input)   Artículo.                             *
      *     peRama   (input)   Rama.                                 *
      *     peArse   (input)   Artículo/Secuencia.                   *
      *     peXrea   (input)   Extra Prima Variable Ingresada.       *
      *     peAcci   (output)                                        *
      *                                                              *
      * Retorna: 0 / -1                                              *
      * ------------------------------------------------------------ *

     P SVPEPV_chkEpvIngresada...
     P                 B                   export
     D SVPEPV_chkEpvIngresada...
     D                 pi             1n
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peNivt                       1  0 const
     D   peNivc                       5  0 const
     D   peArcd                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   peXrea                       5  2 const
     D   peAcci                       1
      *
      *
     D   @eLmin        s              5  2
     D   @eLmax        s              5  2
     D   @eAcci        s              1

      /free

       SVPEPV_Inz();

       if SVPEPV_getAccion(peArcd:
                           peRama:
                           peArse:
                           @eAcci)=-1;
       return *off;
       peAcci = '0';
       else;
       peAcci = @eAcci;
       endif;

       if SVPEPV_getLimiteProductor(peEmpr:
                                    peSucu:
                                    peNivt:
                                    peNivc:
                                    peRama:
                                    @eLmin:
                                    @eLmax)=-1;
         return *off;
       endif;

       k1h6118.t@Empr = peEmpr;
       k1h6118.t@Sucu = peSucu;
       k1h6118.t@Nivt = peNivt;
       k1h6118.t@Nivc = peNivc;
       k1h6118.t@Rama = peRama;

       chain %kds(k1h6118:5) set6118;

       if peXrea > ( @elmax + t@xrea ) or peXrea < ( t@xrea - @elmin );
                seterror (SVPEPV_EPVF
                    : 'Extra Prima Variable Fuera de los Limites');
        return *off;
       endif;

       return *on;

      /end-free

     P SVPEPV_chkEpvIngresada...
     P                 E

      * ------------------------------------------------------------ *
      * SVPEPV_inz(): Inicializa módulo.                             *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     P SVPEPV_inz      B                   export
     D SVPEPV_inz      pi

      /free

       monitor;
         if (Initialized);
           return;
         endif;

       if not %open(set123);
         open set123;
       endif;

       if not %open(set6118);
         open set6118;
       endif;

       if not %open(set621);
         open set621;
       endif;

         return;
         on-error;
         Initialized = *OFF;
       endmon;

       /end-free

     P SVPEPV_inz      E

      * ------------------------------------------------------------ *
      * SVPEPV_End(): Finaliza módulo.                               *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     P SVPEPV_End      B                   export
     D SVPEPV_End      pi

      /free

        close *all;
        initialized = *off;

      /end-free

     P SVPEPV_End      E

      * ------------------------------------------------------------ *
      * SetError(): Setea último error y mensaje.                    *
      *                                                              *
      *     peEnum   (input)   Número de error a setear.             *
      *     peEtxt   (input)   Texto del mensaje.                    *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *

     P SetError        B
     D SetError        pi
     D  peEnum                       10i 0 const
     D  peEtxt                       80a   const

      /free

       Errn = peEnum;
       Errm = peEtxt;

      /end-free

     P SetError...
     P                 E

      * ------------------------------------------------------------ *
      * SVPEPV_Error(): Retorna el último error del service program  *
      *                                                              *
      *     peEnbr   (output)  Número de error (opcional)            *
      *                                                              *
      * Retorna: Mensaje de error.                                   *
      * ------------------------------------------------------------ *

     P SVPEPV_Error    B                   export
     D SVPEPV_Error    pi            80a
     D   peEnbr                      10i 0 options(*nopass:*omit)

      /free

       if %parms >= 1 and %addr(peEnbr) <> *NULL;
          peEnbr = Errn;
       endif;

       return Errm;

      /end-free

     P SVPEPV_Error    E

