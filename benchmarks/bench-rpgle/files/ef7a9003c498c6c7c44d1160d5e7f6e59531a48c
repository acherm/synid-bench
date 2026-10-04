*SRCMBRTXT:Aut.Federal-Manejador de Envío de Archi
     H DEBUG
     H DECEDIT(',') DATEDIT(*YMD/)
     H DFTACTGRP(*NO)  ACTGRP('QILE')
     H BNDDIR('LE00525/TO10BD   ')
     H*****************************************************************
     H*                                                               *
     H*  SYSTEM NAME: SIDEBA -                                        *
     H*                                                               *
     H*  PROGRAM NAME: Gen. de Arch. Txt para Federal                 *
     H*                                                               *
     H*                                                               *
     H*  PROGRAM NO: PRFD01MA                                         *
     H*                                                               *
     H*  DATE:    07/06/2012                                          *
     H*                                                               *
     H*  AUTHOR: SO                                                   *
     H*                                                               *
     H*****************************************************************
     FPRAFED01  UF   E           K DISK
     FPRCRED    IF   E           K DISK
     FBASUPE01  IF   E           K DISK
     F@CPISYS   IF A E           K DISK
     F@CPIUSD   IF A E           K DISK
     FSGSYSV    IF   E             DISK
     D*----------------------------------------------------------------*
     D                 DS
     D  @ZFNKY                 1     24
     D  @FN                    1     24
     D                                     DIM(24)
     D*----------------------------------------------------------------*
     D               ESDS                  EXTNAME(@PSDS)
     D*----------------------------------------------------------------*
     D LDA           E DS                  EXTNAME(LDA)
     D*----------------------------------------------------------------*
     DERRDS            DS
     D ERRTXT                  1    385
     D WWNCU1                  1     55
     D WWNCU2                 56    110
     D WWNCU3                111    165
     D WWNCU4                166    220
     D WWNCB1                221    275
     D WWNCB2                276    330
     D WWNCB3                331    385
     D WWNCB4                386    440
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
     I*----------------------------------------------------------------*
     D OUTPAT          S            255
     D txtFile         S            255
     D FILHND          S             10I 0
     d FechaN          s              8  0
     d FechaC          s              8
     D*
     d buf             s            222
     D*
     d rc              s              3  0
     D*
     d chrCode         s              9B 0
     I*----------------------------------------------------------------*
     c                   Eval      OutPat='/home/Cesion_de_haberes/Federal/'+
     c                                     'Enviados/'
     c                   ExSr      ChkYaProc
     c                   ExSr      CheckBajas
     c                   ExSr      OpenStmF
     c                   ExSr      GenFile
     c                   ExSr      CloseStmF
     c                   ExSr      SndMail
     c                   ExSr      DspOkMsg
     c                   ExSr      EndPgm
     c*---------------------------------------------------------------------
     c* SndMail: Enviar por Mail
     c*---------------------------------------------------------------------
     c     SndMail       BegSr
     c*
     c                   Move      *Blanks       CmdLine        4096
     c                   Eval      CmdLine='SNDMAIL ' +
     c                             ' RECP(PRHA03C1)                          '+
     c                             ' SUBJECT(''Archivo a Enviar a Federal'') '+
     c                             ' FILE('''+%trim(txtFile)+''')'
     c*
     c                   Call      'QCMDEXC'
     c                   Parm                    CmdLine
     c                   Parm      4096          CmdLen           15 5
     c*
     c                   EndSr
     c*---------------------------------------------------------------------
     c* CheckBajas: Cheque las Bajas del Día e inserta en Prafed antes de gen
     c*---------------------------------------------------------------------
     c     CheckBajas    BegSr
     C*
     c                   Call      'PRFD05MA'
     C*
     C                   EndSr
     c*---------------------------------------------------------------------
     c* GenFile: Graba Líneas de Archivo
     c*---------------------------------------------------------------------
     c     GenFile       BegSr
     C*
     C     KFD010        Chain     REPRAFED                           25
     C                   DoW       *IN25 = *Off
     C* ... Controlar si el credito aún existe (No Fue dado de Baja p/PRJV05MM)
     C     KJV010        Chain     REPRCRED                           99
     C                   If        *In99 = *Off
     C* ... Controlar si tiene supervision y esta es positiva
     c                   ExSr      CheckSupe
     c                   If        FlagSupePos=*ON
     c                   ExSr      BuildReg
     C                   ExSr      WrtLin
     c                   Else
     c* ... Marcar que no se envío por supervisión negativa
     c                   Move      'S'           AFESTA
     c                   EndIf
     C                   EndIF
     c                   ExSr      MarcarReg
     C     KFD010        ReadE     REPRAFED                               25
     C                   EndDo
     C*
     C                   EndSr
     c*---------------------------------------------------------------------
     c* CheckSupe: Ver si el credito tiene supervision y si es positiva
     c*---------------------------------------------------------------------
     c     CheckSupe     BegSr
     c*
     c                   Move      *On           FlagSupePos       1
     c*
     C     KSA010        Chain     REBASUPE                           99
     C                   If        *In99 = *OFF and SAHSUP = 0
     c                   Move      *Off          FlagSupePos
     c                   EndIf
     c*
     c                   EndSr
     c*---------------------------------------------------------------------
     c* BuildReg: Armar linea de registro en la variable buf
     c*---------------------------------------------------------------------
     c     BuildReg      BegSr
     C*
     c                   Eval      Buf=*all' '
     c                   Z-Add     AFISEQ        wwisec            6 0
     c                   Eval      %subst(buf:001:006)=%trim(
     C                                           %EditW(wwisec:'0      '))
     c                   Eval      %subst(buf:007:003)='NBR'
     c                   Eval      %subst(buf:010:001)=AFIOPT
     c                   Eval      %subst(buf:011:003)=%trim(
     C                                           %EditW(AFIMDS:'0   '))
     c                   Eval      %subst(buf:014:001)=AFISEX
     c                   Z-Add     AFINDO        WWINDO            8 0
     c                   Eval      %subst(buf:015:008)=%trim(
     C                                           %EditW(WWINDO:'0        '))
     c                   Eval      %subst(buf:023:030)=AFNYAP
     C                   ExSr      BuildIRED
     c                   Eval      %subst(buf:053:002)=WWIRED
     c                   Eval      %subst(buf:055:005)=%subst(AFIBCF:1:5)
     C* ... Es una renov Nro Op. debe contener LA OP VIEJA
     c                   Z-add     AFISUC        wwisuc            2 0
     c                   Z-add     AFINCR        wwincr           10 0
     c                   Z-add     AFIDEG        wwideg            2 0
     c                   Eval      %subst(buf:060:014)=%trim(
     C                                           %EditW(wwisuc:'0  '))+
     c                                                 %trim(
     c                                   %EditW(wwincr:'0          '))+
     c                                                 %trim(
     C                                           %EditW(wwideg:'0  '))
     c* ... Quieren el campo en blanoo no ceros si es cero
     c                   If        AFINCV <> 0
     c                   Z-add     AFEDSU        wwisuc            2 0
     c                   Z-add     AFINCV        wwincr           10 0
     c                   Z-add     AFIDEV        wwideg            2 0
     c                   Eval      %subst(buf:074:014)=%trim(
     C                                           %EditW(wwisuc:'0  '))+
     c                                                 %trim(
     c                                   %EditW(wwincr:'0          '))+
     c                                                 %trim(
     C                                           %EditW(wwideg:'0  '))
     c                   EndIf
     c*
     c                   z-add     AFFECH        WWFECH            8 0
     C                   ExSr      InvFecha
     c                   Eval      %subst(buf:088:010)=%trim(
     C                                       %EditW(WWFECH:'0  /  /    '))
     c                   Z-Add     AF$IMP        WW$IMP            8 2
     c                   Eval      %subst(buf:098:009)=%trim(
     C                                       %EditW(WW$IMP:'0      .  '))
     c                   Eval      %subst(buf:107:003)=%trim(
     C                                       %EditW(AFQCUO:'0   '))
     c                   Z-Add     AF$CUO        WW$CUO            8 2
     c                   Eval      %subst(buf:110:009)=%trim(
     C                                       %EditW(WW$CUO:'0      .  '))
     c                   If        AFIOPT='A'
     C* ... Si el registro es de Alta mandar los siguientes campos para que lo
     C*     rellenen ellos
     C*
     c                   Eval      %subst(buf:119:006)='000000'
     c                   Eval      %subst(buf:125:009)='000000000'
     c                   Eval      %subst(buf:134:016)='  /  /     00:00'
     C*
     c                   Else
     c*                  ... Nro de Proceso
     c                   Move      AFIPRC        WWIPRC            6 0
     c                   Eval      %subst(buf:119:006)=
     c                             %trim(%editw(WWIPRC:'0      '))
     c*                  ... Nro de Autorización
     c                   Z-Add     AFINCE        WWINCE            9 0
     c                   Eval      %subst(buf:125:009)=
     c                             %trim(%editw(WWINCE:'0         '))
     c*                  ... Fecha y Hora de Autorización
     c*                  Eval      %subst(buf:134:016)='12/34/5678 00:00'
     c                   Move      AFFAU1        wwfau1            8
     c                   Move      AFHAU1        wwhau1            6
     c                   Eval      %subst(buf:134:010)=
     c                             %subst(wwfau1:7:2)+ '/' +
     c                             %subst(wwfau1:5:2)+ '/' +
     c                             %subst(wwfau1:1:4)
     c                   Eval      %subst(buf:145:005)=
     c                             %subst(wwhau1:1:2)+ ':' +
     c                             %subst(wwhau1:3:2)
     C                   Endif
     c*
     c                   Eval      %subst(buf:150:003)='   '
     c                   Eval      %subst(buf:153:010)='  /  /    '
     c                   Eval      %subst(buf:163:009)='000000.00'
     c                   Eval      %subst(buf:172:050)=*BLANKS
     c                   Eval      %subst(buf:222:001)=X'25'
     c*
     C                   EndSr
     c*---------------------------------------------------------------------
     c* InvFecha: Invierte Fecha
     c*---------------------------------------------------------------------
     c     InvFecha      BegSr
     C*
     c                   Call      'SBBAINFE'
     C                   Parm                    WWFECH
     C                   Parm      'IN'          Mode              2
     C*
     C                   EndSr
     c*---------------------------------------------------------------------
     c* BuildIRED: Arma el Nro de trabajo en Formato Gobierno
     c*---------------------------------------------------------------------
     c     BuildIRED     BegSr
     C*
     c                   Move      '01'          wwired            2
     C                   Move      AFIRED        wwired
     C                   SELECT
     C     WWIRED        WHENEQ    '0A'
     C                   MOVE      '10'          WWIRED
     C     WWIRED        WHENEQ    '0B'
     C                   MOVE      '11'          WWIRED
     C     WWIRED        WHENEQ    '0C'
     C                   MOVE      '12'          WWIRED
     C     WWIRED        WHENEQ    '0D'
     C                   MOVE      '13'          WWIRED
     C     WWIRED        WHENEQ    '0E'
     C                   MOVE      '14'          WWIRED
     C     WWIRED        WHENEQ    '0F'
     C                   MOVE      '15'          WWIRED
     C     WWIRED        WHENEQ    '0G'
     C                   MOVE      '16'          WWIRED
     C     WWIRED        WHENEQ    '0H'
     C                   MOVE      '17'          WWIRED
     C     WWIRED        WHENEQ    '0I'
     C                   MOVE      '18'          WWIRED
     C     WWIRED        WHENEQ    '0J'
     C                   MOVE      '19'          WWIRED
     C     WWIRED        WHENEQ    '0K'
     C                   MOVE      '20'          WWIRED
     C     WWIRED        WHENEQ    '0L'
     C                   MOVE      '21'          WWIRED
     C     WWIRED        WHENEQ    '0M'
     C                   MOVE      '22'          WWIRED
     C     WWIRED        WHENEQ    '0N'
     C                   MOVE      '23'          WWIRED
     C     WWIRED        WHENEQ    '0O'
     C                   MOVE      '24'          WWIRED
     C     WWIRED        WHENEQ    '0P'
     C                   MOVE      '25'          WWIRED
     C     WWIRED        WHENEQ    '0Q'
     C                   MOVE      '26'          WWIRED
     C     WWIRED        WHENEQ    '0R'
     C                   MOVE      '27'          WWIRED
     C     WWIRED        WHENEQ    '0S'
     C                   MOVE      '28'          WWIRED
     C     WWIRED        WHENEQ    '0T'
     C                   MOVE      '29'          WWIRED
     C     WWIRED        WHENEQ    '0U'
     C                   MOVE      '30'          WWIRED
     C     WWIRED        WHENEQ    '0V'
     C                   MOVE      '31'          WWIRED
     C     WWIRED        WHENEQ    '0W'
     C                   MOVE      '32'          WWIRED
     C     WWIRED        WHENEQ    '0X'
     C                   MOVE      '33'          WWIRED
     C     WWIRED        WHENEQ    '0Y'
     C                   MOVE      '34'          WWIRED
     C     WWIRED        WHENEQ    '0Z'
     C                   MOVE      '35'          WWIRED
     C                   ENDSL
     C     WWIRED        IFEQ      '00'
     C                   MOVE      '01'          WWIRED
     C                   ENDIF
     C                   EndSr
     c*---------------------------------------------------------------------
     c* MarcarReg: Marcar Registros como ya enviadas
     c*---------------------------------------------------------------------
     c     MarcarReg     BegSr
     C*
     c                   Move      AASFEI        AFFTRA
     c                   Time                    AFHTRA
     c                   Move      @PUSER        AFIUSP
     c                   Update    REPRAFED
     C*
     c                   EndSr
     c*---------------------------------------------------------------------
     c* *INZSR: Rutina de Inicialización
     c*---------------------------------------------------------------------
     c     *INZSR        BegSr
     C*
     c     1             Chain     SGSYSV
     C*
     C     KFD010        KList
     C                   KFld                    AASFEI
     C*
     C     KJV010        KList
     C                   KFld                    AFISUC
     C                   KFld                    AFINCR
     C                   KFld                    AFIDEG
     C*
     C     KSA010        KList
     C                   KFld                    AASFEI
     C                   KFld                    JVISUC
     C                   KFld                    JVICCL
     C                   KFld                    JVINCR
     C                   KFld                    JVIDEG
     C*
     C                   EndSr
     c*---------------------------------------------------------------------
     c* CheckYaProcesados
     c*---------------------------------------------------------------------
     c     ChkYaProc     BegSr
     C*
     C                   Move      *OFF          YaEnvFlag         1
     C                   Move      *OFF          RProcesadas       1
     C*
     C     KFD010        Chain     REPRAFED                           25
     C                   DoW       *IN25 = *Off
     C                   IF        AFFTRA <> *ZERO
     C                   Move      *ON           YaEnvFlag
     C                   EndIF
     C                   IF        AFFACR <> *ZERO
     C                   Move      *ON           RProcesadas
     C                   EndIF
     C     KFD010        ReadE     REPRAFED                               25
     C                   EndDo
     C*
     c                   If        YaEnvFlag = *On and RProcesadas=*Off
     c                   Eval      ErrTxt=*blanks
     C                   Eval      ErrTxt='La información correspondiente'+
     C                             ' al día: '+%EditW(AASFEI:'    /  /  ')
     C                   Eval      WWNCU2='Ya fue envíada por:'+AFIUSP+
     C                                    ' A las:'+%EditW(AFHTRA:'  :  :  ')
     C                   Eval      WWNCB3='Presione F10 Para Reprocesar'
     C                   Eval      WWNCB4='Presione F03 Para Cancelar  '
     C                   ExSr      DspErr
     C                   ExSr      ReadParams
     C                   If        @FN(10) <> *ON
     C                   ExSr      EndPgm
     C                   EndIf
     C                   EndIf
     c                   If        YaEnvFlag = *On and RProcesadas=*On
     c                   Eval      ErrTxt=*blanks
     C                   Eval      ErrTxt='La información correspondiente'+
     C                             ' al día: '+%EditW(AASFEI:'    /  /  ')
     C                   Eval      WWNCU2='Ya fue envíada por:'+AFIUSP+
     C                                    ' A las:'+%EditW(AFHTRA:'  :  :  ')
     C                   Eval      WWNCU3='Y las resp. procesadas por:'+AFIUSP+
     C                                    ' A las:'+%EditW(AFHTRA:'  :  :  ')
     C                   Eval      WWNCB4='Presione F03 Para Cancelar  '
     C                   ExSr      DspErr
     C                   ExSr      ReadParams
     C*                  ExSr      EndPgm
     C                   EndIf
     C*
     C                   EndSr
     c*---------------------------------------------------------------------
     c* DspOkMsg: Mostrar Mensaje de Finalización OK
     c*---------------------------------------------------------------------
     c     DspOkMsg      BegSr
     c*
     c                   Eval      ErrTxt=*blanks
     C                   Eval      ErrTxt='La información correspondiente'+
     C                             ' al día: '+%EditW(AASFEI:'    /  /  ')
     C                   Eval      WWNCU2='Ha sido generada y dejada en:'
     C                   Eval      WWNCU3=txtFile
     C                   Eval      WWNCB1='No olvide enviarla a Federal'
     C                   Eval      WWNCB4='Presione F03 Para Salir     '
     C                   ExSr      DspErr
     c*
     c                   EndSr
     c*---------------------------------------------------------------------
     c* EndPgm: Finalizar Programa
     c*---------------------------------------------------------------------
     c     EndPgm        BegSr
     C*
     c                   SetOn                                        LR
     c                   Return
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C* DspErr: Mostrar Mensaje de Error
     C*-------------------------------------------------------------------------
     C     DspErr        BEGSR
     C*
     C                   CALL      'BAER01RS'
     C                   PARM                    WWNCU1
     C                   PARM                    WWNCU2
     C                   PARM                    WWNCU3
     C                   PARM                    WWNCU4
     C                   PARM                    WWNCB1
     C                   PARM                    WWNCB2
     C                   PARM                    WWNCB3
     C                   PARM                    WWNCB4
     C*
     C                   ENDSR
     C*---------------------------------------------------------------------
     C* ReadParms:Leer Parámetros
     C*---------------------------------------------------------------------
     C     ReadParams    BegSr
     C*
     C* Lee registro de Usuario
     C     @PJOBN        Chain(N)  @CPIUSD                            80
     C   80              Z-Add     @PJOBN        @ZJOBN
     C   80              Write     @CPIUSRR
     C* Lee registro de sistema
     C     @PJOBN        Chain(N)  @CPISYS                            90
     C   90              Z-Add     @PJOBN        @ZJOBN
     C   90              Write     @CPISYSR
     C*
     C                   EndSr
     C*----------------------------------------------------------------*
     C* OpnStmF: ABRE ARCHIVO EN IFS
     C*-------------------------------------------------------------------------
     C     OpenStmF      BegSr
     c*
     c                   Z-add     AASFEI        FechaN
     c                   Move      FechaN        FechaC
     c                   Time                    WWTIM             6 0
     c                   Move      WWTIM         CHTIM             6
     c                   Eval      txtFile=%TRIM(OUTPAT)+'prefed_'+FechaC+
     C                                     '_'+%TRIM(@PUSER)+'_'+
     C                                     CHTIM + '.txt'
     C*
     c                   EVAL      FilHnd=open(%trim(txtfile):
     c                                  O_CREAT + O_WRONLY + O_TRUNC +
     c                                  O_CODEPAGE :
     c                                  S_IWUSR+S_IRUSR+S_IRGRP+S_IROTH:
     c                                  819     )
     c*                                 1252    )
     c                   callp     close(FilHnd)
     c                   EVAL      FilHnd=open(%trim(txtfile):
     c                                   O_WRONLY+O_TEXTDATA)
     c*
     C                   EndSr
     C*----------------------------------------------------------------*
     C* CloseStmF: Cierra el Archivo
     C*----------------------------------------------------------------*
     C     CloseStmF     BegSr
     c                   CallP     close(FilHnd)
     C                   EndSr
     C*----------------------------------------------------------------*
     C* WrtLin: Escribe una linea en el Stream File
     C*----------------------------------------------------------------*
     C     WrtLin        BegSr
     C*
     c                   CallP     write(FilHnd: %addr(buf   ): %size(buf   ))
     C*
     C                   EndSr
