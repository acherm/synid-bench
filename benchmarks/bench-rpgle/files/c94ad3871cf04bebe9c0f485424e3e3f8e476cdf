     H dftactgrp(*no) option(*nodebugio)                                         
     H debug decedit('0,') datedit(*DMY/)                                        
     HCOPYRIGHT('S.I.R.I. S.r.l. Soluzioni Informatiche per il Retail Italiano')  
     HAdapted from the FFDRPG program to display a file
      *************************************************************************
      *
      *  prrtvrowcol.rpgle
      *      
      *************************************************************************
      *************************************************************************
      *  Creates array of all DSPF-fields in a format
      *     Name, Row, Col, Length
      *************************************************************************
     D*
     D*  Stand Alone variables
     D*
     D AR              S              1    DIM(9999)
     D AKEY            S             10    DIM(9999)
     D AKS             S              2  0 DIM(9999)
     D J               S              2  0
     D JJ              S              2  0
     D I               S              7  0
     D S               S              7  0
     D RelRecNbr       S              4  0
     D RelRecHiS       S              4  0
     D XX              S              7  0
     D I1              S              1
     D I2              S              2
     D AScrn1          S              1     Inz('Y')
     D*
     D*  Data structures
     D GENDS           DS
     D  OffsetHdr            117    120B 0
     D  SizeHeader           121    124B 0
     D  OffsetList           125    128B 0
     D  NbrInList            133    136B 0
     D  SizeEntry            137    140B 0

     D HeaderDs        DS
     D  OutFileNam             1     10
     D  OutLibName            11     20
     D  OutType               21     25
     D  OutFormat             31     40
     D  RecordLen             41     44B 0
     D  HdrDum                45    512

     D InputDs         DS
     D  UserSpace              1     20
     D  SpaceName              1     10
     D  SpaceLib              11     20
     D  InpFileLib            29     48
     D  InpFFilNam            29     38
     D  InpFFilLib            39     48
     D  InpRcdFmt             49     58

     D ListDs          DS           544
     D  SfFld                  1     10
     D  SfType                11     11
     D  BufferOut             13     16B 0
     D  FieldLen              21     24B 0
     D  Digits                25     28B 0
     D  Decimals              29     32B 0
     D  FieldDesc             33     82
     D  FrmRow               449    452b 0
     D  FrmCol               453    456b 0

     D ErrorDs         DS                  INZ
     D  BytesPrv               1      4B 0
     D  BytesAvl               5      8B 0
     D  MessageId              9     15
     D  ERRNOO                16     16
     D  MessageDta            17    116

     D ReceiveVr2      S            100

     D ReceiveVar      DS          4096
     D  NbrOfFmts             62     63B 0
     D  DBFileOff            317    320B 0

     D FindSelDs       DS           150
     D  NbrOfKeys            117    118B 0
     D  KeyOffset            136    139B 0

     D KeyDataDs       DS
     D  DependKey              1     10
     D FileFmt         S              8
     D IsLog           S              1
     D FmtType         S             10
     D SFileLib        S             20
     D RFileLib        S             20
     D TestType        S              1
     D nF              S              3  0

     D Receiver        DS          4096    INZ
     D  NbrFormats            62     63B 0
     D  DBFileOffS           317    320B 0
     D  AccessType           337    338

     D                 DS
     D  StartPosit             1      4B 0
     D  StartLen               5      8B 0
     D  SpaceLen               9     12B 0
     D  ReceiveLen            13     16B 0
     D  MessageKey            17     20B 0
     D  MsgDtaLen             21     24B 0
     D  MsgQueNbr             25     28B 0
     D nBufLen         S             10I 0
     D szSrcMbr        S             10A
     ** Format to be returned
     D szFmt           S              8A   Inz('MBRD0100')
     ** Qualified source file and library name
     D szQualName      S             20A
     ** Whether or not to ignore overrides (0=Ignore, 1 = Apply)
     D bOvr            S              1A   Inz('0')
     **----------------------------------------------------------------
     ** The structure returned by the QusRMBRD API.
     **----------------------------------------------------------------
     D MbrdRtvLen      S             10I 0 inz( %size( Mbrd0100ds ))
     D MBRD0100ds      DS                                                       MBRL0100
     D   Md1Desc              85    134                                         descr
     D   Md3NbrDtaMbr        157    160I 0                                      Num Dat Mbr
     D   QUSRSV5             339    384                                         Reserved5
     D   Mb3BasOnAry         385   3969                                         Based on list
     D MbrdBasOnP      S               *   inz( %addr( Mb3BasOnAry ))
     D MbrdBasOnDs     DS                  based( MbrdBasOnP )                  Based on File List
     D   MdbFilNam             1     10                                         File Name
     D   MdbFilLib            11     20                                         File Lib
     D   MdbBasMbr            21     30                                         Member Name
     D   MdbFmt               31     40                                         Format Name
     D   MdbFmtNo             41     44I 0                                      Lgl File Rcd Frmt No
     D   MdbNbrRcd            45     48I 0                                      Cur Num Rcds
     D   MdbDltRcd            49     52I 0                                      Num Dlt Rcds
     D   MdbApSiz             53     56I 0                                      Acc Pth Sz
     D   MdbApSizM            57     60I 0                                      Acc Pth Sz Mlt
     D   MdbApShr             61     61                                         Acc Pth Shrd
     D   MdbApVld             62     62                                         Acc Pth Vld
     D   MdbApHld             63     63                                         Acc Pth Hld
     D   MdbApOwnF            64     73                                         Acc Pth Owner File
     D   MdbApOwnL            74     83                                         Acc Pth Owner Lib
     D   MdbApOwnM            84     93                                         Acc Pth Owner Mbr
     D   MdbApJrn             94     94                                         Acc Pth Jrn
     D                        95     96                                         Reserved1
     D   MdbNbrRcds           97    100U 0                                      Cur Num Rcds U
     D   MdbDltRcds          101    104U 0                                      Num Dlt Rcds U
     D                       105    112                                         Reserved2
     DGenSpcPtr                        *
     DLstSpcPtr                        *
     DHdrPtr                           *
     DFldsDs           ds
     D FrRiga                              DIM(999)
     D  FrName                       10    overlay(FrRiga:*NEXT)
     D  FrRow                         3  0 overlay(FrRiga:*NEXT)
     D  FrCol                         3  0 overlay(FrRiga:*NEXT)
     D  FrLen                         3  0 overlay(FrRiga:*NEXT)
     C*---------------------------------------------------------------
     C*  M A I N   L I N E
     C*---------------------------------------------------------------
     C*                                                                                     "
     C*  Entry parm(s) Display File Name
     C*                Format Name
     C*                Array that will contain the data (as defined above)
     C*
     C     *Entry        Plist
     C                   Parm                    FileNam          10
     C                   Parm                    FormNam          10
     C                   Parm                    FldsDs
     **
     c                   Clear                   FldsDs
     c                   eval      nF = 0
     C                   MOVE      '*LIBL     '  FileLib          20
     C                   MOVEl     FileNam       FileLib
     C                   movel     FormNam       EntryFmt         10
     C*
     C* set up variables
     C* Create a user space named FRMFLD in library QTEMP.
     C*
     C                   Movel(p)  'FRMFLD'      SpaceName
     C                   Movel(p)  'QTEMP'       SpaceLib
     C                   Movel     FileLib       InpFFilNam
     C                   Move      FileLib       InpFFilLib
     C                   Eval      BytesPrv = 116
     C                   Seton                                        53
      *
      * Create the user space
      *
     C                   Call      'QUSCRTUS'
     C                   Parm                    UserSpace
     C                   Parm      *BLANKS       SpaceAttr        10
     C                   Parm      4096          SpaceLen
     C                   Parm      *BLANKS       SpaceVal          1
     C                   Parm      '*CHANGE'     SpaceAuth        10
     C                   Parm      *BLANKS       SpaceText        50
     C                   Parm      '*YES'        SpaceRepl        10
     C                   Parm                    ErrorDs
      *
      * Attemp to retrieve object description
      *
     C                   Call      'QUSROBJD'
     C                   Parm                    ReceiveVr2
     C                   Parm      100           ReceiveLen
     C                   Parm      'OBJD0100'    FileFormat        8
     C                   Parm                    FileLib
     C                   Parm      '*FILE'       ObjectType       10
     C                   Parm                    ErrorDs
      *
      *  If file doesn't exist, send message and get out
      *
     C                   If        MessageId <> *BLANKS
     C                   Exsr      $ShutDown
     C                   ENDIF
      *  List fields to user space
     C                   CALL      'QUSLFLD'
     C                   PARM                    UserSpace
     C                   PARM      'FLDL0100'    ListFormat        8
     C                   PARM                    InpFileLIb
     C                   PARM      EntryFmt      InpRcdFmt
     C                   PARM      '1'           OverRide          1
     C                   Parm                    ErrorDs
     C                   If        MessageId <> *BLANKS
     C                   Exsr      $ShutDown
     C                   ENDIF
     C                   Eval      StartPosit = 1
     C                   Eval      StartLen = 140
     C                   CALL      'QUSRTVUS'
     C                   PARM                    UserSpace
     C                   PARM                    StartPosit
     C                   PARM                    StartLen
     C                   PARM                    GENDS
     C                   EVAL      StartPosit = OffsetHdr + 1
     C                   EVAL      StartLen = SizeHeader
     C                   CALL      'QUSRTVUS'
     C                   PARM                    UserSpace
     C                   PARM                    StartPosit
     C                   PARM                    StartLen
     C                   PARM                    HeaderDs
     C                   EVAL      StartPosit = OffsetList + 1
     C                   EVAL      StartLen = SizeEntry
      *  Do for number of fields
B1   C                   DO        NbrInList
     C                   CALL      'QUSRTVUS'
     C                   PARM                    UserSpace
     C                   PARM                    StartPosit
     C                   PARM                    StartLen
     C                   PARM                    ListDs
      *  Write the record to the atrray
     c                   eval      nF = nF + 1
     C                   eval      FrName(nf) = SfFld
     C                   eval      FrRow(nf)  = FrmRow
     C                   eval      FrCol(nf)  = FrmCol
     C                   eval      FrLen(nf)  = FieldLen
     C                   EVAL      StartPosit = StartPosit + SizeEntry
E1   C                   ENDDO
     c                   exsr      $shutdown
     C*------------------------------------------------------------------
     C*  $ShutDown - Kill the program
     C*------------------------------------------------------------------
     C     $ShutDown     Begsr
     C                   Eval      *INLR = *On
     C                   Return
     C                   Endsr