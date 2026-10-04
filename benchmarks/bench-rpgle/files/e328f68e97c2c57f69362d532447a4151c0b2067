     H option(*nodebugio:*noshowcpy:*srcstmt) alwnull(*usrctl)
     H dftactgrp(*no) actgrp(*new)
     H bnddir ( 'HDIILE/HDIBDIR' )

      * ************************************************************ *
      * COWRTV8: Retorna Información de todos los componentes Vida   *
      *                                                              *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *25-Ene-2017            *
      * ------------------------------------------------------------ *
      * ATENCION: Este Servicio reemplaza a COWRTV5.                 *
      *                                                              *
      * ************************************************************ *

     D COWRTV8         pr                  ExtPgm('COWRTV8')
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peComp                            likeds(CompVid2) dim(99)
     D   peCompC                     10i 0
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D COWRTV8         pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peComp                            likeds(CompVid2) dim(99)
     D   peCompC                     10i 0
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)
     D
     D i               s             10i 0
     D o               s             10i 0
     D Data            s          65535a   varying
     D CRLF            s              4a   inz('<br>')
     D separa          s            100a   inz(*all'-')

      /copy './qcpybooks/cowrtv_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'
1
       *inlr  = *on;

       clear peComp;
       clear peMsgs;

       peCompC = 0;
       peErro  = *Zeros;

      //Log de Entrada...
       Data = CRLF                                          + CRLF
            + '<b>COWRTV8 (Request)</b>'                    + CRLF
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
            + 'PEBASE';
       COWLOG_log( peBase : peNctw : Data );

       clear peComp;

       COWRTV_getComponentesVid2 ( peBase
                                 : peNctw
                                 : peComp
                                 : peErro
                                 : peMsgs );

       for i = 1 to 99;
           if peComp(i).rama = 0;
              peCompC = i - 1;
              leave;
           endif;
       endfor;

       Data =
          '<br><br><b>COWRTV8 (Response)</b>'      + CRLF
        + 'Fecha/Hora: '
        + %trim(%char(%date():*iso)) + ' '
        + %trim(%char(%time():*iso));

       COWLOG_log( peBase : peNctw : Data );

       for i = 1 to 99;
          if peComp(i).rama = *zeros;
             leave;
          endif;


           Data =                                               CRLF
                + 'PECOMP(' + %trim(%char(i)) + ')'           + CRLF
                + '&nbsp;RAMA: ' + %editc(peComp(i).rama:'X') + CRLF
                + '&nbsp;POCO: ' + %editc(peComp(i).poco:'X') + CRLF
                + '&nbsp;ARSE: ' + %editc(peComp(i).Arse:'X') + CRLF
                + '&nbsp;ACTI: ' + %editc(peComp(i).Acti:'X') + CRLF
                + '&nbsp;SECU: ' + %editc(peComp(i).Secu:'X') + CRLF
                + '&nbsp;XPRO: ' + %editc(peComp(i).Xpro:'X') + CRLF
                + '&nbsp;NOMB: ' + %trim (peComp(i).Nomb)     + CRLF
                + '&nbsp;TIDO: ' + %editc(peComp(i).tido:'X') + CRLF
                + '&nbsp;NRDO: ' + %editc(peComp(i).nrdo:'X') + CRLF
                + '&nbsp;FNAC: ' + %editc(peComp(i).fnac:'X') + CRLF
                + '&nbsp;NACI: ' + %trim (peComp(i).naci)     + CRLF
                + '&nbsp;CATE: ' + %editc(peComp(i).cate:'X') + CRLF
                + '&nbsp;CANT: ' + %editc(peComp(i).cant:'X') + CRLF
                + '&nbsp;RAED: ' + %editc(peComp(i).raed:'X') + CRLF
                + 'PECOMP';
           COWLOG_log( peBase : peNctw : Data );

          for o = 1 to 20;
            if  peComp(i).cobe(o).secu = *zeros;
             leave;
            endif;
          Data =                                                     CRLF
             + 'COBE(' + %trim(%char(o)) + ')'                     + CRLF
             + '&nbsp;SECU: ' + %editc (peComp(i).Cobe(o).secu:'X')+ CRLF
             + '&nbsp;RIEC: ' + %trim  (peComp(i).Cobe(o).riec)    + CRLF
             + '&nbsp;XCOB: ' + %editc (peComp(i).Cobe(o).xcob:'X')+ CRLF
             + '&nbsp;SACO: ' + %editc (peComp(i).Cobe(o).saco:'K')+ CRLF
             + '&nbsp;PTCO: ' + %editc (peComp(i).Cobe(o).ptco:'K')+ CRLF
             + '&nbsp;XPRI: ' + %editc (peComp(i).Cobe(o).xpri:'K')+ CRLF
             + '&nbsp;PRSA: ' + %editc (peComp(i).Cobe(o).prsa:'X')+ CRLF
             + '&nbsp;ECOB: ' + %trim  (peComp(i).Cobe(o).ecob    )+ CRLF
             + 'COBE';
            COWLOG_log( peBase : peNctw : Data );
          endfor;

          Data =                                                     CRLF
               + '&nbsp;PREM: ' + %editc(peComp(i).prem:'X') + CRLF ;
          COWLOG_log( peBase : peNctw : Data );

           Data =                                                    CRLF
                + 'PECOMP';
           COWLOG_log( peBase : peNctw : Data );

       endfor;

       Data =                                               CRLF
            + 'PEERRO: ' +  %trim(%char(peErro))          + CRLF
            + 'PEMSGS'                                    + CRLF
            + '&nbsp;PEMSEV: ' + %char(peMsgs.peMsev)     + CRLF
            + '&nbsp;PEMSID: ' + peMsgs.peMsid            + CRLF
            + '&nbsp;PEMSG1: ' + %trim(peMsgs.peMsg1)     + CRLF
            + '&nbsp;PEMSG2: ' + %trim(peMsgs.peMsg2)     + CRLF
            + 'PEMSGS' + CRLF;
       COWLOG_log( peBase : peNctw : Data );
       Data = separa;
       COWLOG_log( peBase : peNctw : Data );

       COWRTV_end();

       return;
