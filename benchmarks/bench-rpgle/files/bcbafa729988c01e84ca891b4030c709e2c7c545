*SRCMBRTXT:Link-Ultimos 10 Movimientos de CC      
     H
     FCCCTCT09  IP   E           K DISK
     FCCMOCT01  IF   E           K DISK
     FCCMHCT06  IF   E           K DISK
     FCCCODI    IF   E           K DISK
     FSGSYSV    IF   E             DISK
     FUMOV      O    F  300        DISK
     D DSMOV1          DS
     D  V                      1    250
     D                                     DIM(10)
     D  MOVSTR                 1    250
     D DSMOV2          DS
     D  MOVENT                 1     25
     D  MOVFEC                 1      6  0
     D  MOVDSC                 7     16
     D  MOVSIG                17     17
     D  MOVIMP                18     25  0
     D CTADS           DS
     D  CTALNK                 1     18
     D  LINSUC                 1      4  0
     D  LINGRP                 5      6
     D  LINFIL                 7      9  0
     D  LINCAH                10     16  0
     C*-------------------------------------------------------------------------
     D up              C                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     D lo              C                   'abcdefghijklmnopqrstuvwxyz'
     D Symbols         C                   '|°¬!"#$%&/()=?\¡¿*+~[]{}_-;,:.<>'
     D SymBlanks       C                   '                                '
     D Acentos         C                   'ñÑáéíóúäëïöüãõàèìòùâêîôû@'
     D AceBlanks       C                   'nNAEIOUAEIOUAOAEIOUAEIOU '
     D Apos            C                   ''''
     D APosBlank       C                   ' '
     C*-------------------------------------------------------------------------
     IRECCCTCT      01
     I                                          BMIMON        L1
     C   L1              EXSR      WRTHED
     C   01              EXSR      WRTMOV
     CL1                 EXSR      WRTTRL
     C*-------------------------------------------------------------------------
     C* *INZSR: Inicialización
     C*-------------------------------------------------------------------------
     C     *INZSR        BEGSR
     C*
     C     *ENTRY        PLIST
     C                   PARM                    RUNMDE            1
     C*
     C     WKEY01        KLIST
     C                   KFLD                    BMISUC
     C                   KFLD                    BMICCC
     C     WKEY02        KLIST
     C                   KFLD                    BMISUC
     C                   KFLD                    BMIMON
     C                   KFLD                    BMICCC
     C*
     C     1             CHAIN     SGSYSV                             25
     C                   Z-ADD     AASFEI        FECCOR            8 0
     C                   MOVE      AASFEI        FEEXT             6 0
     C*
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C* WRTHED: Escritura Registro Cabecera
     C*-------------------------------------------------------------------------
     C     WRTHED        BEGSR
     C*
     C                   SELECT
     C     BMIMON        WHENEQ    01
     C                   MOVE      '01'          LINTC             2
     C     BMIMON        WHENEQ    02
     C                   MOVE      '07'          LINTC             2
     C                   OTHER
     C                   MOVE      '00'          LINTC             2
     C                   ENDSL
     C*
     C                   SETOFF                                       99
     C*
     C                   Z-ADD     2             CNTREG            8 0
     C*
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C* WRTMOV: Escribir Movimientos
     C*-------------------------------------------------------------------------
     C     WRTMOV        BEGSR
     C*
     C     LINTC         IFNE      '00'
     C     BMIUCA        ANDEQ     'S'
     C     BMFBAJ        ANDEQ     *ZERO
     C     BMIBCC        ANDEQ     *ZERO
     C     BMIGRC        ANDNE     'IN'
     C*
     C                   Z-ADD     *ZERO         X                 2 0
     C                   CLEAR                   V
     C*
     C     WKEY01        CHAIN     RECCMOCT                           25
     C     RUNMDE        IFNE      'F'
     C     *IN25         ANDEQ     *ON
     C                   GOTO      SINCAM
     C                   ENDIF
     C*
     C     WKEY02        SETGT     RECCMHCC
     C     WKEY02        READPE    RECCMHCC                               25
     C     *IN25         DOWEQ     *OFF
     C     X             ANDLT     10
     C     CEIASC        IFEQ      *ZERO
     C     CEFASI        IFLE      FECCOR
     C                   ADD       1             X
     C                   MOVE      CEFING        MOVFEC
     C                   MOVE      CE$IMP        MOVIMP
     C     CEIMCC        CHAIN     RECCCODI                           25
     C                   MOVEL(P)  BLNCOD        MOVDSC
     C                   ExSr      FixDsc
     C     BLITMO        IFEQ      1
     C                   MOVE      '-'           MOVSIG
     C                   ELSE
     C                   MOVE      '+'           MOVSIG
     C                   ENDIF
     C                   MOVE      MOVENT        V(X)
     C                   ENDIF
     C                   ENDIF
     C     WKEY02        READPE    RECCMHCC                               25
     C                   ENDDO
     C*
     C  N99              EXCEPT    HEDREC
     C  N99              SETON                                        99
     C     X             IFGT      *ZERO
     C                   ADD       1             CNTREG
     C     BM$SOP        IFGE      *ZERO
     C                   MOVE      '+'           LINSIG            1
     C                   Z-ADD     BM$SOP        LINSAL            8 2
     C                   ELSE
     C                   MOVE      '-'           LINSIG
     C     -1            MULT      BM$SOP        LINSAL            8 2
     C                   ENDIF
     C                   Z-ADD     BMISUC        LINSUC
     C                   MOVE      BMIGRC        LINGRP
     C                   Z-ADD     BMICCC        LINCAH
     C                   Z-ADD     *ZEROS        LINFIL
     C                   EXCEPT    DETREC
     C                   ENDIF
     C*
     C                   ENDIF
     C*
     C     SINCAM        ENDSR
     C*-------------------------------------------------------------------------
     C* FixDsc: Elimina caracteres "raros" de descripción
     C*-------------------------------------------------------------------------
     C     FixDsc        BegSr
     C*
     C                   Eval      MOVDSC = %XLATE(Symbols:SymBlanks:MOVDSC)
     C                   Eval      MOVDSC = %XLATE(Acentos:AceBlanks:MOVDSC)
     C                   Eval      MOVDSC = %XLATE(Apos:AposBlank:MOVDSC)
     C                   Eval      MOVDSC = %XLATE(lo:up:MOVDSC)
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C* WRTTRL: Escribir registro Final
     C*-------------------------------------------------------------------------
     C     WRTTRL        BEGSR
     C*
     C     LINTC         IFNE      '00'
     C     *IN99         ANDNE     *OFF
     C                   EXCEPT    TRLREC
     C                   ENDIF
     C*
     C                   ENDSR
     OUMOV      E            HEDREC
     O                                           13 'HRMOVIMIENTOS'
     O                                           17 '0309'
     O                       FEEXT               23
     O                       LINTC               25
     OUMOV      E            DETREC
     O                       CTALNK              18
     O                       LINSIG              19
     O                       LINSAL              27
     O                       MOVSTR             277
     OUMOV      E            TRLREC
     O                                           13 'TRMOVIMIENTOS'
     O                       CNTREG              21
