     H nomain
     H datedit(*DMY/)
      * ************************************************************ *
      * COWRTV: Recuperar datos de una cotización salvada            *
      * ------------------------------------------------------------ *
      * Barranco Julio                       18-Ago-2015             *
      * ------------------------------------------------------------ *
      *> IGN: DLTMOD MODULE(QTEMP/&N)                   <*           *
      *> IGN: DLTSRVPGM SRVPGM(&L/&N)                   <*           *
      *> CRTRPGMOD MODULE(QTEMP/&N) -                   <*           *
      *>           SRCFILE(&L/&F) SRCMBR(*MODULE) -     <*           *
      *>           DBGVIEW(&DV)                         <*           *
      *> CRTSRVPGM SRVPGM(&O/&ON) -                     <*           *
      *>           MODULE(QTEMP/&N) -                   <*           *
      *>           EXPORT(*SRCFILE) -                   <*           *
      *>           SRCFILE(HDIILE/QSRVSRC) -            <*           *
      *>           BNDDIR(HDIILE/HDIBDIR) -             <*           *
      *> TEXT('Prorama de Servicio: Retorna Cotización') <*        *
      *> IGN: DLTMOD MODULE(QTEMP/&N)                   <*           *
      *> IGN: RMVBNDDIRE BNDDIR(HDIILE/HDIBDIR) OBJ((COWRTV)) <*    *
      *> ADDBNDDIRE BNDDIR(HDIILE/HDIBDIR) OBJ((COWRTV)) <*         *
      *> IGN: DLTSPLF FILE(COWRTV)                           <*     *
      * ************************************************************ *
      * Modificaciones:                                              *
      * 15/12/15 - Se realizaron cambios de parametros            *
      * SGF 06/08/2016: Retornar ASEN en _getCabecera()              *
      * SGF 12/08/2016: Retornar IFRA en _getCobVehiculo().          *
      * SGF 16/08/2016: Retornar PROC y RPRO en _getVehiculo().      *
      * SGF 16/08/2016: Retornar PROC en getUbicacion().             *
      * SFA 18/08/2016: Retornar INSP y SUMA en getUbicacion().      *
      * LRG 24/08/2016: Envio de Tipo de vivienda getUbicacion().    *
      * LRG 01/11/2016: Modifica COWRTV_getCobVehiculo(), devuelve   *
      *                 premio del Vehiculo x Cob.                   *
      * LRG 10/11/2016: Modifica _getCobVehiculo(), se devuelve      *
      *                 comisión del premio.                         *
      * SGF 19/01/2017: Depreco "_getCabecera()".                    *
      *                 Uso "_getCabeceraCotizacion()".              *
      * SGF 30/01/2017: En _getComponentesVid2() agrupo por actividad*
      * LRG 15/02/2017: Calcular de manera correcta el Subtotal en   *
      *                 _getImpuestos( peImpu(x).subt)               *
      * JSN 14/03/2017: Se agregan los procedimientos                *
      *                 COWRTV_getVehiculo2                          *
      *                 COWRTV_getVehiculos2                         *
      *                 COWRTV_getCobVehiculo2                       *
      * SGF 27/03/2017: Retornar MA03 en _getUbicacion().            *
      * LRG 18/04/2017: Nuevos procedimientos para retomar una       *
      *                 cotización guardada                          *
      *                 _getComponentesVid3                          *
      *                 _getCoberturasVida2                          *
      *                 _getAsegurado                                *
      * SGF 21/06/2018: Nuevo procedimiento _getComponentesHogar     *
      * JSN 28/02/2019  Recompilacion por cambio en la estructura    *
      *                 PAHASE_T                                     *
      *                                                              *
      * LRG 13/03/2019: Recompilacion por cambio de estructura       *
      *                 peInfv y Tabla ctwet0                        *
      *                 modificacion de getVehiculo2()               *
      *                 se mueven nuevos datos a los campos          *
      *                 peInfv.dweb, peInfv.pweb                     *
      * SGF 23/09/2019: Depreco getVehiculos2() y getVehiculo2().    *
      *                 Se usa getVehiculos3() y getVehiculo3().     *
      * JSN 18/10/2019: Nuevo procedimiento COWRTV_getScoring
      * LRG 15/10/2019: Nuevo procedimiento _getComponentesRGV       *
      *                 Se modifica procedimiento                    *
      *                 COWRTV_getComponentesHogar para que          *
      *                 internamente llame a                         *
      *                 COWRTV_getComponentesRGV                     *
      * LRG 31/07/2020: Modificacion de procedimiento :              *
      *                 _getComponentesRGV                           *
      * JSN 28/05/2021: Se agrega llamar al procedimiento            *
      *                 COWRTV_inz() en _getAsegurado                *
      * SGF 07/03/2022: En _getComponentesRGV2() reemplazo blancos   *
      *                 por "-" en CTA1 y CTA2.                      *
      *                                                              *
      * ************************************************************ *
     Fctw000    if   e           k disk    usropn
     Fctw001    if   e           k disk    usropn
     Fctw001c   if   e           k disk    usropn
     Fctwet0    if   e           k disk    usropn
     Fctwet1    if   e           k disk    usropn
     Fctwet4    if   e           k disk    usropn
     Fctwetc    if   e           k disk    usropn
     Fctwer0    if   e           k disk    usropn
     Fctwer2    if   e           k disk    usropn
     Fctwer4    if   e           k disk    usropn
     Fctwer6    if   e           k disk    usropn
     Fset103    if   e           k disk    usropn
     Fset1031   if   e           k disk    usropn
     Fset250    if   e           k disk    usropn
     Fset160    if   e           k disk    usropn
     Fgntloc02  if   e           k disk    usropn
     Fgntloc    if   e           k disk    usropn
     Fset107    if   e           k disk    usropn
     Fset116    if   e           k disk    usropn prefix(t6:2)
     Fctwev101  if   e           k disk    usropn rename(c1wev1:c1wev101)
     Fctw003    if   e           k disk    usropn

     Fctwev1    if   e           k disk    usropn
     Fctwev2    if   e           k disk    usropn
     Fctwevc    if   e           k disk    usropn
      *--- Copy H -------------------------------------------------- *
      /copy './qcpybooks/cowrtv_h.rpgle'
      /copy './qcpybooks/cowveh_h.rpgle'

     D WSLASE          pr                  ExtPgm('WSLASE')
     D  peBase                             likeds(paramBase) const
     D  peAsen                        7  0 const
     D  peDase                             likeds(pahase_t)
     D  peMase                             likeds(dsMail_t) dim(100)
     D  peMaseC                      10i 0
     D  peErro                             like(paramErro)
     D  peMsgs                             likeds(paramMsgs)


      * --------------------------------------------------- *
      * Setea error global
      * --------------------------------------------------- *
     D wrepl           s          65535a
     D ErrCode         s             10i 0
     D ErrText         s             80A

     Is1t160
     I              t@date                      z@date
      * ---------------------------------------------------------------- *
      *--- Definicion de Procedimiento --------------------------------- *
      * ---------------------------------------------------------------- *
      * COWRTV_getCabecera(): Recupera la cabecera de la Cotización      *
      *                    ****DEPRECATED*****                           *
      *                    Usar getCabeceraCotizacion()                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *        Output:                                                   *
      *                peFctw  -  Fecha de Creación  (aaaammdd)          *
      *                peAsen  -  Código de Cliente (en 0 si es nuevo)   *
      *                peNomb  -  Nombre Asegurado                       *
      *                peMone  -  Código de Moneda                       *
      *                peNmol  -  Descripción de Moneda                  *
      *                peCome  -  Cotización de Moneda                   *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peLoca  -  Localidad                              *
      *                peArcd  -  Código Artículo                        *
      *                peArno  -  Nombre de Artículo                     *
      *                peSpol  -  SuperPóliza                            *
      *                peSspo  -  Suplemento SuperPóliza                 *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de IVA                          *
      *                peNcil  -  Descripción IVA                        *
      *                peTiou  -  Tipo de Operación                      *
      *                peStou  -  Subtipo Operación Usuario              *
      *                peStos  -  Subtipo Operación Sistema              *
      *                peSpo1  -  SuperPóliza Relacionada                *
      *                peCfpg  -  Código Forma de Pago                   *
      *                peDefp  -  Descripción Forma de Pago              *
      *                peNcbu  -  Número de CBU                          *
      *                peCtcu  -  Empresa Tarjeta de Crédito             *
      *                peNrtc  -  Descripción Empresa Tarj de Crédito    *
      *                peFvct  -  FechaVencimiento Tarj Crédito(aaaammdd)*
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getCabecera...
     P                 B                   export
     D COWRTV_getCabecera...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peFctw                       8  0
     D   peAsen                       7  0
     D   peNomb                      40
     D   peMone                       2
     D   peNmol                      30
     D   peCome                       9  6
     D   peCopo                       5  0
     D   peCops                       1  0
     D   peLoca                      25
     D   peArcd                       6  0
     D   peArno                      30
     D   peSpol                       9  0
     D   peSspo                       3  0
     D   peTipe                       1
     D   peCiva                       2  0
     D   peNcil                      30
     D   peTiou                       1  0
     D   peStou                       2  0
     D   peStos                       2  0
     D   peSpo1                       9  0
     D   peCfpg                       3  0
     D   peDefp                      20
     D   peNcbu                      22  0
     D   peCtcu                       3  0
     D   peNrtc                      20  0
     D   peFvct                       6  0
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1y000          ds                  likerec(c1w000:*key)


      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1y000.w0empr = PeBase.peEmpr;
       k1y000.w0sucu = PeBase.peSucu;
       k1y000.w0nivt = PeBase.peNivt;
       k1y000.w0nivc = PeBase.peNivc;
       k1y000.w0nctw = peNctw;

       chain %kds( k1y000 ) ctw000;
       if %found( ctw000 );

         peFctw = w0fctw;
         peNomb = w0nomb;
         peMone = w0mone;
         peNmol = w0noml;
         peCome = w0come;
         peCopo = w0copo;
         peCops = w0cops;
         peLoca = w0loca;
         peArcd = w0arcd;
         peArno = w0arno;
         peSpol = w0spol;
         peSspo = w0sspo;
         peTipe = w0tipe;
         peCiva = w0civa;
         peNcil = w0ncil;
         peTiou = w0tiou;
         peStou = w0stou;
         peStos = w0stos;
         peSpo1 = w0spo1;
         peCfpg = w0nrpp;
         peDefp = w0defp;
         peNcbu = w0ncbu;
         peCtcu = w0ctcu;
         peNrtc = w0nrtc;
         peFvct = w0fvtc;
         peAsen = w0asen;

       endif;

       return;

      /end-free

     P COWRTV_getCabecera...
     P                 E
      * ---------------------------------------------------------------- *
      *                                                                  *
      * COWRTV_getVehiculo(): Recupera los bienes asegurados(Vehículos)  *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                pePoco  -  Número de Componente                   *
      *                peArse  -  Cant.Polizas por Rama/Art              *
      *        Output:                                                   *
      *                peInfV  -  Información del Vehículo               *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getVehiculo...
     P                 B                   export
     D COWRTV_getVehiculo...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   pePoco                       4  0   const
     D   peArse                       2  0   const
     D   peInfV                            likeds(Infvehi)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yet0          ds                  likerec(c1wet0:*key)
     D k1wet1          ds                  likerec(c1wet1:*key)
     D k1tloc          ds                  likerec(g1tloc02:*key)
     D x               s              2  0
     D y               s             10i 0
     D sum_acc         s             15  2

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       clear c1wet0;
       k1yet0.t0empr = PeBase.peEmpr;
       k1yet0.t0sucu = PeBase.peSucu;
       k1yet0.t0nivt = PeBase.peNivt;
       k1yet0.t0nivc = PeBase.peNivc;
       k1yet0.t0nctw = peNctw;
       k1yet0.t0rama = peRama;
       k1yet0.t0poco = pePoco;
       k1yet0.t0Arse = peArse;

       chain %kds( k1yet0 : 8 ) ctwet0;
       if %found( ctwet0 );

         peInfV.Rama = t0rama;
         peInfV.Poco = t0poco;
         peInfV.Arse = t0arse;
         peInfV.Vhmc = t0vhmc;
         peInfV.Vhmo = t0vhmo;
         peInfV.Vhcs = t0vhcs;
         peInfV.Vhcr = t0vhcr;
         peInfV.Vhan = t0vhan;
         peInfV.Vhni = t0vhni;
         peInfV.Moto = t0moto;
         peInfV.Chas = t0chas;
         peInfV.Vhct = t0vhct;
         peInfV.Vhuv = t0vhuv;
         peInfV.M0km = t0m0km;
         peInfV.Copo = t0copo;
         peInfV.Cops = t0cops;
         k1tloc.locopo = t0copo;
         k1tloc.locops = t0cops;
         chain %kds(k1tloc:2) gntloc02;
         if %found;
            peInfv.Rpro = prrpro;
            peInfv.Proc = loproc;
          else;
            peInfv.Rpro = *zeros;
            peInfv.Proc = *blanks;
         endif;
         peInfV.Scta = t0scta;
         peInfV.Mgnc = t0mgnc;
         peInfV.Rgnc = t0rgnc;
         peInfV.Nmat = t0nmat;
         peInfV.Ctre = t0ctre;
         peInfV.Rebr = t0rebr;
         peInfV.Nmer = t0nmer;
         peInfV.Aver = t0aver;
         peInfV.Iris = t0iris;
         peInfV.Cesv = t0cesv;
         COWRTV_getCobVehiculo(peBase:
                               peNctw:
                               peRama:
                               t0arse:
                               t0poco:
                               peInfv.cobe:
                               peInfv.boni:
                               peErro:
                               peMsgs);

         y = 0;
         sum_acc = 0;
         k1wet1.t1empr = t0empr;
         k1wet1.t1sucu = t0sucu;
         k1wet1.t1nivt = t0nivt;
         k1wet1.t1nivc = t0nivc;
         k1wet1.t1nctw = t0nctw;
         k1wet1.t1rama = t0rama;
         k1wet1.t1arse = t0arse;
         k1wet1.t1poco = t0poco;
         setll %kds(k1wet1:8) ctwet1;
         reade %kds(k1wet1:8) ctwet1;
         dow not %eof;
             y += 1;
             sum_acc += t1accv;
             peInfv.Acce(y).secu = t1secu;
             peInfv.Acce(y).accd = t1accd;
             peInfv.Acce(y).accv = t1accv;
             peInfv.Acce(y).mar1 = t1mar1;
          reade %kds(k1wet1:8) ctwet1;
         enddo;

         peInfv.vhvu = t0vhvu - sum_acc;

         return;

       endif;

       return;

      /end-free

     P COWRTV_getVehiculo...
     P                 E
      * ---------------------------------------------------------------- *
      *                                                                  *
      * COWRTV_getVehiculos(): Recupera los bienes asegurados(Vehículos)  *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *        Output:                                                   *
      *                peInfV  -  Información del Vehículo               *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getVehiculos...
     P                 B                   export
     D COWRTV_getVehiculos...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peInfV                            likeds(Infvehi) Dim(10)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yet0          ds                  likerec(c1wet0:*key)
     D x               s              2  0
     D y               s              2  0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yet0.t0empr = PeBase.peEmpr;
       k1yet0.t0sucu = PeBase.peSucu;
       k1yet0.t0nivt = PeBase.peNivt;
       k1yet0.t0nivc = PeBase.peNivc;
       k1yet0.t0nctw = peNctw;
       clear x;
       clear peInfV;

       setll %kds ( k1yet0 : 5 ) ctwet0;
       reade %kds ( k1yet0 : 5 ) ctwet0;
       dow not %eof;

         x += 1;
         COWRTV_getVehiculo(peBase:
                            peNctw:
                            t0rama:
                            t0poco:
                            t0arse:
                            peInfV(x):
                            peErro:
                            peMsgs);


         reade %kds ( k1yet0 : 5 ) ctwet0;
       enddo;

       return;

      /end-free

     P COWRTV_getVehiculos...
     P                 E
      * -----------------------------------------------------------------*
      * COWRTV_getUbicaciones(): Recupera los Bienes asegurados(Hogar)   *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *        Output:                                                   *
      *                peInfu  -  Información de los Bienes              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * -----------------------------------------------------------------*

     P COWRTV_getUbicaciones...
     P                 B                   export
     D COWRTV_getUbicaciones...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peInfU                            likeds(InfUbic) Dim(10)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yer0          ds                  likerec(c1wer0:*key)
     D x               s              2  0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yer0.r0empr = PeBase.peEmpr;
       k1yer0.r0sucu = PeBase.peSucu;
       k1yer0.r0nivt = PeBase.peNivt;
       k1yer0.r0nivc = PeBase.peNivc;
       k1yer0.r0nctw = peNctw;
       clear x;
       clear peInfU;

       setll %kds ( k1yer0 : 5 ) ctwer0;
       reade %kds ( k1yer0 : 5 ) ctwer0;
       dow not %eof;

         x += 1;
         COWRTV_getUbicacion(peBase:
                             peNctw:
                             r0rama:
                             r0poco:
                             r0arse:
                             peInfU(x):
                             peErro:
                             peMsgs);


         reade %kds ( k1yer0 : 5 ) ctwer0;
       enddo;

       return;

      /end-free

     P COWRTV_getUbicaciones...
     P                 E
      * -----------------------------------------------------------------*
      * COWRTV_getUbicacion():   Recupera datos de bien Asegurado        *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                pePoco  -  Número de Componente                   *
      *                peArse  -  Cantidad Polizas por Rama/Articulo     *
      *        Output:                                                   *
      *                peInfu  -  Información de los Bienes              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * -----------------------------------------------------------------*

     P COWRTV_getUbicacion...
     P                 B                   export
     D COWRTV_getUbicacion...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   pePoco                       4  0   const
     D   peArse                       2  0   const
     D   peInfU                            likeds(InfUbic)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yer0          ds                  likerec(c1wer0:*key)
     D k1tloc          ds                  likerec(g1tloc02:*key)
     D @@cobe          ds                  likeds(Cobprima) dim(20)

     D x               s             10i 0
     D rc              s              1N
     D peLbue          s              3  0 dim(10)
     D peLbueC         s             10i 0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       clear c1wer0;
       k1yer0.r0empr = PeBase.peEmpr;
       k1yer0.r0sucu = PeBase.peSucu;
       k1yer0.r0nivt = PeBase.peNivt;
       k1yer0.r0nivc = PeBase.peNivc;
       k1yer0.r0nctw = peNctw;
       k1yer0.r0rama = peRama;
       k1yer0.r0poco = pePoco;
       k1yer0.r0arse = peArse;

       chain %kds( k1yer0 : 8 ) ctwer0;
       if %found( ctwer0 );

         peInfu.Rama = r0rama;
         peInfu.Poco = r0poco;
         peInfu.Arse = r0arse;
         peInfu.Xpro = r0xpro;
         peInfu.Rpro = r0rpro;
         peInfu.Rdes = r0rdes;
         peInfu.Copo = r0copo;
         peInfu.Cops = r0cops;
         peInfu.Suma = r0suas;

         k1tloc.locopo = r0copo;
         k1tloc.locops = r0cops;
         chain %kds(k1tloc:2) gntloc02;
         if %found;
            peInfu.proc = loproc;
          else;
            peInfu.proc = *blanks;
         endif;

         peInfu.Tviv = r0cviv;

         COWRTV_getCobUbicacion(peBase:
                                peNctw:
                                r0Rama:
                                r0arse:
                                r0poco:
                                r0xpro:
                                peInfU.cobe:
                                peErro:
                                peMsgs);

         COWRTV_getCarUbicacion(peBase:
                                peNctw:
                                r0Rama:
                                r0arse:
                                r0poco:
                                peInfU.cara:
                                peErro:
                                peMsgs);

       endif;

       for x = 1 to 20;
         @@cobe(x).riec = peInfu.cobe(x).riec;
         @@cobe(x).xcob = peInfu.cobe(x).xcob;
         @@cobe(x).sac1 = peInfu.cobe(x).sac1;
       endfor;

       peInfU.Insp = COWRGV_GetRequiereInspeccion( peRama
                                                 : @@cobe );

       if SVPBUE_chkProductorEspecial( peBase.peEmpr
                                     : peBase.peSucu
                                     : peBase.peNivt
                                     : peBase.peNivc
                                     : *omit         );
          rc = SVPDRV_getCodBuenResultado( peBase.peEmpr
                                         : peBase.peSucu
                                         : peLbue
                                         : peLbueC       );
          for x = 1 to 20;
              if peInfu.cara(x).ccba <> 0;
                 if %lookup(peInfu.cara(x).ccba:peLbue) <> 0;
                    peInfu.cara(x).ma03 = 'S';
                 endif;
              endif;
          endfor;
       endif;

       return;

      /end-free

     P COWRTV_getUbicacion...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getCobVehiculo(): Recupera las coberturas asociadas       *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                peArse  -  Cantidad Polizas por Rama/Articulo     *
      *                pePoco  -  Número de Componente                   *
      *        Output:                                                   *
      *                peCobV  -  Coberturas                             *
      *                peBonV  -  Bonificaciones                         *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getCobVehiculo...
     P                 B                   export
     D COWRTV_getCobVehiculo...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0   const
     D   pePoco                       4  0   const
     D   peCobV                            likeds(cobVehi) Dim(20)
     D   peBonV                            likeds(BonVeh) Dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yetc          ds                  likerec(c1wetc:*key)
     D y               s             10i 0
     D descob          s             40
     D @@cond          ds                  likeds(condComer_t) dim(99)
     D @@erro          s             10i 0
     D @@msgs          ds                  likeds(paramMsgs)
     D x               s             10i 0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yetc.t0empr = PeBase.peEmpr;
       k1yetc.t0sucu = PeBase.peSucu;
       k1yetc.t0nivt = PeBase.peNivt;
       k1yetc.t0nivc = PeBase.peNivc;
       k1yetc.t0nctw = peNctw;
       k1yetc.t0rama = peRama;
       k1yetc.t0arse = peArse;
       k1yetc.t0poco = pePoco;
       clear y;

       clear peCobV;

       setll %kds( k1yetc : 8 ) ctwetc;
       reade %kds( k1yetc : 8 ) ctwetc;
       dow not %eof;

         y += 1;
         peCobV(y).cobl = t0cobl;
         SPVVEH_CheckCobertura(t0cobl:
                               descob);
         peCobV(y).cobd = descob;
         peCobV(y).rast = t0rras;
         peCobV(y).cras = t0cras;
         peCobV(y).insp = t0rins;
         peCobV(y).sele = t0cobs;
         peCobV(y).ifra = t0ifra;
         COWRTV_getPrimaTot(peBase :
                            peNctw :
                            t0Rama :
                            t0Arse :
                            t0poco :
                            t0cobl :
                            peCobV(y).prim );
         peCobV(y).prem = t0prem;

         // Calcula comision...
         COWRTV_getCondComerciales( peBase
                                  : peNctw
                                  : @@cond
                                  : @@erro
                                  : @@msgs );

         if @@erro = -1;
           peCobV(y).xopr = *Zeros;
         else;
           for x = 1 to 99;
             if @@cond(x).rama = peRama;
               peCobV(y).xopr = ( ( t0prim * @@cond(x).xopr ) / 100 );
               leave;
             endif;
           endfor;
         endif;

         reade %kds( k1yetc : 8 ) ctwetc;
       enddo;

       clear peBonV;
       COWRTV_getBonVehiculo (peBase :
                              peNctw :
                              t0Rama :
                              t0Arse :
                              t0poco :
                              peBonV :
                              peErro :
                              peMsgs );

       return;

      /end-free

     P COWRTV_getCobVehiculo...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getCobUbicacion():Recupera las coberturas asociadas       *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                peArse  -  Cantidad Polizas por Rama/Articulo     *
      *                pePoco  -  Número de Componente                   *
      *                peXpro  -  Código de Producto                     *
      *        Output:                                                   *
      *                peCobU  -  Información del Vehículo               *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getCobUbicacion...
     P                 B                   export
     D COWRTV_getCobUbicacion...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0   const
     D   pePoco                       4  0   const
     D   peXpro                       3  0   const
     D   peCobU                            likeds(cobUbic) Dim(20)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yer2          ds                  likerec(c1wer2:*key)
     D y               s             10i 0
     D descob          s             40
     D k1t107          ds                  likerec(s1t107:*key)
     D k1t116          ds                  likerec(s1t116:*key)

      /free

       COWRTV_inz();

       k1t107.t@rama = peRama;
       k1t116.t6rama = peRama;

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yer2.r2empr = PeBase.peEmpr;
       k1yer2.r2sucu = PeBase.peSucu;
       k1yer2.r2nivt = PeBase.peNivt;
       k1yer2.r2nivc = PeBase.peNivc;
       k1yer2.r2nctw = peNctw;
       k1yer2.r2rama = peRama;
       k1yer2.r2arse = peArse;
       k1yer2.r2poco = pePoco;
       clear y;
       clear peCobu;

       setll %kds( k1yer2 : 8 ) ctwer2;
       reade %kds( k1yer2 : 8 ) ctwer2;
       dow not %eof;

         y += 1;
         peCobu(y).riec = r2riec;
         peCobu(y).xcob = r2xcob;
         peCobu(y).ried = SVPDES_codRiesgo ( peRama : r2riec );
         peCobu(y).cobd = SVPDES_cobCorto  ( peRama : r2xcob );
         peCobu(y).cobl = SVPDES_cobLargo  ( peRama : r2xcob );
         peCobu(y).sac1 = r2saco;
         peCobu(y).prsa = r2prsa;
         peCobu(y).xpri = r2xpri;
         peCobu(y).prim = r2ptco;
         COWRTV_getDatCobFijos( peBase :
                                peNctw :
                                peRama :
                                peXpro :
                                r2riec :
                                r2xcob :
                                peCobu(y).Baop :
                                peCobu(y).Smax :
                                peCobu(y).Smin :
                                peCobu(y).Orie :
                                peCobu(y).Ocob :
                                peCobu(y).Saco );

         COWRTV_getBonUbicacion(peBase :
                                peNctw :
                                peRama :
                                r2Arse :
                                r2poco :
                                r2xcob :
                                peCobu(y).bonu:
                                peErro :
                                peMsgs );

         k1t107.t@cobc = r2xcob;
         chain %kds(k1t107:2) set107;
         if %found;
            k1t116.t6cfac  = t@cfac;
            chain %kds(k1t116:2) set116;
            if %found;
               peCobu(y).cfac = t@cfac;
               peCobu(y).dfac = t6dfac;
             else;
               peCobu(y).cfac = 0;
               peCobu(y).dfac = *all'*';
            endif;
          else;
            peCobu(y).cfac = 0;
            peCobu(y).dfac = *all'*';
         endif;

         reade %kds( k1yer2 : 8 ) ctwer2;
       enddo;

       return;

      /end-free

     P COWRTV_getCobUbicacion...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getCarUbicacion():Recupera las coberturas asociadas       *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                peArse  -  Cantidad Polizas por Rama/Articulo     *
      *                pePoco  -  Número de Componente                   *
      *        Output:                                                   *
      *                peCarU  -  Caracteristicas del bien               *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getCarUbicacion...
     P                 B                   export
     D COWRTV_getCarUbicacion...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0   const
     D   pePoco                       4  0   const
     D   peCarU                            likeds(carUbic) Dim(20)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yer6          ds                  likerec(c1wer6:*key)
     D y               s             10i 0
     D descob          s             40

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yer6.r6empr = PeBase.peEmpr;
       k1yer6.r6sucu = PeBase.peSucu;
       k1yer6.r6nivt = PeBase.peNivt;
       k1yer6.r6nivc = PeBase.peNivc;
       k1yer6.r6nctw = peNctw;
       k1yer6.r6rama = peRama;
       k1yer6.r6arse = peArse;
       k1yer6.r6poco = pePoco;
       clear y;
       clear peCarU;

       setll %kds( k1yer6 : 8 ) ctwer6;
       reade %kds( k1yer6 : 8 ) ctwer6;
       dow not %eof;

         y += 1;
         peCaru(y).ccba = r6ccba;
         peCaru(y).dcba = SVPDES_codCaracteristica(r6empr :
                                                   r6sucu :
                                                   r6rama :
                                                   r6ccba );
         COWRTV_getDatCarFijos( r6empr
                              : r6sucu
                              : r6rama
                              : r6ccba
                              : peCaru(y).ma01
                              : peCaru(y).ma02
                              : peCaru(y).ma03 );

         peCaru(y).ma01m= r6ma01;
         peCaru(y).ma02m= r6ma02;

         reade %kds( k1yer6 : 8 ) ctwer6;
       enddo;

       return;

      /end-free

     P COWRTV_getCarUbicacion...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getBonUbicacion():Recupera las bonificaciones de las      *
      *                          coberturas                              *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                peArse  -  Cantidad Polizas por Rama/Articulo     *
      *                pePoco  -  Número de Componente                   *
      *                peXcob  -  Código de Cobertura                    *
      *        Output:                                                   *
      *                peBonu  -  Datos Bonificacion/Recargo             *
      *                peErro  -  Error                                  *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getBonUbicacion...
     P                 B                   export
     D COWRTV_getBonUbicacion...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0   const
     D   pePoco                       4  0   const
     D   peXcob                       3  0   const
     D   peBonU                            likeds(bonUbic) dim(10)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yer4          ds                  likerec(c1wer4:*key)
     D y               s              2  0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yer4.r4empr = PeBase.peEmpr;
       k1yer4.r4sucu = PeBase.peSucu;
       k1yer4.r4nivt = PeBase.peNivt;
       k1yer4.r4nivc = PeBase.peNivc;
       k1yer4.r4nctw = peNctw;
       k1yer4.r4rama = peRama;
       k1yer4.r4arse = peArse;
       k1yer4.r4poco = pePoco;
       k1yer4.r4xcob = peXcob;
       clear y;
       clear peBonu;

       setll %kds( k1yer4 : 9 ) ctwer4;
       reade %kds( k1yer4 : 9 ) ctwer4;
       dow not %eof;

         y += 1;
         peBonu(y).nive = r4nive;
         peBonu(y).ccbp = r4ccbp;
         peBonu(y).reca = r4reca;
         peBonu(y).boni = r4boni;

         reade %kds( k1yer4 : 9 ) ctwer4;
       enddo;

       return;

      /end-free

     P COWRTV_getBonUbicacion...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getBonVehiculo(): Recupera las bonificaciones de las      *
      *                          coberturas.                             *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                peArse  -  Cantidad Polizas por Rama/Articulo     *
      *                pePoco  -  Número de Componente                   *
      *        Output:                                                   *
      *                peBonv  -  Datos Bonificacion/Recargo             *
      *                peErro  -  Error                                  *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getBonVehiculo...
     P                 B                   export
     D COWRTV_getBonVehiculo...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0   const
     D   pePoco                       4  0   const
     D   peBonv                            likeds(bonVeh) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yet4          ds                  likerec(c1wet4:*key)
     D y               s             10i 0
     D p@Arcd          s              6  0
     D p@pcbm          s              5  2
     D p@pcbx          s              5  2
     D p@modi          s              1

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yet4.t4empr = PeBase.peEmpr;
       k1yet4.t4sucu = PeBase.peSucu;
       k1yet4.t4nivt = PeBase.peNivt;
       k1yet4.t4nivc = PeBase.peNivc;
       k1yet4.t4nctw = peNctw;
       k1yet4.t4rama = peRama;
       k1yet4.t4arse = peArse;
       k1yet4.t4poco = pePoco;
       p@Arcd = COWGRAI_getArticulo ( peBase :
                                     peNctw );
       clear y;
       clear peBonv;

       setll %kds( k1yet4 : 8 ) ctwet4;
       reade %kds( k1yet4 : 8 ) ctwet4;
       dow not %eof;

         y += 1;
         peBonv(y).cobl = t4cobl;
         peBonv(y).ccbp = t4ccbp;
         peBonv(y).dcbp = SVPDES_codBonificacion(t4Empr :
                                                 t4Sucu :
                                                 p@arcd :
                                                 t4rama :
                                                 t4Ccbp );
         peBonv(y).pcbp = t4pcbp * -1;

         COWRTV_getBonFijos ( t4Empr   :
                              t4Sucu   :
                              p@arcd   :
                              t4rama   :
                              t4Ccbp   :
                              p@pcbm   :
                              p@pcbx   :
                              p@modi  );

         peBonv(y).pcbm = p@pcbm * -1;
         peBonv(y).pcbx = p@pcbx * -1;
         peBonv(y).modi = p@modi;

         reade %kds( k1yet4 : 8 ) ctwet4;
       enddo;

       return;

      /end-free

     P COWRTV_getBonVehiculo...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getDatCobFijos():Recupera datos de las coberturas que son *
      *                         fijos asociados al codigo y riesgo       *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                peXpro  -  Código Producto                        *
      *                peRiec  -  Código de Riesgo                       *
      *                peCobc  -  Código de Cobertura                    *
      *        Output:                                                   *
      *                pebaop  -  Básica u Optativa                      *
      *                pesmax  -  Suma Asegurada Máxima                  *
      *                pesmin  -  Suma Asegurada Mínima                  *
      *                peorie  -  Código de Riesgo                       *
      *                peocob  -  Código de Cobertura                    *
      *                pesaco  -  Suma Asegurada Default                 *
      *                                                                  *
      *                                                                  *
      * ---------------------------------------------------------------- *
     P COWRTV_getDatCobFijos...
     P                 B                   export
     D COWRTV_getDatCobFijos...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peXpro                       3  0   const
     D   peRiec                       3      const
     D   peCobc                       3  0   const
     D   peBaop                       1
     D   peSmax                      15  2
     D   peSmin                      15  2
     D   peOrie                       3
     D   peOcob                       3  0
     D   peSaco                      15  2

     D k1y103          ds                  likerec(s1t103:*key)
     D k1y1031         ds                  likerec(s1t1031:*key)

      /free

       COWRTV_inz();

       clear peBaop;
       clear peSaco;
       clear peSmax;
       clear peSmin;
       clear peOrie;
       clear peOcob;

       k1y103.t@rama = peRama;
       k1y103.t@xpro = peXpro;
       k1y103.t@riec = peRiec;
       k1y103.t@cobc = peCobc;
       k1y103.t@mone = COWGRAI_monedaCotizacion ( peBase:
                                                  peNctw );
       chain %kds( k1y103 : 5 ) set103;
       if %found;

         peBaop = t@baop;
         peSaco = t@saco;

       endif;

       chain %kds( k1y103 : 5 ) set1031;
       if %found;

         peSmax = t@sacox;
         peSmin = t@lmin;
         peOrie = t@riecx;
         peOcob = t@cobcx;

       endif;

       return;

      /end-free

     P COWRTV_getDatCobFijos...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getDatCarFijos():Recupera datos de caracteristicas que son*
      *                         fijas asociadas a la rama y codigo de    *
      *                         caracteristicas.                         *
      *        Input :                                                   *
      *                                                                  *
      *                peEmpr  -  Código de Empresa                      *
      *                peSucu  -  Código de Sucursal                     *
      *                peRama  -  Rama                                   *
      *                peCcba  -  Cod.Caracteristica del Bien            *
      *        Output:                                                   *
      *                peMa01  -  VALOR POR DEFECTO                      *
      *                peMa02  -  APLICA POR DEFECTO                     *
      *                peMa03  -  Permite modificas Tiene/no Tiene (Opc) *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getDatCarFijos...
     P                 B                   export
     D COWRTV_getDatCarFijos...
     D                 pi
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peRama                       2  0 const
     D   peCcba                       3  0 const
     D   peMa01                       1
     D   peMa02                       1
     D   peMa03                       1a   options(*nopass:*omit)

     D k1y160          ds                  likerec(s1t160:*key)

      /free

       COWRTV_inz();

       peMa01 = *Blanks;
       peMa02 = *Blanks;

       if %parms >= 7 and %addr(peMa03) <> *null;
          peMa03 = *blanks;
       endif;

       k1y160.t@empr = peEmpr;
       k1y160.t@sucu = peSucu;
       k1y160.t@rama = peRama;
       k1y160.t@ccba = peCcba;

       chain %kds( k1y160 ) set160;
       if %found( set160 );

         peMa01 = t@Ma01;
         peMa02 = t@Ma02;

         if %parms >= 7 and %addr(peMa03) <> *null;
            peMa03 = t@ma04;
         endif;

       endif;

       return;

      /end-free

     P COWRTV_getDatCarFijos...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getBonFijos():Recupera los campos de bonificacion que son *
      *                      fijos de automovil                          *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peEmpr  -  Código de Empresa                      *
      *                peSucu  -  Código de Sucursal                     *
      *                peArcd  -  Código de Artículo                     *
      *                peRama  -  Rama                                   *
      *                peCcbp  -  Código de Componente Bonifi            *
      *                                                                  *
      *        Output:                                                   *
      *                                                                  *
      *                peEppd  -  Rango Desde Compo.Bonif.               *
      *                peEpph  -  Rango Hasta Compo.Bonif.               *
      *                peMcbp  -  S/N Permite o no cambiar %             *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getBonFijos...
     P                 B                   export
     D COWRTV_getBonFijos...
     D                 pi
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peArcd                       6  0 const
     D   peRama                       2  0 const
     D   peCcbp                       3  0 const
     D   peEppd                       5  2
     D   peEpph                       5  2
     D   peMcbp                       1

     D k1y250          ds                  likerec(s1t250:*key)

      /free

       COWRTV_inz();

       peEppd = *Zeros;
       peEpph = *Zeros;
       peMcbp = *Blanks;

       k1y250.stEmpr = peEmpr;
       k1y250.stSucu = peSucu;
       k1y250.stArcd = peArcd;
       k1y250.stRama = peRama;
       k1y250.stCcbp = peCcbp;
       k1y250.stmar1 = 'C';

       chain %kds( k1y250 : 6 ) set250;
       if %found( set250 );

         peEppd = stEppd;
         peEpph = stEpph;
         peMcbp = stmar6;

       endif;

       return;

      /end-free

     P COWRTV_getBonFijos...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getPrimaTot():Recupera la prima total de la cobertura     *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                peArse  -  Cantidad Polizas por Rama/Articulo     *
      *                pePoco  -  Número de Componente                   *
      *                peCobl  -  Cobertura                              *
      *                peCobl  -  Prima Total                            *
      *                                                                  *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getPrimaTot...
     P                 B                   export
     D COWRTV_getPrimaTot...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0   const
     D   pePoco                       4  0   const
     D   peCobl                       2      const
     D   pePrim                      15  2

     D k1yetc          ds                  likerec(c1wetc:*key)

      /free

       COWRTV_inz();

       pePrim = *Zeros;

       k1yetc.t0empr = PeBase.peEmpr;
       k1yetc.t0sucu = PeBase.peSucu;
       k1yetc.t0nivt = PeBase.peNivt;
       k1yetc.t0nivc = PeBase.peNivc;
       k1yetc.t0nctw = peNctw;
       k1yetc.t0rama = peRama;
       k1yetc.t0arse = peArse;
       k1yetc.t0poco = pePoco;
       k1yetc.t0cobl = peCobl;

       chain %kds( k1yetc : 9 ) ctwetc;
       if %found;

         pePrim = t0prim;

       else;

         pePrim = *Zeros;

       endif;

       return;

      /end-free

     P COWRTV_getPrimaTot...
     P                 E
      * ------------------------------------------------------------ *
      * COWRTV_getOperacion(): Devuelve tipo y subtipo de operacion. *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peTiou  -  Tipo operacion usuario             *
      *                peStou  -  Subtipo operacion usuario          *
      *                peStos  -  Subtipo operacion sistema          *
      *                                                              *
      * ------------------------------------------------------------ *

     P COWRTV_getOperacion...
     P                 B                   export
     D COWRTV_getOperacion...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peTiou                       1  0
     D   peStou                       2  0
     D   peStos                       2  0

     D k1y000          ds                  likerec(c1w000:*key)

      /free

       COWRTV_inz();

       peTiou = *Zeros;
       peStou = *Zeros;
       peStos = *Zeros;

       k1y000.w0empr = PeBase.peEmpr;
       k1y000.w0sucu = PeBase.peSucu;
       k1y000.w0nivt = PeBase.peNivt;
       k1y000.w0nivc = PeBase.peNivc;
       k1y000.w0nctw = peNctw;

       chain %kds( k1y000 : 5 ) ctw000;
       if %found( ctw000 );

         peTiou = w0tiou;
         peStou = w0stou;
         peStos = w0stos;

       endif;

       return;

      /end-free

     P COWRTV_getOperacion...
     P                 E
      * ------------------------------------------------------------ *
      * COWRTV_getImpuestos(): Devuelve tipo y subtipo de operacion. *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peImpu  -  Impuestos                          *
      *                                                              *
      * ------------------------------------------------------------ *

     P COWRTV_getImpuestos...
     P                 B                   export
     D COWRTV_getImpuestos...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peImpu                            likeds(primPrem) dim(99)

     D k1y001          ds                  likerec(c1w001:*key)

     D x               s             10i 0

      /free

       COWRTV_inz();

       k1y001.w1empr = PeBase.peEmpr;
       k1y001.w1sucu = PeBase.peSucu;
       k1y001.w1nivt = PeBase.peNivt;
       k1y001.w1nivc = PeBase.peNivc;
       k1y001.w1nctw = peNctw;

       x = *Zeros;

       setll %kds( k1y001 : 5 ) ctw001;
       reade %kds( k1y001 : 5 ) ctw001;

       dow not %eof( ctw001 );

         x += 1;

         peImpu(x).rama = w1rama;
         peImpu(x).arse = 1;
         peImpu(x).prim = COWGRAI_getPrimaRamaArse ( peBase : peNctw
                                                   : w1rama : 1 );
         peImpu(x).xref = w1xref;
         peImpu(x).refi = ( ( peImpu(x).prim * w1xref ) / 100 );
         peImpu(x).dere = w1dere;
         peImpu(x).subt = COWGRAI_getPrimaSubtot ( peBase
                                                 : peNctw
                                                 : w1rama
                                                 : peImpu(x).prim  );
         peImpu(x).seri = w1seri;
         peImpu(x).seem = w1seem;
         peImpu(x).pimi = w1pimi;
         peImpu(x).impi = w1impi;
         peImpu(x).psso = w1psso;
         peImpu(x).sers = w1sers;
         peImpu(x).pssn = w1pssn;
         peImpu(x).tssn = w1tssn;
         peImpu(x).pivi = w1pivi;
         peImpu(x).ipr1 = w1ipr1;
         peImpu(x).pivn = w1pivn;
         peImpu(x).ipr4 = w1ipr4;
         peImpu(x).pivr = w1pivr;
         peImpu(x).ipr3 = w1ipr3;
         peImpu(x).ipr5 = w1ipr5;
         peImpu(x).ipr6 = w1ipr6;
         peImpu(x).ipr7 = w1ipr7;
         peImpu(x).ipr8 = w1ipr8;
         peImpu(x).ipr9 = w1ipr9;
         peImpu(x).prem = w1prem;

         reade %kds( k1y001 : 5 ) ctw001;

       enddo;

       return;

      /end-free

     P COWRTV_getImpuestos...
     P                 E
      * ------------------------------------------------------------ *
      * COWRTV_getCondComerciales() Retorna condiciones comerciales  *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peCond  -  Condiciones Comerciales            *
      *                peErro  -  Error                              *
      *                peMsgs  -  Estructura de Error                *
      *                                                              *
      * ------------------------------------------------------------ *

     P COWRTV_getCondComerciales...
     P                 B                   export
     D COWRTV_getCondComerciales...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peCond                            likeds(condComer_t) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1y001          ds                  likerec(c1w001c:*key)

     D x               s             10i 0

      /free

       COWRTV_inz();

       k1y001.w1empr = PeBase.peEmpr;
       k1y001.w1sucu = PeBase.peSucu;
       k1y001.w1nivt = PeBase.peNivt;
       k1y001.w1nivc = PeBase.peNivc;
       k1y001.w1nctw = peNctw;

       x = *Zeros;

       setll %kds( k1y001 : 5 ) ctw001c;
         if not %equal( ctw001c );

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0127'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );
           peErro = -1;
           return;

         endif;

       reade %kds( k1y001 : 5 ) ctw001c;

       dow not %eof( ctw001c );

         x += 1;

         peCond(x).rama = w1rama;
         peCond(x).arse = 1;
         peCond(x).xrea = w1xrea;
         peCond(x).read = w1read;
         peCond(x).xopr = w1xopr;
         peCond(x).copr = w1copr;

         reade %kds( k1y001 : 5 ) ctw001c;

       enddo;

       return;

      /end-free

     P COWRTV_getCondComerciales...
     P                 E
      * ------------------------------------------------------------ *
      * COWRTV_getComponenteVida() Retorna todos componentes de Vida *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peCond  -  Condiciones Comerciales            *
      *                                                              *
      * ------------------------------------------------------------ *

     P COWRTV_getComponenteVida...
     P                 B                   export
     D COWRTV_getComponenteVida...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peComp                            likeds(CompVida)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yev1          ds                  likerec(c1wev1:*key)
     D k1yevc          ds                  likerec(c1wevc:*key)

     D x               s             10i 0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yev1.v1empr = PeBase.peEmpr;
       k1yev1.v1sucu = PeBase.peSucu;
       k1yev1.v1nivt = PeBase.peNivt;
       k1yev1.v1nivc = PeBase.peNivc;
       k1yev1.v1nctw = peNctw;
       k1yev1.v1rama = perama;
       k1yev1.v1arse = pearse;
       k1yev1.v1poco = pepoco;

       x = *Zeros;
       clear peComp;

       chain %kds( k1yev1 : 8 ) ctwev1;
       if %found( ctwev1 );

         peComp.Rama = v1Rama;
         peComp.Arse = 1;
         peComp.Poco = v1Poco;
         peComp.Paco = v1Paco;
         peComp.Acti = v1Acti;
         peComp.Secu = v1Secu;
         peComp.Xpro = v1Xpro;
         peComp.Nomb = v1Nomb;
         peComp.Tido = v1Tido;
         peComp.Nrdo = v1Nrdo;
         peComp.Fnac = v1Fnac;
         peComp.Naci = v1Naci;
         peComp.Cate = v1Cate;

         COWRTV_getCoberturasVida ( peBase :
                                    peNctw :
                                    v1Rama :
                                    v1Arse :
                                    v1Poco :
                                    peComp.Cobe :
                                    peErro :
                                    peMsgs );

         k1yevc.v0empr = PeBase.peEmpr;
         k1yevc.v0sucu = PeBase.peSucu;
         k1yevc.v0nivt = PeBase.peNivt;
         k1yevc.v0nivc = PeBase.peNivc;
         k1yevc.v0nctw = peNctw;
         k1yevc.v0rama = perama;
         k1yevc.v0arse = pearse;
         k1yevc.v0acti = v1acti;
         k1yevc.v0secu = v1secu;

         chain %kds( k1yevc : 9 ) ctwevc;
         if %found( ctwevc );

           if v0cant<>0;

             peComp.Prem = v0Prem / v0cant;

           endif;

         endif;

       endif;

       return;

      /end-free

     P COWRTV_getComponenteVida...
     P                 E
      * ------------------------------------------------------------ *
      * COWRTV_getComponentesVida() Retorna todos componentes de Vida*
      *                                                              *
      *  ****** DEPRECATED ****** Usar _getComponentesVid2()         *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peCond  -  Condiciones Comerciales            *
      *                                                              *
      * ------------------------------------------------------------ *

     P COWRTV_getComponentesVida...
     P                 B                   export
     D COWRTV_getComponentesVida...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peComp                            likeds(CompVida) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yev1          ds                  likerec(c1wev1:*key)
     D k1yevc          ds                  likerec(c1wevc:*key)
     D p@Cobe          ds                  likeds(CobeVida) dim(10)

     D x               s             10i 0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yev1.v1empr = PeBase.peEmpr;
       k1yev1.v1sucu = PeBase.peSucu;
       k1yev1.v1nivt = PeBase.peNivt;
       k1yev1.v1nivc = PeBase.peNivc;
       k1yev1.v1nctw = peNctw;

       x = *Zeros;
       clear peComp;

       setll %kds( k1yev1 : 5 ) ctwev1;
       reade %kds( k1yev1 : 5 ) ctwev1;

       dow not %eof( ctwev1 );

         x += 1;

         peComp(x).Rama = v1Rama;
         peComp(x).Arse = 1;
         peComp(x).Poco = v1Poco;
         peComp(x).Paco = v1Paco;
         peComp(x).Acti = v1Acti;
         peComp(x).Secu = v1Secu;
         peComp(x).Xpro = v1Xpro;
         peComp(x).Nomb = v1Nomb;
         peComp(x).Tido = v1Tido;
         peComp(x).Nrdo = v1Nrdo;
         peComp(x).Fnac = v1Fnac;
         peComp(x).Naci = v1Naci;
         peComp(x).Cate = v1Cate;

         COWRTV_getCoberturasVida ( peBase :
                                    peNctw :
                                    v1Rama :
                                    v1Arse :
                                    v1Poco :
                                    p@Cobe :
                                    peErro :
                                    peMsgs );

         pecomp(x).cobe = p@Cobe;

         k1yevc.v0empr = PeBase.peEmpr;
         k1yevc.v0sucu = PeBase.peSucu;
         k1yevc.v0nivt = PeBase.peNivt;
         k1yevc.v0nivc = PeBase.peNivc;
         k1yevc.v0nctw = peNctw;
         k1yevc.v0rama = v1rama;
         k1yevc.v0arse = v1arse;
         k1yevc.v0acti = v1acti;
         k1yevc.v0secu = v1secu;

         chain %kds( k1yevc : 9 ) ctwevc;
         if %found( ctwevc );

           if v0cant<>0;

             peComp(x).Prem = v0Prem / v0cant;

           endif;

         endif;

         reade %kds( k1yev1 : 5 ) ctwev1;

       enddo;

       return;

      /end-free

     P COWRTV_getComponentesVida...
     P                 E
      * ------------------------------------------------------------ *
      * COWRTV_getComponentesVid2() Retorna todos componentes de Vida*
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peCond  -  Condiciones Comerciales            *
      *                                                              *
      * ------------------------------------------------------------ *

     P COWRTV_getComponentesVid2...
     P                 B                   export
     D COWRTV_getComponentesVid2...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peComp                            likeds(CompVid2) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1wev1          ds                  likerec(c1wev1:*key)
     D k1wevc          ds                  likerec(c1wevc:*key)
     D k1wev2          ds                  likerec(c1wev2:*key)

     D i               s             10i 0
     D x               s             10i 0
     D idx             s             13a   dim(100)
     D s               s             13a
     D @cobe           ds                  likeds(CobeVida) dim(10)

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1wevc.v0empr = PeBase.peEmpr;
       k1wevc.v0sucu = PeBase.peSucu;
       k1wevc.v0nivt = PeBase.peNivt;
       k1wevc.v0nivc = PeBase.peNivc;
       k1wevc.v0nctw = peNctw;
       setll %kds(k1wevc:5) ctwevc;
       reade %kds(k1wevc:5) ctwevc;
       dow not %eof;
           clear @cobe;
           clear idx;
           x +=1;
           k1wev1.v1empr = v0empr;
           k1wev1.v1sucu = v0sucu;
           k1wev1.v1nivt = v0nivt;
           k1wev1.v1nivc = v0nivc;
           k1wev1.v1nctw = v0nctw;
           setll %kds(k1wev1:5) ctwev1;
           reade %kds(k1wev1:5) ctwev1;
           dow not %eof;
               if v1acti = v0acti and v1secu = v0secu;
                  peComp(x).rama = v1rama;
                  peComp(x).arse = v1arse;
                  peComp(x).poco = v1poco;
                  peComp(x).paco = v1paco;
                  peComp(x).acti = v1acti;
                  peComp(x).secu = v1secu;
                  peComp(x).xpro = v1xpro;
                  peComp(x).nomb = v1nomb;
                  peComp(x).tido = v1tido;
                  peComp(x).nrdo = v1nrdo;
                  peComp(x).fnac = v1fnac;
                  peComp(x).naci = v1naci;
                  peComp(x).cate = v1cate;
                  peComp(x).cant = v0cant;
                  peComp(x).raed = v0raed;
                  k1wev2.v2empr = v1empr;
                  k1wev2.v2sucu = v1sucu;
                  k1wev2.v2nivt = v1nivt;
                  k1wev2.v2nivc = v1nivc;
                  k1wev2.v2nctw = v1nctw;
                  k1wev2.v2rama = v1rama;
                  k1wev2.v2arse = v1arse;
                  k1wev2.v2poco = v1poco;
                  k1wev2.v2paco = v1paco;
                  setll %kds(k1wev2:9) ctwev2;
                  reade %kds(k1wev2:9) ctwev2;
                  dow not %eof;
                      s = %editc(v1acti:'X')
                        + %editc(v1secu:'X')
                        + %trim(v2riec)
                        + %editc(v2xcob:'X');
                      i = %lookup(s:idx);
                      if i = 0;
                         i = %lookup(*blanks:idx);
                      endif;
                      idx(i) = s;
                      @cobe(i).secu  = v1secu;
                      @cobe(i).ecob  = v2ecob;
                      @cobe(i).riec  = v2riec;
                      @cobe(i).xcob  = v2xcob;
                      @cobe(i).saco  = v2saco;
                      @cobe(i).prsa  = v2prsa;
                      @cobe(i).xpri  = v2xpri;
                      @cobe(i).ptco += v2ptco;
                   reade %kds(k1wev2:9) ctwev2;
                  enddo;
               endif;
            reade %kds(k1wev1:5) ctwev1;
           enddo;
           peComp(x).cobe = @cobe;
        reade %kds(k1wevc:5) ctwevc;
       enddo;

       return;

      /end-free

     P COWRTV_getComponentesVid2...
     P                 E
      * ------------------------------------------------------------ *
      * COWRTV_getCoberturasVida() Retorna Coberturas del componente *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Polizas por Rama                   *
      *                pePoco  -  Número de Componente               *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peComp  -  Retorna datos del componente       *
      *                                                              *
      * ------------------------------------------------------------ *

     P COWRTV_getCoberturasVida...
     P                 B                   export
     D COWRTV_getCoberturasVida...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobe                            likeds(CobeVida) dim(10)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yev2          ds                  likerec(c1wev2:*key)

     D x               s             10i 0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yev2.v2empr = PeBase.peEmpr;
       k1yev2.v2sucu = PeBase.peSucu;
       k1yev2.v2nivt = PeBase.peNivt;
       k1yev2.v2nivc = PeBase.peNivc;
       k1yev2.v2nctw = peNctw;
       k1yev2.v2rama = perama;
       k1yev2.v2arse = pearse;
       k1yev2.v2poco = pepoco;

       x = *Zeros;
       clear pecobe;

       setll %kds( k1yev2 : 8 ) ctwev2;
       reade %kds( k1yev2 : 8 ) ctwev2;
       dow not %eof;

         x += 1;

         peCobe(x).secu = v2secu;
         peCobe(x).riec = v2riec;
         peCobe(x).xcob = v2xcob;
         peCobe(x).saco = v2saco;
         peCobe(x).ptco = v2ptco;
         peCobe(x).xpri = v2xpri;
         peCobe(x).prsa = v2prsa;
         peCobe(x).ecob = v2ecob;

         reade %kds( k1yev2 : 8 ) ctwev2;
       enddo;

       return;

      /end-free

     P COWRTV_getCoberturasVida...
     P                 E

      * ---------------------------------------------------------------- *
      * COWRTV_getCabeceraCotizacion: Recupera registro de CTW000        *
      *                                                                  *
      *      peBase (input)  Base                                        *
      *      peNctw (input)  Nro de Cotizacion                           *
      *                                                                  *
      * Retorna *on si encontró / *off si no encuentra                   *
      * ---------------------------------------------------------------- *
     P COWRTV_getCabeceraCotizacion...
     P                 B                   Export
     D COWRTV_getCabeceraCotizacion...
     D                 pi              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peCcot                            likeds(CabeceraCot_t)

     D k1w000          ds                  likerec(c1w000:*key)

      /free

       COWRTV_inz();

       k1w000.w0empr = peBase.peEmpr;
       k1w000.w0sucu = peBase.peSucu;
       k1w000.w0nivt = peBase.peNivt;
       k1w000.w0nivc = peBase.peNivc;
       k1w000.w0nctw = peNctw;
       chain %kds(k1w000:5) ctw000;
       if not %found;
          return *off;
       endif;

       peCcot.empr = w0empr;
       peCcot.sucu = w0sucu;
       peCcot.nivt = w0nivt;
       peCcot.nivc = w0nivc;
       peCcot.nctw = w0nctw;
       peCcot.nit1 = w0nit1;
       peCcot.niv1 = w0niv1;
       peCcot.fctw = w0fctw;
       peCcot.nomb = w0nomb;
       peCcot.soln = w0soln;
       peCcot.fpro = w0fpro;
       peCcot.mone = w0mone;
       peCcot.noml = w0noml;
       peCcot.come = w0come;
       peCcot.copo = w0copo;
       peCcot.cops = w0cops;
       peCcot.loca = w0loca;
       peCcot.arcd = w0arcd;
       peCcot.arno = w0arno;
       peCcot.spol = w0spol;
       peCcot.sspo = w0sspo;
       peCcot.tipe = w0tipe;
       peCcot.civa = w0civa;
       peCcot.ncil = w0ncil;
       peCcot.tiou = w0tiou;
       peCcot.stou = w0stou;
       peCcot.stos = w0stos;
       peCcot.dsop = w0dsop;
       peCcot.spo1 = w0spo1;
       peCcot.cest = w0cest;
       peCcot.cses = w0cses;
       peCcot.dest = w0dest;
       peCcot.vdes = w0vdes;
       peCcot.vhas = w0vhas;
       peCcot.cfpg = w0cfpg;
       peCcot.defp = w0defp;
       peCcot.ncbu = w0ncbu;
       peCcot.ctcu = w0ctcu;
       peCcot.nrtc = w0nrtc;
       peCcot.fvtc = w0fvtc;
       peCcot.mp01 = w0mp01;
       peCcot.mp02 = w0mp02;
       peCcot.mp03 = w0mp03;
       peCcot.mp04 = w0mp04;
       peCcot.mp05 = w0mp05;
       peCcot.mp06 = w0mp06;
       peCcot.mp07 = w0mp07;
       peCcot.mp08 = w0mp08;
       peCcot.mp09 = w0mp09;
       peCcot.mp10 = w0mp10;
       peCcot.nrpp = w0nrpp;
       peCcot.asen = w0asen;

       return *on;

      /end-free

     P COWRTV_getCabeceraCotizacion...
     P                 E

      * ------------------------------------------------------------ *
      * COWRTV_inz(): Inicializa módulo.                             *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     P COWRTV_inz      B                   export
     D COWRTV_inz      pi

      /free

       if not %open(ctw000);
         open ctw000;
       endif;

       if not %open(ctw001);
         open ctw001;
       endif;

       if not %open(ctw001c);
         open ctw001c;
       endif;

       if not %open(ctwet0);
         open ctwet0;
       endif;

       if not %open(ctwet1);
         open ctwet1;
       endif;

       if not %open(ctwet4);
         open ctwet4;
       endif;

       if not %open(ctwetc);
         open ctwetc;
       endif;

       if not %open(ctwer0);
         open ctwer0;
       endif;

       if not %open(ctwer2);
         open ctwer2;
       endif;

       if not %open(ctwer4);
         open ctwer4;
       endif;

       if not %open(ctwer6);
         open ctwer6;
       endif;

       if not %open(set103);
         open set103;
       endif;

       if not %open(set1031);
         open set1031;
       endif;

       if not %open(set250);
         open set250;
       endif;

       if not %open(set160);
         open set160;
       endif;

       if not %open(ctwev1);
         open ctwev1;
       endif;

       if not %open(ctwev2);
         open ctwev2;
       endif;

       if not %open(ctwevc);
         open ctwevc;
       endif;

       if not %open(gntloc02);
         open gntloc02;
       endif;

       if not %open(gntloc);
         open gntloc;
       endif;

       if not %open(set107);
         open set107;
       endif;

       if not %open(set116);
         open set116;
       endif;

       if not %open(ctwev101);
         open ctwev101;
       endif;

       if not %open(ctw003);
         open ctw003;
       endif;

       return;

      /end-free

     P COWRTV_inz      E

      * ------------------------------------------------------------ *
      * COWRTV_End(): Finaliza módulo.                               *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     P COWRTV_End      B                   export
     D COWRTV_End      pi

      /free

       close *all;

       return;

      /end-free

     P COWRTV_End      E
      * ---------------------------------------------------------------- *
      *                                                                  *
      * COWRTV_getVehiculo2(): Recupera los bienes asegurados(Vehículos) *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                pePoco  -  Número de Componente                   *
      *                peArse  -  Cant.Polizas por Rama/Art              *
      *        Output:                                                   *
      *                peInfV  -  Información del Vehículo               *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getVehiculo2...
     P                 B                   export
     D COWRTV_getVehiculo2...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   pePoco                       4  0   const
     D   peArse                       2  0   const
     D   peInfV                            likeds(Infvehi2)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D p@InfV          ds                  likeds(Infvehi3_t)

      /free

       clear p@InfV;

       COWRTV_getVehiculo3( peBase
                          : peNctw
                          : peRama
                          : pePoco
                          : peArse
                          : p@InfV
                          : peErro
                          : peMsgs );

       eval-corr peInfV = p@InfV;

       return;

      /end-free

     P COWRTV_getVehiculo2...
     P                 E
      * ---------------------------------------------------------------- *
      *                                                                  *
      * COWRTV_getVehiculos2(): Recupera los bienes asegurados(Vehículos)*
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *        Output:                                                   *
      *                peInfV  -  Información del Vehículo               *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getVehiculos2...
     P                 B                   export
     D COWRTV_getVehiculos2...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peInfV                            likeds(Infvehi2) Dim(10)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yet0          ds                  likerec(c1wet0:*key)
     D x               s              2  0
     D y               s              2  0

     D p@InfV          ds                  likeds(InfVehi3_t) dim(10)

      /free

       clear p@infV;

       COWRTV_getVehiculos3( peBase
                           : peNctw
                           : p@InfV
                           : peErro
                           : peMsgs  );

       eval-corr peInfV = p@InfV;

       return;

      /end-free

     P COWRTV_getVehiculos2...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getCobVehiculo2(): Recupera las coberturas asociadas      *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Código de Rama                         *
      *                peArse  -  Cantidad Polizas por Rama/Articulo     *
      *                pePoco  -  Número de Componente                   *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo del Código Postal               *
      *                pevhvu  -  Suma asegurada                         *
      *        Output:                                                   *
      *                peCobV  -  Coberturas                             *
      *                peBonV  -  Bonificaciones                         *
      *                peImpu  -  Impuestos                              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getCobVehiculo2...
     P                 B                   export
     D COWRTV_getCobVehiculo2...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0   const
     D   pePoco                       4  0   const
     D   peCopo                       5  0   const
     D   peCops                       1  0   const
     D   peVhvu                      15  2   const
     D   peCobV                            likeds(cobVehi2) Dim(20)
     D   peBonV                            likeds(BonVeh)   Dim(99)
     D   peImpu                            likeds(Impuesto) Dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yetc          ds                  likerec(c1wetc:*key)
     D y               s             10i 0
     D descob          s             40
     D @@cond          ds                  likeds(condComer_t) dim(99)
     D @@erro          s             10i 0
     D @@msgs          ds                  likeds(paramMsgs)
     D x               s             10i 0
     D j               s             10i 0
     D p@Impu          ds                  likeds(Impuesto)

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       k1yetc.t0empr = PeBase.peEmpr;
       k1yetc.t0sucu = PeBase.peSucu;
       k1yetc.t0nivt = PeBase.peNivt;
       k1yetc.t0nivc = PeBase.peNivc;
       k1yetc.t0nctw = peNctw;
       k1yetc.t0rama = peRama;
       k1yetc.t0arse = peArse;
       k1yetc.t0poco = pePoco;
       clear y;

       clear peCobV;

       setll %kds( k1yetc : 8 ) ctwetc;
       reade %kds( k1yetc : 8 ) ctwetc;
       dow not %eof;

         y += 1;
         peCobV(y).cobl = t0cobl;
         SPVVEH_CheckCobertura(t0cobl:
                               descob);
         peCobV(y).cobd = descob;
         peCobV(y).rast = t0rras;
         peCobV(y).cras = t0cras;
         peCobV(y).insp = t0rins;
         peCobV(y).sele = t0cobs;
         peCobV(y).ifra = t0ifra;
         peCobV(y).prrc = t0prrc;
         peCobV(y).prac = t0prac;
         peCobV(y).prin = t0prin;
         peCobV(y).prro = t0prro;
         peCobV(y).pacc = t0pacc;
         peCobV(y).praa = t0praa;
         peCobV(y).prsf = t0prsf;
         peCobV(y).prce = t0prce;
         peCobV(y).prap = t0prap;
         peCobV(y).rcle = t0rcle;
         peCobV(y).rcco = t0rcco;
         peCobV(y).rcac = t0rcac;
         peCobV(y).lrce = t0lrce;
         peCobV(y).claj = t0claj;

         COWRTV_getPrimaTot(peBase :
                            peNctw :
                            t0Rama :
                            t0Arse :
                            t0poco :
                            t0cobl :
                            peCobV(y).prim );
         peCobV(y).prem = t0prem;

         // Calcula comision...
         COWRTV_getCondComerciales( peBase
                                  : peNctw
                                  : @@cond
                                  : @@erro
                                  : @@msgs );

         if @@erro = -1;
           peCobV(y).xopr = *Zeros;
         else;
           for x = 1 to 99;
             if @@cond(x).rama = peRama;
               peCobV(y).xopr = ( ( t0prim * @@cond(x).xopr ) / 100 );
               leave;
             endif;
           endfor;
         endif;

         Clear p@Impu;
         COWGRAI_getImpuestos( peBase
                             : peNctw
                             : peRama
                             : peCobV(y).prim
                             : pevhvu
                             : peCopo
                             : peCops
                             : p@Impu );

           peImpu(y).cobl = t0cobl;
           peImpu(y).xrea = p@Impu.xrea;
           peImpu(y).read = p@Impu.read;
           peImpu(y).xopr = p@Impu.xopr;
           peImpu(y).copr = p@Impu.copr;
           peImpu(y).xref = p@Impu.xref;
           peImpu(y).refi = p@Impu.refi;
           peImpu(y).dere = p@Impu.dere;
           peImpu(y).seri = p@Impu.seri;
           peImpu(y).seem = p@Impu.seem;
           peImpu(y).pimi = p@Impu.pimi;
           peImpu(y).impi = p@Impu.impi;
           peImpu(y).psso = p@Impu.psso;
           peImpu(y).sers = p@Impu.sers;
           peImpu(y).pssn = p@Impu.pssn;
           peImpu(y).tssn = p@Impu.tssn;
           peImpu(y).pivi = p@Impu.pivi;
           peImpu(y).ipr1 = p@Impu.ipr1;
           peImpu(y).pivn = p@Impu.pivn;
           peImpu(y).ipr4 = p@Impu.ipr4;
           peImpu(y).pivr = p@Impu.pivr;
           peImpu(y).ipr3 = p@Impu.ipr3;
           peImpu(y).ipr6 = p@Impu.ipr6;
           peImpu(y).ipr7 = 0;
           peImpu(y).ipr8 = 0;

         reade %kds( k1yetc : 8 ) ctwetc;
       enddo;

       clear peBonV;
       COWRTV_getBonVehiculo (peBase :
                              peNctw :
                              t0Rama :
                              t0Arse :
                              t0poco :
                              peBonV :
                              peErro :
                              peMsgs );

       return;

      /end-free

     P COWRTV_getCobVehiculo2...
     P                 E
      * ---------------------------------------------------------------- *
      * COWRTV_getComponentesVid3() Retorna todos componentes de Vida    *
      *                                                                  *
      *       peBase ( input  ) -  Base                                  *
      *       peNctw ( input  ) -  Nro de Cotizacion                     *
      *       peRama ( output ) -  Rama                                  *
      *       peArse ( output ) -  Cant. de Polizas de Rama              *
      *       peNrpp ( output ) -  Plan de Pagos                         *
      *       peVdes ( output ) -  Vigencia Desde                        *
      *       peVhas ( output ) -  Vigencia Hasta                        *
      *       peXpro ( output ) -  Producto                              *
      *       peClie ( output ) -  Cliente                               *
      *       peActi ( output ) -  Estructura de Actividades             *
      *       peActiC( output ) -  Cant. de Actividad                    *
      *       peImpu ( output ) -  Impuestos                             *
      *       pePrim ( output ) -  Prima Total                           *
      *       pePrem ( output ) -  Premio Total                          *
      *       peErro ( output ) -  Marca de Error                        *
      *       peMsgs ( output ) -  Estructura de Errores                 *
      *                                                                  *
      * ---------------------------------------------------------------- *

     P COWRTV_getComponentesVid3...
     P                 B                   export
     D COWRTV_getComponentesVid3...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0
     D   peArse                       2  0
     D   peNrpp                       3  0
     D   peVdes                       8  0
     D   peVhas                       8  0
     D   peXpro                       3  0
     D   peClie                            likeds(ClienteCot_t)
     D   peActi                            likeds(Activ_t)  dim(99)
     D   peActiC                     10i 0
     D   peImpu                            likeds(Impuesto)
     D   pePrim                      15  2
     D   pePrem                      15  2
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D   k1y000        ds                  likerec( c1w000   : *key )
     D   k1yevc        ds                  likerec( c1wevc   : *key )
     D   k1yev1        ds                  likerec( c1wev101 : *key )
     D   k1yloc        ds                  likerec( g1tloc02 : *key )

     D   @@impu        ds                  likeds(Impuesto)
     D   @@prem        s             15  2
     D   @@prim        s             15  2
     D   @@suas        s             15  2
     D   @@ctw3        ds                  likeds(Asegurado_t) dim(999)
     D   @@ctw3C       s             10i 0
     D   @@nasen       s              7  0
     D   x             s             10i 0

      /free

       COWRTV_inz();

       clear peRama;
       clear peArse;
       clear peNrpp;
       clear peVdes;
       clear peVhas;
       clear peXpro;
       clear peClie;
       clear peActi;
       clear peActi;
       clear peImpu;
       clear pePrim;
       clear pePrem;
       clear peErro;
       clear peMsgs;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;
         peErro = -1;
         return;
       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;
         ErrText = COWGRAI_Error(ErrCode);
         if COWGRAI_COTNP = ErrCode;
           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));
           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );
         endif;
         peErro = -1;
         return;
       endif;

       k1y000.w0empr = PeBase.peEmpr;
       k1y000.w0sucu = PeBase.peSucu;
       k1y000.w0nivt = PeBase.peNivt;
       k1y000.w0nivc = PeBase.peNivc;
       k1y000.w0nctw = peNctw;
       chain(n) %kds( k1y000 : 5 ) ctw000;
       if %found( ctw000 );
         peNrpp = w0nrpp;
         peVdes = w0vdes;
         peVhas = w0vhas;
         peClie.asen = w0asen;
         peClie.nomb = w0nomb;
         peClie.cuit = *Blanks;
         peClie.tipe = w0tipe;
         peClie.proc = *zeros;
         peClie.copo = w0copo;
         peClie.cops = w0cops;
         peClie.civa = w0civa;
       endif;

       // Clientes...
       if COWRTV_getAsegurado( peBase
                             : peNctw
                             : @@ctw3
                             : @@ctw3C
                             : @@nasen );

         for x = 1 to @@ctw3c;
           peClie.tido = @@ctw3(x).w3tido;
           peClie.nrdo = @@ctw3(x).w3nrdo;
           peClie.nomb = @@ctw3(x).w3nomb;
           peClie.cuit = @@ctw3(x).w3cuit;
         endfor;
       endif;

       k1yloc.locopo = peClie.copo;
       k1yloc.locops = peClie.cops;
       chain %kds( k1yloc : 2 ) gntloc02;
       if %found( gntloc02 );
         peClie.proc = loproc;
         peClie.rpro = prrpro;
       else;
         peClie.proc = *blanks;
         peClie.rpro = *zeros;
       endif;

       k1yevc.v0empr = PeBase.peEmpr;
       k1yevc.v0sucu = PeBase.peSucu;
       k1yevc.v0nivt = PeBase.peNivt;
       k1yevc.v0nivc = PeBase.peNivc;
       k1yevc.v0nctw = peNctw;
       setll %kds( k1yevc : 5 ) ctwevc;
       reade %kds( k1yevc : 5 ) ctwevc;
       dow not %eof(  ctwevc );
         peRama = v0rama;
         peArse = v0arse;

         peActiC += 1;
         peActi(peActiC).acti = v0acti;
         peActi(peActiC).secu = v0secu;
         peActi(peActiC).cant = v0cant;
         peActi(peActiC).cate = v0cate;
         peActi(peActiC).raed = v0raed;
         peActi(peActiC).prem = v0prem;
         peActi(peActiC).prim = v0prim;
         @@prem += v0prem;
         @@prim += v0prim;
         @@suas += v0suas;

         k1yev1.v1empr = v0empr;
         k1yev1.v1sucu = v0sucu;
         k1yev1.v1nivt = v0nivt;
         k1yev1.v1nivc = v0nivc;
         k1yev1.v1nctw = v0nctw;
         k1yev1.v1rama = v0rama;
         k1yev1.v1arse = v0arse;
         k1yev1.v1acti = v0acti;
         k1yev1.v1secu = v0secu;
         chain(n) %kds( k1yev1 : 9 ) ctwev101;
           if %found( ctwev101 );
             peXpro = v1xpro;
             peActi(peActiC).paco = v1paco;
           endif;
         COWRTV_getCoberturasVida2( peBase
                                  : peNctw
                                  : peActi(peActiC).acti
                                  : peActi(peActiC).secu
                                  : peActi(peActiC).Cobe
                                  : peActi(peActiC).CobeC );

       // Devuelve Impuestos Por Coberturas
         clear @@Impu;
         COWGRAI_getImpuestos( peBase
                             : peNctw
                             : peRama
                             : v0prim
                             : v0suas
                             : peClie.Copo
                             : peClie.Cops
                             : @@Impu );

         @@Impu.cobl = *all'X';
         peActi(peActiC).Impu = @@Impu;

        reade %kds(k1yevc:5) ctwevc;
       enddo;

       // Devuelve Impuestos Por Coberturas
       clear @@Impu;
       COWGRAI_getImpuestos( peBase
                           : peNctw
                           : peRama
                           : @@prim
                           : @@suas
                           : peClie.Copo
                           : peClie.Cops
                           : @@Impu      );
       @@Impu.cobl = *all'X';
       peImpu = @@Impu;
       pePrim = @@prim;
       pePrem = @@prem;

       return;
      /end-free

     P COWRTV_getComponentesVid3...
     P                 e
      * ---------------------------------------------------------------- *
      * COWRTV_getCoberturasVida2(): Retoma Coberturas de una actividad  *
      *                                                                  *
      *       peBase ( input )  - Base                                   *
      *       peNctw ( input )  - Nro. de Cotización                     *
      *       peActi ( input )  - Código de Actividad                    *
      *       peSecu ( input )  - Secuencia                              *
      *       peCobe ( output ) - Estructura de Cobertura                *
      *       peCobeC( output ) - Cantidad de Coberturas                 *
      *                                                                  *
      * Retorna *on / *off                                               *
      * ---------------------------------------------------------------- *

     P COWRTV_getCoberturasVida2...
     P                 b                   export
     D COWRTV_getCoberturasVida2...
     D                 pi              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peActi                       5  0 const
     D   peSecu                       2  0 const
     D   peCobe                            likeds(Cobprima) dim(20)
     D   peCobeC                     10i 0

     D   x             s             10i 0
     D   idx           s              6a   dim(10)
     D   i             s             10i 0
     D   s             s              6a

     D   k1yev1        ds                  likerec( c1wev1 : *key )
     D   k1yev2        ds                  likerec( c1wev2 : *key )

      /free

        COWRTV_inz();

        clear idx;
        clear peCobe;
        clear peCobeC;
        i = 0;

        k1yev1.v1empr = peBase.peEmpr;
        k1yev1.v1sucu = peBase.peSucu;
        k1yev1.v1nivt = peBase.peNivt;
        k1yev1.v1nivc = peBase.peNivc;
        k1yev1.v1nctw = peNctw;
        setll %kds(k1yev1:5) ctwev1;
        reade(n) %kds(k1yev1:5) ctwev1;
        dow not %eof( ctwev1 );
          if v1acti = peActi and v1secu = peSecu;
            k1yev2.v2empr = v1empr;
            k1yev2.v2sucu = v1sucu;
            k1yev2.v2nivt = v1nivt;
            k1yev2.v2nivc = v1nivc;
            k1yev2.v2nctw = v1nctw;
            k1yev2.v2rama = v1rama;
            k1yev2.v2arse = v1arse;
            k1yev2.v2poco = v1poco;
            k1yev2.v2paco = v1paco;
            setll %kds( k1yev2 : 9 ) ctwev2;
            reade(n) %kds( k1yev2 : 9 ) ctwev2;
            dow not %eof( ctwev2 );
              s = %trim( v2riec )
                + %editc( v2xcob : 'X' );
              peCobeC = %lookup(s:idx);
              if peCobeC = 0;
                peCobeC = %lookup( *blanks : idx );
                idx( peCobeC ) = s;
              endif;
              peCobe( peCobeC ).riec  = v2riec;
              peCobe( peCobeC ).xcob  = v2xcob;
              peCobe( peCobeC ).sac1  = v2saco;
              peCobe( peCobeC ).prim += v2ptco;
              peCobe( peCobeC ).xpri  = v2xpri;
             reade(n) %kds( k1yev2 : 9 ) ctwev2;
            enddo;
          endif;
        reade(n) %kds( k1yev1 : 5 ) ctwev1;
       enddo;

       return *on;

      /end-free

     P COWRTV_getCoberturasVida2...
     P                 e
      * ---------------------------------------------------------------- *
      * COWRTV_getAsegurado(): Retorna Asegurado de una Cotizacion       *
      *                                                                  *
      *       peBase ( input )  - Base                                   *
      *       peNctw ( input )  - Nro. de Cotización                     *
      *       peAseg ( output ) - Estructura de Asegurados               *
      *       peAsegC( output ) - Cantidad de Asegurados                 *
      *       peNase ( input  ) - Tipo Asegurado          ( opcional )   *
      *                                                                  *
      * Retorna *ON = Asegurados  / *off = No encontro                   *
      * ---------------------------------------------------------------- *

     P COWRTV_getAsegurado...
     P                 b                   export
     D COWRTV_getAsegurado...
     D                 pi              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peAseg                            likeds(Asegurado_t) dim(999)
     D   peAsegC                     10i 0
     D   peNase                       7  0 options( *nopass : *omit )

     D   k1y003        ds                  likerec( c1w003 : *key )
     D   dsCtw3        ds                  likerec( c1w003 : *input )

      /free

       COWRTV_inz();

       clear peAseg;
       clear peAsegC;

       k1y003.w3empr =  peBase.peEmpr;
       k1y003.w3sucu =  peBase.peSucu;
       k1y003.w3nivt =  peBase.peNivt;
       k1y003.w3nivc =  peBase.peNivc;
       k1y003.w3nctw =  peNctw;
       if %parms >= 5  and %addr( peNase ) <> *Null;
         k1y003.w3nase =  peNase;
         setll %kds( k1y003 : 6 ) ctw003;
         reade(n) %kds( k1y003 : 6 ) ctw003 dsCtw3;
       else;
         setll %kds( k1y003 : 5 ) ctw003;
         reade(n) %kds( k1y003 : 5 ) ctw003 dsCtw3;
       endif;
       dow not %eof( ctw003 );
         peAsegC += 1;
         peAseg( peAsegc ) = dsCtw3;
         if %parms >= 5  and %addr( peNase ) <> *Null;
           reade(n) %kds( k1y003 : 6 ) ctw003 dsCtw3;
         else;
           reade(n) %kds( k1y003 : 5 ) ctw003 dsCtw3;
         endif;
       enddo;

       if peAsegc = 0;
         return *off;
       else;
         return *on;
       endif;

      /end-free
     P COWRTV_getAsegurado...
     P                 e

      * ---------------------------------------------------------------- *
      * COWRTV_getComponentesHogar(): Retorna cotización de hogar guarda-*
      *                               da.                                *
      *           ************ Deprecado *********************           *
      *                                                                  *
      *    peBase    (input)   Parámetro Base                            *
      *    peNctw    (input)   Número de Cotización                      *
      *    peRama    (input)   Rama                                      *
      *    peArse    (input)   Secuencia artículo/rama                   *
      *    peCfpg    (output)  Forma de Pago                             *
      *    peClie    (output)  Estructura de cliente                     *
      *    pePoco    (output)  Estructura de componentes                 *
      *    pePocoC   (output)  Cantidad de componentes                   *
      *    peXrea    (output)  % de Extra Prima Variable                 *
      *    peImpu    (output)  Detalle de Prima a Premio                 *
      *    peSuma    (output)  Suma Asegurada Total                      *
      *    pePrim    (output)  Prima Total                               *
      *    pePrem    (output)  Premio Total                              *
      *    peCond    (output)  Condiciones Comerciales                   *
      *    peCon1    (output)  Condiciones Comerciales                   *
      *    peErro    (output)  Señal de Error                            *
      *    peMsgs    (output)  Mensajes de Error                         *
      *                                                                  *
      * ---------------------------------------------------------------- *
     P COWRTV_getComponentesHogar...
     P                 B                   Export
     D COWRTV_getComponentesHogar...
     D                 pi
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peRama                        2  0 const
     D  peArse                        2  0 const
     D  peCfpg                        3  0
     D  peClie                             likeds(ClienteCot_t)
     D  pePoco                             likeds(UbicPoc_t) dim(10)
     D  pePocoC                      10i 0
     D  peXrea                        5  2
     D  peImpu                             likeds(PrimPrem) dim(99)
     D  peSuma                       13  2
     D  pePrim                       15  2
     D  pePrem                       15  2
     D  peCond                             likeds(condCome2_t)
     D  peCon1                             likeds(condCome)
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

      /free

        COWRTV_getComponentesRGV( peBase
                                : peNctw
                                : peRama
                                : peArse
                                : peCfpg
                                : peClie
                                : pePoco
                                : pePocoC
                                : peXrea
                                : peImpu
                                : peSuma
                                : pePrim
                                : pePrem
                                : peCond
                                : peCon1
                                : peErro
                                : peMsgs );

       return;

      /end-free

     P COWRTV_getComponentesHogar...
     P                 E

      * ------------------------------------------------------------ *
      * COWRTV_getVehiculos3(): Recupera los bienes asegurados       *
      *                         (Vehículos).                         *
      *        Input :                                               *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *        Output:                                               *
      *                peInfV  -  Información del Vehículo           *
      *                peErro  -  Indicador de Error                 *
      *                peMsgs  -  Estructura de Error                *
      * ------------------------------------------------------------ *
     P COWRTV_getVehiculos3...
     P                 B                   export
     D COWRTV_getVehiculos3...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peInfV                            likeds(Infvehi3_t) Dim(10)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yet0          ds                  likerec(c1wet0:*key)
     D x               s              2  0
     D y               s              2  0

      /free

       COWRTV_inz();

       peErro = *Zeros;

       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;
          peErro = -1;
          return;
       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;
          ErrText = COWGRAI_Error(ErrCode);
          if COWGRAI_COTNP = ErrCode;
             %subst(wrepl:1:7) = %trim(%char(peNctw));
             %subst(wrepl:8:1) = %char(peBase.peNivt);
             %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));
             SVPWS_getMsgs( '*LIBL'
                          : 'WSVMSG'
                          : 'COW0008'
                          : peMsgs
                          : %trim(wrepl)
                          : %len(%trim(wrepl))  );
          endif;
          peErro = -1;
          return;
       endif;

       k1yet0.t0empr = PeBase.peEmpr;
       k1yet0.t0sucu = PeBase.peSucu;
       k1yet0.t0nivt = PeBase.peNivt;
       k1yet0.t0nivc = PeBase.peNivc;
       k1yet0.t0nctw = peNctw;
       clear x;
       clear peInfV;

       setll %kds ( k1yet0 : 5 ) ctwet0;
       reade %kds ( k1yet0 : 5 ) ctwet0;
       dow not %eof;
           x += 1;
           COWRTV_getVehiculo3( peBase
                              : peNctw
                              : t0rama
                              : t0poco
                              : t0arse
                              : peInfV(x)
                              : peErro
                              : peMsgs);
         reade %kds ( k1yet0 : 5 ) ctwet0;
       enddo;

       return;

      /end-free

     P COWRTV_getVehiculos3...
     P                 E

      * ------------------------------------------------------------ *
      * COWRTV_getVehiculo3(): Recupera los bienes asegurados        *
      *                        (Vehículos).                          *
      *        Input :                                               *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                peRama  -  Código de Rama                     *
      *                pePoco  -  Número de Componente               *
      *                peArse  -  Cant.Polizas por Rama/Art          *
      *        Output:                                               *
      *                peInfV  -  Información del Vehículo           *
      *                peErro  -  Indicador de Error                 *
      *                peMsgs  -  Estructura de Error                *
      * ------------------------------------------------------------ *
     P COWRTV_getVehiculo3...
     P                 B                   export
     D COWRTV_getVehiculo3...
     D                 pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   pePoco                       4  0   const
     D   peArse                       2  0   const
     D   peInfV                            likeds(Infvehi3_t)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D k1yet0          ds                  likerec(c1wet0:*key)
     D k1wet1          ds                  likerec(c1wet1:*key)
     D k1tloc          ds                  likerec(g1tloc02:*key)
     D @@taaj          s              2  0
     D x               s             10i 0
     D y               s             10i 0
     D sum_acc         s             15  2
     D @@Item          ds                  likeds(items_t) dim(200)

      /free

       COWRTV_inz();

       peErro = *Zeros;

       //Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;

         peErro = -1;
         return;

       endif;

       //Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;

         ErrText = COWGRAI_Error(ErrCode);

         if COWGRAI_COTNP = ErrCode;

           %subst(wrepl:1:7) = %trim(%char(peNctw));
           %subst(wrepl:8:1) = %char(peBase.peNivt);
           %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));

           SVPWS_getMsgs( '*LIBL'
                        : 'WSVMSG'
                        : 'COW0008'
                        : peMsgs
                        : %trim(wrepl)
                        : %len(%trim(wrepl))  );

         endif;

         peErro = -1;
         return;

       endif;

       clear c1wet0;
       k1yet0.t0empr = PeBase.peEmpr;
       k1yet0.t0sucu = PeBase.peSucu;
       k1yet0.t0nivt = PeBase.peNivt;
       k1yet0.t0nivc = PeBase.peNivc;
       k1yet0.t0nctw = peNctw;
       k1yet0.t0rama = peRama;
       k1yet0.t0poco = pePoco;
       k1yet0.t0Arse = peArse;

       chain %kds( k1yet0 : 8 ) ctwet0;
       if %found( ctwet0 );

         peInfV.Rama = t0rama;
         peInfV.Poco = t0poco;
         peInfV.Arse = t0arse;
         peInfV.Vhmc = t0vhmc;
         peInfV.Vhmo = t0vhmo;
         peInfV.Vhcs = t0vhcs;
         peInfV.Vhcr = t0vhcr;
         peInfV.Vhan = t0vhan;
         peInfV.Vhni = t0vhni;
         peInfV.Moto = t0moto;
         peInfV.Chas = t0chas;
         peInfV.Vhct = t0vhct;
         peInfV.Vhuv = t0vhuv;
         peInfV.M0km = t0m0km;
         peInfV.Copo = t0copo;
         peInfV.Cops = t0cops;
         k1tloc.locopo = t0copo;
         k1tloc.locops = t0cops;
         chain %kds(k1tloc:2) gntloc02;
         if %found;
            peInfv.Rpro = prrpro;
            peInfv.Proc = loproc;
          else;
            peInfv.Rpro = *zeros;
            peInfv.Proc = *blanks;
         endif;
         peInfV.Scta = t0scta;
         peInfV.Mgnc = t0mgnc;
         peInfV.Rgnc = t0rgnc;
         peInfV.Nmat = t0nmat;
         peInfV.Ctre = t0ctre;
         peInfV.Rebr = t0rebr;
         peInfV.Nmer = t0nmer;
         peInfV.Aver = t0aver;
         peInfV.Iris = t0iris;
         peInfV.Cesv = t0cesv;
         COWRTV_getCobVehiculo2(peBase:
                                peNctw:
                                peRama:
                                t0arse:
                                t0poco:
                                t0copo:
                                t0cops:
                                t0vhvu:
                                peInfv.cobe:
                                peInfv.boni:
                                peInfv.impu:
                                peErro:
                                peMsgs);

         y = 0;
         sum_acc = 0;
         k1wet1.t1empr = t0empr;
         k1wet1.t1sucu = t0sucu;
         k1wet1.t1nivt = t0nivt;
         k1wet1.t1nivc = t0nivc;
         k1wet1.t1nctw = t0nctw;
         k1wet1.t1rama = t0rama;
         k1wet1.t1arse = t0arse;
         k1wet1.t1poco = t0poco;
         setll %kds(k1wet1:8) ctwet1;
         reade %kds(k1wet1:8) ctwet1;
         dow not %eof;
             y += 1;
             sum_acc += t1accv;
             peInfv.Acce(y).secu = t1secu;
             peInfv.Acce(y).accd = t1accd;
             peInfv.Acce(y).accv = t1accv;
             peInfv.Acce(y).mar1 = t1mar1;
          reade %kds(k1wet1:8) ctwet1;
         enddo;

         y = 0;
         clear @@Taaj;
         clear @@Item;
         if COWRTV_getScoring( peBase
                             : t0Nctw
                             : t0Rama
                             : t0Poco
                             : t0Arse
                             : @@Taaj
                             : @@Item );

           for x = 1 to 200;
             if @@Item(x).Cosg <> *blanks;
               y += 1;
               peInfv.Scor(y).Cosg = @@Item(x).Cosg;
               peInfv.Scor(y).Cosd = SVPDES_pregunta( @@Taaj
                                                    : @@Item(x).Cosg );
               peInfv.Scor(y).Vefa = @@Item(x).Vefa;
               peInfv.Scor(y).Cant = @@Item(x).Cant;
             endif;
           endfor;
         endif;

         peInfv.vhvu = t0vhvu - sum_acc - t0rgnc;

         peInfv.dweb = t0dweb;
         peInfv.pweb = t0pweb;
         peInfv.taaj = @@taaj;

         return;

       endif;

       return;

      /end-free

     P COWRTV_getVehiculo3...
     P                 E

      * ------------------------------------------------------------ *
      * COWRTV_getScoring(): Recupera Datos del Scoring.             *
      *                                                              *
      *        Input :                                               *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                peRama  -  Código de Rama                     *
      *                pePoco  -  Número de Componente               *
      *                peArse  -  Cant.Polizas por Rama/Art          *
      *        Output:                                               *
      *                peTaaj  -  Código de Cuestionario             *
      *                peItem  -  Items de Scoring                   *
      *                                                              *
      * Retorna: *ON = Si encontró / *OFF = No encontró              *
      * ------------------------------------------------------------ *
     P COWRTV_getScoring...
     P                 B                   export
     D COWRTV_getScoring...
     D                 pi              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   pePoco                       4  0 const
     D   peArse                       2  0 const
     D   peTaaj                       2  0
     D   peItem                            likeds(items_t) dim(200)

     D x               s             10i 0
     D peDst3          ds                  likeds(dsCtwet3_t) dim(999)
     D peDst3C         s             10i 0
     D peForm          s              1    inz('S')

      /free

       COWRTV_inz();

       clear peDst3C;
       clear peDst3;

       if COWVEH_getCtwet3( peBase.peEmpr
                          : peBase.peSucu
                          : peBase.peNivt
                          : peBase.peNivc
                          : peNctw
                          : peRama
                          : peArse
                          : pePoco
                          : *omit
                          : *omit
                          : peDst3
                          : peDst3C
                          : peForm        );

         for x = 1 to peDst3C;

           if x = 1;
             peTaaj = peDst3(x).t3Taaj;
           endif;

           peItem(x).Cosg = peDst3(x).t3Cosg;
           peItem(x).Tiaj = peDst3(x).t3Tiaj;
           peItem(x).Tiac = peDst3(x).t3Tiac;
           peItem(x).Vefa = peDst3(x).t3Vefa;
           peItem(x).Corc = peDst3(x).t3Corc;
           peItem(x).Coca = peDst3(x).t3Coca;
           peItem(x).Cant = peDst3(x).t3Cant;

         endfor;

         return *on;
       endif;

       return *off;

      /end-free

     P COWRTV_getScoring...
     P                 E

      * ---------------------------------------------------------------- *
      * COWRTV_getComponentesRGV(): Retorna cotización de RGV guardada.  *
      *                                                                  *
      * >>>>> DEPRECATED <<<<<< Usar getComponentesRGV2                  *
      *                                                                  *
      *    peBase    (input)   Parámetro Base                            *
      *    peNctw    (input)   Número de Cotización                      *
      *    peRama    (input)   Rama                                      *
      *    peArse    (input)   Secuencia artículo/rama                   *
      *    peCfpg    (output)  Forma de Pago                             *
      *    peClie    (output)  Estructura de cliente                     *
      *    pePoco    (output)  Estructura de componentes                 *
      *    pePocoC   (output)  Cantidad de componentes                   *
      *    peXrea    (output)  % de Extra Prima Variable                 *
      *    peImpu    (output)  Detalle de Prima a Premio                 *
      *    peSuma    (output)  Suma Asegurada Total                      *
      *    pePrim    (output)  Prima Total                               *
      *    pePrem    (output)  Premio Total                              *
      *    peCond    (output)  Condiciones Comerciales                   *
      *    peCon1    (output)  Condiciones Comerciales                   *
      *    peErro    (output)  Señal de Error                            *
      *    peMsgs    (output)  Mensajes de Error                         *
      *                                                                  *
      * ---------------------------------------------------------------- *
     P COWRTV_getComponentesRGV...
     P                 B                   Export
     D COWRTV_getComponentesRGV...
     D                 pi
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peRama                        2  0 const
     D  peArse                        2  0 const
     D  peCfpg                        3  0
     D  peClie                             likeds(ClienteCot_t)
     D  pePoco                             likeds(UbicPoc_t) dim(10)
     D  pePocoC                      10i 0
     D  peXrea                        5  2
     D  peImpu                             likeds(PrimPrem) dim(99)
     D  peSuma                       13  2
     D  pePrim                       15  2
     D  pePrem                       15  2
     D  peCond                             likeds(condCome2_t)
     D  peCon1                             likeds(condCome)
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

     D pxPoco          ds                  likeds(UbicPoc2_t) dim(10)

      /free

       COWRTV_inz();

       clear pxPoco;

       COWRTV_getComponentesRGV2( peBase
                                : peNctw
                                : peRama
                                : peArse
                                : peCfpg
                                : peClie
                                : pxPoco
                                : pePocoC
                                : peXrea
                                : peImpu
                                : peSuma
                                : pePrim
                                : pePrem
                                : peCond
                                : peCon1
                                : peErro
                                : peMsgs  );

       eval-corr pePoco = pxPoco;

       return;

      /end-free

     P COWRTV_getComponentesRGV...
     P                 E

      * ------------------------------------------------------------ *
      * COWRTV_getComponentesSepelio(): Retorna cotizacion de Sepelio*
      *                                 guardada.                    *
      *                                                              *
      *    peBase    (input)   Parámetro Base                        *
      *    peNctw    (input)   Número de Cotización                  *
      *    peRama    (input)   Rama                                  *
      *    peArse    (input)   Secuencia artículo/rama               *
      *    peNrpp    (output)  Forma de Pago                         *
      *    peClie    (output)  Estructura de cliente                 *
      *    peCsep    (output)  Componente de Cotizacion de Sepelio   *
      *    peXrea    (output)  % de Extra Prima Variable             *
      *    peImpu    (output)  Detalle de Prima a Premio             *
      *    peSuma    (output)  Suma Asegurada Total                  *
      *    pePrim    (output)  Prima Total                           *
      *    pePrem    (output)  Premio Total                          *
      *    peCond    (output)  Condiciones Comerciales               *
      *    peCon1    (output)  Condiciones Comerciales               *
      *    peErro    (output)  Señal de Error                        *
      *    peMsgs    (output)  Mensajes de Error                     *
      *                                                              *
      * ------------------------------------------------------------ *
     P COWRTV_getComponentesSepelio...
     P                 B                   Export
     D COWRTV_getComponentesSepelio...
     D                 pi
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peRama                        2  0 const
     D  peArse                        2  0 const
     D  peNrpp                        3  0
     D  peVdes                        8  0
     D  peXpro                        3  0
     D  peClie                             likeds(ClienteCot_t)
     D  peCsep                             likeds(CompSepelio_t)
     D  peImpu                             likeds(Impuesto)
     D  peSuma                       13  2
     D  pePrim                       15  2
     D  pePrem                       15  2
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

     D rc              s              1n
     D x               s             10i 0
     D q               s             10i 0
     D @@Dase          ds                  likeds(pahase_t)
     D @@Mase          ds                  likeds(dsMail_t) dim(100)
     D @@MaseC         s             10i 0
     D peWsep          ds                  likeds(ctwsep_t)
     D peWse1          ds                  likeds(ctwse1_t) dim(20)
     D Rec001          ds                  likeds(dsctw001_t) dim(999)
     D Rec001C         s             10i 0
     D peCabe          ds                  likeds(dsctw000_t)

      /free

       COWRTV_inz();

       peNrpp = 0;
       peVdes = 0;
       peXpro = 0;
       peErro = 0;
       pePrim = 0;
       pePrem = 0;
       peSuma = 0;
       clear peMsgs;
       clear peClie;
       clear peCsep;
       clear peImpu;

       // Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;
          peErro = -1;
          return;
       endif;

       // Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;
          ErrText = COWGRAI_Error(ErrCode);
          if COWGRAI_COTNP = ErrCode;
            %subst(wrepl:1:7) = %trim(%char(peNctw));
            %subst(wrepl:8:1) = %char(peBase.peNivt);
            %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'COW0008'
                         : peMsgs
                         : %trim(wrepl)
                         : %len(%trim(wrepl))  );
          endif;
          peErro = -1;
          return;
       endif;

       COWRTV_getClienteCotizacion( peBase
                                  : peNctw
                                  : peClie
                                  : peErro
                                  : peMsgs );
       if peErro = -1;
          return;
       endif;

       rc = COWGRAI_getCtw000( peBase: peNctw: peCabe );

       peNrpp = peCabe.w0nrpp;

       rc = COWSEP_getCabecera( peBase
                              : peNctw
                              : peRama
                              : peArse
                              : peWsep );
       if rc;
          peCsep.paco = peWsep.eppaco;
          peXpro      = peWsep.epxpro;
          peCsep.cant = peWsep.epcant;
          peCsep.raed = peWsep.epraed;
       endif;

       q = COWSEP_getCoberturas( peBase
                               : peNctw
                               : peRama
                               : peArse
                               : peWse1 );
       peCsep.cobeC = q;
       for x = 1 to q;
           peCsep.cobe(x).riec = peWse1(x).e1riec;
           peCsep.cobe(x).xcob = peWse1(x).e1xcob;
           peCsep.cobe(x).sac1 = peWse1(x).e1saco;
           peCsep.cobe(x).xpri = peWse1(x).e1xpri;
           peCsep.cobe(x).prim = peWse1(x).e1ptco;
           pePrim += peWse1(x).e1ptco;
           peSuma += peWse1(x).e1saco;
       endfor;

       rc = COWGRAI_getImpuestosCotizacion( peBase
                                          : peNctw
                                          : peRama
                                          : peImpu );

       rc = COWGRAI_getCtw001( peBase
                             : peNctw
                             : peRama
                             : Rec001  );

       pePrem = Rec001(1).w1prem;
       peCsep.prim = pePrim;
       peCsep.prem = pePrem;

       return;

      /end-free

     P COWRTV_getComponentesSepelio...
     P                 E

      * ------------------------------------------------------------ *
      * COWRTV_getClienteCotizacion(): Retorna estructura peClie     *
      *                                                              *
      *    peBase    (input)   Parámetro Base                        *
      *    peNctw    (input)   Número de Cotización                  *
      *    peClie    (output)  Estructura de Cliente de Cotizacion   *
      *    peErro    (output)  Señal de Error                        *
      *    peMsgs    (output)  Mensajes de Error                     *
      *                                                              *
      * ------------------------------------------------------------ *
     P COWRTV_getClienteCotizacion...
     P                 b                   export
     D COWRTV_getClienteCotizacion...
     D                 pi
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peClie                             likeds(ClienteCot_t)
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

     D rc              s              1n
     D @@Dase          ds                  likeds(pahase_t)
     D @@Mase          ds                  likeds(dsMail_t) dim(100)
     D @@MaseC         s             10i 0
     D peCabe          ds                  likeds(dsctw000_t)

      /free

       COWRTV_inz();

       peErro = 0;
       clear peMsgs;
       clear peClie;

       // Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;
          peErro = -1;
          return;
       endif;

       // Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;
          ErrText = COWGRAI_Error(ErrCode);
          if COWGRAI_COTNP = ErrCode;
            %subst(wrepl:1:7) = %trim(%char(peNctw));
            %subst(wrepl:8:1) = %char(peBase.peNivt);
            %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'COW0008'
                         : peMsgs
                         : %trim(wrepl)
                         : %len(%trim(wrepl))  );
          endif;
          peErro = -1;
          return;
       endif;

       rc = COWGRAI_getCtw000( peBase: peNctw: peCabe );

       peClie.asen = peCabe.w0asen;
       peClie.nomb = peCabe.w0nomb;
       peClie.tipe = peCabe.w0tipe;
       peClie.copo = peCabe.w0copo;
       peClie.cops = peCabe.w0cops;
       peClie.civa = peCabe.w0civa;
       peClie.cuit = *blanks;
       peClie.proc = *blanks;
       peClie.rpro = 0;

       chain (peCabe.w0copo:peCabe.w0cops) gntloc02;
       if %found;
          peClie.proc = loproc;
          peClie.rpro = prrpro;
       endif;

       WSLASE( peBase
             : peClie.asen
             : @@Dase
             : @@Mase
             : @@MaseC
             : peErro
             : peMsgs );
       if peErro = 0;
          peClie.tido = @@Dase.astido;
          peClie.nrdo = @@Dase.asnrdo;
          peClie.cuit = @@Dase.ascuit;
       endif;

       return;

      /end-free

     P COWRTV_getClienteCotizacion...
     P                 e

      * ---------------------------------------------------------------- *
      * COWRTV_getComponentesRGV2():Retorna cotización de RGV guardada.  *
      *                                                                  *
      *    peBase    (input)   Parámetro Base                            *
      *    peNctw    (input)   Número de Cotización                      *
      *    peRama    (input)   Rama                                      *
      *    peArse    (input)   Secuencia artículo/rama                   *
      *    peCfpg    (output)  Forma de Pago                             *
      *    peClie    (output)  Estructura de cliente                     *
      *    pePoco    (output)  Estructura de componentes                 *
      *    pePocoC   (output)  Cantidad de componentes                   *
      *    peXrea    (output)  % de Extra Prima Variable                 *
      *    peImpu    (output)  Detalle de Prima a Premio                 *
      *    peSuma    (output)  Suma Asegurada Total                      *
      *    pePrim    (output)  Prima Total                               *
      *    pePrem    (output)  Premio Total                              *
      *    peCond    (output)  Condiciones Comerciales                   *
      *    peCon1    (output)  Condiciones Comerciales                   *
      *    peErro    (output)  Señal de Error                            *
      *    peMsgs    (output)  Mensajes de Error                         *
      *                                                                  *
      * ---------------------------------------------------------------- *
     P COWRTV_getComponentesRGV2...
     P                 B                   Export
     D COWRTV_getComponentesRGV2...
     D                 pi
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peRama                        2  0 const
     D  peArse                        2  0 const
     D  peCfpg                        3  0
     D  peClie                             likeds(ClienteCot_t)
     D  pePoco                             likeds(UbicPoc2_t) dim(10)
     D  pePocoC                      10i 0
     D  peXrea                        5  2
     D  peImpu                             likeds(PrimPrem) dim(99)
     D  peSuma                       13  2
     D  pePrim                       15  2
     D  pePrem                       15  2
     D  peCond                             likeds(condCome2_t)
     D  peCon1                             likeds(condCome)
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

     DSPGETPSUA        pr                  extpgm('SPGETPSUA')
     D  rama                          2  0 const
     D  xpro                          3  0 const
     D  retu                          2  0

     D k1w01c          ds                  likerec(c1w001c:*key)
     D k1wer0          ds                  likerec(c1wer0:*key)
     D k1wer2          ds                  likerec(c1wer2:*key)
     D k1wer6          ds                  likerec(c1wer6:*key)
     D k1t160          ds                  likerec(s1t160:*key)
     D peCabe          ds                  likeds(dsctw000_t)
     D rc              s              1n
     D x               s              5i 0
     D i               s              5i 0
     D z               s              5i 0
     D peXopr          s              5  2
     D peTiou          s              1  0
     D peStou          s              2  0
     D peStos          s              2  0
     D peXop1          s              5  2
     D peXre1          s              5  2
     D @@Dase          ds                  likeds(pahase_t)
     D @@Mase          ds                  likeds(dsMail_t) dim(100)
     D @@MaseC         s             10i 0
     D Rec001          ds                  likeds(dsctw001_t) dim(999)

      /free

       COWRTV_inz();

       // Valido ParmBase
       if SVPWS_chkParmBase ( peBase : peMsgs ) = *off;
          peErro = -1;
          return;
       endif;

       // Valido Cotización
       if COWGRAI_chkCotizacion ( peBase : peNctw ) = *off;
          ErrText = COWGRAI_Error(ErrCode);
          if COWGRAI_COTNP = ErrCode;
            %subst(wrepl:1:7) = %trim(%char(peNctw));
            %subst(wrepl:8:1) = %char(peBase.peNivt);
            %subst(wrepl:9:5) = %trim(%char(peBase.peNivc));
            SVPWS_getMsgs( '*LIBL'
                         : 'WSVMSG'
                         : 'COW0008'
                         : peMsgs
                         : %trim(wrepl)
                         : %len(%trim(wrepl))  );
          endif;
          peErro = -1;
          return;
       endif;

       rc = COWGRAI_getTipoDeOperacion( peBase
                                      : peNctw
                                      : peTiou
                                      : peStou
                                      : peStos );
       if rc = *off;
          peTiou = 0;
       endif;

       rc = COWGRAI_getCtw000( peBase: peNctw: peCabe );
       if rc = *off;
       endif;

       peCfpg = peCabe.w0nrpp;
       peClie.asen = peCabe.w0asen;
       peClie.nomb = peCabe.w0nomb;
       peClie.tipe = peCabe.w0tipe;
       peClie.copo = peCabe.w0copo;
       peClie.cops = peCabe.w0cops;
       peClie.civa = peCabe.w0civa;
       peClie.cuit = *blanks;
       peClie.proc = *blanks;
       peClie.rpro = 0;

       chain (peCabe.w0copo:peCabe.w0cops) gntloc02;
       if %found;
          peClie.proc = loproc;
          peClie.rpro = prrpro;
       endif;

       WSLASE( peBase
             : peClie.asen
             : @@Dase
             : @@Mase
             : @@MaseC
             : peErro
             : peMsgs );
       if peErro = 0;
          peClie.tido = @@Dase.astido;
          peClie.nrdo = @@Dase.asnrdo;
          peClie.cuit = @@Dase.ascuit;
       endif;

       k1wer0.r0empr = peBase.peEmpr;
       k1wer0.r0sucu = peBase.peSucu;
       k1wer0.r0nivt = peBase.peNivt;
       k1wer0.r0nivc = peBase.peNivc;
       k1wer0.r0nctw = peNctw;
       k1wer0.r0rama = peRama;
       setll %kds(k1wer0:6) ctwer0;
       reade %kds(k1wer0:6) ctwer0;
       dow not %eof;

           pePocoC += 1;

           pePoco(pePocoC).poco = r0poco;
           pePoco(pePocoC).xpro = r0xpro;
           pePoco(pePocoC).tviv = r0cviv;
           pePoco(pePocoC).copo = r0copo;
           pePoco(pePocoC).cops = r0cops;
           pePoco(pePocoC).ctar = r0ctar;
           for z = 1 to %len(r0cta1);
               if %subst(r0cta1:z:1) = ' ';
                  %subst(r0cta1:z:1) = '-';
               endif;
           endfor;
           for z = 1 to %len(r0cta2);
               if %subst(r0cta2:z:1) = ' ';
                  %subst(r0cta2:z:1) = '-';
               endif;
           endfor;
           pePoco(pePocoC).cta1 = r0cta1;
           pePoco(pePocoC).cta2 = r0cta2;
           pePoco(pePocoC).clfr = r0clfr;
           pePoco(pePocoC).cagr = r0cagr;
           chain (r0copo:r0cops) gntloc;
           if %found;
              pePoco(pePocoC).scta = lozrrv;
           endif;
           pePoco(pePocoC).bure = 0;
           pePoco(pePocoC).insp = COWRGV_getInspeccion( peBase
                                                      : peNctw
                                                      : peRama
                                                      : peArse
                                                      : r0poco  );

           x = 0;
           k1wer6.r6empr = r0empr;
           k1wer6.r6sucu = r0sucu;
           k1wer6.r6nivt = r0nivt;
           k1wer6.r6nivc = r0nivc;
           k1wer6.r6nctw = r0nctw;
           k1wer6.r6rama = r0rama;
           k1wer6.r6arse = r0arse;
           k1wer6.r6poco = r0poco;
           setll %kds(k1wer6:8) ctwer6;
           reade %kds(k1wer6:8) ctwer6;
           dow not %eof;
               x += 1;
               pePoco(pePocoC).cara(x).ccba = r6ccba;
               pePoco(pePocoC).cara(x).ma01 = r6ma01;
               pePoco(pePocoC).cara(x).ma02 = r6ma02;
               pePoco(pePocoC).cara(x).ma03 = r0ma03;
               k1t160.t@empr = r6empr;
               k1t160.t@sucu = r6sucu;
               k1t160.t@rama = r6rama;
               k1t160.t@ccba = r6ccba;
               chain %kds(k1t160:4) set160;
               if %found;
                  pePoco(pePocoC).cara(x).dcba = t@dcba;
                  pePoco(pePocoC).cara(x).cbae = t@cbae;
               endif;
            reade %kds(k1wer6:8) ctwer6;
           enddo;

           pePoco(pePocoC).CaraC = x;

           x = 0;
           k1wer2.r2empr = r0empr;
           k1wer2.r2sucu = r0sucu;
           k1wer2.r2nivt = r0nivt;
           k1wer2.r2nivc = r0nivc;
           k1wer2.r2nctw = r0nctw;
           k1wer2.r2rama = r0rama;
           k1wer2.r2arse = r0arse;
           k1wer2.r2poco = r0poco;
           setll %kds(k1wer2:8) ctwer2;
           reade %kds(k1wer2:8) ctwer2;
           dow not %eof;
               x += 1;
               pePoco(pePocoC).suma += r2saco;
               pePoco(pePocoC).cobe(x).riec = r2riec;
               pePoco(pePocoC).cobe(x).xcob = r2xcob;
               pePoco(pePocoC).cobe(x).sac1 = r2saco;
               pePoco(pePocoC).cobe(x).xpri = r2xpri;
               pePoco(pePocoC).cobe(x).prim = r2ptco;
            reade %kds(k1wer2:8) ctwer2;
           enddo;

           if peTiou = 2;
              SPGETPSUA( r0rama: r0xpro: pePoco(pePocoC).psua );
            else;
              pePoco(pePocoC).psua = 0;
           endif;

           peSuma += pePoco(pePocoC).suma;

        reade %kds(k1wer0:6) ctwer0;
       enddo;

       COWGRAI_getCondComercialesA( peBase
                                  : peNctw
                                  : peRama
                                  : peXrea
                                  : peXopr );

       COWGRAI_getCondComerciales ( peBase
                                  : peNctw
                                  : peRama
                                  : peXre1
                                  : peXop1 );

       pePrim = COWGRAI_getPrimaRamaArse(peBase:peNctw:peRama:peArse);
       rc = COWGRAI_getCtw001( peBase
                             : peNctw
                             : peRama
                             : Rec001  );
       clear pePrem;
       if rc;
          pePrem = Rec001(1).w1prem;
       endif;

       COWRTV_getImpuestos( peBase
                          : peNctw
                          : peImpu );

       k1w01c.w1Empr = peBase.peEmpr;
       k1w01c.w1Sucu = peBase.peSucu;
       k1w01c.w1Nivt = peBase.peNivt;
       k1w01c.w1Nivc = peBase.peNivc;
       k1w01c.w1Nctw = peNctw;
       k1w01c.w1Rama = peRama;
       chain %kds( k1w01c : 6 ) ctw001c;
       if %found( ctw001c );
         peCon1.xrea = w1Xrea;
         peCond.xrea = w1Xrea;
         peCond.read = w1Read;
         peCond.xopr = w1Xopr;
         peCond.copr = w1Copr;
       endif;

       peCon1.rama = peRama;
       peCond.rama = peRama;
       peCond.arse = peArse;
       peCond.xre1 = peXre1;
       peCond.xop1 = peXop1;

       return;

      /end-free

     P COWRTV_getComponentesRGV2...
     P                 E

