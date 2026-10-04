     H DFTACTGRP(*NO) OPTION(*SRCSTMT: *NODEBUGIO)

     **  This program will find all places that a bound module is called.
     **    (by searching all ILE programs in the user libraries)
     **
     **         Scott Klement,  May 7, 1997
     **

     fQSYSPRT   O    F   80        PRINTER OFLIND(*INOF)
      *
      *  Field Definitions.
      *
     d searchlibrary   s             10
     d ObjectLibrary   s             20

     d EC_Escape       PR
     d   When                        60A   const
     d   CallStackCnt                10I 0 value
     d   ErrorCode                32766A   options(*varsize)

      * List ILE program information API
     d QBNLPGMI        PR                  ExtPgm('QBNLPGMI')
     d   UsrSpc                      20A   const
     d   Format                       8A   const
     d   PgmName                     20A   const
     d   Errors                   32766A   options(*varsize)

      * List ILE service program information API
     d QBNLSPGM        PR                  ExtPgm('QBNLSPGM')
     d   UsrSpc                      20A   const
     d   Format                       8A   const
     d   SrvPgm                      20A   const
     d   Errors                   32766A   options(*varsize)

      * Create User Space API
     d QUSCRTUS        PR                  ExtPgm('QUSCRTUS')
     d   UsrSpc                      20A   const
     d   ExtAttr                     10A   const
     d   InitSize                    10I 0 const
     d   InitVal                      1A   const
     d   PublicAuth                  10A   const
     d   Text                        50A   const
     d   Replace                     10A   const
     d   Errors                   32766A   options(*varsize)

      * Retrieve pointer to user space API
     d QUSPTRUS        PR                  ExtPgm('QUSPTRUS')
     d   UsrSpc                      20A   const
     d   Pointer                       *

      * API error code structure
     d dsEC            DS
     d  dsECBytesP                   10I 0 inz(%size(dsEC))
     d  dsECBytesA                   10I 0 inz(0)
     d  dsECMsgID                     7A
     d  dsECReserv                    1A
     d  dsECMsgDta                  240A

      *  List API generic header structure
     d p_Header        S               *
     d dsLH            DS                   BASED(p_Header)
      *                                     Filler
     d   dsLHFill1                  103A
      *                                     Status (I=Incomplete,C=Complete
     d   dsLHStatus                   1A
     d   dsLHFill2                   12A
     d   dsLHHdrOff                  10I 0
     d   dsLHHdrSiz                  10I 0
     d   dsLHLstOff                  10I 0
     d   dsLHLstSiz                  10I 0
     d   dsLHEntCnt                  10I 0
     d   dsLHEntSiz                  10I 0
      *
      * PGML0100 format: modules in program
      * SPGL0100 format: modules in service program
      * (these fields are the same in both APIs)
     d p_Entry         S               *
     d dsPgm           DS                  based(p_Entry)
     d   dsPgm_Pgm                   10A
     d   dsPgm_PgmLib                10A
     d   dsPgm_Module                10A
     d   dsPgm_ModLib                10A
     d   dsPgm_SrcF                  10A
     d   dsPgm_SrcLib                10A
     d   dsPgm_SrcMbr                10A
     d   dsPgm_Attrib                10A
     d   dsPgm_CrtDat                13A
     d   dsPgm_SrcDat                13A

     d peModule        S             10A
     d Entry           S             10I 0

     c     *entry        plist
     c                   parm                    peModule
     c                   parm                    SearchLibrary


     c                   except    PrtHeader
      * Create a user space to stuff module info into
     c                   callp     QUSCRTUS('MODULES   QTEMP': 'USRSPC':
     c                                5120*3072: x'00': '*ALL':
     c                                'List of modules': '*YES': dsEC)
     c                   if        dsECBytesA > 0
     c                   callp     EC_Escape('Calling QUSCRTUS API':3:dsEC)
     c                   endif
     c                   callp     QUSPTRUS('MODULES   QTEMP': p_Header)
     c                   eval      objectLibrary = '*ALL      ' +
     c                                             searchlibrary
      * List all ILE programs modules to space
     c                   callp     QBNLPGMI('MODULES   QTEMP': 'PGML0100':
     c                                objectLibrary : dsEC)
     c                   if        dsECBytesA > 0
     c                   callp     EC_Escape('Calling QBNLPGMI API':3:dsEC)
     c                   endif
      * List occurrances of our module
     c                   eval      p_Entry = p_Header + dsLHLstOff

     c                   for       Entry = 1 to dsLHEntCnt
     c                   if        dsPgm_Module = peModule
     c                   except    PrtModule
     c                   endif
     c                   eval      p_Entry = p_Entry + dsLHEntSiz

     c                   endfor
      * List all ILE service program modules to space
     c                   callp     QBNLSPGM('MODULES   QTEMP': 'SPGL0100':
     c                                '*ALL      *ALLUSR': dsEC)
     c                   if        dsECBytesA > 0
     c                   callp     EC_Escape('Calling QBNLSPGM API':3:dsEC)
     c                   endif
      * List occurrances of our module
     c                   eval      p_Entry = p_Header + dsLHLstOff

     c                   for       Entry = 1 to dsLHEntCnt
     c                   if        dsPgm_Module = peModule
     c                   except    PrtModule
     c                   endif
     c                   eval      p_Entry = p_Entry + dsLHEntSiz
     c                   endfor
      * And that's about the size of it
     c                   eval      *inlr = *on


     OQSYSPRT   E            PrtHeader         2  3
     o                       *DATE         Y     10
     o                                           +3 'Listing of programs'
     o                                           +1 'that use module'
     o                       peModule            +1
     o                                           75 'Page'
     o                       PAGE          Z     80

     o          E            PrtModule         2  3
     o                       dsPgm_Pgm           10
     o                       dsPgm_PgmLib        +1
     o                       dsPgm_SrcF          +1
     o                       dsPgm_SrcLib        +1
     o                       dsPgm_SrcMbr        +1
     o                       dsPgm_SrcDat        +1

      * Send back an escape message based on an API error code DS
     P EC_Escape       B
     d EC_Escape       PI
     d   When                        60A   const
     d   CallStackCnt                10I 0 value
     d   ErrorCode                32766A   options(*varsize)

      * Send Program Message API
     d QMHSNDPM        PR                  ExtPgm('QMHSNDPM')
     d   MessageID                    7A   Const
     d   QualMsgF                    20A   Const
     d   MsgData                    256A   Const
     d   MsgDtaLen                   10I 0 Const
     d   MsgType                     10A   Const
     d   CallStkEnt                  10A   Const
     d   CallStkCnt                  10I 0 Const
     d   MessageKey                   4A
     d   Errors                       1A

      * API error code (passed from caller)
     d p_EC            S               *
     d dsEC            DS                  based(p_EC)
     d  dsECBytesP                   10I 0
     d  dsECBytesA                   10I 0
     d  dsECMsgID                     7A
     d  dsECReserv                    1A
     d  dsECMsgDta                  240A

      * API error code (no error handling requested)
     d dsNullError     DS
     d  dsNullError0                 10I 0 inz(0)

     d MsgDtaLen       S             10I 0
     d MsgKey          S              4A

     c                   eval      p_EC = %addr(ErrorCode)
     c                   if        dsECBytesA <= 16
     c                   eval      MsgDtaLen = 0
     c                   else
     c                   eval      MsgDtaLen = dsECBytesA - 16
     c                   endif
      * diagnostic msg tells us when the error occurred in our pgm
     c                   callp     QMHSNDPM('CPF9897': 'QCPFMSG   *LIBL':
     c                               When: %Len(%trimr(when)): '*DIAG':
     c                               '*': 1:  MsgKey: dsNullError)
      * send back actual error from API
     c                   callp     QMHSNDPM(dsECMsgID: 'QCPFMSG   *LIBL':
     c                               dsECMsgDta: MsgDtaLen: '*ESCAPE':
     c                               '*': CallStackCnt: MsgKey:
     c                               dsNullError)
     P                 E