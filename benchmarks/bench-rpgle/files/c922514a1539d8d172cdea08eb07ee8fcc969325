*SRCMBRTXT:Movs. de Ctas a Excell                 
     F@CPISYS   UF   E           K DISK
     F@CPIUSD   UF   E           K DISK
     D*----------------------------------------------------------------*
     D*----------------------------------------------------------------*
     D                 DS
     D  @ZFNKY                 1     24
     D  @FN                    1     24
     D                                     DIM(24)
     D*----------------------------------------------------------------*
     D               ESDS                  EXTNAME(@PSDS)
     D*----------------------------------------------------------------*
     D LDA           E DS                  EXTNAME(LDA)
     I*----------------------------------------------------------------*
     D QryStr          S           2048
     D Where           S           2048
     D*----------------------------------------------------------------*
     DERRDS            DS
     D ERRTXT                  1    255
     D WWNCU1                  1     55
     D WWNCU2                 56    110
     D WWNCU3                111    165
     D WWNCU4                166    220
     D WWNCB1                221    275
     D WWNCB2                276    330
     D WWNCB3                331    385
     D WWNCB4                386    440

     D CONDCNT         S              3S 0 INZ(0)
     D ERROR           S               N
     D*----------------------------------------------------------------*
     C                   EXSR      GETPAR
     C                   DOW       @FN(03) = *OFF AND  @FN(12) = *OFF
     C                   MOVE      @CISUB        ISUB              2
     C                   EXSR      BLDQRY
     C                   EXSR      VALQRY
     C                   IF        ERROR
     C                   EXSR      DSPERR
     C                   ELSE
     C                   EXSR      OPNXLS
     C                   ENDIF
     C                   EXSR      GETPAR
     C                   ENDDO
     C                   SETON                                        LR
     C*-------------------------------------------------------------------------
     C* GETPAR : OBTENER PARAMETROS
     C*-------------------------------------------------------------------------
     C     GETPAR        BEGSR
     C                   CALL      'ACGD00RS'
     C     @PJOBN        CHAIN(N)  @CPIUSRR                           99
     C     @PJOBN        CHAIN(N)  @CPISYS                            99
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C* OPNXLS : ABRIR PLANILLA DE EXCEL
     C*-------------------------------------------------------------------------
     C     OPNXLS        BEGSR
     C                   EXSR      ASKPWD
     C                   CALL      'ACGD00C4'
     C                   PARM                    QRYSTR
     C                   PARM                    @CISUB
     C                   PARM                    @CNYAP
     C     @PJOBN        CHAIN     @CPIUSRR                           99
     C                   MOVE      ISUB          @CISUB
     C                   UPDATE    @CPIUSRR
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C* ASKPWD : PREGUNTAR CONTRASEÑA
     C*-------------------------------------------------------------------------
     C     ASKPWD        BEGSR
     C                   CALL      'SPTQ01RS'
     C     @PJOBN        CHAIN(N)  @CPIUSRR                           99
     C     @PJOBN        CHAIN(N)  @CPISYS                            99
     C                   IF        @FN(03) = *ON  or @FN(12) = *ON
     C                   SETON                                        LR
     C                   RETURN
     C                   ENDIF
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C* BLDQRY : BUILD QUERY
     C*-------------------------------------------------------------------------
     C     BLDQRY        BEGSR
     C*
     C                   EVAL      where=''
     C                   EVAL      CONDCNT=0
     C*
     C                   IF        ISUB='CC'
     C                   EVAL      QRYSTR='SELECT                      '+
     C                             ' CEISUC SUCURSAL       ,           '+
     C                             ' CEICCC CTACTE         ,           '+
     C                             ' OSNCCL NOMBRE         ,           '+
     C                             ' CEFING FECINGRESO     ,           '+
     C                             ' CEFASI FECHAASTO      ,           '+
     C                             ' CEIMCC CODMOVTO       ,           '+
     C                             ' BLACOD DSCMOVTO       ,           '+
     C                             ' CEITMO DB_1_CR_2      ,           '+
     C                             ' CEICAJ CAJA           ,           '+
     C                             ' CEISAL SUCALTA        ,           '+
     C                             ' CEICHE NROCBTE        ,           '+
     C                             ' CEIASC CTRASTO        ,           '+
     C                             ' CE$IMP IMPORTE                    '+
     C                             ' FROM SDBFIL02/CCMHCT              '+
     C                             ' LEFT JOIN BAICCL ON               '+
     C                             ' CEISUC=OSISUC AND CEICCC=OSICCL   '+
     C                             ' LEFT JOIN CCCODI ON CEIMCC=BLIMCC '+
     C                             ' WHERE CEISUC=CEISUC               '
     C* Fecha Asto Desde....
     C                   IF        @CFDES <>  0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CFDES        CHFDES            8
     C                   Eval      where =%TRIM(where )+
     C                             ' AND CEFASI>='+CHFDES
     C                   ENDIF
     C* Fecha Asto HASTA....
     C                   IF        @CFHAS <>  0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CFHAS        CHFHAS            8
     C                   Eval      where =%TRIM(where )+
     C                             ' AND CEFASI<='+CHFHAS
     C                   ENDIF
     C* Número de sucursal .
     C                   IF        @CISUC <> 0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CISUC        CHISUC            5
     C                   Eval      where =%TRIM(where )+
     C                             ' AND CEISUC='+CHISUC
     C                   ENDIF
     C* Cód Mov
     C                   IF        @CIMCA <>  0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CIMCA        CHIMPR            3
     C                   Eval      where =%TRIM(where )+
     C                             ' AND CEIMCC='+CHIMPR
     C                   ENDIF
     C* Sucursal de Alta....
     C                   IF        @CISAL <>  0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CISAL        CHISAL            5
     C                   Eval      where =%TRIM(where )+
     C                             ' AND CEISAL ='+CHISAL
     C                   ENDIF
     C* Número de CAJA     .
     C                   IF        @CICAJ <> 0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CICAJ        CHICAJ            5
     C                   Eval      where =%TRIM(where )+
     C                             ' AND CEICAJ='+CHICAJ
     C                   ENDIF
     C* Número de CUENTA   .
     C                   IF        @CICAH <> 0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CICAH        CHICCC           11
     C                   Eval      where =%TRIM(where )+
     C                             ' AND CEICCC='+CHICCC
     C                   ENDIF
     C                   ELSE
     C                   EVAL      QRYSTR='SELECT                       '+
     C                             ' GDISUC SUCURSAL       ,           '+
     C                             ' GDICAH CAJAAHORRO     ,           '+
     C                             ' OSNCCL NOMBRE         ,           '+
     C                             ' GDFALT FECINGRESO     ,           '+
     C                             ' GDFASI FECHAASTO      ,           '+
     C                             ' GDIMCA CODMOVTO       ,           '+
     C                             ' FXACOD DSCMOVTO       ,           '+
     C                             ' GDITMO DB_1_CR_2      ,           '+
     C                             ' GDICAJ CAJA           ,           '+
     C                             ' GDISAL SUCALTA        ,           '+
     C                             ' GDICHE NROCBTE        ,           '+
     C                             ' GDIASC CTRASTO        ,           '+
     C                             ' GD$IMP IMPORTE                    '+
     C                             ' FROM ACMOVH LEFT JOIN BAICCL       '+
     C                             ' ON GDISUC=OSISUC AND GDICAH=OSICCL '+
     C                             ' LEFT JOIN ACCODI ON GDIMCA=FXIMCA  '+
     C                             ' WHERE GDISUC=GDISUC                '
     C* Fecha Asto Desde....
     C                   IF        @CFDES <>  0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CFDES        CHFDES            8
     C                   Eval      where =%TRIM(where )+
     C                             ' AND GDFASI>='+CHFDES
     C                   ENDIF
     C* Fecha Asto HASTA....
     C                   IF        @CFHAS <>  0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CFHAS        CHFHAS            8
     C                   Eval      where =%TRIM(where )+
     C                             ' AND GDFASI<='+CHFHAS
     C                   ENDIF
     C* Número de sucursal .
     C                   IF        @CISUC <> 0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CISUC        CHISUC            5
     C                   Eval      where =%TRIM(where )+
     C                             ' AND GDISUC='+CHISUC
     C                   ENDIF
     C* Cód Mov
     C                   IF        @CIMCA <>  0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CIMCA        CHIMPR            3
     C                   Eval      where =%TRIM(where )+
     C                             ' AND GDIMCA='+CHIMPR
     C                   ENDIF
     C* Sucursal de Alta....
     C                   IF        @CISAL <>  0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CISAL        CHISAL            5
     C                   Eval      where =%TRIM(where )+
     C                             ' AND GDISAL ='+CHISAL
     C                   ENDIF
     C* Número de CAJA     .
     C                   IF        @CICAJ <> 0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CICAJ        CHICAJ            5
     C                   Eval      where =%TRIM(where )+
     C                             ' AND GDICAJ='+CHICAJ
     C                   ENDIF
     C* Número de CUENTA   .
     C                   IF        @CICAH <> 0
     C                   ADD       1             CONDCNT
     C                   MOVE      @CICAH        CHICAH           11
     C                   Eval      where =%TRIM(where )+
     C                             ' AND GDICAH='+CHICAH
     C                   ENDIF
     C                   ENDIF
     c                   Eval      QryStr=%trim(qrystr)+' '+where
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C* VALQRY: Validar Parametros
     C*-------------------------------------------------------------------------
     C     VALQRY        BEGSR
     C
     C*
     C                   MOVE      @CFDES        FECHA             8 0
     C                   CALL      'SBBAINFE'
     C                   PARM                    FECHA
     C                   PARM      'IN'          EDTMDE            2
     C*
     C                   Z-ADD     *ZERO         PADIAS           15 0
     C                   MOVE      *ZERO         PAIERR            1
     C                   CALL      'SBBACFEC'
     C                   PARM                    FECHA
     C                   PARM                    PADIAS
     C                   PARM                    PAIERR
     C                   MOVE      PADIAS        PADESD           15 0
     C*
     C                   MOVE      @CFHAS        FECHA             8 0
     C                   CALL      'SBBAINFE'
     C                   PARM                    FECHA
     C                   PARM      'IN'          EDTMDE            2
     C                   Z-ADD     *ZERO         PADIAS
     C                   MOVE      *ZERO         PAIERR
     C                   CALL      'SBBACFEC'
     C                   PARM                    FECHA
     C                   PARM                    PADIAS
     C                   PARM                    PAIERR
     C                   MOVE      PADIAS        PAHAST           15 0
     C*
     C     PAHAST        SUB       PADESD        DIAS             15 0
     C                   Eval      ERROR=*OFF
     C                   Select
     C                   When      @CFDES = *ZERO or @CFHAS = *ZERO
     C                   Eval      ERRTXT='Debe ingresarse fecha desde y fe'+
     C                             'cha hasta'
     C                   Eval      ERROR=*ON
     C                   When      ISUB='AC' AND DIAS > 10 AND CONDCNT < 3
     C                   Eval      ERRTXT='Debe ingresarse por lo menos 1 c'+
     C                             'riterio de filtrado ademas de las fechas'
     C                   Eval      ERROR=*ON
     C                   When      ISUB='AC' AND DIAS > 40 AND CONDCNT < 3
     C                   Eval      ERRTXT='Debe ingresarse por lo menos 1 c'+
     C                             'riterio de filtrado ademas de las fechas'
     C                   Eval      ERROR=*ON
     c                   EndSl
     C                   ENDSR
     C*-------------------------------------------------------------------------
     C* DSPERR: Mostrar Mensaje de Error
     C*-------------------------------------------------------------------------
     C     DSPERR        BEGSR
     C                   CALL      'BAER00RS'
     C                   PARM                    WWNCU1
     C                   PARM                    WWNCU2
     C                   PARM                    WWNCU3
     C                   PARM                    WWNCU4
     C                   PARM                    WWNCB1
     C                   PARM                    WWNCB2
     C                   PARM                    WWNCB3
     C                   PARM                    WWNCB4
     C                   ENDSR
