*SRCMBRTXT:BC5619 Req. Adic. Inf. Lineas de Créd. 
     H DFTACTGRP(*NO)  ACTGRP('QILE')
     H DATEDIT(*YMD)
     H*****************************************************************
     H*                                                               *
     H*  SYSTEM NAME: SIDEBA                                          *
     H*                                                               *
     H*  PROGRAM NAME: Gen. de Arch. INVPROD14AUT.TXT                 *
     H*                                                               *
     H*  PROGRAM NO: BCAU00RG                                         *
     H*                                                               *
     H*  DATE:    05.12.2014                                          *
     H*                                                               *
     H*  AUTHOR: SO                                                   *
     H*                                                               *
     H*****************************************************************
     FBC43AU    IF   E           K DISK
     FSGSYSV    IF   E             DISK
     D*---------------------------------------------------------------------
     D* Prototipos para las llamadas a la API
     D*---------------------------------------------------------------------
     D*------------------
     D opendir         PR              *   EXTPROC('opendir')
     D   dirname                       *   VALUE options(*string)
     D*------------------
     D closedir        PR            10I 0 EXTPROC('closedir')
     D   dirhandle                     *   VALUE
     D*------------------
     D readdir         PR              *   EXTPROC('readdir')
     D   dirhandle                     *   VALUE
     D*------------------
     D rename          PR            10I 0 EXTPROC('Qp0lRenameUnlink')
     D   old                           *   VALUE options(*string)
     D   new                           *   VALUE options(*string)

     D open            PR            10I 0 ExtProc('open')
     D  filename                       *   value options(*string)
     D  openflags                    10I 0 value
     D  mode                         10U 0 value options(*nopass)
     D  codepage                     10U 0 value options(*nopass)

     D fseek           PR            10I 0 ExtProc('fseek')
     D  filehandler                  10I 0 value
     D  fileoffset                   10I 0 value
     D  start_pos                    10I 0 value

     D unlink          PR            10I 0 ExtProc('unlink')
     D   path                          *   Value options(*string)

     D write           PR            10I 0 ExtProc('write')
     D  handle                       10I 0 value
     D  buffer                         *   value
     D  bytes                        10U 0 value

     D Close           PR            10I 0 ExtProc('close')
     D   Sock_Desc                   10I 0 Value
     D*---------------------------------------------------------------------
     D* Estructuras de Datos que devuelven las API
     D*---------------------------------------------------------------------
      *********************************************************
      * Definitions needed to make IFS API calls.  Note that
      * these should really be in a separate /copy file]
      *********************************************************
     D O_WRONLY        C                   2
     D SEEK_SET        C                   0
     D O_RDWR          C                   4
     D O_CREAT         C                   8
     D O_TRUNC         C                   64
     D O_TEXTDATA      C                   16777216
     D O_CODEPAGE      C                   8388608

     D*** file permissions
     D S_IRUSR         S             10I 0 INZ(256)
     D S_IWUSR         S             10I 0 INZ(128)
     D S_IXUSR         S             10I 0 INZ(64)
     D S_IRWXU         S             10I 0 INZ(448)
     D S_IRGRP         S             10I 0 INZ(32)
     D S_IWGRP         S             10I 0 INZ(16)
     D S_IXGRP         S             10I 0 INZ(8)
     D S_IRWXG         S             10I 0 INZ(56)
     D S_IROTH         S             10I 0 INZ(4)
     D S_IWOTH         S             10I 0 INZ(2)
     D S_IXOTH         S             10I 0 INZ(1)
     D S_IRWXO         S             10I 0 INZ(7)
     D AsciiCodePage   S             10U 0 INZ(850)
     D*----------------------------------------------------------------*
     D               ESDS                  EXTNAME(@PSDS)
     I*----------------------------------------------------------------*
     D*---------------------------------------------------------------------
     D* Variables y Estructuras de Datos del Programa
     D*---------------------------------------------------------------------
     D txtFile         S            255
     D FILHND          S             10I 0
     d buf             s           4096
     D buflen          S             10I 0
     D*---------------------------------------------------------------------
     c                   ExSr      OpenStmF
     C                   Read      REBC43AU                               99
     C                   DoW       *IN99 = *OFF
     c*
     C                   Eval      buf=*blanks
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1ITII:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1INUI:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1INCR:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(       A1IABM     )+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1NSEC:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(       A1FAU1     )+';'
     C                   Eval      buf=%trim(buf)+%trim(       A1FAU2     )+';'
     C                   Eval      buf=%trim(buf)+%trim(       A1FAU3     )+';'
     C                   Eval      buf=%trim(buf)+%trim(       A1IF58     )+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1PLDI:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1IPAA:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$$SC:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$IMP:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$OCA:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1TNA$:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1TNAU:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(       A1BLK1     )+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$BUA:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1IDVA:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1IPTD:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1DIA1:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1PAFC:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$MCA:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1DIA2:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1QDSV:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1QCAN:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1EGES:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$NAD:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$NAH:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$PAN:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1GMCA:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1PAFD:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$MIP:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1DIA3:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$MMR:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1IADD:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1VFLD:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1QCA2:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1IAEX:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1VF06:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$MPC:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(       A1BLK0     )+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$GAR:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$GS1:'Z'))+';'
     C                   Eval      buf=%trim(buf)+%trim(%EditC(A1$GS2:'Z'))+';'
     C                   Eval      buf=%trim(buf)+x'0d'+x'25'+x'00'
     c*
     c                   Eval      buflen = %len(%trim(buf))-1
     c                   CALLP     write(FilHnd: %addr(buf): buflen)
     C*
     C                   Read      REBC43AU                               99
     C                   EndDo
     c                   ExSr      CloseStmF
     C                   ExSr      EndPgm
     C*-------------------------------------------------------------------------
     C     EndPgm        BegSr
     C*
     C                   SetOn                                        LR
     C                   Return
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     OpenStmF      BegSr
     C*
     c                   Eval      txtFile=%TRIM(OUTPAT)+'INVPROD14AUT.TXT'
     c                   EVAL      FilHnd=open(%trim(txtfile):
     c                                  O_CREAT + O_WRONLY + O_TRUNC +
     c                                  O_CODEPAGE :
     c                                  S_IWUSR+S_IRUSR+S_IRGRP+S_IROTH:
     c                                  1252    )
     c                   callp     close(FilHnd)
     c                   EVAL      FilHnd=open(%trim(txtfile):
     c                                   O_WRONLY+O_TEXTDATA)
     c*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     CloseStmF     BegSr
     C*
     c                   callp     close(FilHnd)
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     *INZSR        BegSr
     C*
     C     *ENTRY        PLIST
     C                   PARM                    OUTPAT           50
     C*
     C     1             CHAIN     SGSYSV                             80
     C*
     C                   EndSr
     C*=====================================================================
