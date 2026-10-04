      *----------------------------------------------------------------*
      *   AUTOR: CaRLOS Rojas  - 2018                                  *
      *----------------------------------------------------------------*
      * Crea archivo temporal de trabajo para el monitoreo de archivos *
      * test commit                                                    *
      *----------------------------------------------------------------*
      ***************************************************************
            ctl-opt bnddir('QC2LE')  ;

        dcl-proc Pr_Retardo;
           dcl-pi *n;
              WTiempo char(4) value;
           end-pi;
        dcl-pr sleep extproc('sleep') ;
          *n uns(10) value  ;
        end-pr ;
        dcl-s  Tiempo    Zoned(4:0) inz(0);
        dcl-s  $source  Char(20);
        dcl-s  $pos     zoned(5) ;
             tiempo = %dec(WTiempo :4 :0 );


                $source = 'AABC1ABD2AB3A';

                $pos = %check ('ABCD' : %trim($source));
                dsply $pos; //DSPLY      5

                $pos = %check ('ABCD' : %trim($source) :6);
                dsply $pos; //DSPLY      9

                $pos = %checkr ('ABCD' : %trim($source));
                dsply $pos; //DSPLY     12

                $pos = %checkr ('ABCD' : %trim($source) : 11);
                   dsply $pos; //DSPLY      9

           *inlr = *on;
          sleep (tiempo);
       end-proc;
