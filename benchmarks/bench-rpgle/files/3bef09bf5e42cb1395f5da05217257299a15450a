     H option(*nodebugio:*srcstmt)
     H actgrp(*new) dftactgrp(*no)
     H bnddir ( 'HDIILE/HDIBDIR' )
      * ************************************************************ *
      * COWVEH14:WebService                                          *
      *          Cotización Autos - wrapper para _cotizarWeb()       *
      * ------------------------------------------------------------ *
      * Jennifer Segovia                         *12-Sep-2019        *
      * ------------------------------------------------------------ *
      * ************************************************************ *
      /copy './qcpybooks/cowveh_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'

     D COWVEH14        pr                  ExtPgm('COWVEH14')
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peVhvu                      15  2 const
     D   peMgnc                       1    const
     D   peRgnc                       7  2 const
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
     D   peScta                       1  0 const
     D   peClin                       1    const
     D   peBure                       1  0 const
     D   peCfpg                       3  0 const
     D   peTipe                       1    const
     D   peCiva                       2  0 const
     D   peAcce                            likeds(AccVeh_t) dim(100) const
     D   peDesE                       5  2 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh) dim(20)
     D   peBoni                            likeds(bonVeh) dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D COWVEH14        pi
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peVhvu                      15  2 const
     D   peMgnc                       1    const
     D   peRgnc                       7  2 const
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
     D   peScta                       1  0 const
     D   peClin                       1    const
     D   peBure                       1  0 const
     D   peCfpg                       3  0 const
     D   peTipe                       1    const
     D   peCiva                       2  0 const
     D   peAcce                            likeds(AccVeh_t) dim(100) const
     D   peDesE                       5  2 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh) dim(20)
     D   peBoni                            likeds(bonVeh) dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

     D i               s             10i 0
     D Data            s          65535a   varying
     D CRLF            s              4a   inz('<br>')
     D separa          s            100a
     D @@DsTim         ds                  likeDs( Dsctwtim_t)

      /free

       *inlr = *on;

       clear pePaxc;
       clear peBoni;
       clear peImpu;
       clear peErro;
       clear peMsgs;
       separa = *all'-';

       Data = CRLF                                     + CRLF
            + '<b>COWVEH14-Cotizar Vehiculos(Request)</b>' + CRLF
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
            + 'PERAMA: '  + %editc(peRama:'X')         + CRLF
            + 'PEARSE: '  + %editc(peArse:'X')         + CRLF
            + 'PEPOCO: '  + %editc(pePoco:'X')         + CRLF
            + 'PEVHAN: '  + peVhan                     + CRLF
            + 'PEVHMC: '  + %trim(peVhmc)              + CRLF
            + 'PEVHMO: '  + %trim(peVhmo)              + CRLF
            + 'PEVHCS: '  + %trim(peVhcs)              + CRLF
            + 'PEVHVU: '  + %trim(%editc(peVhvu:'K'))  + CRLF
            + 'PEMGNC: '  + %trim(peMgnc)              + CRLF
            + 'PERGNC: '  + %trim(%editc(peRgnc:'K'))  + CRLF
            + 'PECOPO: '  + %editc(peCopo:'X')         + CRLF
            + 'PECOPS: '  + %editc(peCops:'X')         + CRLF
            + 'PESCTA: '  + %editc(peScta:'X')         + CRLF
            + 'PECLIN: '  + %trim(peClin)              + CRLF
            + 'PEBURE: '  + %editc(peBure:'X')         + CRLF
            + 'PECFPG: '  + %editc(peCfpg:'X')         + CRLF
            + 'PETIPE: '  + %trim(peTipe)              + CRLF
            + 'PECIVA: '  + %editc(peCiva:'X');
       COWLOG_log( peBase : peNctw : Data );

       for i = 1 to 100;
           if peAcce(i).secu = *Zeros;
              leave;
           endif;
           Data =                                               CRLF
                + 'PEACCE(' + %trim(%char(i)) + ')'           + CRLF
                + '&nbsp;PESECU: '+%editc(peAcce(i).secu:'X') + CRLF
                + '&nbsp;PEACCD: '+%trim(peAcce(i).accd)      + CRLF
                + '&nbsp;PEACCV: '+%editc(peAcce(i).accv:'X') + CRLF
                + '&nbsp;PEMAR1: '+%trim(peAcce(i).mar1)      + CRLF
                + 'PEACCE'                                    + CRLF;
       COWLOG_log( peBase : peNctw : Data );
       endfor;

       Data =                                        CRLF
            + 'PEDESE: '  + %editc(peDesE:'X')     + CRLF
            + 'PETAAJ: '  + %editc(peTaaj:'X')           ;
       COWLOG_log( peBase : peNctw : Data );

       for i = 1 to 200;
           if peScor(i).cosg = *blanks;
              leave;
           endif;
           Data =                                               CRLF
                + 'PESCOR(' + %trim(%char(i)) + ')'           + CRLF
                + '&nbsp;PECOSG: '+%trim(peScor(i).cosg)      + CRLF
                + '&nbsp;PEVEFA: '+%trim(peScor(i).vefa)      + CRLF
                + '&nbsp;PECANT: '+%editc(peScor(i).cant:'X') + CRLF
                + 'PESCOR'                                    + CRLF;
       COWLOG_log( peBase : peNctw : Data );
       endfor;

       callp COWVEH_cotizarWeb3( peBase
                               : peNctw
                               : peRama
                               : peArse
                               : pePoco
                               : peVhan
                               : peVhmc
                               : peVhmo
                               : peVhcs
                               : peVhvu
                               : peMgnc
                               : peRgnc
                               : peCopo
                               : peCops
                               : peScta
                               : peClin
                               : peBure
                               : peCfpg
                               : peTipe
                               : peCiva
                               : peAcce
                               : peDesE
                               : peTaaj
                               : peScor
                               : peCtre
                               : pePaxc
                               : peBoni
                               : peImpu
                               : peErro
                               : peMsgs  );

        clear @@DsTim;
        if COWGRAI_getAuditoria( peBase
                               : peNctw
                               : @@DsTim );
          @@DsTim.w0fcot = %dec(%date : *iso);
          @@DsTim.w0hcot = %dec(%time);
          COWGRAI_setAuditoria( @@DsTim );
        endif;
       Data =
            '<br><b>COWVEH14-Cotizar Vehiculos(Response)</b>' + CRLF
            + 'Fecha/Hora: '
            + %trim(%char(%date():*iso)) + ' '
            + %trim(%char(%time():*iso))               + CRLF
            + 'PECTRE: '  + %editc(peCtre:'X');
       COWLOG_log( peBase : peNctw : Data );

       for i = 1 to 20;
           if pePaxc(i).cobl = *blanks;
              leave;
           endif;
           Data =                                               CRLF
                + 'PEPAXC(' + %trim(%char(i)) + ')'           + CRLF
                + '&nbsp;COBL: ' + pePaxc(i).cobl                  + CRLF
                + '&nbsp;COBD: ' + pePaxc(i).cobd                  + CRLF
                + '&nbsp;RAST: ' + pePaxc(i).rast                  + CRLF
                + '&nbsp;CRAS: ' + %editc(pePaxc(i).cras:'X')      + CRLF
                + '&nbsp;INSP: ' + pePaxc(i).insp                  + CRLF
                + '&nbsp;SELE: ' + pePaxc(i).sele                  + CRLF
                + '&nbsp;PRIM: ' + %editc(pePaxc(i).prim:'K')      + CRLF
                + '&nbsp;PREM: ' + %editc(pePaxc(i).prem:'K')      + CRLF
                + '&nbsp;CDFT: ' + pePaxc(i).cdft                  + CRLF
                + '&nbsp;IFRA: ' + %editc(pePaxc(i).ifra:'K')      + CRLF
                + '&nbsp;RCLE: ' + %editc(pePaxc(i).rcle:'K')      + CRLF
                + '&nbsp;RCCO: ' + %editc(pePaxc(i).rcco:'K')      + CRLF
                + '&nbsp;RCAC: ' + %editc(pePaxc(i).rcac:'K')      + CRLF
                + '&nbsp;LRCE: ' + %editc(pePaxc(i).lrce:'K')      + CRLF
                + '&nbsp;CLAJ: ' + %editc(pePaxc(i).claj:'X')      + CRLF
                + 'PEPAXC';
           COWLOG_log( peBase : peNctw : Data );
       endfor;

       for i = 1 to 99;
           if peBoni(i).cobl = *blanks;
              leave;
           endif;
           Data =                                               CRLF
                + 'PEBONI(' + %trim(%char(i)) + ')'           + CRLF
                + '&nbsp;COBL: ' + peBoni(i).cobl                  + CRLF
                + '&nbsp;CCBP: ' + %editc(peBoni(i).ccbp:'X')      + CRLF
                + '&nbsp;DCBP: ' + peBoni(i).dcbp                  + CRLF
                + '&nbsp;PCBP: ' + %editw(peBoni(i).pcbp:' 0 ,  ') + CRLF
                + '&nbsp;PCBM: ' + %editw(peBoni(i).pcbm:' 0 ,  ') + CRLF
                + '&nbsp;PCBX: ' + %editw(peBoni(i).pcbx:' 0 ,  ') + CRLF
                + '&nbsp;MODI: ' + peBoni(i).modi                  + CRLF
                + 'PEBONI';
           COWLOG_log( peBase : peNctw : Data );
       endfor;

       for i = 1 to 99;
           if peImpu(i).cobl = *blanks;
              leave;
           endif;
           Data =                                               CRLF
                + 'PEIMPU(' + %trim(%char(i)) + ')'           + CRLF
                + '&nbsp;COBL: ' + peImpu(i).cobl                  + CRLF
                + '&nbsp;XREA: ' + %editw(peImpu(i).xrea:' 0 ,  ') + CRLF
                + '&nbsp;READ: ' + %editc(peImpu(i).read:'K')      + CRLF
                + '&nbsp;XOPR: ' + %editw(peImpu(i).xopr:' 0 ,  ') + CRLF
                + '&nbsp;COPR: ' + %editc(peImpu(i).copr:'K')      + CRLF
                + '&nbsp;XREF: ' + %editw(peImpu(i).xref:' 0 ,  ') + CRLF
                + '&nbsp;REFI: ' + %editc(peImpu(i).refi:'K')      + CRLF
                + '&nbsp;DERE: ' + %editc(peImpu(i).dere:'K')      + CRLF
                + '&nbsp;SERI: ' + %editc(peImpu(i).seri:'K')      + CRLF
                + '&nbsp;SEEM: ' + %editc(peImpu(i).seem:'K')      + CRLF
                + '&nbsp;PIMI: ' + %editw(peImpu(i).pimi:' 0 ,  ') + CRLF
                + '&nbsp;IMPI: ' + %editc(peImpu(i).impi:'K')      + CRLF
                + '&nbsp;PSSO: ' + %editw(peImpu(i).psso:' 0 ,  ') + CRLF
                + '&nbsp;SERS: ' + %editc(peImpu(i).sers:'K')      + CRLF
                + '&nbsp;PSSN: ' + %editw(peImpu(i).pssn:' 0 ,  ') + CRLF
                + '&nbsp;TSSN: ' + %editc(peImpu(i).tssn:'K')      + CRLF
                + '&nbsp;PIVI: ' + %editw(peImpu(i).pivi:' 0 ,  ') + CRLF
                + '&nbsp;IPR1: ' + %editc(peImpu(i).ipr1:'K')      + CRLF
                + '&nbsp;PIVN: ' + %editw(peImpu(i).pivn:' 0 ,  ') + CRLF
                + '&nbsp;IPR4: ' + %editc(peImpu(i).ipr4:'K')      + CRLF
                + '&nbsp;PIVR: ' + %editw(peImpu(i).pivr:' 0 ,  ') + CRLF
                + '&nbsp;IPR3: ' + %editc(peImpu(i).ipr3:'K')      + CRLF
                + '&nbsp;IPR6: ' + %editc(peImpu(i).ipr6:'K')      + CRLF
                + '&nbsp;IPR7: ' + %editc(peImpu(i).ipr7:'K')      + CRLF
                + '&nbsp;IPR8: ' + %editc(peImpu(i).ipr8:'K')      + CRLF
                + 'PEIMPU';
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

       return;

      /end-free
