     //-----------------------------------------------------------------*/
     // Create Instructions:                                            */
     //                                                                 */
     //  CRTBNDRPG PGM(GA4BSENDR) SRCFILE(QRPGLESRC) DFTACTGRP(*NO)     */
     //-----------------------------------------------------------------*/

     //-----------------------------------------------------------------*/
     // Prototypes                                                      */
     //-----------------------------------------------------------------*/
     D GA4BSENDR       PR                  EXTPGM('GA4BSENDR')
     D  Email                       256
     D  Password                    256
     D  Document                    128
     D  Directory                   128

     D main            PR                  STATIC
     D                                     EXTPROC(*JAVA
     D                                        : 'com.csdainc.gfi.GA4BSendJ'
     D                                        : 'main')
     D                                 O   CLASS(*JAVA:'java.lang.String')
     D                                     DIM(4)
     D                                     CONST

     D String          PR              O   EXTPROC(
     D                                     *JAVA:
     D                                     'java.lang.String':
     D                                     *CONSTRUCTOR)
     D                                     CLASS(
     D                                      *JAVA:
     D                                     'java.lang.String')
     D bytes                         50A   CONST VARYING

     D args            s               O   CLASS(
     D                                     *JAVA:
     D                                     'java.lang.String')
     D                                     DIM(4)

     //-----------------------------------------------------------------*/
     // Entry Parameters                                                */
     //-----------------------------------------------------------------*/
     D GA4BSENDR       PI
     D  Email                       256
     D  Password                    256
     D  Document                    128
     D  Directory                   128

      /free

       args(1) = String(%trim(Email   ));
       args(2) = String(%trim(Password));
       args(3) = String(%trim(Document));
       args(4) = String(%trim(Directory));

       main(args);

       *Inlr = *on;

