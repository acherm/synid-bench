     H option(*nodebugio:*noshowcpy:*srcstmt)
     H actgrp(*new) dftactgrp(*no)
     H bnddir ('HDIILE/HDIBDIR')
      * ************************************************************ *
      * PRWASE9: WebService                                          *
      *          Propuesta Web                                       *
      *          Wrapper para _insertAseguradoAdicional()            *
      * ------------------------------------------------------------ *
      * ATENCION: Este servicio REEMPLAZA a PRWASE4.                 *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                         *04-Ene-2016        *
      * ************************************************************ *

      /copy './qcpybooks/prwase_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'

     D PRWASE9         pr                  ExtPgm('PRWASE9')
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peAsen                       7  0   const
     D   peNase                       6  0   const
     D   peNomb                      40a     const
     D   peDomi                            likeds(prwaseDomi_t) const
     D   peDocu                            likeds(prwaseDocu_t) const
     D   peNtel                            likeds(prwaseTele_t) const
     D   peTiso                       2  0   const
     D   peNaci                            likeds(prwaseNaco_t) const
     D   peCprf                       3  0   const
     D   peSexo                       1  0   const
     D   peEsci                       1  0   const
     D   peRaae                       3  0   const
     D   peMail                            likeds(prwaseEmail_t) const
     D   peAgpe                       1a   const
     D   peTarc                            likeds(prwaseTarc_t) const
     D   peNcbu                      22  0   const
     D   peCbus                      22  0   const
     D   peRuta                      16  0   const
     D   peCiva                       2  0   const
     D   peInsc                            likeds(prwaseInsc_t) const
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D PRWASE9         pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peAsen                       7  0   const
     D   peNase                       6  0   const
     D   peNomb                      40a     const
     D   peDomi                            likeds(prwaseDomi_t) const
     D   peDocu                            likeds(prwaseDocu_t) const
     D   peNtel                            likeds(prwaseTele_t) const
     D   peTiso                       2  0   const
     D   peNaci                            likeds(prwaseNaco_t) const
     D   peCprf                       3  0   const
     D   peSexo                       1  0   const
     D   peEsci                       1  0   const
     D   peRaae                       3  0   const
     D   peMail                            likeds(prwaseEmail_t) const
     D   peAgpe                       1a   const
     D   peTarc                            likeds(prwaseTarc_t) const
     D   peNcbu                      22  0   const
     D   peCbus                      22  0   const
     D   peRuta                      16  0   const
     D   peCiva                       2  0   const
     D   peInsc                            likeds(prwaseInsc_t) const
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D Data            s          65535a   varying
     D CRLF            s              4a   inz('<br>')
     D separa          s            100a

      /free

       *inlr = *on;

       separa = *all'-';

       Data = '<br><br>'
            + '<b>PRWASE9  (Request)</b>'              + CRLF
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
            + 'PEASEN: '  + %editc(peAsen:'X')         + CRLF
            + 'PENASE: '  + %editc(peNase:'X')         + CRLF
            + 'PENOMB: '  + peNomb                     + CRLF
            + 'PEDOMI'                                 + CRLF
            + '&nbsp;DOMI: ' + peDomi.domi             + CRLF
            + '&nbsp;COPO: ' + %editc(peDomi.copo:'X') + CRLF
            + '&nbsp;COPS: ' + %editc(peDomi.cops:'X') + CRLF
            + 'PEDOMI'                                 + CRLF
            + 'PEDOCU'                                 + CRLF
            + '&nbsp;TIDO: ' + %editc(peDocu.tido:'X') + CRLF
            + '&nbsp;NRDO: ' + %editc(peDocu.nrdo:'X') + CRLF
            + '&nbsp;CUIT: ' + %editc(peDocu.cuit:'X') + CRLF
            + '&nbsp;CUIL: ' + %editc(peDocu.cuil:'X') + CRLF
            + 'PEDOCU'                                 + CRLF
            + 'PENTEL'                                 + CRLF
            + '&nbsp;NTE1: ' + peNtel.nte1             + CRLF
            + '&nbsp;NTE2: ' + peNtel.nte2             + CRLF
            + '&nbsp;NTE3: ' + peNtel.nte3             + CRLF
            + '&nbsp;NTE4: ' + peNtel.nte4             + CRLF
            + '&nbsp;PWEB: ' + peNtel.pweb             + CRLF
            + 'PENTEL'                                 + CRLF
            + 'PETISO: '  + %editc(peTiso:'X')         + CRLF
            + 'PENACI'                                 + CRLF
            + '&nbsp;FNAC: ' + %editc(peNaci.fnac:'X') + CRLF
            + '&nbsp;LNAC: ' + peNaci.lnac             + CRLF
            + '&nbsp;PAIN: ' + %editc(peNaci.pain:'X') + CRLF
            + '&nbsp;CNAC: ' + %editc(peNaci.cnac:'X') + CRLF
            + 'PENACI'                                 + CRLF
            + 'PECPRF: '  + %editc(peCprf:'X')         + CRLF
            + 'PESEXO: '  + %editc(peSexo:'X')         + CRLF
            + 'PEESCI: '  + %editc(peEsci:'X')         + CRLF
            + 'PERAAE: '  + %editc(peRaae:'X')         + CRLF
            + 'PEMAIL'                                 + CRLF
            + '&nbsp;CTCE: ' + %editc(peMail.ctce:'X') + CRLF
            + '&nbsp;MAIL: ' + peMail.mail             + CRLF
            + 'PEMAIL'                                 + CRLF
            + 'PEAGPE: '  + peAgpe                     + CRLF
            + 'PETARC'                                 + CRLF
            + '&nbsp;CTCU: ' + %editc(peTarc.ctcu:'X') + CRLF
            + '&nbsp;NRTC: ' + %editc(peTarc.nrtc:'X') + CRLF
            + '&nbsp;FFTA: ' + %editc(peTarc.ffta:'X') + CRLF
            + '&nbsp;FFTM: ' + %editc(peTarc.fftm:'X') + CRLF
            + 'PETARC'                                 + CRLF
            + 'PENCBU: '  + %editc(peNcbu:'X')         + CRLF
            + 'PECBUS: '  + %editc(peCbus:'X')         + CRLF
            + 'PERUTA: '  + %editc(peRuta:'X')         + CRLF
            + 'PECIVA: '  + %editc(peCiva:'X')         + CRLF
            + 'PEINSC'                                 + CRLF
            + '&nbsp;FEIN: ' + %editc(peInsc.fein:'X') + CRLF
            + '&nbsp;NRIN: ' + %editc(peInsc.nrin:'X') + CRLF
            + '&nbsp;FECO: ' + %editc(peInsc.feco:'X') + CRLF
            + 'PEINSC';
       COWLOG_log( peBase : peNctw : Data );

       PRWASE_insertAseguradoAdicional2( peBase
                                       : peNctw
                                       : peAsen
                                       : peNase
                                       : peNomb
                                       : peDomi
                                       : peDocu
                                       : peNtel
                                       : peTiso
                                       : peNaci
                                       : peCprf
                                       : peSexo
                                       : peEsci
                                       : peRaae
                                       : peMail
                                       : peAgpe
                                       : peTarc
                                       : peNcbu
                                       : peCbus
                                       : peRuta
                                       : peCiva
                                       : peInsc
                                       : peErro
                                       : peMsgs );

       Data = '<br><br>'
            + '<b>PRWASE9 (Response)</b>'                 + CRLF
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
       COWLOG_log( peBase : peNctw : Data );
       Data = separa;
       COWLOG_log( peBase : peNctw : Data );

       return;

      /end-free
