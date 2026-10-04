     H option(*nodebugio:*noshowcpy:*srcstmt)
     H alwnull(*usrctl) dftactgrp(*no)
     H bnddir ( 'HDIILE/HDIBDIR' )
     H actgrp(*new)
      * ********************************************************* *
      * COWGRA10: Verifica bloqueo de intermediario               *
      * --------------------------------------------------------- *
      * Sergio Fernandez                    *07-Oct-2016          *
      * --------------------------------------------------------- *
      * Modificaciones:                                           *
      *                                                           *
      * ********************************************************* *

     D COWGRA10        pr                  extpgm('COWGRA10')
     D  peBase                             likeds(paramBase) const
     D  peTiou                        1  0 const
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

     D COWGRA10        pi
     D  peBase                             likeds(paramBase) const
     D  peTiou                        1  0 const
     D  peErro                       10i 0
     D  peMsgs                             likeds(paramMsgs)

      /copy './qcpybooks/svpws_h.rpgle'
      /copy './qcpybooks/cowgrai_h.rpgle'

      /free

       *inlr = *on;

       if COWGRAI_bloqueoProd( peBase
                             : peTiou )  = *OFF;
         SVPWS_getMsgs( '*LIBL'
                      : 'WSVMSG'
                      : 'COW0105'
                      : peMsgs     );
         peErro = -1;
       endif;

       COWGRAI_End();

       return;

      /end-free
