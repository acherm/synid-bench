      /if defined(SVPLRC_H)
      /eof
      /endif
      /define SVPLRC_H

      * ------------------------------------------------------------ *
      * Inz():   Inicializa módulo.                                  *
      *                                                              *
      * ------------------------------------------------------------ *
     D SVPLRC_Inz      pr

      * ------------------------------------------------------------ *
      * End():   Finaliza módulo.                                    *
      *                                                              *
      * ------------------------------------------------------------ *
     D SVPLRC_End      pr

      * ------------------------------------------------------------ *
      * Error(): Retorna último error del módulo.                    *
      *                                                              *
      *       peErrn    (output)   Código de Error (opcional)        *
      *                                                              *
      * ------------------------------------------------------------ *
     D SVPLRC_Error    pr            80a
     D   peErrn                      10i 0 options(*nopass)

      * ------------------------------------------------------------ *
      * getLimiteRc():   Retorna límite de RC a una fecha.           *
      *                                                              *
      *       peEmpr    (input)  Empresa                             *
      *       peSucu    (input)  Sucursal                            *
      *       peFemi    (input)  Fecha de Emisión (aaammdd). Opcional*
      *                                                              *
      * retorna: Límite de RC o 0 si no encuentra.                   *
      * ------------------------------------------------------------ *
     D SVPLRC_getLimiteRc...
     D                 pr            15  2
     D   peEmpr                       1a   const
     D   peSucu                       2a   const
     D   peFemi                       8  0 const options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * getInicioVigencia():  Obtiene fecha de inicio de póliza      *
      *                                                              *
      *       peEmpr    (input)  Empresa                             *
      *       peSucu    (input)  Sucursal                            *
      *       peRama    (input)  Rama                                *
      *       pePoli    (input)  Póliza                              *
      *                                                              *
      * retorna: Fecha de inicio de vigencia.                        *
      * ------------------------------------------------------------ *
     D SVPLRC_getInicioDeVigencia...
     D                 pr             8  0
     D   peEmpr                       1a   const
     D   peSucu                       2a   const
     D   peRama                       2  0 const
     D   pePoli                       7  0 const

      * ------------------------------------------------------------ *
      * getInicioVigeSpol():  Obtiene fecha de inicio de superpóliza *
      *                                                              *
      *       peEmpr    (input)  Empresa                             *
      *       peSucu    (input)  Sucursal                            *
      *       peArcd    (input)  Artículo                            *
      *       peSpol    (input)  SuperPóliza                         *
      *                                                              *
      * retorna: Fecha de inicio de vigencia.                        *
      * ------------------------------------------------------------ *
     D SVPLRC_getInicioDeVigeSpol...
     D                 pr             8  0
     D   peEmpr                       1a   const
     D   peSucu                       2a   const
     D   peArcd                       6  0 const
     D   peSpol                       9  0 const

