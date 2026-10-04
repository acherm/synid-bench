*SRCMBRTXT:Calculo de cuotas                      
     H DEBUG
     H DFTACTGRP(*NO)  ACTGRP('QILE')
     H*****************************************************************
     H*                                                               *
     H*  SYSTEM NAME: SIDEBA - Prestamos                              *
     H*                                                               *
     H*  PROGRAM NAME: Calculo de cuotas                              *
     H*                                                               *
     H*  PROGRAM NO: PR0400RG                                         *
     H*                                                               *
     H*  DATE: 19.01.2006                                             *
     H*                                                               *
     H*  AUTHOR: Luis Romanazzi                                       *
     H*                                                               *
     H*  Modif.: Carolina I. Cova - PR00543                           *
     H*                                                               *
     H*****************************************************************
     FBAPFIS05  IF   E           K DISK
     FBC430507  IF   E           K DISK
     FBAITAS    IF   E           K DISK
     FPRICTA    IF   E           K DISK
     FBASCEL    IF   E           K DISK
     FPRMLIN02  IF   E           K DISK
     F@CPIUSD   UF   E           K DISK
     FPRCUOT61  UF A E           K DISK
     F*----S1-------------------------------------------------------------------
     FPRPIVA    IF   E           K DISK
     FPREIVA    IF   E           K DISK
     FPRCODI    IF   E           K DISK
     FBAICCL    IF   E           K DISK
     FBADCCL01  IF   E           K DISK
     FBAPFIS    IF   E           K DISK    RENAME(REBAPFIS:RBAPFIS)
     FBAPJUR    IF   E           K DISK
     FPRCRED    IF   E           K DISK
     F*----S2-------------------------------------------------------------------
     FPRPARM    IF   E           K DISK
     FPRCUOT01  IF   E           K DISK
     FPRLICR    IF   E           K DISK
     F*----S2-------------------------------------------------------------------
     D PR0400S1        PR
     D  WWITDO                        2  0
     D  WWINDO                       15  0
     D  WW$CAP                       15  2
     D  WW$IMP                       15  2
     D PR0400S2        PR
     D WWISUC                         5  0
     D WWIMPR                         3  0
     D WWIMON                         9  0
     D WW$CAA                        15  2
     D WW$IMP                        15  2
     D PR0400S3        PR
     D WWISUC                         5  0
     D WWIMPR                         3  0
     D WWIMON                         9  0
     D WW$CAA                        15  2
     D WW$IMP                        15  2
     D*----------------------------------------------------------------*
     D               ESDS                  EXTNAME(@PSDS)
     I*----------------------------------------------------------------*
     C*
     C                   EXSR      SRPROC
     C     @CIASC        IFEQ      *ZEROS
     C     FLAG          ANDEQ     *ON
     C                   CALL      'PR0400TE'
     C                   ENDIF
     C                   MOVEL     *ON           *INLR
     C*
     C*----------------------------------------------------------------*
     C* INICIO - Busca datos para inicio del programa
     C*----------------------------------------------------------------*
     C     *INZSR        BEGSR
     C*
     C     *ENTRY        PLIST
1    C                   PARM                    WW$CAP           15 2
2    C                   PARM                    WWICUO            3 0
3    C                   PARM                    WWIPLA            4 0
4    C                   PARM                    WWISUC            5 0
5    C                   PARM                    WWITDO            2 0
6    C                   PARM                    WWINDO           15 0
7    C                   PARM                    WWIMON            9 0
8    C                   PARM                    WWILCR            4 0
9    C                   PARM                    WWIEMP            5 0
10   C                   PARM                    FLAG              1
     C*
     C     WKEY02        KLIST
     C                   KFLD                    WXISUC            5 0
     C                   KFLD                    WWILCR
     C                   KFLD                    WWIMPR
     C                   Z-ADD     99999         WXISUC
     C*
     C                   Z-ADD     *ZEROS        PADIAS           15 0
     C                   MOVEL     *BLANK        PADSEM            2
     C                   MOVEL     *BLANK        PADIRR            1
     C                   Z-ADD     *ZEROS        WW$IVA           15 2
     C                   Z-ADD     *ZEROS        WW$COM           15 2
     C                   Z-ADD     *ZEROS        WWIMPR            3 0
     C                   Z-ADD     *ZEROS        WW$CUI           15 2
     C                   Z-ADD     *ZEROS        WW$DVI           15 2
     C                   Z-ADD     *ZEROS        WW$SCA           15 2
     C                   Z-ADD     *ZEROS        WW$TOT           15 2
     C                   Z-ADD     *ZEROS        WW$IV1           15 2
     C                   Z-ADD     *ZEROS        WW$GAS           15 2
     C                   Z-ADD     *ZEROS        WW$NET           15 2
     C                   Z-ADD     *ZEROS        WW$VAL           15 2
     C     @PJOBN        CHAIN(N)  @CPIUSD                            80
     C* ... Obtiene fecha vto. y fecha de inicio
     C                   Z-ADD     @CFCIM        WWF1VT            8 0
     C                   EXSR      OBTFEI
     C* ... Blanqueo PRCUOT60
     C     FLAG          IFEQ      *ON
     C     @PJOBN        CHAIN     PRCUOT61                           80
     C     *IN80         DOWEQ     *OFF
     C                   DELETE    REPRCU60
     C     @PJOBN        READE     PRCUOT61                               80
     C                   ENDDO
     C                   ENDIF
     C*
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* SRPROC - Proceso
     C*----------------------------------------------------------------*
     C     SRPROC        BEGSR
     C*
     C                   EXSR      PROC01
     C     @PJOBN        CHAIN     @CPIUSD                            80
     C                   Z-ADD     WWTGLI        @CTGLI
     C                   Z-ADD     WW$CUI        @C$INE
     C                   Z-ADD     WW$DVI        @C$TRE
     C*                  Z-ADD     WW$SCA        @C$PRM
     C                   Z-ADD     GASORI        @C$PRM
     C                   ADD       TOCO77        @C$PRM
     C                   ADD       TOCO78        @C$PRM
     C*
     C*                  Z-ADD     WW$TOT        @C$LCJ
     c*@C$LCJ=@C$INP-@C$PRM
     C                   Z-ADD     @C$INP        @C$LCJ
     C                   SUB       @C$PRM        @C$LCJ
     c*
     C                   SUB       TOCO77        WW$NET
     C                   SUB       TOCO78        WW$NET
     C                   Z-ADD     WW$NET        @C$ICU
     C                   SUB       @C$MON        @C$ICU
     C                   Z-ADD     WW$VAL        @C$MAX
     C                   UPDATE    @CPIUSRR
     C*
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC01
     C*----------------------------------------------------------------*
     C     PROC01        BEGSR
     C* Fecha de Alta
     C                   Z-ADD     WWFALT        PAFECH            8 0
     C                   MOVE      'IN'          PACINV            2
     C                   CALL      'SBBAINFE'
     C                   PARM                    PAFECH
     C                   PARM                    PACINV
     C                   Z-ADD     *ZEROS        PADIAS
     C                   MOVEL     *BLANK        PADSEM
     C                   MOVEL     *BLANK        PADIRR
     C                   CALL      'SBBAFECH'
     C                   PARM                    PAFECH
     C                   PARM                    PADIAS
     C                   PARM                    PADSEM
     C                   PARM                    PADIRR
     C                   Z-ADD     PADIAS        DIAS1            15 0
     C* Fecha de 1 Vto
     C                   Z-ADD     WWF1VT        PAFECH
     C                   MOVE      'IN'          PACINV            2
     C                   CALL      'SBBAINFE'
     C                   PARM                    PAFECH
     C                   PARM                    PACINV
     C                   Z-ADD     *ZEROS        PADIAS
     C                   MOVEL     *BLANK        PADSEM
     C                   MOVEL     *BLANK        PADIRR
     C                   CALL      'SBBAFECH'
     C                   PARM                    PAFECH
     C                   PARM                    PADIAS
     C                   PARM                    PADSEM
     C                   PARM                    PADIRR
     C                   Z-ADD     PADIAS        DIAS2            15 0
     C*
     C     DIAS2         SUB       DIAS1         DIFDIA           15 0
     C     WWILCR        CHAIN     PRLICR                             80
     C     DUITRU        IFEQ      10
     C     DUIOPE        ANDEQ     80
     C     DUITRU        OREQ      11
     C     DUIOPE        ANDEQ     80
     C                   Z-ADD     30            DIFDIA
     C                   ENDIF
     C* PRUEBA
     C                   EXSR      TASA
     C                   Z-ADD     WWTGLI        WW$TAS            9 4
     C* Calcula indice
     C     WW$TAS        MULT      WWIPLA        INDICE           15 9
     C     INDICE        DIV(H)    36500         INDICE
     C* Calcula valor1
     C*
     C                   Z-ADD     1             I1                3 0
     C                   Z-ADD     *ZEROS        R1               18 9
     C                   Z-ADD     *ZEROS        R2               18 9
     C                   Z-ADD     *ZEROS        R3               18 9
     C                   Z-ADD     *ZEROS        FEC               8 0
     C     INDICE        ADD       1             INDIC1           15 9
     C* ... Exponencial a gamba ...
     C     I1            DOWLT     WWICUO
     C     I1            IFEQ      1
     C     INDIC1        MULT      INDIC1        R1
     C                   ELSE
     C     R1            MULT      INDIC1        R1
     C                   ENDIF
     C                   ADD       1             I1
     C                   ENDDO
     C     R1            SUB       1             R2
     C     R1            MULT      INDICE        R1
     C     R1            DIV       R2            R3
     C                   MULT(H)   WW$CAP        R3
     C                   Z-ADD     R3            VALOR1           15 2
     C* Calcula cuotas
     C                   Z-ADD     1             I1                3 0
     C                   Z-ADD     WW$CAP        WW$CAA           15 2
     C     I1            DOWLE     WWICUO
     C                   Z-ADD     *ZEROS        CAP              15 2
     C                   Z-ADD     *ZEROS        INT              15 2
     C*
     C     I1            IFEQ      1
     C     INDICE        MULT      WW$CAP        CAP
     C     VALOR1        SUB       CAP           CAP
     C     DIFDIA        MULT      WW$TAS        INT
     C                   MULT      WW$CAP        INT
     C                   DIV(H)    36500         INT
     C                   Z-ADD     WWF1VT        FEC
     C                   ENDIF
     C*
     C     I1            IFNE      1
     C     I1            ANDNE     WWICUO
     C     WWIPLA        MULT      WW$TAS        INT
     C                   MULT      WW$CAA        INT
     C                   DIV(H)    36500         INT
     C     VALOR1        SUB       INT           CAP
     C                   EXSR      CALFEC
     C                   ENDIF
     C*
     C     I1            IFEQ      WWICUO
     C                   Z-ADD     WW$CAA        CAP
     C     VALOR1        SUB       CAP           INT
     C                   EXSR      CALFEC
     C                   ENDIF
     C*
     C                   SUB       CAP           WW$CAA
     C                   Z-ADD     18            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              EXSR      PROC02
     c*
     C                   SELECT
     C     WWILCR        WHENEQ    80
     C*                  EXSR      PROC03
     C                   EXSR      PROC13
     C     WWILCR        WHENEQ    5
     C     WWILCR        OREQ      8
     C                   EXSR      PROC04
     C                   EXSR      PROC14
     C     WWILCR        WHENEQ    9
     C                   EXSR      PROC04
     C                   EXSR      PROC16
     C     WWILCR        WHENEQ    6
     C                   EXSR      PROC05
     C                   EXSR      PROC15
     C                   ENDSL
     C* Estos codigos figuran para todas las lineas por eso fuera del select
     C                   IF        I1 = 1
     C                   EXSR      PROC77
     C                   EXSR      PROC78
     C                   ENDIF
     c*
     C                   Z-ADD     @PJOBN        KGIJOB
     C                   Z-ADD     I1            KGICUO
     C                   Z-ADD     FEC           KGFVCU
     C                   Z-ADD     CAP           KG$CUC
     C                   Z-ADD     INT           KG$CUI
     C                   Z-ADD     WW$IVA        KG$DVI
     C                   Z-ADD     WW$COM        KG$SCA
     C                   ADD       INT           WW$CUI
     C                   ADD       WW$IVA        WW$DVI
     C                   ADD       WW$COM        WW$SCA
     C                   ADD       CAP           WW$TOT
     C                   ADD       INT           WW$TOT
     C                   ADD       WW$IVA        WW$TOT
     C                   ADD       WW$COM        WW$TOT
     C*
     C                   Z-ADD     CAP           WW$TO1           15 2
     C                   ADD       INT           WW$TO1
     C                   ADD       WW$IVA        WW$TO1
     C                   ADD       WW$COM        WW$TO1
     C*
     C     WW$TO1        IFGT      WW$VAL
     C                   Z-ADD     WW$TO1        WW$VAL
     C                   ENDIF
     C     FLAG          IFEQ      *ON
     C                   WRITE     REPRCU60
     C                   ENDIF
     C*
     C*                    SUB  CAP       WW$CAA
     C*
     C                   ADD       1             I1
     C                   ENDDO
     C*
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* CALFEC
     C*----------------------------------------------------------------*
     C     CALFEC        BEGSR
     C*
     C                   Z-ADD     *ZEROS        DIAS1            15 0
     C                   Z-ADD     FEC           PAFECH
     C                   MOVEL     'IN'          PACINV
     C                   CALL      'SBBAINFE'
     C                   PARM                    PAFECH            8 0
     C                   PARM                    PACINV            2
     C*
     C                   Z-ADD     *ZEROS        PADIAS           15 0
     C                   MOVEL     *BLANK        PADSEM            2
     C                   MOVEL     *BLANK        PADIRR            1
     C*
     C                   CALL      'SBBAFECH'
     C*
     C                   PARM                    PAFECH
     C                   PARM                    PADIAS
     C                   PARM                    PADSEM
     C                   PARM                    PADIRR
     C                   Z-ADD     PADIAS        DIAS1
     C*
     C                   ADD       30            DIAS1
     C                   Z-ADD     DIAS1         PADIAF
     C                   Z-ADD     *ZERO         PAFECF
     C                   EXSR      BUSFER
     C                   Z-ADD     PADIAF        DIAS1
     C*
     C                   MOVEL     *BLANK        PADSEM            2
     C                   MOVEL     *BLANK        PADIRR            1
     C                   Z-ADD     *ZEROS        PAFECH
     C*
     C                   CALL      'SBBAFECH'
     C                   PARM                    PAFECH
     C                   PARM                    DIAS1
     C                   PARM                    PADSEM
     C                   PARM                    PADIRR
     C                   MOVEL     'NI'          PACINV
     C                   CALL      'SBBAINFE'
     C                   PARM                    PAFECH            8 0
     C                   PARM                    PACINV            2
     C                   Z-ADD     PAFECH        FEC
     C*
     C                   ENDSR
      *--------------------------------------------------------------*
      * Subrutina BUSFER - Busqueda de día hábil                     *
      *--------------------------------------------------------------*
     C     BUSFER        BEGSR
      *
     C* Busca próximo dia habil
     C                   CALL      'SBBABFER'
     C                   PARM                    PAFECF            8 0
     C                   PARM                    PADIAF           15 0
     C                   PARM                    WWISUC
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC02 - IVA
     C*----------------------------------------------------------------*
     C     PROC02        BEGSR
     C                   Z-ADD     *ZEROS        WW$IVA
     C                   CALLP     PR0400S1(               +
     C                                           WWITDO  : +
     C                                           WWINDO  : +
     C                                           INT     : +
     C                                           WW$IVA  )
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC03 - COMISION
     C*----------------------------------------------------------------*
     C     PROC03        BEGSR
     C                   Z-ADD     *ZEROS        WW$COM
     C                   Z-ADD     70            WWIMPR
     C     WW$CAA        ADD       CAP           WW$CA1           15 2
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALLP     PR0400S2 (             +
     C                                           WWISUC : +
     C                                           WWIMPR:  +
     C                                           WWIMON:  +
     C                                           WW$CA1:  +
     C                                           WW$COM   )
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC13 - GASTOS ORIGINACION
     C*----------------------------------------------------------------*
     C     PROC13        BEGSR
     C                   Z-ADD     *ZEROS        WW$GAS
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   Z-ADD     *ZEROS        WW$NET
     C                   Z-ADD     44            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALLP     PR0400S2 (            +
     C                                           WWISUC: +
     C                                           WWIMPR: +
     C                                           WWIMON: +
     C                                           WW$CAP: +
     C                                           WW$GAS )
     C* IVA
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   CALLP     PR0400S1 (            +
     C                                           WWITDO: +
     C                                           WWINDO: +
     C                                           WW$GAS: +
     C                                           WW$IV1  )
     C     WW$CAP        SUB       WW$GAS        WW$NET
     C                   SUB       WW$IV1        WW$NET
     C                   Z-ADD     WW$GAS        GASORI           15 2
     C                   ADD       WW$IV1        GASORI
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC77 - Impuesto de Sellos Pciales Doc
     C*----------------------------------------------------------------*
     C     PROC77        BEGSR
     C                   Z-ADD     *ZEROS        WW$GAS
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   Z-ADD     *ZEROS        WW$NET
     C                   Z-ADD     77            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALLP     PR0400S2 (            +
     C                                           WWISUC: +
     C                                           WWIMPR: +
     C                                           WWIMON: +
     C                                           WW$CAP: +
     C                                           WW$GAS )
     C     WW$CAP        SUB       WW$GAS        WW$NET
     C                   Z-ADD     WW$GAS        TOCO77           15 2
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC78 - Impuesto de Sellos Pciales Sol
     C*----------------------------------------------------------------*
     C     PROC78        BEGSR
     C                   Z-ADD     *ZEROS        WW$GAS
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   Z-ADD     *ZEROS        WW$NET
     C                   Z-ADD     78            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALLP     PR0400S2 (            +
     C                                           WWISUC: +
     C                                           WWIMPR: +
     C                                           WWIMON: +
     C                                           WW$CAP: +
     C                                           WW$GAS )
     C     WW$CAP        SUB       WW$GAS        WW$NET
     C                   Z-ADD     WW$GAS        TOCO78           15 2
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC04 - COMISION
     C*----------------------------------------------------------------*
     C     PROC04        BEGSR
     C                   Z-ADD     *ZEROS        WW$COM
     C                   Z-ADD     75            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALLP     PR0400S3 (       +
     C                                           WWISUC: +
     C                                           WWIMPR: +
     C                                           WWIMON: +
     C                                           WW$CAP: +
     C                                           WW$COM )
     C                   ADD       WW$GAS        GASORI
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC14 - GASTOS ORIGINACION
     C*----------------------------------------------------------------*
     C     PROC14        BEGSR
     C                   Z-ADD     *ZEROS        WW$GAS
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   Z-ADD     *ZEROS        WW$NET
     C                   Z-ADD     46            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALL      'PR0400S2'
     C                   PARM                    WWISUC
     C                   PARM                    WWIMPR
     C                   PARM                    WWIMON
     C                   PARM                    WW$CAP
     C                   PARM                    WW$GAS
     C* IVA
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   CALLP     PR0400S1 (              +
     C                                           WWITDO :  +
     C                                           WWINDO :  +
     C                                           WW$GAS :  +
     C                                           WW$IV1    )
     C     WW$CAP        SUB       WW$GAS        WW$NET
     C                   SUB       WW$IV1        WW$NET
     C                   Z-ADD     WW$GAS        GASORI           15 2
     C                   ADD       WW$IV1        GASORI
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC16 - GASTOS ORIGINACION - linea 9
     C*----------------------------------------------------------------*
     C     PROC16        BEGSR
     C                   Z-ADD     *ZEROS        WW$GAS
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   Z-ADD     *ZEROS        WW$NET
     C                   Z-ADD     60            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALL      'PR0400S2'
     C                   PARM                    WWISUC
     C                   PARM                    WWIMPR
     C                   PARM                    WWIMON
     C                   PARM                    WW$CAP
     C                   PARM                    WW$GAS
     C* IVA
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   CALLP     PR0400S1 (              +
     C                                           WWITDO :  +
     C                                           WWINDO :  +
     C                                           WW$GAS :  +
     C                                           WW$IV1    )
     C     WW$CAP        SUB       WW$GAS        WW$NET
     C                   SUB       WW$IV1        WW$NET
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC05 - COMISION
     C*----------------------------------------------------------------*
     C     PROC05        BEGSR
     C                   Z-ADD     *ZEROS        WW$COM
     C                   Z-ADD     76            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALLP     PR0400S3 (            +
     C                                           WWISUC: +
     C                                           WWIMPR: +
     C                                           WWIMON: +
     C                                           WW$CAP: +
     C                                           WW$COM  )
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* PROC15 - GASTOS ORIGINACION
     C*----------------------------------------------------------------*
     C     PROC15        BEGSR
     C                   Z-ADD     *ZEROS        WW$GAS
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   Z-ADD     *ZEROS        WW$NET
     C                   Z-ADD     46            WWIMPR
     C     WKEY02        CHAIN     PRMLIN02                           66
     C  N66              CALLP     PR0400S2 (            +
     C                                           WWISUC: +
     C                                           WWIMPR: +
     C                                           WWIMON: +
     C                                           WW$CAP: +
     C                                           WW$GAS )
     C* IVA
     C                   Z-ADD     *ZEROS        WW$IV1
     C                   CALLP     PR0400S1  (            +
     C                                           WWITDO:  +
     C                                           WWINDO:  +
     C                                           WW$GAS:  +
     C                                           WW$IV1   )
     C     WW$CAP        SUB       WW$GAS        WW$NET
     C                   SUB       WW$IV1        WW$NET
     C                   Z-ADD     WW$GAS        GASORI           15 2
     C                   ADD       WW$IV1        GASORI
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* TASA   - TASA
     C*----------------------------------------------------------------*
     C     TASA          BEGSR
     C* Situacion
     C                   Z-ADD     1             WWISIT            2 0
     C     WWINDO        CHAIN     REBAPFIS                           99
     C     *IN99         IFEQ      *OFF
     C                   Z-ADD     A#ICUI        CUIT             11 0
     C     CUIT          CHAIN     REBC4305                           99
     C     *IN99         IFEQ      *OFF
     C                   Z-ADD     B5ISIT        WWISIT
     C     WWISIT        IFEQ      21
     C                   Z-ADD     2             WWISIT
     C                   ENDIF
     C                   ENDIF
     C                   ENDIF
     C* SCORING-EMPRESA-LINEA
     C     WKEY33        KLIST
     C                   KFLD                    WWIEMP
     C                   KFLD                    WWILCR
     C     WKEY33        CHAIN     BASCEL                             56
     C     *IN56         IFEQ      *OFF
     C     ELIVSO        IFEQ      'N'
     C                   Z-ADD     1             WWISIT
     C                   ENDIF
     C                   ENDIF
     C* Tabla Tasa de Empresas p/SCORING
     C     WKEY03        KLIST
     C                   KFLD                    WWIEMP
     C                   KFLD                    WWILCR
     C                   KFLD                    WWISIT
     C                   Z-ADD     *ZEROS        WWITAS            2 0
     C     WKEY03        CHAIN     BAITAS                             99
     C     *IN99         DOWEQ     *OFF
     C     WWICUO        IFGE      ASQCCL
     C     WWICUO        ANDLE     ASQCCE
     C                   Z-ADD     ASITAS        WWITAS            2 0
     C                   ENDIF
     C     WKEY03        READE     BAITAS                                 99
     C                   ENDDO
     C* Tipo de tabla tasa
     C                   Z-ADD     *ZEROS        WWTGLI            8 4
     C     WWITAS        CHAIN     PRICTA                             99
     C     *IN99         IFEQ      *OFF
     C                   Z-ADD     HZTGLI        WWTGLI
     C                   ENDIF
     C* Calculos
     C                   Z-ADD     *ZEROS        TEA
     C                   Z-ADD     *ZEROS        X
     C                   Z-ADD     WWIPLA        Y
     C     WWTGLI        DIV       100           X
     C                   CALL      'SBPRCTEA'
     C                   PARM                    X                 8 4
     C                   PARM                    Y                 4 0
     C                   PARM                    TEA              10 6
     C     TEA           MULT      100           WWTGLI
     C*
     C                   Z-ADD     WWTGLI        WWTEAP            8 4
     C                   Z-ADD     *ZEROS        WWTGLI
     C                   CALL      'SBCTNTEA'
     C                   PARM                    WWTEAP
     C                   PARM                    WWIPLA
     C                   PARM                    WWTGLI
     C*
     C                   ENDSR
     C*----------------------------------------------------------------*
     C* OBTFEI
     C*----------------------------------------------------------------*
     C     OBTFEI        BEGSR
     C* Fecha de 1 Vto
     C                   Z-ADD     WWF1VT        PAFECH
     C                   MOVE      'IN'          PACINV            2
     C                   CALL      'SBBAINFE'
     C                   PARM                    PAFECH
     C                   PARM                    PACINV
     C                   Z-ADD     *ZEROS        PADIAS
     C                   MOVEL     *BLANK        PADSEM
     C                   MOVEL     *BLANK        PADIRR
     C                   CALL      'SBBAFECH'
     C                   PARM                    PAFECH
     C                   PARM                    PADIAS
     C                   PARM                    PADSEM
     C                   PARM                    PADIRR
     C                   Z-ADD     PADIAS        DIAS2            15 0
     C                   SUB       29            DIAS2
     C                   Z-ADD     *ZEROS        PAFECH
     C* Busca próximo dia habil
     C                   CALL      'SBBABFE2'
     C                   PARM                    PAFECH            8 0
     C                   PARM                    DIAS2
     C                   PARM                    WWISUC
     C                   MOVE      'NI'          PACINV            2
     C                   CALL      'SBBAINFE'
     C                   PARM                    PAFECH
     C                   PARM                    PACINV
     C                   Z-ADD     PAFECH        WWFALT            8 0
     C*
     C                   ENDSR
     C*-------------------------------------------------------------------------
     P PR0400S1        B
     D PR0400S1        PI
     D  WWITDO                        2  0
     D  WWINDO                       15  0
     D  WW$CAP                       15  2
     D  WW$IMP                       15  2
      *   .......Busca datos sobre a quien aplicar el IVA
     C     @PJOBN        CHAIN     @CPIUSD                            79
     C                   EXSR      SRDEFN
      *
      *   .......Busca categoria y alicuota de iva por titular operac.
     C                   EXSR      BUSALI
      *
      *   .......Busca total a aplicar en IVA
     C                   EXSR      BUSTOT
      *
      *   .......Calcula IVA a generar
     C     WW$IVA        IFNE      *ZERO
     C                   EXSR      GENIVA
     C  N79              Z-ADD     WW$IMP        @C$IMP
     C  N79              UPDATE    @CPIUSRR
     C                   END
      *
     C                   MOVE      *ON           *INLR
     C                   RETURN
      *----------------------------------------------------------------*
      * BUSALI - Lee la cuenta y busca titulares
      *----------------------------------------------------------------*
     C     BUSALI        BEGSR
      *
     C                   Z-ADD     *ZERO         WWICIV
      *
     C     @KEY01        CHAIN     RBAPFIS                            50
     C     *IN50         IFEQ      *OFF
     C     A#ICIV        IFEQ      1
     C     WWIDFO        ANDEQ     40
     C                   Z-ADD     3             WWICIV
     C                   ELSE
     C                   Z-ADD     A#ICIV        WWICIV
     C                   ENDIF
     C                   END
      *
      *   .......Si no encuentra catergoría toma consumidor final
     C     WWICIV        IFEQ      *ZERO
     C                   Z-ADD     3             WWICIV
     C                   ENDIF
      *
     C*   .......Busca alicuotas de IVA a aplicar según categoria titu.
     C     KEIVA         KLIST
     C                   KFLD                    WWICIV
     C                   KFLD                    WWIDFO
     C     KEIVA         CHAIN     PREIVA                             80
     C     *IN80         IFEQ      *ON
     C     WWICIV        CHAIN     PRPIVA                             80
     C     *IN80         IFEQ      *ON
     C                   CLEAR                   REPRPIVA
     C                   ENDIF
     C                   ELSE
     C                   Z-ADD     QYICIN        NFICIN
     C                   Z-ADD     QYPIIN        NFPIIN
     C                   Z-ADD     QY$IMI        NF$IMI
     C                   Z-ADD     QYICNI        NFICNI
     C                   Z-ADD     QYPINI        NFPINI
     C                   Z-ADD     QY$IMN        NF$IMN
     C                   Z-ADD     QYIVRE        NFIVRE
     C                   Z-ADD     QYPIRE        NFPIRE
     C                   Z-ADD     QY$IMR        NF$IMR
     C                   Z-ADD     QYICBO        NFICBO
     C                   Z-ADD     QYPIIB        NFPIIB
     C                   Z-ADD     QYICNB        NFICNB
     C                   Z-ADD     QYPINB        NFPINB
     C                   Z-ADD     QYIVRB        NFIVRB
     C                   Z-ADD     QYPIRB        NFPIRB
     C                   ENDIF
      *
     C                   ENDSR
      *----------------------------------------------------------------*
      * BUSTOT - Calcula totales de IVA a cobrar
      *----------------------------------------------------------------*
     C     BUSTOT        BEGSR
      *
     C                   Z-ADD     *ZERO         WW$IMP
     C                   Z-ADD     WW$CAP        WW$IVA
     C*                    ADD  @C$MON    WW$IVA
      *
     C                   ENDSR
      *-------------------------------------------------------------.
      * GENIVA - Genera IVA sobre el total de movimientos
      *-------------------------------------------------------------'
     C     GENIVA        BEGSR
      *
      *   .......Genera IVA inscrípto
     C     NFPIIN        IFNE      *ZERO
     C     WW$IVA        ANDGT     NF$IMI
     C     WW$IVA        MULT(H)   NFPIIN        WK$IMP
     C                   DIV(H)    100           WK$IMP
     C     NFPIIB        IFNE      *ZERO
     C     WK$IMP        ANDNE     *ZERO
     C     @CFE01        ANDGE     19960401
     C     WK$IMP        MULT(H)   NFPIIB        WW$IM1
     C                   DIV(H)    100           WW$IM1
     C                   SUB       WW$IM1        WK$IMP
     C                   END
     C     WK$IMP        IFNE      *ZERO
     C                   ADD       WK$IMP        WW$IMP
     C                   END
     C                   END
      *
     C*   .......Genera IVA no inscrípto
     C     NFPINI        IFNE      *ZERO
     C     WW$IVA        ANDGT     NF$IMN
     C     WW$IVA        MULT(H)   NFPINI        WK$IMP
     C                   DIV(H)    100           WK$IMP
     C     NFPINB        IFNE      *ZERO
     C     WK$IMP        ANDNE     *ZERO
     C     @CFE01        ANDGE     19960401
     C     WK$IMP        MULT(H)   NFPINB        WW$IM1
     C                   DIV(H)    100           WW$IM1
     C                   SUB       WW$IM1        WK$IMP
     C                   END
     C     WK$IMP        IFNE      *ZERO
     C                   ADD       WK$IMP        WW$IMP
     C                   END
     C                   END
      *
     C*   .......Genera retención de IVA
     C     NFPIRE        IFNE      *ZERO
     C     WW$IVA        ANDGT     NF$IMR
     C     WW$IVA        MULT(H)   NFPIRE        WK$IMP
     C                   DIV(H)    100           WK$IMP
     C     NFPIRB        IFNE      *ZERO
     C     WK$IMP        ANDNE     *ZERO
     C     @CFE01        ANDGE     19960401
     C     WK$IMP        MULT(H)   NFPIRB        WW$IM1
     C                   DIV(H)    100           WW$IM1
     C                   SUB       WW$IM1        WK$IMP
     C                   END
     C     WK$IMP        IFNE      *ZERO
     C                   ADD       WK$IMP        WW$IMP
     C                   END
     C                   END
      *
     C     ENGIVA        ENDSR
      *-------------------------------------------------------------.
      * SRDEFN -
      *-------------------------------------------------------------'
     C     SRDEFN        BEGSR
      *
     C     @KEY01        KLIST
     C                   KFLD                    WWITDO
     C                   KFLD                    WWINDO
      *
     C     *LIKE         DEFINE    NFICIV        WWICIV
     C     *LIKE         DEFINE    @C$IMP        WK$IMP
     C     *LIKE         DEFINE    @C$IMP        WW$IVA
     C     *LIKE         DEFINE    @C$IMP        WW$IM1
     C     *LIKE         DEFINE    @C$IMP        WW$IMP
      *
     C                   Z-ADD     *ZEROS        WWICIV            3 0
     C                   Z-ADD     40            WWIDFO            3 0
     C                   ENDSR
     P PR0400S1        E
     C*-------------------------------------------------------------------------
     P PR0400S2        B
     D PR0400S2        PI
     D WWISUC                         5  0
     D WWIMPR                         3  0
     D WWIMON                         9  0
     D WW$CAA                        15  2
     D WW$IMP                        15  2
     C     @PJOBN        CHAIN     @CPIUSD                            79
      *
     C                   EXSR      INICIO
      *
      * Determina si se trata de un porcentaje o un importe fijo
     C     WKEY01        SETLL     PRPARM
     C                   READ      PRPARM                                 80
      *
     C     *IN80         IFNE      *OFF
     C     MFISUC        ORNE      WWISUC
     C     MFIMPR        ORNE      WWIMPR
     C     MFIMON        ORNE      WWIMON
     C                   Z-ADD     99999         WWISUC
     C     WKEY01        SETLL     PRPARM
     C                   READ      PRPARM                                 80
     C                   END
      *
     C     *IN80         IFEQ      *OFF
     C     MFISUC        ANDEQ     WWISUC
     C     MFIMPR        ANDEQ     WWIMPR
     C     MFIMON        ANDEQ     WWIMON
      *                                                           |
     C     MF$POS        COMP      *ZERO                                  21
     C     MF$FIJ        COMP      *ZERO                                  22
     C   22              EXSR      PSELLA
     C   21              Z-ADD     MF$FIJ        WW$IMP
     C  N79              Z-ADD     WW$IMP        @C$IMP
     C  N79              UPDATE    @CPIUSRR
     C                   END
      *
      * Finaliza programa
     C     FINAL         TAG
     C                   MOVE      *ON           *INLR
     C                   RETURN
     C*----------------------------------------------------------------
     C* INICIO - Lee CPI y define Klist de acceso.
     C*----------------------------------------------------------------
     C     INICIO        BEGSR
      *
     C     WWIMPR        CHAIN     PRCODI                             80
      *
     C     *LIKE         DEFINE    @C$IMP        WW$IMP
     C     *LIKE         DEFINE    @CISUC        WWISUC
     C     *LIKE         DEFINE    @C$IMP        WC$IMP
      *
     C     WKEY01        KLIST
     C                   KFLD                    WWISUC
     C                   KFLD                    WWIMPR
     C                   KFLD                    WWIMON
      *
     C                   ENDSR
     C*----------------------------------------------------------------
     C* PSELLA - Calcula importe Comisión Reembolso
     C*----------------------------------------------------------------
     C     PSELLA        BEGSR
      *
     C     WW$CAA        MULT      MF$POS        WW$IMP
     C     WWIMPR        IFEQ      70
     C                   DIV       1000          WW$IMP
     C                   ELSE
     C                   DIV       100           WW$IMP
     C                   ENDIF
      *
     C                   ENDSR
     C*----------------------------------------------------------------
     P                 E
     C*-------------------------------------------------------------------------
     P PR0400S3        B
     D PR0400S3        PI
     D WWISUC                         5  0
     D WWIMPR                         3  0
     D WWIMON                         9  0
     D WW$CAA                        15  2
     D WW$IMP                        15  2
     C     @PJOBN        CHAIN     @CPIUSD                            79
      *
     C                   EXSR      INICIO
      *
      * Determina si se trata de un porcentaje o un importe fijo
     C     WKEY01        SETLL     PRPARM
     C                   READ      PRPARM                                 80
      *
     C     *IN80         IFNE      *OFF
     C     MFISUC        ORNE      WWISUC
     C     MFIMPR        ORNE      WWIMPR
     C     MFIMON        ORNE      WWIMON
     C                   Z-ADD     99999         WWISUC
     C     WKEY01        SETLL     PRPARM
     C                   READ      PRPARM                                 80
     C                   END
      *
     C     *IN80         IFEQ      *OFF
     C     MFISUC        ANDEQ     WWISUC
     C     MFIMPR        ANDEQ     WWIMPR
     C     MFIMON        ANDEQ     WWIMON
      *                                                           |
     C     MF$POS        COMP      *ZERO                                  21
     C     MF$FIJ        COMP      *ZERO                                  22
     C   22              EXSR      PSELLA
     C   21              Z-ADD     MF$FIJ        WW$IMP
     C  N79              Z-ADD     WW$IMP        @C$IMP
     C  N79              UPDATE    @CPIUSRR
     C                   END
      *
      * Finaliza programa
     C     FINAL         TAG
     C                   MOVE      *ON           *INLR
     C                   RETURN
     C*----------------------------------------------------------------
     C* INICIO - Lee CPI y define Klist de acceso.
     C*----------------------------------------------------------------
     C     INICIO        BEGSR
      *
     C     WWIMPR        CHAIN     PRCODI                             80
      *
     C     *LIKE         DEFINE    @C$IMP        WW$IMP
     C     *LIKE         DEFINE    @CISUC        WWISUC
     C     *LIKE         DEFINE    @C$IMP        WC$IMP
      *
     C     WKEY01        KLIST
     C                   KFLD                    WWISUC
     C                   KFLD                    WWIMPR
     C                   KFLD                    WWIMON
      *
     C                   ENDSR
     C*----------------------------------------------------------------
     C* PSELLA - Calcula importe Comisión Reembolso
     C*----------------------------------------------------------------
     C     PSELLA        BEGSR
      *
     C     WW$CAA        MULT      MF$POS        WW$IMP
     C                   DIV       100           WW$IMP
      *
     C                   ENDSR
     P                 E
