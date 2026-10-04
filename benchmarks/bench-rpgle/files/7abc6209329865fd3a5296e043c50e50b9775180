      /if defined(RTVUSR_H)
      /eof
      /endif
      /define RTVUSR_H

      * --------------------------------------------------- *
      * Estrucutura de datos con el último error
      * --------------------------------------------------- *
     D RTVUSR_ERDS_T   ds                  qualified
     D                                     based(template)
     D   Errno                        4s 0
     D   Msg                         80a

      * ---------------------------------------------- *
      * Estructura de datos de error para APIs
      * ---------------------------------------------- *
     D QUsec_t         ds                  qualified
     D                                     based(template)
     D   BytesProvided...
     D                               10i 0
     D   BytesAvailables...
     D                               10i 0
     D   MessageID                    7a
     D   Reserved                     1a
     D   ApiEcExDt                  127a

      * --------------------------------------------------- *
      * Constantes
      * --------------------------------------------------- *
     D USR_EXIST       c                   const(*ON)
     D USR_NOTEXIST    c                   const(*OFF)

      * --------------------------------------------------- *
      * RTVUSR_Inz(): Inicializa módulo.                    *
      *                                                     *
      * Este procedimiento será llamado por todos los demás *
      * procedimiento exportados.                           *
      *                                                     *
      * --------------------------------------------------- *
     D RTVUSR_Inz      pr            10i 0

      * --------------------------------------------------- *
      * RTVUSR_Chk(): Chequea existencia de usuario.        *
      *                                                     *
      *   peUser (input) = Perfil de Usuario a chequear.    *
      *                    *CURRENT = Usuario del Trabajo.  *
      *                                                     *
      * Retorna USR_EXIST o USR_NOTEXIST                    *
      * --------------------------------------------------- *
     D RTVUSR_Chk      pr             1N
     D  peUser                       10a   const

      * --------------------------------------------------- *
      * RTVUSR_Error():Retorna la descripción del último    *
      *                  error del programa.                *
      *                                                     *
      * Retorna útlimo error.                               *
      * --------------------------------------------------- *
     D RTVUSR_Error    pr                  likeds(RTVUSR_ERDS_T)

