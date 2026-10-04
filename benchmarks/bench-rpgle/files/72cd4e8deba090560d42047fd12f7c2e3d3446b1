*SRCMBRTXT:Switch-Adapter      -Trans CBU Proceso 
     H DFTACTGRP(*NO) ACTGRP(*NEW) BNDDIR('QC2LE')
     F*
     FSPTRTR05  UF   E           K DISK
     FSGSYSV    IF   E             DISK
     F*
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
     D*--------------------------------------------------------------------
     D* Read From a File
     D*
     D* ssize_t read(int handle, void *buffer, size_t bytes);
     D*--------------------------------------------------------------------
     D read            PR            10I 0 ExtProc('read')
     D  handle                       10i 0 value
     D  buffer                         *   value
     D  bytes                        10U 0 value
     D*---------------------------------------------------------------------
     D* Estructuras de Datos que devuelven las API
     D*---------------------------------------------------------------------
     D/copy LE00525/SOCKETSRPG,errno_h
     D*---------------------------------------------------------------------
     D p_dirent        s               *
     D dirent          DS                  BASED(p_dirent)
     D  d_reserved1                  16A
     D  d_fileno_gid                 10U 0
     D  d_fileno                     10U 0
     D  d_reclen                     10U 0
     D  d_reserved3                  10I 0
     D  d_reserved4                   8A
     D  d_nlsinfo                    12A
     D    nls_ccsid                  10I 0 OVERLAY(d_nlsinfo:1)
     D    nls_entry                   2A   OVERLAY(d_nlsinfo:5)
     D    nls_lang                    3A   OVERLAY(d_nlsinfo:7)
     D    nls_reserv                  3A   OVERLAY(d_nlsinfo:10)
     D  d_namelen                    10U 0
     D  d_name                      640A
      *********************************************************
      * Definitions needed to make IFS API calls.  Note that
      * these should really be in a separate /copy file]
      *********************************************************
     D SEEK_SET        C                   0
     D O_RDONLY        C                   1
     D O_WRONLY        C                   2
     D O_RDWR          C                   4
     D O_CREAT         C                   8
     D O_EXCL          C                   16
     D O_TRUNC         C                   64
     D O_APPEND        C                   256
     D O_CODEPAGE      C                   8388608
     D O_TEXTDATA      C                   16777216

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
     D*----------------------------------------------------------------*
     D LDA           E DS                  EXTNAME(LDA)
     I*----------------------------------------------------------------*
     D*---------------------------------------------------------------------
     D* Variables y Estructuras de Datos del Programa
     D*---------------------------------------------------------------------
     D filename        S            255A
     D error           S              1A
     D FilDes          S             10I 0
     D lasterror       S            255A
     D rc              S             10I 0
     Dbufferds         ds
     D  buffer                 1    244A
     D   header                1    244A
     D    heatar               1     25A
     D    heafec              26     31A
     D   detail                1    244A
     D    detfiid              1      4A
     D    detpan               5     23A
     D    detmem              24     26A
     d    defite              27     30A
     D    dettid              31     36A
     D    dettty              37     38A
     d    desqno              39     44A
     d    demstp              45     48A
     d    depoda              49     54A
     d    detrda              55     60A
     d    detrti              61     66A
     d    detrcd              67     72A
     d    deticu              69     70A
     d    deimon              73     75A
     d    defrac              76     94A
     d    dencbu              95    116A
     d    deimpo             117    126A
     d    detica             127    136A
     d    dereco             137    139A
     d    demoti             140    142A
     d    derefe             143    154A
     d    detcde             155    156A
     d    deprop             157    157A
     d    denomb             158    179A
     d    decuit             180    190A
     d    defill             191    244A
     C*---------------------------------------------------------------------
     c                   exsr      opnfil
     c                   exsr      redhed
     c                   exsr      redlin
     c                   dow       *in99 = *off
     c                   exsr      prctrn
     c                   exsr      redlin
     c                   enddo
     c                   exsr      clofil
     c                   exsr      noinfo
     c                   exsr      endpgm
     C*---------------------------------------------------------------------
     c     prctrn        begsr
     c*
     c                   exsr      buildKeys
     c     ksptrtr       chain     resptrtr                           99
     c     *in99         doweq     *off
     c                   if        (trdtxt = 'TRANS.LINK.ATM      '     or
     c                              trdtxt = 'TRANS.LINK.HBA      '     or
     c                              trdtxt = 'TRANS.LINK.CEL      '   ) and
     c                              TR$IMP= ww$imp                      and
     c                              TRNCPA=dencbu                       and
     c                              TRCOTR= *BLANKS                     and
     c                              TRICCC= wwICCC
     c*
     c                   move      decuit        TRICUI
     c                   move      '00'          TRITPR
     c                   update    resptrtr
     c                   if        deprop='S'
     c                   exsr      contrimpu
     c                   endif
     c*
     c                   leave
     c                   endif
     c     ksptrtr       reade     resptrtr                               99
     c                   enddo
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     noinfo        begsr
     c*
     c                   eval      wwisub='CC'
     C                   exsr      updnoinf
     c                   eval      wwisub='AC'
     C                   exsr      updnoinf
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     updnoinf      begsr
     c*
     c     ksptrtr02     chain     resptrtr                           99
     c     *in99         doweq     *off
     c                   if        (trdtxt = 'TRANS.LINK.ATM      '     or
     c                              trdtxt = 'TRANS.LINK.HBA      '     or
     c                              trdtxt = 'TRANS.LINK.CEL      '   ) and
     c                             (trcotr = *BLANKS)                   and
     c                             (tritpr <> '00'  )
     c                   select
     c                   when      TRITPR = '02'
     c                   move      '01'          TRITPR
     c                   z-add     AAFS24        TRFALT
     c                   z-add     AAFS24        TRFECO
     c                   z-add     AAFS24        TRFPRE
     c                   update    resptrtr
     c                   when      TRITPR = '01'
     c                   move      '00'          TRITPR
     c                   update    resptrtr
     c                   endsl
     c                   endif
     c     ksptrtr02     reade     resptrtr                               99
     c                   enddo
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     contrimpu     begsr
     c                   endsr
     C*---------------------------------------------------------------------
     c     buildKeys     begsr
     c*
     c                   move      *blanks       auedsu            4
     c                   move      *blanks       auiccc            9
     c                   move      *blanks       aufeco            8
     c                   move      *blanks       kk                8
     c                   eval      auedsu=%SUBST(dencbu:4:4)
     c                   eval      auiccc=%SUBST(defrac:5:2)+
     c                                    %SUBST(defrac:10:7)
     c                   move      auedsu        wwedsu
     c                   move      auiccc        wwiccc
     c*
     c                   eval      aufeco='20'+detrda
     c                   move      aufeco        wwfeco
     c*
     c                   move      deimpo        ww$imp           10 2
     c*
     c                   eval      wwisub='CC'
     c                   if        deticu='11' or deticu='15'
     c                   eval      wwisub='AC'
     c                   endif
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     redhed        begsr
     c*
     c                   exsr      redlin
     c     *in99         ifeq      *on
     c                   eval      lasterror='Arc. de formato incorrecto'
     c                   exsr      EndPgm
     c                   endif
     c                   if        heatar <> 'TRANSFERENCIA MINORISTA'
     c                   eval      lasterror='Arc. de formato incorrecto'
     c                   exsr      EndPgm
     C                   endif
     c*
     C                   MOVE      heafec        AUFECH            8
     C                   MOVEL     '20'          AUFECH
     C                   MOVE      AUFECH        WWFECH
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     opnfil        begsr
     c*
     C                   EVAL      filename=%trim(filename)+X'00'
     C                   EVAL      FilDes = open(%ADDR(filename) :
     C                             O_RDONLY              + O_TEXTDATA
     C                                                         )
     C     FilDes        COMP      *ZERO                                25
     c   25              eval      lasterror=%str(strerror(errno))
     C   25              EXSR      EndPgm
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     clofil        begsr
     c*
     C                   CALLP     close(FilDes)
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     redlin        begsr
     c*
     c                   eval      lasterror=*blanks
     C                   eval      rc=read(FilDes:%ADDR(buffer):244)
     c     rc            comp      244                                  99
     c   99              eval      lasterror=%str(strerror(errno))
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     endpgm        begsr
     c*
     c                   seton                                        lr
     c                   return
     c*
     c                   endsr
     C*---------------------------------------------------------------------
     c     *inzsr        begsr
     c*
     c     *entry        plist
     c                   parm                    filename
     c                   parm                    lasterror
     c*
     c     *like         define    trisub        wwisub
     c     *like         define    trfeco        wwfeco
     c     *like         define    trfeco        wwfech
     c     *like         define    tremsu        wwedsu
     c     *like         define    triccc        wwiccc
     c*
     c     ksptrtr       klist
     c                   kfld                    wwISUB
     c                   kfld                    AASFEI
     c                   kfld                    wwEDSU
     c                   kfld                    wwICCC
     c*
     c     ksptrtr02     klist
     c                   kfld                    wwISUB
     c                   kfld                    aasfei
     c*
     C     1             CHAIN     SGSYSV
     c*
     c                   endsr
     C*---------------------------------------------------------------------
      /define ERRNO_LOAD_PROCEDURE
      /copy SOCKETSRPG,errno_h
