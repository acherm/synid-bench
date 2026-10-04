     H actgrp('SGF') dftactgrp(*no)
     H option(*nounref: *nodebugio: *srcstmt)

     D GETLIBATT       pr
     D  peLibr                       10a   const

     D GETLIBATT       pi
     D  peLibr                       10a   const

      /copy './qcpybooks/qlirlibd_h.rpgle'

     D Attributes      ds                  likeds(Attributes_t)
     D Receiver        ds                  likeds(Receiver_t)
     D QUsec           ds                  likeds(QUsec_t)
     D LirEntry        ds                  likeds(LirLibdEntry_t)
     D                                     based(Entry_p)
     D x               s             10i 0

      * ************************************************************ *
      * Atributos
      * ************************************************************ *
     D Tipo            s             10a
     D NbrAsp          s             10i 0
     D CrtAut          s             10a
     D CrtObjAud       s             10a
     D Texto           s             50a
     D TotalSize       s             20i 0
     D NbrObjs         s             10i 0
     D AspDevName      s             10a
     D AspGrpName      s             10a
     D CurJrn          s             10a
     D CurLstJrn       s             10a
     D CurLstJrnLib    s             10a
     D JrnImg          s             10a
     D OmtJrnEnt       s              1a
     D NewObjInhJrn    s              1a
     D JrnLstStrDatTim...
     D                 s              8a
     D JrnRcvNamApply  s             10a
     D JrnRcvNamAppLib...
     D                 s             10a
     D JrnRcvAspNam    s             10a
     D JrnRcvAspLib    s             10a

      /free

       Attributes.NbrAtts = 21;
       Attributes.Key(1)  = 1;
       Attributes.Key(2)  = 2;
       Attributes.Key(3)  = 3;
       Attributes.Key(4)  = 4;
       Attributes.Key(5)  = 5;
       Attributes.Key(6)  = 6;
       Attributes.Key(7)  = 7;
       Attributes.Key(8)  = 8;
       Attributes.Key(9)  = 9;
       Attributes.Key(10) = 10;
       Attributes.Key(11) = 11;
       Attributes.Key(12) = 12;
       Attributes.Key(13) = 13;
       Attributes.Key(14) = 14;
       Attributes.Key(15) = 15;
       Attributes.Key(16) = 16;
       Attributes.Key(17) = 17;
       Attributes.Key(18) = 18;
       Attributes.Key(19) = 19;
       Attributes.Key(20) = 20;
       Attributes.Key(21) = 21;

       QLIRLIBD( Receiver
               : %size(Receiver)
               : %trim(peLibr)
               : Attributes
               : QUsec       );

       Entry_p = %addr(Receiver) + %size(Receiver.hdr);

       for x = 1 to Receiver.Hdr.VarLenRecRet;
           select;
            when (LirEntry.EntryHdr.CtlKey = 1);
                 select;
                  when (LirEntry.Type = '0');
                       Tipo = '*PROD';
                  when (LirEntry.Type = '1');
                       Tipo = '*TEST';
                  other;
                       Tipo = '*ERROR';
                 endsl;
            when (LirEntry.EntryHdr.CtlKey = 2);
                 NbrAsp = LirEntry.AspNbr;
            when (LirEntry.EntryHdr.CtlKey = 3);
                 CrtAut = LirEntry.CrtAut;
            when (LirEntry.EntryHdr.CtlKey = 4);
                 CrtObjAud = LirEntry.CrtObjAud;
            when (LirEntry.EntryHdr.CtlKey = 5);
                 Texto = LirEntry.Text;
            when (LirEntry.EntryHdr.CtlKey = 6);
                 TotalSize = LirEntry.Size * LirEntry.SizeMult;
            when (LirEntry.EntryHdr.CtlKey = 7);
                 NbrObjs = LirEntry.NbrOfObjs;
            when (LirEntry.EntryHdr.CtlKey = 8);
                 AspDevName = LirEntry.AspDevName;
            when (LirEntry.EntryHdr.CtlKey = 9);
                 AspGrpName = LirEntry.AspGrpName;
            when (LirEntry.EntryHdr.CtlKey = 10);
                 CurJrn     = LirEntry.CurJrn;
            when (LirEntry.EntryHdr.CtlKey = 11);
                 CurLstJrn  = LirEntry.CurLstJrn;
            when (LirEntry.EntryHdr.CtlKey = 12);
                 CurLstJrnLib  = LirEntry.CurLstJrnLib;
            when (LirEntry.EntryHdr.CtlKey = 13);
                 JrnImg = LirEntry.JrnImg;
            when (LirEntry.EntryHdr.CtlKey = 14);
                 OmtJrnEnt = LirEntry.OmtJrnEnt;
            when (LirEntry.EntryHdr.CtlKey = 15);
                 NewObjInhJrn = LirEntry.NewObjInhJrn;
            when (LirEntry.EntryHdr.CtlKey = 16);
                 JrnLstStrDatTim = LirEntry.JrnLstStrDatTim;
            when (LirEntry.EntryHdr.CtlKey = 17);
                 JrnRcvNamApply  = LirEntry.JrnRcvNamApply;
            when (LirEntry.EntryHdr.CtlKey = 18);
                 JrnRcvNamAppLib = LirEntry.JrnRcvNamAppLib;
            when (LirEntry.EntryHdr.CtlKey = 19);
                 JrnRcvAspNam    = LirEntry.JrnRcvAspNam;
            when (LirEntry.EntryHdr.CtlKey = 20);
                 JrnRcvAspLib    = LirEntry.JrnRcvAspLib;
           endsl;
           Entry_p += LirEntry.EntryHdr.VarLenRecLen;
       endfor;

       return;

      /end-free
