      //This example assumes that the file has
      //only one key field with name myField1 (type character)
      //and it has also another character field with name myfield2

     H DFTACTGRP(*no) ACTGRP(*NEW)

     D/COPY QRPGLESRC,FILE001P

     D dsKey           S                   LikeDS(keyFILE001_t)
     D wSampleField    S                   Like(FILE001_t.myfield2)

      /free
            dsKey.myField1 = '123';
            if find_FILE001(dsKey);
              wSampleField = get_myfield2_FILE001();
            endif;
            dsply wSampleField;

            *inlr ='1';
