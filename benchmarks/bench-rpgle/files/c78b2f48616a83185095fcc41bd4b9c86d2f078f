     H option(*nodebugio:*noshowcpy:*srcstmt)
     H actgrp(*new) dftactgrp(*no)
     H bnddir ( 'HDIILE/HDIBDIR' )
      * ************************************************************ *
      * COWRCE2: WebService                                          *
      *          Renovación Responsabilidad Civil - wrapper para     *
      *          _cotizarWeb()                                       *
      *                                                              *
      * ------------------------------------------------------------ *
      * Luis R. Gomez                            *22-May-2019        *
      * ------------------------------------------------------------ *
      *                                                              *
      * ************************************************************ *

      /copy './qcpybooks/cowlog_h.rpgle'
      /copy './qcpybooks/cowrce_h.rpgle'
      /copy './qcpybooks/svpcob_h.rpgle'
      /copy './qcpybooks/getsysv_h.rpgle'

     D COWGRA3         pr                  extpgm('COWGRA3')
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0   const
     D  peAsen                        7  0   const
     D  peNomb                       40      const
     D  peCiva                        2  0   const
     D  peTipe                        1      const
     D  peCopo                        5  0   const
     D  peCops                        1  0   const
     D  peCuit                       11a     const
     D  peTido                        1  0   const
     D  peNrdo                        8  0   const
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

     D COWRCE2         pr                  ExtPgm('COWRCE2')
     D   peBase                            likeds(paramBase) const
     D   peArcd                       6  0   const
     D   peSpol                       9  0   const
     D   peNctw                       7  0
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D COWRCE2         pi
     D   peBase                            likeds(paramBase) const
     D   peArcd                       6  0   const
     D   peSpol                       9  0   const
     D   peNctw                       7  0
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D COWGRA1         pr                  ExtPgm('COWGRA1')
     D   peBase                            likeds(paramBase) const
     D   peArcd                       6  0   const
     D   peMone                       2      const
     D   peTiou                       1  0   const
     D   peStou                       2  0   const
     D   peStos                       2  0   const
     D   peSpo1                       7  0   const
     D   peNctw                       7  0
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D COWRCE1         pr                  ExtPgm('COWRCE1')
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peRama                        2  0 const
     D  peArse                        2  0 const
     D  peCfpg                        3  0 const
     D  peClie                             likeds(ClienteCot_t)
     D  pePoco                             likeds(UbicPoc_t) dim(10)
     D  pePocoC                      10i 0 const
     D  peXrea                        5  2 const
     D  peImpu                             likeds(PrimPrem) dim(99)
     D  peSuma                       13  2
     D  pePrim                       15  2
     D  pePrem                       15  2
     D  peCond                             likeds(condCome2_t)
     D  peCon1                             likeds(condCome)
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

     D i               s             10i 0
     D x               s             10i 0
     D peLnsp          s              1
     D peSuma          s             13  2
     D peBoni          ds                  likeds(Bonific) dim(200)
     D peImpu          ds                  likeds(PrimPrem) dim(99)
     D peClie          ds                  likeds(ClienteCot_t)
     D peCond          ds                  likeds(condCome2_t)
     D peCon1          ds                  likeds(condCome)
     D pePrem          s             15  2
     D pePrim          s             15  2
     D peXrea          s              5  2
     D peCfpg          s              3  0
     D peRama          s              2  0
     D peArse          s              2  0
     D peSpo1          s              7  0
     D peMone          s              2
     D peTiou          s              1  0
     D peStou          s              2  0
     D peStos          s              2  0
     D Data            s          65535a   varying
     D CRLF            s              4a   inz('<br>')
     D separa          s            100a
     D pePoco          ds                  likeds( UbicPoc_t ) dim(10)
     D pePocoC         s             10i 0
     D curlib          s             10a
     D AS400Sys        s             10a

      /free

       *inlr = *on;

       clear peErro ;
       clear peMsgs ;
       clear peNctw ;

       separa = *all'-';

       AS400Sys = rtvSysName();

       setLogInicio();

       if not chkRenovacion();
         setErrorCOWRCE2();
         return;
       endif;

       peTiou = 2;
       peMone = '01';
       peSpo1 = peSpol;
       clear pePoco;
       clear peClie;
       clear peStou;
       clear peStos;
       clear peSuma;

       if not setCOWGRA1();
         setErrorCOWRCE2();
         return;
       endif;

       if not getInfo();
         setErrorCOWRCE2();
         return;
       endif;

       if not setCOWRCE1();
         setErrorCOWRCE2();
         return;
       endif;

       if not setCOWGRA3();
         setErrorCOWRCE2();
         return;
       endif;

       data = separa;
       COWLOG_spolog( peArcd : peSpol : Data );

       return;

      /end-free

      * ------------------------------------------------------------------ *
      * setLogInicio : Graba log inicial                                   *
      *                                                                    *
      * ------------------------------------------------------------------ *
     P setLogInicio...
     P                 B
     D setLogInicio...
     D                 pi

       Data = CRLF                                     + CRLF
            + '<b>COWRCE2</b>'
            + '<b> Renovación Responsabilidad Civil(Request)</b>' + CRLF
            + 'Fecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))               + CRLF
            + 'PEBASE'                                 + CRLF
            + '&nbsp;PEEMPR: ' + peBase.peEmpr         + CRLF
            + '&nbsp;PESUCU: ' + peBase.peSucu         + CRLF
            + '&nbsp;PENIVT: ' + %editc(peBase.peNivt:'X')  + CRLF
            + '&nbsp;PENIVC: ' + %editc(peBase.peNivc:'X')  + CRLF
            + '&nbsp;PENIT1: ' + %editc(peBase.peNit1:'X')  + CRLF
            + '&nbsp;PENIV1: ' + %editc(peBase.peNiv1:'X')  + CRLF
            + 'PEBASE'                                 + CRLF
            + 'PEARCD: '  + %editc(peArcd:'X')         + CRLF
            + 'PESPOL: '  + %editc(peSpol:'X')         + CRLF;

       COWLOG_spolog( peArcd : peSpol : Data );

       return;
     P setLogInicio...
     P                 e

      * ------------------------------------------------------------------ *
      * chkRenovacion : Llamada a Wrapper chkRenovacion                    *
      *                                                                    *
      * Retorna *on = Ok / *off = Error                                    *
      * ------------------------------------------------------------------ *
     P chkRenovacion...
     P                 B
     D chkRenovacion...
     D                 pi              n
      /free
       Data = CRLF
            + '<b>&nbspchkRenovacion (Request)</b>'  + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );

       Data = '&nbsp&nbspFecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))               + CRLF
            + '&nbsp&nbspPEBASE'                                 + CRLF
            + '&nbsp&nbsp&nbsp;PEEMPR: ' + peBase.peEmpr         + CRLF
            + '&nbsp&nbsp&nbsp;PESUCU: ' + peBase.peSucu         + CRLF
            + '&nbsp&nbsp&nbsp;PENIVT: ' + %editc(peBase.peNivt:'X')  + CRLF
            + '&nbsp&nbsp&nbsp;PENIVC: ' + %editc(peBase.peNivc:'X')  + CRLF
            + '&nbsp&nbsp&nbsp;PENIT1: ' + %editc(peBase.peNit1:'X')  + CRLF
            + '&nbsp&nbsp&nbsp;PENIV1: ' + %editc(peBase.peNiv1:'X')  + CRLF
            + '&nbsp&nbspPEBASE'                                 + CRLF
            + '&nbsp&nbspPEARCD: '  + %editc(peArcd:'X')         + CRLF
            + '&nbsp&nbspPESPOL: '  + %editc(peSpol:'X')         + CRLF;

       COWLOG_spolog( peArcd : peSpol : Data );

       COWRCE_chkRenovacion( peBase
                           : peArcd
                           : peSpol
                           : peErro
                           : peMsgs );
       if peErro <> *zeros;
         Data = CRLF
              + '<b>&nbspchkRenovacion (Reponse)</b> :Error';
         COWLOG_spolog( peArcd : peSpol : Data );
         return *off;
       endif;

       Data = CRLF
            + '&nbsp<b>chkRenovacion (Reponse)</b> :OK';
       COWLOG_spolog( peArcd : peSpol : Data );
       return *on;

      /end-free
     P chkRenovacion...
     P                 E

      * ------------------------------------------------------------------ *
      * setCOWGRA1 : Llamadad a Wrapper COWGRA1 - Cotizar                  *
      *                                                                    *
      * Retorna *on = Ok / *off = Error                                    *
      * ------------------------------------------------------------------ *
     P setCOWGRA1...
     P                 B
     D setCOWGRA1...
     D                 pi              n
      /free

       Data = CRLF + CRLF
            + '&nbsp<b>COWGRA1 </b>'
            + '<b>Obtener Nro. de Cotización (Request)</b>' + CRLF
            + '&nbspFecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))                    + CRLF
            + '&nbsp&nbspPEBASE'                                      + CRLF
            + '&nbsp&nbsp&nbsp;PEEMPR: ' + peBase.peEmpr              + CRLF
            + '&nbsp&nbsp&nbsp;PESUCU: ' + peBase.peSucu              + CRLF
            + '&nbsp&nbsp&nbsp;PENIVT: ' + %editc(peBase.peNivt:'X')  + CRLF
            + '&nbsp&nbsp&nbsp;PENIVC: ' + %editc(peBase.peNivc:'X')  + CRLF
            + '&nbsp&nbsp&nbsp;PENIT1: ' + %editc(peBase.peNit1:'X')  + CRLF
            + '&nbsp&nbsp&nbsp;PENIV1: ' + %editc(peBase.peNiv1:'X')  + CRLF
            + '&nbsp&nbspPEBASE'                                      + CRLF
            + '&nbsp&nbspPEARCD: '       + %editc(peArcd:'X')         + CRLF
            + '&nbsp&nbspPEMONE: '       + peMone                     + CRLF
            + '&nbsp&nbspPETIOU: '       + %editc(peTiou:'X')         + CRLF
            + '&nbsp&nbspPESTOU: '       + %editc(peStou:'X')         + CRLF
            + '&nbsp&nbspPESTOS: '       + %editc(peStos:'X')         + CRLF
            + '&nbsp&nbspPESPO1: '       + %editc(peSpo1:'X');
       COWLOG_spolog( peArcd : peSpol : Data );

       COWGRA1( peBase
              : peArcd
              : peMone
              : peTiou
              : peStou
              : peStos
              : peSpo1
              : peNctw
              : peErro
              : peMsgs );

       if peErro <> 0;
         Data = CRLF + CRLF
              + '&nbsp<b>COWGRA1 (Reponse)</b> :Error';
         COWLOG_spolog( peArcd : peSpol : Data );
         return *off;
       else;
         Data = CRLF + CRLF
              + '&nbsp<b>COWGRA1 (Response)</b> : OK '       + CRLF
              + '&nbspFecha/Hora: '
              + %trim(%char(%date():*iso)) + ' '
              + %trim(%char(%time():*iso))                   + CRLF
              + '&nbspPENCTW: '       + %editc(peNctw:'X')   + CRLF
              + '&nbsp<a href='
              + '"http://'
              + %trim(AS400SyS)
              + ':8050/wsrest/dsplogwf/?X1NCTW='
              + %editc(peNctw:'X') +'/">'+ 'Ver Log de la Cotización</a>'
              + CRLF;
         COWLOG_spolog( peArcd : peSpol : Data );

       endif;

       return *on;
      /end-free
     P setCOWGRA1...
     P                 E

      * ------------------------------------------------------------------ *
      * getInfo: Obtener informacion de bienes                             *
      *                                                                    *
      * Retorna *on = Ok / *off = Error                                    *
      * ------------------------------------------------------------------ *
     P getInfo...
     P                 B
     D getInfo...
     D                 pi              n
      /free

       Data = CRLF
            + '&nbsp<b>COWRGV_getInfo</b>'
            + '&nbsp<b> Obtener información de bienes (Request)</b>' + CRLF
            + '&nbspFecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))                        + CRLF
            + '&nbspPEBASE'                                     + CRLF
            + '&nbsp&nbspPEEMPR: ' + peBase.peEmpr              + CRLF
            + '&nbsp&nbspPESUCU: ' + peBase.peSucu              + CRLF
            + '&nbsp&nbspPENIVT: ' + %editc(peBase.peNivt:'X')  + CRLF
            + '&nbsp&nbspPENIVC: ' + %editc(peBase.peNivc:'X')  + CRLF
            + '&nbsp&nbspPENIT1: ' + %editc(peBase.peNit1:'X')  + CRLF
            + '&nbsp&nbspPENIV1: ' + %editc(peBase.peNiv1:'X')  + CRLF
            + '&nbspPEBASE'                                      + CRLF
            + '&nbspPEARCD: '  + %editc(peArcd:'X')              + CRLF
            + '&nbspPESPOL: '  + %editc(peSpol:'X')              + CRLF
            + '&nbspPENCTW: '  + %editc(peNctw:'X');

       COWLOG_spolog( peArcd : peSpol : Data );

       COWRGV_getInfo( peBase
                     : peArcd
                     : peSpol
                     : peNctw
                     : peRama
                     : peArse
                     : peCfpg
                     : peClie
                     : pePoco
                     : peXrea );

         for i = 1 to 10;
           if pePoco(i).Poco <= 0;
             leave;
           else;
             pePocoC += 1;
           endif;
         endfor;

       Data =  CRLF + CRLF
            + '&nbsp<b>COWRGV_getInfo(Response)</b>'         + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );

       Data = '&nbspFecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso));
       COWLOG_spolog( peArcd : peSpol : Data );

       Data = CRLF
          + '&nbspPECLIE' + CRLF
          + '&nbsp&nbsp;ASEN: ' + %editc(peClie.Asen:'X') + CRLF
          + '&nbsp&nbsp;TIDO: ' + %editc(peClie.Tido:'X') + CRLF
          + '&nbsp&nbsp;NRDO: ' + %editc(peClie.Nrdo:'X') + CRLF
          + '&nbsp&nbsp;NOMB: ' + %trim(peClie.Nomb) + CRLF
          + '&nbsp&nbsp;CUIT: ' + %trim(peClie.Cuit) + CRLF
          + '&nbsp&nbsp;TIPE: ' + %trim(peClie.Tipe) + CRLF
          + '&nbsp&nbsp;PROC: ' + %trim(peClie.Proc) + CRLF
          + '&nbsp&nbsp;RPRO: ' + %editc(peClie.Rpro:'X') + CRLF
          + '&nbsp&nbsp;COPO: ' + %editc(peClie.Copo:'X') + CRLF
          + '&nbsp&nbsp;COPS: ' + %editc(peClie.Cops:'X') + CRLF
          + '&nbsp&nbsp;CIVA: ' + %editc(peClie.Civa:'X') + CRLF
          + '&nbspPECLIE' + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );
       for i = 1 to 10;
         if pePoco(i).Poco <= 0;
           leave;
         endif;
         Data = '&nbspPEPOCO(' + %trim(%char(i)) + ')' + CRLF
              + '&nbsp&nbsp;POCO: ' + %editc(pePoco(i).Poco:'X') + CRLF
              + '&nbsp&nbsp;XPRO: ' + %editc(pePoco(i).Xpro:'X') + CRLF
              + '&nbsp&nbsp;TVIV: ' + %editc(pePoco(i).Tviv:'X') + CRLF
              + '&nbsp&nbsp;COPO: ' + %editc(pePoco(i).Copo:'X') + CRLF
              + '&nbsp&nbsp;COPS: ' + %editc(pePoco(i).Cops:'X') + CRLF
              + '&nbsp&nbsp;SCTA: ' + %editc(pePoco(i).Scta:'X') + CRLF
              + '&nbsp&nbsp;BURE: ' + %editc(pePoco(i).Bure:'X') + CRLF
              + '&nbsp&nbsp;CARAC:' + %editc(pePoco(i).CaraC:'X') + CRLF;
         COWLOG_spolog( peArcd : peSpol : Data );

         for x = 1 to pePoco(i).CaraC;
           if pePoco(i).Cara(x).Ccba <= 0;
             leave;
           endif;
           Data = '&nbspCARA(' + %trim(%char(i)) + ')' + CRLF
                + '&nbsp&nbsp;CCBA: '
                + %editc(pePoco(i).Cara(x).Ccba:'X') + CRLF
                + '&nbsp&nbsp;DCBA: ' + %trim(pePoco(i).Cara(x).Dcba) + CRLF
                + '&nbsp&nbsp;MA01: ' + %trim(pePoco(i).Cara(x).Ma01) + CRLF
                + '&nbsp&nbsp;MA02: ' + %trim(pePoco(i).Cara(x).Ma02) + CRLF
                + '&nbsp&nbsp;MA03: ' + %trim(pePoco(i).Cara(x).Ma03) + CRLF
                + '&nbsp&nbsp;CBAE: ' + %trim(pePoco(i).Cara(x).Cbae) + CRLF
                + '&nbspCARA' + CRLF;
           COWLOG_spolog( peArcd : peSpol : Data );
         endfor;

         for x = 1 to 20;
           if pePoco(i).Cobe(x).Riec = *blanks;
             leave;
           endif;
           Data = '&nbspCOBE(' + %trim(%char(i)) + ')' + CRLF
                + '&nbsp&nbsp;RIEC: ' + %trim(pePoco(i).Cobe(x).Riec) + CRLF
                + '&nbsp&nbsp;XCOB: '
                + %editc(pePoco(i).Cobe(x).Xcob:'X') + CRLF
                + '&nbsp&nbsp;SAC1: ' +
                      %editw(pePoco(i).Cobe(X).Sac1:'  .   .   . 0 ,  ') + CRLF
                + '&nbsp&nbsp;XPRI: ' +
                      %editw(pePoco(i).Cobe(X).Xpri:' 0 ,      ') + CRLF
                + '&nbsp&nbsp;PRIM: ' +
                      %editw(pePoco(i).Cobe(X).Prim:'  .   .   . 0 ,  ') + CRLF
                + '&nbspCOBE';
           COWLOG_spolog( peArcd : peSpol : Data );
         endfor;
       endfor;

       return *on;
      /end-free
     P getInfo...
     P                 E

      * ------------------------------------------------------------------ *
      * setCOWRCE1 : Llamada a Wrapper COWRCE1 - Cotizar                   *
      *                                                                    *
      * Retorna *on = Ok / *off = Error                                    *
      * ------------------------------------------------------------------ *
     P setCOWRCE1...
     P                 B
     D setCOWRCE1...
     D                 pi              n
      /free

       Data = CRLF + CRLF
            + '<b>COWRCE1 '
            + 'Cotización Responsabilidad Civil (Request)</b>' + CRLF
            + 'Fecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))                    + CRLF
            + 'PEBASE'                                      + CRLF
            + '&nbsp;PEEMPR: ' + peBase.peEmpr              + CRLF
            + '&nbsp;PESUCU: ' + peBase.peSucu              + CRLF
            + '&nbsp;PENIVT: ' + %editc(peBase.peNivt:'X')  + CRLF
            + '&nbsp;PENIVC: ' + %editc(peBase.peNivc:'X')  + CRLF
            + '&nbsp;PENIT1: ' + %editc(peBase.peNit1:'X')  + CRLF
            + '&nbsp;PENIV1: ' + %editc(peBase.peNiv1:'X')  + CRLF
            + 'PEBASE'                                      + CRLF
            + 'PERAMA: '  + %editc(peRama:'X')              + CRLF
            + 'PEARSE: '  + %editc(peArse:'X')              + CRLF
            + 'PECFPG: '  + %editc(peCfpg:'X')              + CRLF
            + 'PEXREA: '  + %editw(peXrea:' 0 ,  ')         + CRLF
            + 'PEPOCOC:'  + %editc(pePocoC:'X')             + CRLF;

       COWLOG_spolog( peArcd : peSpol : Data );

       Data = 'PECLIE' + CRLF
          + '&nbsp;ASEN: ' + %editc(peClie.Asen:'X') + CRLF
          + '&nbsp;TIDO: ' + %editc(peClie.Tido:'X') + CRLF
          + '&nbsp;NRDO: ' + %editc(peClie.Nrdo:'X') + CRLF
          + '&nbsp;NOMB: ' + %trim(peClie.Nomb) + CRLF
          + '&nbsp;CUIT: ' + %trim(peClie.Cuit) + CRLF
          + '&nbsp;TIPE: ' + %trim(peClie.Tipe) + CRLF
          + '&nbsp;PROC: ' + %trim(peClie.Proc) + CRLF
          + '&nbsp;RPRO: ' + %editc(peClie.Rpro:'X') + CRLF
          + '&nbsp;COPO: ' + %editc(peClie.Copo:'X') + CRLF
          + '&nbsp;COPS: ' + %editc(peClie.Cops:'X') + CRLF
          + '&nbsp;CIVA: ' + %editc(peClie.Civa:'X') + CRLF
          + 'PECLIE' + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );

       for i = 1 to 10;
         if pePoco(i).Poco <= 0;
           leave;
         endif;
         Data = 'PEPOCO(' + %trim(%char(i)) + ')' + CRLF
              + '&nbsp;POCO: ' + %editc(pePoco(i).Poco:'X') + CRLF
              + '&nbsp;XPRO: ' + %editc(pePoco(i).Xpro:'X') + CRLF
              + '&nbsp;TVIV: ' + %editc(pePoco(i).Tviv:'X') + CRLF
              + '&nbsp;COPO: ' + %editc(pePoco(i).Copo:'X') + CRLF
              + '&nbsp;COPS: ' + %editc(pePoco(i).Cops:'X') + CRLF
              + '&nbsp;SCTA: ' + %editc(pePoco(i).Scta:'X') + CRLF
              + '&nbsp;BURE: ' + %editc(pePoco(i).Bure:'X') + CRLF
              + '&nbsp;CARAC:' + %editc(pePoco(i).CaraC:'X') + CRLF;
         COWLOG_spolog( peArcd : peSpol : Data );

         for x = 1 to pePoco(i).CaraC;
           if pePoco(i).Cara(x).Ccba <= 0;
             leave;
           endif;
           Data = 'CARA(' + %trim(%char(i)) + ')' + CRLF
                + '&nbsp;CCBA: ' + %editc(pePoco(i).Cara(x).Ccba:'X') + CRLF
                + '&nbsp;DCBA: ' + %trim(pePoco(i).Cara(x).Dcba) + CRLF
                + '&nbsp;MA01: ' + %trim(pePoco(i).Cara(x).Ma01) + CRLF
                + '&nbsp;MA02: ' + %trim(pePoco(i).Cara(x).Ma02) + CRLF
                + '&nbsp;MA03: ' + %trim(pePoco(i).Cara(x).Ma03) + CRLF
                + '&nbsp;CBAE: ' + %trim(pePoco(i).Cara(x).Cbae) + CRLF
                + 'CARA' + CRLF;
           COWLOG_spolog( peArcd : peSpol : Data );
         endfor;

         for x = 1 to 20;
           if pePoco(i).Cobe(x).Riec = *blanks;
             leave;
           endif;
           Data = 'COBE(' + %trim(%char(i)) + ')' + CRLF
                + '&nbsp;RIEC: ' + %trim(pePoco(i).Cobe(x).Riec) + CRLF
                + '&nbsp;XCOB: ' + %editc(pePoco(i).Cobe(x).Xcob:'X') + CRLF
                + '&nbsp;SAC1: ' +
                      %editw(pePoco(i).Cobe(X).Sac1:'  .   .   . 0 ,  ') + CRLF
                + '&nbsp;XPRI: ' +
                      %editw(pePoco(i).Cobe(X).Xpri:' 0 ,      ') + CRLF
                + '&nbsp;PRIM: ' +
                      %editw(pePoco(i).Cobe(X).Prim:'  .   .   . 0 ,  ') + CRLF
                + 'COBE' + CRLF;
           COWLOG_spolog( peArcd : peSpol : Data );
         endfor;
       endfor;

       COWRCE1( peBase
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
              : peMsgs  );

       Data = CRLF                                     + CRLF
            + '<b>COWRCE1 (Response)</b>'              + CRLF
            + 'Fecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))               + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );

       for i = 1 to 10;
         if pePoco(i).Poco <= 0;
           leave;
         endif;

         for x = 1 to 20;
           if pePoco(i).Cobe(x).Riec = *blanks;
             leave;
           endif;
           Data = 'COBE(' + %trim(%char(i)) + ')' + CRLF
                + '&nbsp;RIEC: ' + %trim(pePoco(i).Cobe(x).Riec) + CRLF
                + '&nbsp;XCOB: ' + %editc(pePoco(i).Cobe(x).Xcob:'X') + CRLF
                + '&nbsp;SAC1: ' +
                      %editw(pePoco(i).Cobe(X).Sac1:'  .   .   . 0 ,  ') + CRLF
                + '&nbsp;XPRI: ' +
                      %editw(pePoco(i).Cobe(X).Xpri:' 0 ,      ') + CRLF
                + '&nbsp;PRIM: ' +
                      %editw(pePoco(i).Cobe(X).Prim:'  .   .   . 0 ,  ') + CRLF
                + 'COBE' + CRLF;
           COWLOG_spolog( peArcd : peSpol : Data );
         endfor;

         for x = 1 to 200;
           if pePoco(i).Boni(x).Xcob <= 0;
              leave;
           endif;
           Data = 'BONI(' + %trim(%char(x)) + ')' + CRLF
                + '&nbsp;XCOB: ' + %editc(pePoco(i).Boni(x).Xcob:'X') + CRLF
                + '&nbsp;CCBP: ' + %editc(pePoco(i).Boni(x).Ccbp:'X') + CRLF
                + '&nbsp;DCBP: ' + pePoco(i).Boni(x).Dcbp             + CRLF
                + '&nbsp;NIVE: ' + %editc(pePoco(i).Boni(x).Nive:'X') + CRLF
                + '&nbsp;PBON: ' + %editw(pePoco(i).Boni(x).Pbon:' 0 ,  ')+CRLF
                + '&nbsp;PREC: ' + %editw(pePoco(i).Boni(x).Prec:' 0 ,  ')+CRLF
                + 'BONI' + CRLF;
           COWLOG_spolog( peArcd : peSpol : Data );
         endfor;

         for x = 1 to 99;
           if pePoco(i).Impu(x).cobl = *blanks;
              leave;
           endif;
           Data = 'IMPU(' + %trim(%char(x)) + ')' + CRLF
                + '&nbsp;COBL: ' + pePoco(i).Impu(x).cobl             + CRLF
                + '&nbsp;XREA: ' + %editw(pePoco(i).Impu(x).xrea:' 0 ,  ')+CRLF
                + '&nbsp;READ: ' +
                     %editw(pePoco(i).Impu(x).read:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;XOPR: ' + %editw(pePoco(i).Impu(x).xopr:' 0 ,  ')+CRLF
                + '&nbsp;COPR: ' +
                     %editw(pePoco(i).Impu(x).copr:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;XREF: ' + %editw(pePoco(i).Impu(x).xref:' 0 ,  ')+CRLF
                + '&nbsp;REFI: ' +
                     %editw(pePoco(i).Impu(x).refi:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;DERE: ' +
                     %editw(pePoco(i).Impu(x).dere:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;SERI: ' +
                     %editw(pePoco(i).Impu(x).seri:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;SEEM: ' +
                     %editw(pePoco(i).Impu(x).seem:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;PIMI: ' + %editw(pePoco(i).Impu(x).pimi:' 0 ,  ')+CRLF
                + '&nbsp;IMPI: ' +
                     %editw(pePoco(i).Impu(x).impi:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;PSSO: ' + %editw(pePoco(i).Impu(x).psso:' 0 ,  ')+CRLF
                + '&nbsp;SERS: ' +
                     %editw(pePoco(i).Impu(x).sers:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;PSSN: ' + %editw(pePoco(i).Impu(x).pssn:' 0 ,  ')+CRLF
                + '&nbsp;TSSN: ' +
                     %editw(pePoco(i).Impu(x).tssn:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;PIVI: ' + %editw(pePoco(i).Impu(x).pivi:' 0 ,  ')+CRLF
                + '&nbsp;IPR1: ' +
                     %editw(pePoco(i).Impu(x).ipr1:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;PIVN: ' + %editw(pePoco(i).Impu(x).pivn:' 0 ,  ')+CRLF
                + '&nbsp;IPR4: ' +
                     %editw(pePoco(i).Impu(x).ipr4:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;PIVR: ' + %editw(pePoco(i).Impu(x).pivr:' 0 ,  ')+CRLF
                + '&nbsp;IPR3: ' +
                     %editw(pePoco(i).Impu(x).ipr3:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;IPR6: ' +
                     %editw(pePoco(i).Impu(x).ipr6:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;IPR7: ' +
                     %editw(pePoco(i).Impu(x).ipr7:' .   .   .   . 0 ,  ')+CRLF
                + '&nbsp;IPR8: ' +
                     %editw(pePoco(i).Impu(x).ipr8:' .   .   .   . 0 ,  ')+CRLF
                + 'IMPU' + CRLF;
           COWLOG_spolog( peArcd : peSpol : Data );

         endfor;

         Data = 'SUMA: ' + %editw(pePoco(i).Suma:'  .   .   . 0 ,  ') + CRLF
              + 'INSP: ' + pePoco(i).Insp                             + CRLF
              + 'PREM: ' + %editw(pePoco(i).Prem:'  .   .   . 0 ,  ') + CRLF
              + 'PSUA: ' + %editc(pePoco(i).Psua:'X') + CRLF;
         COWLOG_spolog( peArcd : peSpol : Data );

       endfor;

       Data = 'PESUMA: ' + %editw(peSuma:'  .   .   . 0 ,  ') + CRLF
            + 'PEPRIM: ' + %editw(pePrim:' .   .   .   . 0 ,  ') + CRLF
            + 'PEPREM: ' + %editw(pePrem:' .   .   .   . 0 ,  ') + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );

       for x = 1 to 99;
         if peImpu(x).rama = *zeros;
           leave;
         endif;
         Data = 'PEIMPU(' + %trim(%char(x)) + ')' + CRLF
              + '&nbsp;RAMA: ' + %editc(peImpu(x).rama:'X')      + CRLF
              + '&nbsp;ARSE: ' + %editc(peImpu(x).arse:'X')      + CRLF
              + '&nbsp;PRIM: ' +
                   %editw(peImpu(x).prim:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;XREF: ' + %editw(peImpu(x).xref:' 0 ,  ') + CRLF
              + '&nbsp;REFI: ' +
                   %editw(peImpu(x).refi:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;DERE: ' +
                   %editw(peImpu(x).dere:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;SUBT: ' +
                   %editw(peImpu(x).subt:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;SERI: ' +
                   %editw(peImpu(x).seri:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;SEEM: ' +
                   %editw(peImpu(x).seem:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;PIMI: ' + %editw(peImpu(x).pimi:' 0 ,  ') + CRLF
              + '&nbsp;IMPI: ' +
                   %editw(peImpu(x).impi:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;PSSO: ' + %editw(peImpu(x).psso:' 0 ,  ') + CRLF
              + '&nbsp;SERS: ' +
                   %editw(peImpu(x).sers:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;PSSN: ' + %editw(peImpu(x).pssn:' 0 ,  ') + CRLF
              + '&nbsp;TSSN: ' +
                   %editw(peImpu(x).tssn:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;PIVI: ' + %editw(peImpu(x).pivi:' 0 ,  ') + CRLF
              + '&nbsp;IPR1: ' +
                   %editw(peImpu(x).ipr1:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;PIVN: ' + %editw(peImpu(x).pivn:' 0 ,  ') + CRLF
              + '&nbsp;IPR4: ' +
                   %editw(peImpu(x).ipr4:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;PIVR: ' + %editw(peImpu(x).pivr:' 0 ,  ') + CRLF
              + '&nbsp;IPR3: ' +
                   %editw(peImpu(x).ipr3:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;IPR5: ' +
                   %editw(peImpu(x).ipr5:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;IPR6: ' +
                   %editw(peImpu(x).ipr6:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;IPR7: ' +
                   %editw(peImpu(x).ipr7:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;IPR8: ' +
                   %editw(peImpu(x).ipr8:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;IPR9: ' +
                   %editw(peImpu(x).ipr9:' .   .   .   . 0 ,  ') + CRLF
              + '&nbsp;PREM: ' +
                   %editw(peImpu(x).prem:' .   .   .   . 0 ,  ') + CRLF
              + 'PEIMPU' + CRLF;
         COWLOG_spolog( peArcd : peSpol : Data );

       endfor;

       Data = 'PECON1(' + %trim(%char(x)) + ')'  + CRLF
            + 'RAMA: ' + %editc(peCon1.Rama:'X') + CRLF
            + 'XREA: ' + %editw(peCon1.Xrea:' 0 ,  ') + CRLF
            + 'PECON1' + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );

       Data = 'PECOND(' + %trim(%char(x)) + ')'  + CRLF
            + 'RAMA: ' + %editc(peCond.Rama:'X') + CRLF
            + 'ARSE: ' + %editc(peCond.Arse:'X') + CRLF
            + 'XREA: ' + %editw(peCond.Xrea:' 0 ,  ') + CRLF
            + 'READ: ' + %editw(peCond.Read:' .   .   .   . 0 ,  ') + CRLF
            + 'XOPR: ' + %editw(peCond.Xopr:' 0 ,  ') + CRLF
            + 'COPR: ' + %editw(peCond.Copr:' .   .   .   . 0 ,  ') + CRLF
            + 'XRE1: ' + %editw(peCond.Xre1:' 0 ,  ') + CRLF
            + 'XOP1: ' + %editw(peCond.Xop1:' 0 ,  ') + CRLF
            + 'PECOND';
       COWLOG_spolog( peArcd : peSpol : Data );

       Data = 'PEERRO: ' +  %trim(%char(peErro))          + CRLF
            + 'PEMSGS'                                    + CRLF
            + '&nbsp;PEMSEV: ' + %char(peMsgs.peMsev)     + CRLF
            + '&nbsp;PEMSID: ' + peMsgs.peMsid            + CRLF
            + '&nbsp;PEMSG1: ' + %trim(peMsgs.peMsg1)     + CRLF
            + '&nbsp;PEMSG2: ' + %trim(peMsgs.peMsg2)     + CRLF
            + 'PEMSGS';
       COWLOG_spolog( peArcd : peSpol : Data );
       if peErro <> 0;
         return *off;
       endif;

       return *on;
      /end-free
     P setCOWRCE1...
     P                 E

      * ------------------------------------------------------------------ *
      * setCOWGRA3 : Llamada a Wrapper COWGRA3 - Salvar Cotización.        *
      *                                                                    *
      * Retorna *on = Ok / *off = Error                                    *
      * ------------------------------------------------------------------ *
     P setCOWGRA3...
     P                 B
     D setCOWGRA3...
     D                 pi              n
      /free

       Data = CRLF                                          + CRLF
            + '<b>COWGRA3 (Request)</b>'                    + CRLF
            + 'Fecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))                    + CRLF
            + 'PEBASE'                                      + CRLF
            + '&nbsp;PEEMPR: ' + peBase.peEmpr              + CRLF
            + '&nbsp;PESUCU: ' + peBase.peSucu              + CRLF
            + '&nbsp;PENIVT: ' + %editc(peBase.peNivt:'X')  + CRLF
            + '&nbsp;PENIVC: ' + %editc(peBase.peNivc:'X')  + CRLF
            + '&nbsp;PENIT1: ' + %editc(peBase.peNit1:'X')  + CRLF
            + '&nbsp;PENIV1: ' + %editc(peBase.peNiv1:'X')  + CRLF
            + 'PEBASE'                                      + CRLF
            + 'PEASEN: '  + %editc(peClie.asen:'X')         + CRLF
            + 'PENOMB: '  + %trim(peClie.nomb)              + CRLF
            + 'PECIVA: '  + %editc(peClie.civa:'X')         + CRLF
            + 'PETIPE: '  + %trim(peClie.tipe)              + CRLF
            + 'PECOPO: '  + %editc(peClie.copo:'X')         + CRLF
            + 'PECOPS: '  + %editc(peClie.cops:'X')         + CRLF
            + 'PECUIT: '  + peclie.cuit                     + CRLF
            + 'PETIDO: '  + %editc(peClie.tido:'X')         + CRLF
            + 'PENRDO: '  + %editc(peclie.Nrdo:'X');
       COWLOG_spolog( peArcd : peSpol : Data );

       COWGRA3( peBase
              : peNctw
              : peClie.asen
              : peClie.nomb
              : peClie.civa
              : peClie.tipe
              : peClie.copo
              : peClie.cops
              : peClie.cuit
              : peClie.tido
              : peClie.nrdo
              : peErro
              : peMsgs        );
       if peErro <> 0;
         Data = '<br><br><b>COWGRA3 (Response)</b> : OK'    + CRLF;
       else;
         Data = '<br><br><b>COWGRA3 (Response)</b> : Error' + CRLF;
       endif;
       COWLOG_spolog( peArcd : peSpol : Data );

       Data = 'Fecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))                  + CRLF
            + 'PEERRO: ' +  %trim(%char(peErro))          + CRLF
            + 'PEMSGS'                                    + CRLF
            + '&nbsp;PEMSEV: ' + %char(peMsgs.peMsev)     + CRLF
            + '&nbsp;PEMSID: ' + peMsgs.peMsid            + CRLF
            + '&nbsp;PEMSG1: ' + %trim(peMsgs.peMsg1)     + CRLF
            + '&nbsp;PEMSG2: ' + %trim(peMsgs.peMsg2)     + CRLF
            + 'PEMSGS' + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );

       if peErro <> 0;
         return *off;
       endif;

       return *on;

      /end-free
     P setCOWGRA3...
     P                 E

      * ------------------------------------------------------------------ *
      * setErrorCOWRCE2 : Llamada a Wrapper COWRCE2 - Error.               *
      *                                                                    *
      * Retorna *on = Ok / *off = Error                                    *
      * ------------------------------------------------------------------ *
     P setErrorCOWRCE2...
     P                 B
     D setErrorCOWRCE2...
     D                 pi
      /free

       Data = '<br><br><b>COWRCE2 (Response)</b> : Error' + CRLF
            + 'Fecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))                  + CRLF
            + 'PEERRO: ' +  %trim(%char(peErro))          + CRLF
            + 'PEMSGS'                                    + CRLF
            + '&nbsp;PEMSEV: ' + %char(peMsgs.peMsev)     + CRLF
            + '&nbsp;PEMSID: ' + peMsgs.peMsid            + CRLF
            + '&nbsp;PEMSG1: ' + %trim(peMsgs.peMsg1)     + CRLF
            + '&nbsp;PEMSG2: ' + %trim(peMsgs.peMsg2)     + CRLF
            + 'PEMSGS' + CRLF;
       COWLOG_spolog( peArcd : peSpol : Data );

      /end-free
     P setErrorCOWRCE2...
     P                 E

      /define PMSG_LOAD_PROCEDURE
      /copy inf1luis/qcpybooks,pmsg_h

      /define PSYS_LOAD_PROCEDURE
      /copy inf1luis/qcpybooks,psys_h

      /define LOAD_CURLIB_PROCEDURE
      /copy inf1luis/qcpybooks,curlib_h

      /define GETSYSV_LOAD_PROCEDURE
      /copy inf1luis/qcpybooks,getsysv_h

