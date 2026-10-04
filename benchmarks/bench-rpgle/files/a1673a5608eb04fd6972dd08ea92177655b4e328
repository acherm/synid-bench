     H nomain
     H datedit(*DMY/)
      * ************************************************************ *
      * SPVFAC: Programa de Servicio.                                *
      *         Facutas ODP                                          *
      * ------------------------------------------------------------ *
      * Alvarez Fernando                     10-Jun-2013             *
      * ************************************************************ *
      * Modificaciones:                                              *
      * SFA 20/01/15 - Controlo CUIT = '00000000000'                 *
      * SFA 16/03/15 - Agrego procedimiento SPVFAC_updFacPacp        *
      *                Agrego procedimiento SPVFAC_updSecu           *
      *                Agrego nuevo campo en CNHFAC                  *
      * ************************************************************ *
     Fcnhfac    uf a e           k disk    usropn
     Fcnhfap    if   e           k disk    usropn

      *--- Copy H -------------------------------------------------- *
      /copy './qcpybooks/spvfac_h.rpgle'

      * --------------------------------------------------- *
      * Setea error global
      * --------------------------------------------------- *
     D SetError        pr
     D  ErrN                         10i 0 const
     D  ErrM                         80a   const

     D ErrN            s             10i 0
     D ErrM            s             80a

     D Initialized     s              1N

      *--- PR Externos --------------------------------------------- *

      *--- Definicion de Procedimiento ----------------------------- *
      * ------------------------------------------------------------ *
      * SPVFAC_chkDispFac(): Valida Disponibilidad Factura ODP       *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peFech   (input)   Fecha                                 *
      *     peEmpr   (output)  Empresa                               *
      *     peSucu   (output)  Sucursal                              *
      *     peArtc   (output)  Codigo Area Tecnica                   *
      *     pePacp   (output)  Numero ODP                            *
      *     peSeco   (output)  Secuencia Comprobante de Pago ODP     *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_chkDispFac...
     P                 B                   export
     D SPVFAC_chkDispFac...
     D                 pi              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peFech                       8  0 options(*nopass:*omit)
     D   peEmpr                       1    options(*nopass:*omit)
     D   peSucu                       2    options(*nopass:*omit)
     D   peArtc                       2  0 options(*nopass:*omit)
     D   pePacp                       6  0 options(*nopass:*omit)
     D   peSeco                       2  0 options(*nopass:*omit)

     Ddisp             s               n

     D k1yfac          ds                  likerec(c1hfac:*key)
     D k2yfac          ds                  likerec(c1hfac:*key)

      /free

       SPVFAC_inz();

       if peCuit = *Blanks or peCuit = '00000000000';
         SetError( SPVFAC_CUITB
                 : 'Cuit en Blanco' );
         return *On;
       endif;

       if %parms >= 5 and %addr(peFech) <> *Null;
         disp = SPVFAC_getEstFac ( peCuit
                                 : peTifa
                                 : peSufa
                                 : peNrfa
                                 : peFech );
       else;
         disp = SPVFAC_getEstFac ( peCuit
                                 : peTifa
                                 : peSufa
                                 : peNrfa );
       endif;

       if disp;
         if %parms >= 6 and %addr(peEmpr) <> *Null;
           peEmpr = *Blanks;
         endif;
         if %parms >= 7 and %addr(peSucu) <> *Null;
           peSucu = *Blanks;
         endif;
         if %parms >= 8 and %addr(peArtc) <> *Null;
           peArtc = *Zeros;
         endif;
         if %parms >= 9 and %addr(pePacp) <> *Null;
           pePacp = *Zeros;
         endif;
         if %parms >= 10 and %addr(peSeco) <> *Null;
           peSeco = *Zeros;
         endif;
         return *On;
       else;
         if %parms >= 5 and %addr(peFech) <> *Null;
           k1yfac.accuit = peCuit;
           k1yfac.actifa = peTifa;
           k1yfac.acsufa = peSufa;
           k1yfac.acnrfa = peNrfa;
           k1yfac.acfech = peFech;
           setgt %kds(k1yfac:5) cnhfac;
           k2yfac.accuit = peCuit;
           k2yfac.actifa = peTifa;
           k2yfac.acsufa = peSufa;
           k2yfac.acnrfa = peNrfa;
           readpe(n) %kds(k2yfac:4) cnhfac;
         else;
           k1yfac.accuit = peCuit;
           k1yfac.actifa = peTifa;
           k1yfac.acsufa = peSufa;
           k1yfac.acnrfa = peNrfa;
           setgt %kds(k1yfac:4) cnhfac;
           readpe(n) %kds(k1yfac:4) cnhfac;
         endif;
         if %parms >= 6 and %addr(peEmpr) <> *Null;
           peEmpr = acempr;
         endif;
         if %parms >= 7 and %addr(peSucu) <> *Null;
           peSucu = acsucu;
         endif;
         if %parms >= 8 and %addr(peArtc) <> *Null;
           peArtc = acartc;
         endif;
         if %parms >= 9 and %addr(pePacp) <> *Null;
           pePacp = acpacp;
         endif;
         if %parms >= 10 and %addr(peSeco) <> *Null;
           peSeco = acseco;
         endif;
         SetError( SPVFAC_FACND
                 : 'Factura no Disponible' );
         return *Off;
       endif;

      /end-free

     P SPVFAC_chkDispFac...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_setFac(): Graba Factura                               *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peFefa   (input)   Fecha Facura                          *
      *     peEmpr   (input)   Empresa                               *
      *     peSucu   (input)   Sucursal                              *
      *     peArtc   (input)   Codigo Area Tecnica                   *
      *     pePacp   (input)   Numero ODP                            *
      *     peComa   (input)   Codigo Mayor Auxiliar                 *
      *     peNrma   (input)   Numero Mayor Auxiliar                 *
      *     peMoti   (input)   Motivo                                *
      *     peUser   (input)   Usuario                               *
      *     peMar1   (input)   Marca Disponible                      *
      *     peSeco   (input)   Secuencia Comprobante ODP             *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_setFac...
     P                 B                   export
     D SPVFAC_setFac...
     D                 pi              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peFefa                       8  0 const
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peArtc                       2  0 const
     D   pePacp                       6  0 const
     D   peComa                       2    const
     D   peNrma                       7  0 const
     D   peMoti                     350    const
     D   peUser                      10    const
     D   peMar1                       1    options(*nopass:*omit)
     D   peSeco                       2  0 options(*nopass:*omit)

      /free

       SPVFAC_inz();

       if peCuit = *Blanks or peCuit = '00000000000';
         SetError( SPVFAC_CUITB
                 : 'Cuit en Blanco' );
         return *Off;
       endif;

       if %parms >= 14 and %addr(peMar1) <> *Null;
         if peMar1 <> 'S' and peMar1 <> 'N';
           SetError( SPVFAC_MARER
                   : 'Marca Erronea' );
           return *Off;
         endif;
       endif;

       accuit = peCuit;
       actifa = peTifa;
       acsufa = peSufa;
       acnrfa = peNrfa;
       acfefa = peFefa;
       acfech = *year*10000+*month*100+*day;
       acsecu = SPVFAC_getSec(peCuit : peTifa : peSufa : peNrfa) + 1;
       acempr = peEmpr;
       acsucu = peSucu;
       acartc = peArtc;
       acpacp = pePacp;
       accoma = peComa;
       acnrma = peNrma;
       acmoti = peMoti;
       acma02 = *Blanks;
       acma03 = *Blanks;
       acma04 = *Blanks;
       acma05 = *Blanks;
       acma06 = *Blanks;
       acma07 = *Blanks;
       acma08 = *Blanks;
       acma09 = *Blanks;
       acma10 = *Blanks;
       if %parms >= 14 and %addr(peMar1) <> *Null;
         acma01 = peMar1;
       else;
         acma01 = 'N';
       endif;
       acuser = peUser;
       acdate = udate;
       actime = %dec(%time():*iso);
       if %parms >= 15 and %addr(peSeco) <> *Null;
         acseco = peSeco;
       else;
         acseco = 1;
       endif;

       write c1hfac;
       return *On;

      /end-free

     P SPVFAC_setFac...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_updFac(): Actualiza Estado en Factura                 *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peUser   (input)   Usuario                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_updFac...
     P                 B                   export
     D SPVFAC_updFac...
     D                 pi              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peUser                      10    const

     D k1yfac          ds                  likerec(c1hfac:*key)
     D k2yfac          ds                  likerec(c1hfac:*key)

     D@@fech           s              8  0
     D@@marc           s              1

      /free

       SPVFAC_inz();

       if peCuit = *Blanks or peCuit = '00000000000';
         SetError( SPVFAC_CUITB
                 : 'Cuit en Blanco' );
         return *Off;
       endif;

       @@Fech = *year*10000+*month*100+*day;
       k1yfac.accuit = peCuit;
       k1yfac.actifa = peTifa;
       k1yfac.acsufa = peSufa;
       k1yfac.acnrfa = peNrfa;
       k1yfac.acfech = @@Fech;
       setgt %kds(k1yfac:5) cnhfac;
       k2yfac.accuit = peCuit;
       k2yfac.actifa = peTifa;
       k2yfac.acsufa = peSufa;
       k2yfac.acnrfa = peNrfa;
       readpe(n) %kds(k2yfac:4) cnhfac;

       if %eof;
         SetError( SPVFAC_FACIN
                 : 'Factura Inexistente' );
         return *Off;
       endif;

       if acma01 = 'S';
         @@marc = 'N';
       else;
         @@marc = 'S';
       endif;

       SPVFAC_setFac ( accuit
                     : actifa
                     : acsufa
                     : acnrfa
                     : acfefa
                     : acempr
                     : acsucu
                     : acartc
                     : acpacp
                     : accoma
                     : acnrma
                     : acmoti
                     : peUser
                     : @@marc
                     : acseco );

       return *On;

      /end-free

     P SPVFAC_updFac...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_getEstFac(): Obitiene Disponibilidad Factura ODP      *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_getEstFac...
     P                 B                   export
     D SPVFAC_getEstFac...
     D                 pi              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peFech                       8  0 options(*nopass:*omit)

     D k1yfac          ds                  likerec(c1hfac:*key)
     D k2yfac          ds                  likerec(c1hfac:*key)

      /free

       SPVFAC_inz();

       if peCuit = *Blanks or peCuit = '00000000000';
         SetError( SPVFAC_CUITB
                 : 'Cuit en Blanco' );
         return *On;
       endif;

       if %parms >= 5 and %addr(peFech) <> *Null;
         k1yfac.accuit = peCuit;
         k1yfac.actifa = peTifa;
         k1yfac.acsufa = peSufa;
         k1yfac.acnrfa = peNrfa;
         k1yfac.acfech = peFech;
         setgt %kds(k1yfac:5) cnhfac;
         k2yfac.accuit = peCuit;
         k2yfac.actifa = peTifa;
         k2yfac.acsufa = peSufa;
         k2yfac.acnrfa = peNrfa;
         readpe(n) %kds(k2yfac:4) cnhfac;
       else;
         k1yfac.accuit = peCuit;
         k1yfac.actifa = peTifa;
         k1yfac.acsufa = peSufa;
         k1yfac.acnrfa = peNrfa;
         setgt %kds(k1yfac:4) cnhfac;
         readpe(n) %kds(k1yfac:4) cnhfac;
       endif;

       select;
       when %eof;
         return *On;
       when acma01 = 'S';
         return *On;
       other;
         return *Off;
       endsl;

      /end-free

     P SPVFAC_getEstFac...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_getSec(): Obtiene Secuencia de nuevo registro         *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *                                                              *
      * Retorna: Secuencia                                           *
      * void                                                         *
      * ------------------------------------------------------------ *

     P SPVFAC_getSec...
     P                 B                   export
     D SPVFAC_getSec...
     D                 pi             3  0
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const

     D k1yfac          ds                  likerec(c1hfac:*key)

     D@@fech           s              8  0

      /free

       SPVFAC_inz();

       @@Fech = *year*10000+*month*100+*day;
       k1yfac.accuit = peCuit;
       k1yfac.actifa = peTifa;
       k1yfac.acsufa = peSufa;
       k1yfac.acnrfa = peNrfa;
       k1yfac.acfech = @@fech;
       setgt %kds(k1yfac:5) cnhfac;
       readpe(n) %kds(k1yfac:5) cnhfac;

       if %eof;
         return *Zeros;
       else;
         return acsecu;
       endif;

      /end-free

     P SPVFAC_getSec...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_chkFac(): Valida si Existe Factura en CNHFAC          *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_chkFac...
     P                 B                   export
     D SPVFAC_chkFac...
     D                 pi              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const

     D k1yfac          ds                  likerec(c1hfac:*key)

      /free

       SPVFAC_inz();

       if peCuit = *Blanks or peCuit = '00000000000';
         SetError( SPVFAC_CUITB
                 : 'Cuit en Blanco' );
         return *Off;
       endif;

       k1yfac.accuit = peCuit;
       k1yfac.actifa = peTifa;
       k1yfac.acsufa = peSufa;
       k1yfac.acnrfa = peNrfa;
       setll %kds(k1yfac:4) cnhfac;

       if not %equal;
         SetError( SPVFAC_FACIN
                 : 'Factura Inexistente' );
         return *Off;
       endif;

       return *On;

      /end-free

     P SPVFAC_chkFac...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_updOdpFac(): Actualiza datos de ODP en factura        *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peEmpr   (input)   Empresa                               *
      *     peSucu   (input)   Sucursal                              *
      *     peArtc   (input)   Codigo Area Tecnica                   *
      *     pePacp   (input)   Numero ODP                            *
      *     peUser   (input)   Usuario                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_updOdpFac...
     P                 B                   export
     D SPVFAC_updOdpFac...
     D                 pi              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peArtc                       2  0 const
     D   pePacp                       6  0 const
     D   peUser                      10    const

     D k1yfac          ds                  likerec(c1hfac:*key)

      /free

       SPVFAC_inz();

       k1yfac.accuit = peCuit;
       k1yfac.actifa = peTifa;
       k1yfac.acsufa = peSufa;
       k1yfac.acnrfa = peNrfa;
       setgt %kds(k1yfac:4) cnhfac;
       readpe %kds(k1yfac:4) cnhfac;

       if %eof;
         SetError( SPVFAC_FACIN
                 : 'Factura Inexistente' );
         return *Off;
       endif;

       acempr = peEmpr;
       acsucu = peSucu;
       acartc = peArtc;
       acpacp = pePacp;
       acuser = peUser;
       acdate = udate;
       actime = %dec(%time():*iso);

       update c1hfac;
       return *On;

      /end-free

     P SPVFAC_updOdpFac...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_getValSini(): Obtiene si valida o no siniestros       *
      *                                                              *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_getValSini...
     P                 B                   export
     D SPVFAC_getValSini...
     D                 pi              n
     D   peFech                       8  0 options(*nopass:*omit)

     D k1yfap          ds                  likerec(c1hfap:*key)

      /free

       SPVFAC_inz();

       if %parms >= 1 and %addr(peFech) <> *Null;
         k1yfap.apfech = peFech;
         setll %kds(k1yfap:1) cnhfap;
       else;
         setll *Start cnhfap;
       endif;

       read(n) cnhfap;

       if apsini = 'S';
         return *On;
       else;
         return *Off;
       endif;

      /end-free

     P SPVFAC_getValSini...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_getValAdmi(): Obtiene si valida o no contaduria       *
      *                                                              *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_getValAdmi...
     P                 B                   export
     D SPVFAC_getValAdmi...
     D                 pi              n
     D   peFech                       8  0 options(*nopass:*omit)

     D k1yfap          ds                  likerec(c1hfap:*key)

      /free

       SPVFAC_inz();

       if %parms >= 1 and %addr(peFech) <> *Null;
         k1yfap.apfech = peFech;
         setll %kds(k1yfap:1) cnhfap;
       else;
         setll *Start cnhfap;
       endif;

       read(n) cnhfap;

       if apadmi = 'S';
         return *On;
       else;
         return *Off;
       endif;

      /end-free

     P SPVFAC_getValAdmi...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_getValLega(): Obtiene si valida o no legales          *
      *                                                              *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_getValLega...
     P                 B                   export
     D SPVFAC_getValLega...
     D                 pi              n
     D   peFech                       8  0 options(*nopass:*omit)

     D k1yfap          ds                  likerec(c1hfap:*key)

      /free

       SPVFAC_inz();

       if %parms >= 1 and %addr(peFech) <> *Null;
         k1yfap.apfech = peFech;
         setll %kds(k1yfap:1) cnhfap;
       else;
         setll *Start cnhfap;
       endif;

       read(n) cnhfap;

       if aplega = 'S';
         return *On;
       else;
         return *Off;
       endif;

      /end-free

     P SPVFAC_getValLega...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_inz(): Inicializa módulo.                             *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     P SPVFAC_inz      B                   export
     D SPVFAC_inz      pi

      /free

       if (initialized);
          return;
       endif;

       if not %open(cnhfac);
         open cnhfac;
       endif;

       if not %open(cnhfap);
         open cnhfap;
       endif;

       initialized = *ON;
       return;

      /end-free

     P SPVFAC_inz      E

      * ------------------------------------------------------------ *
      * SPVFAC_End(): Finaliza módulo.                               *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     P SPVFAC_End      B                   export
     D SPVFAC_End      pi

      /free

       close *all;
       initialized = *OFF;

       return;

      /end-free

     P SPVFAC_End      E

      * ------------------------------------------------------------ *
      * SPVFAC_Error(): Retorna el último error del service program  *
      *                                                              *
      *     peEnbr   (output)  Número de error (opcional)            *
      *                                                              *
      * Retorna: Mensaje de error.                                   *
      * ------------------------------------------------------------ *

     P SPVFAC_Error    B                   export
     D SPVFAC_Error    pi            80a
     D   peEnbr                      10i 0 options(*nopass:*omit)

      /free

       if %parms >= 1 and %addr(peEnbr) <> *NULL;
          peEnbr = ErrN;
       endif;

       return ErrM;

      /end-free

     P SPVFAC_Error    E

      * ------------------------------------------------------------ *
      * SetError(): Setea último error y mensaje.                    *
      *                                                              *
      *     peErrn   (input)   Número de error a setear.             *
      *     peErrm   (input)   Texto del mensaje.                    *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *

     P SetError        B
     D SetError        pi
     D  peErrn                       10i 0 const
     D  peErrm                       80a   const

      /free

       ErrN = peErrn;
       ErrM = peErrm;

      /end-free

     P SetError...
     P                 E

      * ------------------------------------------------------------ *
      * SPVFAC_updFacPacp(): Actualiza Estado en por nro de Comprob. *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peArtc   (input)   Codigo Area Tecnica                   *
      *     pePacp   (input)   Numero ODP                            *
      *     peUser   (input)   Usuario                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     P SPVFAC_updFacPacp...
     P                 B                   export
     D SPVFAC_updFacPacp...
     D                 pi              n
     D   peCuit                      11    const
     D   peArtc                       2  0 const
     D   pePacp                       6  0 const
     D   peUser                      10    const

     D k1yfac          ds                  likerec(c1hfac:*key)

     D@@marc           s              1

      /free

       SPVFAC_inz();

       if peCuit = *Blanks or peCuit = '00000000000';
         SetError( SPVFAC_CUITB
                 : 'Cuit en Blanco' );
         return *Off;
       endif;

       k1yfac.accuit = peCuit;
       setll %kds(k1yfac:1) cnhfac;
       reade(n) %kds(k1yfac:1) cnhfac;

       dow not %eof (cnhfac);

         if acartc = peArtc and acpacp = pePacp;

           if acma01 = 'N';

             @@marc = 'S';

             SPVFAC_setFac ( accuit
                           : actifa
                           : acsufa
                           : acnrfa
                           : acfefa
                           : acempr
                           : acsucu
                           : acartc
                           : acpacp
                           : accoma
                           : acnrma
                           : acmoti
                           : peUser
                           : @@marc
                           : acseco );

           endif;

         endif;

         reade(n) %kds(k1yfac:1) cnhfac;

       enddo;

       return *On;

      /end-free

     P SPVFAC_updFacPacp...
     P                 E
