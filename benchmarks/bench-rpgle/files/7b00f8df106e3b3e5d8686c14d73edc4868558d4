*SRCMBRTXT:OJ-Import Arch. Internet-Copia a OJMOFI
      *//OVRDBF FILE(INPFIL) TOFILE(OJMOFI)
      *//CRTBNDRPG PGM(SDB02.PGM/OJim10r1) SRCFILE(SDB02.SRC/QRPGSRC)
     FINPFIL    IP   E           K DISK
     FOJMOFI01  UF A E           K DISK    RENAME(REOJMOFI:REC)
     F*JTCTA    IF   E           K DISK
     F*JMRES    O    E           K DISK
     D OFINUM          S             11S 0
     C                   WRITE     REC
     C*                  EXSR      GENRES
     C*-------------------------------------------------------------------------
     C*    GENRES        BEGSR
     C*    *LOVAL        SETLL     REOJTCTA
     C*                  READ      REOJTCTA                               25
     C*                  DOW       NOT *IN25
     C*                  MOVE      M4INUI        M6INUI
     C*                  MOVE      M4INDO        M6INDO
     C*                  MOVE      M4ITDO        M6ITDO
     C*                  MOVE      M7ITPR        M6ITPR
     C*                  MOVE      M4ESCL        M6ESCL
     C*                  WRITE     REOJMRES
     C*                  READ      REOJTCTA                               25
     C*                  ENDDO
     C*                  ENDSR
