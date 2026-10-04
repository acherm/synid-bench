**FREE
      //DFTACTGRP(*NO) OPTION(*SRCSTMT: *NODEBUGIO)

     Ctl-Opt Option(*Srcstmt: *Nodebugio);

      //  This program will find all places that a bound module is called.
      //    (by searching all ILE programs in the user libraries)
      //
      //         Scott Klement,  May 7, 1997
      //

     Dcl-F SRVPGMMODE USAGE(*OUTPUT);

      //
      //  Field Definitions.
      //
     // Dcl-s searchlibrary    Char(10);
     // Dcl-s ObjectLibrary    Char(10);

     Dcl-PR EC_Escape;
       Whenx           Char(60)     const;
       CallStackCnt    Int(10)      value;
       ErrorCode       Char(32766)  options(*varsize);
     end-pr;

      // List ILE program information API
     Dcl-PR QBNLPGMI    ExtPgm('QBNLPGMI');
       UsrSpc     Char(20)     const;
       Format     Char(8)      const;
       PgmName    Char(20)     const;
       Errors     Char(32766)  options(*varsize);
     end-pr;

      // List ILE service program information API
     Dcl-PR QBNLSPGM    ExtPgm('QBNLSPGM');
       UsrSpc    Char(20)     const;
       Format    Char(8)      const;
       SrvPgm    Char(20)     const;
       Errors    Char(32766)  options(*varsize);
     end-pr;

      // Create User Space API
     Dcl-Pr QUSCRTUS    ExtPgm('QUSCRTUS');
       UsrSpc       Char(20)     const;
       ExtAttr      Char(10)     const;
       InitSize     Int(10)      const;
       InitVal      Char(1)      const;
       PublicAuth   Char(10)     const;
       Text         Char(50)     const;
       Replace      Char(10)     const;
       Errors       Char(32766)  options(*varsize);
     end-pr;

      // Retrieve pointer to user space API
     Dcl-PR QUSPTRUS    ExtPgm('QUSPTRUS');
       UsrSpc     Char(20)   const;
       Pointer    pointer;
     end-pr;

      // API error code structure
     dcl-ds dsEC;
       dsECBytesP    Int(10) inz(%size(dsEC));
       dsECBytesA    Int(10) inz(0);
       dsECMsgID     Char(7);
       dsECReserv    Char(1);
       dsECMsgDta    Char(240);
     end-ds;

      //  List API generic header structure
     dcl-s p_Header    pointer;

     dcl-ds dsLH    BASED(p_Header);
      //                                     Filler
       dsLHFill1     char(103);
      //  Status (I=Incomplete,C=Complete
       dsLHStatus    char(1);
       dsLHFill2     char(12);
       dsLHHdrOff    int(10);
       dsLHHdrSiz    int(10);
       dsLHLstOff    int(10);
       dsLHLstSiz    int(10);
       dsLHEntCnt    int(10);
       dsLHEntSiz    int(10);
     end-ds;
      //
      // PGML0100 format: modules in program
      // SPGL0100 format: modules in service program
      // (these fields are the same in both APIs)
     dcl-s p_Entry    Pointer;

     dcl-ds dsPgm       based(p_Entry);
       dsPgm_Pgm       Char(10);
       dsPgm_PgmLib    Char(10);
       dsPgm_Module    Char(10);
       dsPgm_ModLib    Char(10);
       dsPgm_SrcF      Char(10);
       dsPgm_SrcLib    Char(10);
       dsPgm_SrcMbr    Char(10);
       dsPgm_Attrib    Char(10);
       dsPgm_CrtDat    Char(13);
       dsPgm_SrcDat    Char(13);
     end-ds;

     // dcl-s peModule    char(10);

     // dcl-s Searchlibrary  Char(10);
     dcl-s Objectlibrary  Char(20);
     dcl-s Entry          int(10);
     // dcl-s peModule       Char(10);


     dcl-PR Main ExtPgm('GetSrvPgm');
        peModule         Char(10);
        Searchlibrary    Char(10);
     end-PR;

     dcl-PI main;
        peModule         Char(10);
        Searchlibrary    Char(10);
     end-PI;



       // except PrtHeader;

       // Create a user space to stuff module info into
       QUSCRTUS( 'MODULES   QTEMP'
               : 'USRSPC'
               : 5120*3072
               : x'00'
               : '*ALL'
               : 'List of modules'
               : '*YES'
               : dsEC
               );

       if dsECBytesA > 0;
         EC_Escape( 'Calling QUSCRTUS API'
                  : 3
                  : dsEC
                  );
       endif;

       QUSPTRUS( 'MODULES   QTEMP'
               : p_Header
               );

       objectLibrary = '*ALL      ' + searchlibrary;

       // List all ILE programs modules to space
       QBNLPGMI( 'MODULES   QTEMP'
               : 'PGML0100'
               : objectLibrary
               : dsEC
               );

       if dsECBytesA > 0;
         EC_Escape( 'Calling QBNLPGMI API'
                  : 3
                  : dsEC
                  );
       endif;

       // List occurrances of our module
       p_Entry = p_Header + dsLHLstOff;

       for Entry = 1 to dsLHEntCnt;
         if dsPgm_Module = peModule;

           Pgm_Pgm    = dsPgm_Pgm;
           Pgm_PgmLib = dsPgm_PgmLib;
           Pgm_Module = dsPgm_Module;
           Pgm_ModLib = dsPgm_ModLib;
           Pgm_SrcF   = dsPgm_SrcF;
           Pgm_SrcLib = dsPgm_SrcLib;
           Pgm_SrcMbr = dsPgm_SrcMbr;
           Pgm_Attrib = dsPgm_Attrib;
           Pgm_CrtDat = dsPgm_CrtDat;
           Pgm_SrcDat = dsPgm_SrcDat;

           write srvpgmModR;

         endif;
         p_Entry = p_Entry + dsLHEntSiz;
       endfor;

       // List all ILE service program modules to space
       QBNLSPGM( 'MODULES   QTEMP'
               : 'SPGL0100'
               : '*ALL      *ALLUSR'
               : dsEC
               );

       if dsECBytesA > 0;
         EC_Escape( 'Calling QBNLSPGM API'
                  : 3
                  : dsEC
                  );
       endif;

       // List occurrances of our module
       p_Entry = p_Header + dsLHLstOff;

       for Entry = 1 to dsLHEntCnt;
         if dsPgm_Module = peModule;

           Pgm_Pgm    = dsPgm_Pgm;
           Pgm_PgmLib = dsPgm_PgmLib;
           Pgm_Module = dsPgm_Module;
           Pgm_ModLib = dsPgm_ModLib;
           Pgm_SrcF   = dsPgm_SrcF;
           Pgm_SrcLib = dsPgm_SrcLib;
           Pgm_SrcMbr = dsPgm_SrcMbr;
           Pgm_Attrib = dsPgm_Attrib;
           Pgm_CrtDat = dsPgm_CrtDat;
           Pgm_SrcDat = dsPgm_SrcDat;

           write srvpgmModR;

         endif;
         p_Entry = p_Entry + dsLHEntSiz;
       endfor;

       // And that's about the size of it
       *inlr = *on;



     //OQSYSPRT   E            PrtHeader         2  3
     //o                       *DATE         Y     10
     //o                                           +3 'Listing of programs'
     //o                                           +1 'that use module'
     //o                       peModule            +1
     //o                                           75 'Page'
     //o                       PAGE          Z     80

     //o          E            PrtModule         2  3
     //o                       dsPgm_Pgm           10
     //o                       dsPgm_PgmLib        +1
     //o                       dsPgm_SrcF          +1
     //o                       dsPgm_SrcLib        +1
     //o                       dsPgm_SrcMbr        +1
     //o                       dsPgm_SrcDat        +1

      // Send back an escape message based on an API error code DS
     DCL-PROC EC_Escape ;

     Dcl-PI *N;
        Whenx           char(60)    const;
        CallStackCnt    int(10)     value;
        ErrorCode       char(32766) options(*varsize);
     End-PI;

      // Send Program Message API
     Dcl-Pr QMHSNDPM    ExtPgm('QMHSNDPM');
        MessageID     Char(7)   Const;
        QualMsgF      Char(20)  Const;
        MsgData       Char(256) Const;
        MsgDtaLen     Int(10)   Const;
        MsgType       Char(10)  Const;
        CallStkEnt    Char(10)  Const;
        CallStkCnt    Int(10)   Const;
        MessageKey    Char(4);
        Errors        Char(1);
     End-Pr;

      // API error code (passed from caller)
     Dcl-s p_EC    pointer;

     Dcl-Ds dsEC    based(p_EC);
       dsECBytesP    int(10);
       dsECBytesA    int(10);
       dsECMsgID     Char(7);
       dsECReserv    Char(1);
       dsECMsgDta    Char(240);
     End-Ds;

      // API error code (no error handling requested)
     Dcl-Ds dsNullError;
       dsNullError0    Int(10) inz(0);
     end-ds;

     dcl-S MsgDtaLen    Int(10);
     dcl-S MsgKey       Char(4);


       p_EC = %addr(ErrorCode);
       if dsECBytesA <= 16;
         MsgDtaLen = 0;
       else;
         MsgDtaLen = dsECBytesA - 16;
       endif;

       // diagnostic msg tells us when the error occurred in our pgm
       QMHSNDPM( 'CPF9897'
               : 'QCPFMSG   *LIBL'
               :  Whenx
               : %Len(%trimr(whenx))
               : '*DIAG'
               : '*'
               : 1
               :  MsgKey
               : dsNullError
               );

       // send back actual error from API
       QMHSNDPM(dsECMsgID
               : 'QCPFMSG   *LIBL'
               : dsECMsgDta
               : MsgDtaLen
               : '*ESCAPE'
               : '*': CallStackCnt: MsgKey
               : dsNullError
               );

     End-Proc;
