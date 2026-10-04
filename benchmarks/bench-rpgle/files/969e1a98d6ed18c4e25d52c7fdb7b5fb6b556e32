*SRCMBRTXT:Gen. de Archivo Refresh de Recibos de A
     H DFTACTGRP(*NO)  ACTGRP('QILE')
     H DEBUG DATEDIT(*YMD) GENLVL(20)
     F*----------------------------------------------------------------*
     F*  ANLI08R1                                                      *
     F*  REFRESH DE RECIBOS DE ANSES PARA LINK                         *
     F*
     F*  CREADO     POR: S. OTTONELLO     - PR00525 - 27.04.2011
     F*----------------------------------------------------------------*
     FSGSYSV    IF   E           K DISK
     F*  The system values file
     F*----------------------------------------------------------------*
     F@CPISYS   IF   E           K DISK
     F*  Program interface containing system values.
     F*----------------------------------------------------------------*
     F@CPIUSD   IF   E           K DISK
     F*  Program interface containing user values.
     F*----------------------------------------------------------------*
     FANLIHA15  IF   E           K DISK
     F*  Registro unico de liquidacion de haberes
     F*----------------------------------------------------------------*
     FACCTAC    IF   E           k DISK
     F*  Registro unico de liquidacion de haberes
     F*----------------------------------------------------------------*
     FBAENTI    IF   E           K DISK
     F*  Datos generales de la entidad
     F*----------------------------------------------------------------*
     FANCODI    IF   E           K DISK
     F*  Códigos de pago / descuento ANSES
     F*----------------------------------------------------------------*
     D  NormalizaStr   PR           360A
     D    Name                      360A
     I*  Program status data structure.
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
     F*----------------------------------------------------------------*
     D*  Function keys from common program interface                   *
     D*----------------------------------------------------------------*
     D* Series utilizadas para datos de campos
     D @DES            S             16    DIM(25)
     D TABCOD          S              3  0 DIM(80) CTDATA PERRCD(1)
     D TABEMP          S              3  0 DIM(80) ALT(TABCOD)
     D*----------------------------------------------------------------*
     D                 DS
     D  @ZFNKY                 1     24
     D  @FN                    1     24
     D                                     DIM(24)
     D                 DS
     D  WRKARA                 1   3600
     D  LINREC                 1   3600
     D                                     DIM(100)
     D  PAGREC                 1   3600
     D                                     DIM(10)
     D
     D*----------------------------------------------------------------*
     D* Estructura de datos para @DES
     D                 DS
     D  DESCUE                 1     16
     D  WWCONC                 1      3  0
     D  WWEMPR                 4      6  0
     D  WWIMPO                 7     16  2
     D* Estructura de datos para armar la hora HHMM
     D                 DS
     D  HORA                   1      6  0
     D  WWHORA                 1      4  0
     D* Estructura de datos para armar la fecha DDMMAA
     D                 DS
     D  FECHA                  1      8  0
     D  DIA                    1      2  0
     D  MES                    3      4  0
     D  SIGLO                  5      6  0
     D  AÑO                    7      8  0
     D  WWFECH                 9     14  0
     D  WWDIA                  9     10  0
     D  WWMES                 11     12  0
     D  WWAÑO                 13     14  0
     D* Estructura de datos para descuentos del ANSES
     D                 DS
     D  WWKEYA                 1     27
     D  WWCUIA                 1     11  0
     D  WWIECJ                12     13  0
     D  WWITBE                14     14  0
     D  WWINBE                15     21  0
     D  WWIICP                22     22  0
     D  WWIDVA                23     23  0
     D  WWIPEA                24     27  0
     D* Estructura de datos para Concepto Pago / Desc.
     D                 DS
     D  CODCON                 1      6  0
     D  WWCON1                 1      3  0
     D  WWEMP1                 4      6  0
     D                 DS
     D  WXCODI                 1      3  0
     D  WXCONC                 1      3  0
     D  WXEMPR                 4      6  0
     D*----------------------------------------------------------------*
     D LDA           E DS                  EXTNAME(LDA)
     D*  Fetch external description of Local Data Area
     D*----------------------------------------------------------------*
     D               ESDS                  EXTNAME(@PSDS)
     D*---------------------------------------------------------------------
     D* Variables y Estructuras de Datos del Programa
     D*---------------------------------------------------------------------
     D FILHND          S             10I 0
     d buf             s            460
     d TIPCTA          s              2
     d Count           s              8S 0
     d txtfile         s            255
     d WWNCTA          s             19
     D*---------------------------------------------------------------------
     d*-------------------------------------------------------------------------
     D CTADS           DS
     D  CTALNK                 1     19
     D  LINSUC                 1      3  0
     D  LINFI2                 4      4  0
     D  LINGRP                 5      6
     D  LINFIL                 7      9  0
     D  LINCAH                10     16  0
     I*----------------------------------------------------------------*
     DANLIHA15DS       DS
     D ANFILL1                 1    134
     D @DES                  135    534
     D ANCC01                135    137  0
     D ANCE01                138    140  0
     D ANIM01                141    150  2
     D ANCC02                151    153  0
     D ANCE02                154    156  0
     D ANIM02                157    166  2
     D ANCC03                167    169  0
     D ANCE03                170    172  0
     D ANIM03                173    182  2
     D ANCC04                183    185  0
     D ANCE04                186    188  0
     D ANIM04                189    198  2
     D ANCC05                199    201  0
     D ANCE05                202    204  0
     D ANIM05                205    214  2
     D ANCC06                215    217  0
     D ANCE06                218    220  0
     D ANIM06                221    230  2
     D ANCC07                231    233  0
     D ANCE07                234    236  0
     D ANIM07                237    246  2
     D ANCC08                247    249  0
     D ANCE08                250    252  0
     D ANIM08                253    262  2
     D ANCC09                263    265  0
     D ANCE09                266    268  0
     D ANIM09                269    278  2
     D ANCC10                279    281  0
     D ANCE10                282    284  0
     D ANIM10                285    294  2
     D ANCC11                295    297  0
     D ANCE11                298    300  0
     D ANIM11                301    310  2
     D ANCC12                311    313  0
     D ANCE12                314    316  0
     D ANIM12                317    326  2
     D ANCC13                327    329  0
     D ANCE13                330    332  0
     D ANIM13                333    342  2
     D ANCC14                343    345  0
     D ANCE14                346    348  0
     D ANIM14                349    358  2
     D ANCC15                359    361  0
     D ANCE15                362    364  0
     D ANIM15                365    374  2
     D ANCC16                375    377  0
     D ANCE16                378    380  0
     D ANIM16                381    390  2
     D ANCC17                391    393  0
     D ANCE17                394    396  0
     D ANIM17                397    406  2
     D ANCC18                407    409  0
     D ANCE18                410    412  0
     D ANIM18                413    422  2
     D ANCC19                423    425  0
     D ANCE19                426    428  0
     D ANIM19                429    438  2
     D ANCC20                439    441  0
     D ANCE20                442    444  0
     D ANIM20                445    454  2
     D ANCC21                455    457  0
     D ANCE21                458    460  0
     D ANIM21                461    470  2
     D ANCC22                471    473  0
     D ANCE22                474    476  0
     D ANIM22                477    486  2
     D ANCC23                487    489  0
     D ANCE23                490    492  0
     D ANIM23                493    502  2
     D ANCC24                503    505  0
     D ANCE24                506    508  0
     D ANIM24                509    518  2
     D ANCC25                519    521  0
     D ANCE25                522    524  0
     D ANIM25                525    534  2
     C*----------------------------------------------------------------*
     c
     c                   Z-Add     *ZERO         WKISUC
     c                   Z-Add     *ZERO         WKICAH
     c                   Z-Add     *ZERO         Count
     c                   ExSr      OpenStmF
     c                   ExSr      WrtFilHdr
     C     *LOVAL        SETLL     ANLIHA15
     C                   Read      ANLIHA15                               99
     C                   DoW       *IN99 = *OFF
     c                   If        ANICAH <> 0
     c     KFU000        Chain     REACCTAC                           99
     c                   If        *IN99 = *OFF and FUIUCA='S'
     c                   If        ANISUC <> WKISUC or ANICAH <> WKICAH
     C                   If        WKICAH <> *ZERO
     c                   ExSr      WriteVector
     C                   EndIf
     c                   Clear                   LINREC
     C                   Z-Add     *ZERO         I                 3 0
     c                   Z-Add     ANISUC        WKISUC
     c                   Z-Add     ANICAH        WKICAH
     C                   ExSr      GetCtaLink
     c                   EndIf
     c                   ExSr      BuildVector
     c                   EndIf
     c                   EndIf
     C                   Read      ANLIHA15                               99
     C                   EndDo
     c                   ExSr      WrtFilFtr
     c                   ExSr      CloseStmF
     C                   ExSr      EndPgm
     C*
     C*-------------------------------------------------------------------------
     c     WrtFilHdr     BegSr
     C*-------------------------------------------------------------------------
     C*
     C                   Eval      buf=*blanks
     C                   Eval      %subst(buf:001:006)='HR_ICP'
     C                   Eval      %subst(buf:007:004)='0309'
     C                   Eval      %subst(buf:011:006)='999999'
     C                   Eval      %subst(buf:017:008)=%EDITW(AASFEI:'        ')
     C                   Eval      %subst(buf:025:436)=*BLANKS
     C*
     c                   CALLP     write(FilHnd: %addr(buf   ): %size(buf   ))
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     c     WrtFilFtr     BegSr
     C*-------------------------------------------------------------------------
     C*
     C* ... Incluir Registros de Pie y Cabecera en la Cantidad
     c                   Add       2             Count
     C                   Eval      buf=*blanks
     C                   Eval      %subst(buf:001:006)='TR_ICP'
     C                   Eval      %subst(buf:007:008)=%TRIM(
     C                                                %EDITW(Count:'0        ')
     C                                                 )
     C*
     c                   CALLP     write(FilHnd: %addr(buf   ): %size(buf   ))
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     c     WriteVector   BegSr
     C*-------------------------------------------------------------------------
     C     I             DIV       10            CANPAG            2 0
     C                   IF        %REM(I:10) <> 0
     C                   ADD       1             CANPAG
     C                   ENDIF
     C                   Z-ADD     *ZERO         J                 2 0
     C                   FOR       J= 1 TO CANPAG
     C                   Eval      buf=*blanks
     C                   Eval      %subst(buf:001:002)='11'
     C                   Eval      %subst(buf:003:019)=WWNCTA
     C                   Eval      %subst(buf:022:008)='00000000'
     C                   Eval      %subst(buf:030:008)='00000000'
     c                   Z-Add     ANINBE        AXINBE           12 0
     C                   MOVE      AXINBE        CODBEN           12
     C                   Eval      %subst(buf:038:012)=CODBEN
     C                   Z-ADD     ANINDA        AXICUI           11 0
     C                   MOVE      AXICUI        ANICUI           11
     C                   Eval      %subst(buf:050:011)=ANICUI
     C                   Eval      %subst(buf:061:002)=%TRIM(%EDITW(J:'0  '))
     C                   Eval      %subst(buf:063:002)=%TRIM(%EDITW(CANPAG:
     C                                                  '0  '))
     C*                  Eval      %subst(buf:065:036)='CBTE. PREVISIONAL PAG.'+
     C*                            ':'+%TRIM(%EDITW(J     :
     c*                             '0  '))+ ' DE ' +
     c*                            %TRIM(%EDITW(CANPAG:
     c*                             '0  '))
     C                   Eval      %subst(buf:065:036)='EMITIDO POR ATM'
     C                   Eval      %subst(buf:101:360)=NormalizaStr(PAGREC(J))
     C*
     c                   CALLP     write(FilHnd: %addr(buf   ): %size(buf   ))
     c                   Add       1             Count
     C*
     C                   ENDFOR
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     C     BldRecHdr     BegSr
     C*-------------------------------------------------------------------------
     C*
      /FREE
       //         0        1         2         3
       //         123456789012345678901234567890123456
       I=I+1;
       LINREC(I)='MTEySS,SSS/ANSES CUIT: 33-63761744-9';
       I=I+2;
       LINREC(I)=MLNBAN;
       I=I+1;
       LINREC(I)='SUC.:'+WWISUC+' AGENCIA ANSES:'+%EDITW(ANICBP:' 0 ')+'-'+
                                                  %EDITW(ANIABP:' 0 ');
       I=I+2;
       LINREC(I)='TITULAR:'+ANNYAA;
       I=I+1;
       LINREC(I)='DOC:'+%EDITW(ANITDA:'  ')+'-'+%EDITW(ANINDA:'  .   .   ')+
                 ' CUIL:'+%EDITW(ANCUIA:'  -        - ');
       I=I+1;
       LINREC(I)='APODERADO:'+ANNAAP;
       I=I+1;
       LINREC(I)='DOC.:'+%EDITW(ANITDP:'  ')+'-'+%EDITW(ANINDP:'  .   .   ');
       I=I+2;
       LINREC(I)='BENEFICIO:'+ %TRIM(%EDITW(ANIECJ:'0 ')      ) +'-'+
                                %TRIM(%EDITW(ANITBE:'0 ')      ) +'-'+
                                %TRIM(%EDITW(ANINBE:'0       ')) +'-'+
                                %TRIM(%EDITW(ANIICP:'0 ')      ) +'-'+
                                %TRIM(%EDITW(ANIDVA:'0 ')      )  ;
       I=I+1;
       LINREC(I)='PERIODO LIQUIDADO:'+%EDITW(ANIPEA:'  -  ');
       I=I+1;

      /END-FREE
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     EndPgm        BegSr
     C*-------------------------------------------------------------------------
     C*
     C                   SetOn                                        LR
     C                   Return
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     GetCtaLink    BegSr
     C*-------------------------------------------------------------------------
     C*
     C                   Z-ADD     FUISUC        LINSUC
     C                   MOVE      FUIGRC        LINGRP
     C                   Z-ADD     FUICAH        LINCAH
     C                   Z-ADD     *ZEROS        LINFIL
     C                   Z-ADD     *ZEROS        LINFI2
     C
     C                   MOVE      CTALNK        WWNCTA
     C*
     C                   EndSr
     C*----------------------------------------------------------------*
     C     *INZSR        BEGSR
     C*----------------------------------------------------------------*
     C*  ........get the LDA
     C                   IN        LDA
     C*  ........LDA data structure as *LDA
     C     *DTAARA       DEFINE    *LDA          LDA
     C*  ........Get the program starting date and time
     C     *LOVAL        SETLL     SGSYSV
     C                   READ      SGSYSV                                 99
     C                   MOVE      '00000'       WWISUC            5
     C                   MOVE      ANISUC        WWISUC
     C* .........Arma la fecha del sistema con formato DDMMAA
     C                   Z-ADD     AASFEN        FECHA
     C                   Z-ADD     DIA           WWDIA
     C                   Z-ADD     MES           WWMES
     C                   Z-ADD     AÑO           WWAÑO
     C*  ........Accede a información sobre la entidad
     C     *LOVAL        SETLL     BAENTI
     C                   READ      BAENTI                                 99
     C*
     c     KFU000        KLIST
     C                   KFLD                    ANISUC
     C                   KFLD                    ANICAH
     C*
     C                   Z-ADD     *ZEROS        WWRRNO           11 0
     c*
     c     *LIKE         DEFINE    ANISUC        WKISUC
     c     *LIKE         DEFINE    ANICAH        WKICAH
     c*
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C     OpenStmF      BegSr
     C*-------------------------------------------------------------------------
     C*
     C* ... Formato Nombre ibbbeeeeevaammdd
     C*     -I         (Mayúscula) Valor Fijo
     C*     -bbb       Código Banco BCRA
     C*     -eeeee     Entidad             (99999 Para ANSES)
     C*     -V         Nro de Versión en el día (Por si se manda mas de una vez)
     C*     -aammdd    Fecha de Envío
     C*
     c                   MOVE      AASFEI        FECHA6            6
     c                   EVAL      txtfile='/home/LINKBEE/REFRESH/'+
     c                                     'I30999991'+FECHA6
     c                   EVAL      FilHnd=open(%trim(txtfile):
     c                                  O_CREAT + O_WRONLY + O_TRUNC +
     c                                  O_CODEPAGE :
     c                                  S_IWUSR+S_IRUSR+S_IRGRP+S_IROTH:
     c                                  819     )
     c                   callp     close(FilHnd)
     c                   EVAL      FilHnd=open(%trim(txtfile):
     c                                   O_WRONLY+O_TEXTDATA)
     c*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     CloseStmF     BegSr
     C*-------------------------------------------------------------------------
     C*
     c                   callp     close(FilHnd)
     C*
     C                   EndSr
     C*----------------------------------------------------------------
     C* FOR003   Formulario FORM003
     C*----------------------------------------------------------------
     C     BuildVector   BEGSR
     C*----------------------------------------------------------------
     C* Impresión de cabecera de la pisada                           %TRIM(
     C                   ExSr      BldRecHdr
     C* Impresión de detalle de la pisada                            %TRIM(
     C                   SETOFF                                       969798
     C                   SETOFF                                       616263
     C                   Z-ADD     *ZEROS        WXIMPO            7 2
     C                   Z-ADD     *ZEROS        WX$LQ2            7 2
     C     1             DO        25            N                 2 0
     C                   MOVEL     @DES(N)       DESCUE
     C                   Z-ADD     WWCONC        CONC01            3 0
     C                   Z-ADD     WWEMPR        EMPR01            3 0
     C                   Z-ADD     WWCONC        WWCON1
     C                   Z-ADD     WWEMPR        WWEMP1
     C                   MOVE      *OFF          *IN61
     C                   Z-ADD     *ZEROS        WXCODI
     C                   Z-ADD     WWCONC        WXCONC
     C     WXCONC        LOOKUP    TABCOD        TABEMP                   66
     C     *IN66         IFEQ      *ON
     C                   MOVE      TABEMP        WXEMPR
     C     WXEMPR        IFEQ      999
     C                   MOVE      *ON           *IN61
     C                   MOVE      *ON           *IN62
     C                   ADD       WWIMPO        WXIMPO            7 2
     C                   GOTO      SIGO
     C                   ENDIF
     C     WXEMPR        IFEQ      WWEMPR
     C                   MOVE      *ON           *IN61
     C                   MOVE      *ON           *IN62
     C                   ADD       WWIMPO        WXIMPO            7 2
     C                   ENDIF
     C                   ENDIF
     C     SIGO          TAG
     C                   Z-ADD     CODCON        WWICCU            6 0
     C     WWICCU        CHAIN     REANCODI                           95
     C     *IN95         IFEQ      *ON
     C                   MOVEL     *BLANKS       CDDTXT
     C                   ENDIF
     C     WWCONC        IFGE      200
     C     WWCONC        ANDLE     699
     C                   SETON                                        96
     C                   ELSE
     C                   SETOFF                                       96
     C                   END
     C                   Z-ADD     WWIMPO        IMPO01            7 2
     C     CONC01        IFEQ      *ZEROS
     C                   GOTO      PIE
     C                   ELSE
     c                   ADD       1             I
     C                   MOVE      ' $ '         SIMBOLO           3
     C                   IF        *IN61=*ON
     C                   MOVE      '(*)'         SIMBOLO           3
     C                   ENDIF
     C                   MOVE      *BLANKS       IMPCHAR          12
     C                   EVAL      IMPCHAR  =' '+
     C                             %EDITW(IMPO01: '     0 ,  ') +' '
     C                   IF        *IN96 = *ON
     C                   EVAL      IMPCHAR  ='('+
     C                             %EDITW(IMPO01: '     0 ,  ') +')'
     C                   ENDIF
     C                   EVAL      LINREC(I)= %TRIM(%EDITW(CONC01:'0   '))+'-'+
     c                                        %TRIM(%EDITW(EMPR01:'0   '))+' '+
     C                                         %SUBST(CDDTXT:1:13)+
     C                                         SIMBOLO+IMPCHAR
     C                   Z-ADD     *ZEROS        CONC01
     C                   Z-ADD     *ZEROS        EMPR01
     C                   Z-ADD     *ZEROS        IMPO01
     C                   ENDIF
     C* Impresión de pie de la pisada                                %TRIM(
     C     PIE           TAG
     C     AN$AF1        IFNE      *ZEROS
     C     AN$AF2        ORNE      *ZEROS
     C                   SETON                                        97
     C                   END
     C   62AN$LQ2        SUB       WXIMPO        WX$LQ2
     C   62WX$LQ2        IFLT      *ZEROS
     C                   SETON                                        63
     C                   ENDIF
     C                   ENDDO
     C                   ExSr      BldRecFtr
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C     BldRecFtr     BegSr
     C*
      /FREE
       I=I+1;
       I=I+1;
       LINREC(I)= 'TOTAL HABERES   :$ '+%EDITW(AN$THA:' .   .   .   ,  ');
       I=I+1;
       LINREC(I)= 'TOTAL DESCUENTOS:$('+%EDITW(AN$DET:' .   .   .   ,  ')+')';
       I=I+1;
       LINREC(I)= 'NETO ANSES      :$('+%EDITW(AN$LQA:' .   .   .   ,  ')+')';
       IF *IN97 = *ON;
         I=I+1;
         LINREC(I)= 'CTA MORAT.AFIP:$('+%EDITW(AN$AF1:' .   .   .   ,  ')+')';
         I=I+1;
         LINREC(I)= 'RETROAC.MOR.AFIP:$('+%EDITW(AN$AF2:' .   .   .   ,  ')+')';
       ENDIF;
       I=I+1;
       LINREC(I)=   'NETO A COBRAR   :$ '+%EDITW(AN$LQ2:' .   .   .   ,  ')+' ';
       IF *IN62 = *ON;
         I=I+1;
         LINREC(I)= 'DESC P/SCOR(*)  :$'+%EDITW(WXIMPO:' .   .   .   ,  ')+' ';
       IF *IN63 = *ON;
       I=I+1;
       LINREC(I)=   'NETO P/SCOR(*)  :$ '+%EDITW(WX$LQ2:' .   .   .   ,  ')+' ';
       ELSE;
       I=I+1;
       LINREC(I)=   'NETO P/SCOR(*)  :$('+%EDITW(WX$LQ2:' .   .   .   ,  ')+')';
       ENDIF;
       ENDIF;
       I=I+1;
       I=I+1;
       LINREC(I)= 'FECHA PROX. COBRO DESDE:'+ %EDITW(ANIFPP:'  -  -    ');
      /END-FREE
     C*
     C                   EndSr
     C*=========================================================================
     P NormalizaStr    B
     D  NormalizaStr   PI           360A
     D    Name                      360A
     D*
     D up              C                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     D lo              C                   'abcdefghijklmnopqrstuvwxyz'
     D Symbols         C                   '|°¬/¡¿~[]{}'
     D SymBlanks       C                   '           '
     D Acentos         C                   'ñÑáéíóúäëïöüãõàèìòùâêîôû@'
     D AceBlanks       C                   'nNAEIOUAEIOUAOAEIOUAEIOU '
     D Apos            C                   ''''
     D APosBlank       C                   ' '
     D*
     C                   Eval      NAME = %XLATE(Symbols:SymBlanks:NAME)
     C                   Eval      NAME = %XLATE(Acentos:AceBlanks:NAME)
     C                   Eval      NAME = %XLATE(Apos:AposBlank:NAME)
     C                   Eval      NAME = %XLATE(lo:up:NAME)
     C                   Return    NAME
     P NormalizaStr    E
     C*----------------------------------------------------------------
** Codigos ANSES
002000
022022
135000
061000
076000
010000
102000
060000
170000
195999
060999
022999
108999
116999
123999
124999
125999
126999
700999
106025
133033
058000
133035
