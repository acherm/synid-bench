
       Ctl-Opt BndDir('MIXBND');

       Dcl-F Article3 disk usage(*Input) keyed;
       Dcl-F Custome3 disk usage(*Input) keyed;

       Dcl-Pi *n ;
         Country       Char(2);
         Art_Info      LikeDs(Art_Ds) Dim(50);
       End-Pi;

       Dcl-Pr Values;
         *n Char(10);
       End-Pr;

       /Include QcpySrc,Article
       /Include QcpySrc,Familly
       /Include QcpySrc,Country
       /Include QcpySrc,Customer
       /Include QcpySrc,Vat
       /Include QcpySrc,Order

       Dcl-Ds Ord_Ds     ExtName('DETORD')  Qualified End-Ds;
       Dcl-Ds Art_Msc_Ds ExtName('ARTICLE') Qualified End-Ds;

       Dcl-Ds Art_Ds Qualified;
         Art_Cust_Id   Packed(5:0);
         Art_Cust_Name Char(30)   ;
         Art_Msc_Info  LikeDs(Art_Msc_Ds) Dim(50);
       End-Ds;
       Dcl-S Inx  Packed(2:0) Inz(1);
       Dcl-S Inx1 Packed(2:0) Inz(1);

      * ------------------------------------------------------------------------
      * Validate the country and then fetch customers using country id
      * ------------------------------------------------------------------------
        If ExistCountry(Country);
          ExSr FindValidCustomers;
          Inx  = Inx +1;
        EndIf;

       *Inlr = *On;

      * ------------------------------------------------------------------------
      * Validate the order against selected customers then get the order
      * details from DETORD file
      * ------------------------------------------------------------------------

       BegSr FindQualifiedArticle;
          If Ord_Ds.OdTot = (GetArtRefSalPrice(Ord_Ds.OdArid) * GetArtCusQty
                            (Ord_Ds.OdArid));
             ExSr FillDetailsOnArray;

          EndIf;
       EndSr;

      * ------------------------------------------------------------------------
      * Get the article details based on article id and fill the output array
      * using other details like country name, customer name, order numer etc
      * ------------------------------------------------------------------------
       BegSr FillDetailsOnArray;

         Art_Info(Inx).Art_Cust_Id   = CuId;
         Art_Info(Inx).Art_Cust_Name = CustNm;

         Art_Info(Inx).Art_Msc_Info(Inx1).ARID
                                          = Ord_Ds.OdArid;
         Art_Info(Inx).Art_Msc_Info(Inx1).ARDESC
                                          = GetArtDesc(Art_Msc_Ds.ARID);
         Art_Info(Inx).Art_Msc_Info(Inx1).ARSALEPR
                                          = GetArtRefSalPrice(Ord_Ds.OdArid);
         Art_Info(Inx).Art_Msc_Info(Inx1).ARWHSPR
                                          = GetArtStockPrice(Ord_Ds.OdArid);
         Art_Info(Inx).Art_Msc_Info(Inx1).ARTIFA
                                          = GetArtFam(Ord_Ds.OdArid);
         Art_Info(Inx).Art_Msc_Info(Inx1).ARSTOCK
                                          = GetArtStock(Ord_Ds.OdArid);
         Art_Info(Inx).Art_Msc_Info(Inx1).ARMINQTY
                                          = GetArtMinStock(Ord_Ds.OdArid);
         Art_Info(Inx).Art_Msc_Info(Inx1).ARCUSQTY
                                          = GetArtCusQty(Ord_Ds.OdArid);
      *  Art_Info(Inx).ARPURQTY=
         Art_Info(Inx).Art_Msc_Info(Inx1).ARVATCD
                                          = GetArtVatCode(Ord_Ds.OdArid);
      *  Art_Info(Inx).ARCREA  =
      *  Art_Info(Inx).ARMOD   =
      *  Art_Info(Inx).ARMODID =
      *  Art_Info(Inx).ARDEL   =
         Exec Sql
           Insert InTo Article (ArId)
           Values(:Ord_Ds.OdArid);

         Inx1 = Inx1 +1;

       EndSr;
      * ------------------------------------------------------------------------
       BegSr FindValidCustomers;
         Setll Country Custome3;
         Reade Country Custome3;
         Dow Not%Eof(Custome3) And ExistCountry(Country);
           If ExistCus(CuId) And GetOrderNumber(Cuid) > *Zero And
             GetCusLimCredit(CuId) <=5000;

             Ord_Ds = GetOrderDetails(GetOrderNumber(Cuid));
             // Validate the Net Amount If Amount is Matched the it eligible for
             // further process
             ExSr FindQualifiedArticle;

           EndIf;
           Reade Country Custome3;
         EndDo;
       EndSr;
