        Ctl-Opt dftactgrp(*no) BndDir('QC2LE');

        Dcl-Pr OpenFile int(10) extproc('open') ;
          *n pointer value options(*string) ;
          *n int(10) value ;
          *n uns(10) value options(*nopass) ;
          *n uns(10) value options(*nopass) ;
          *n uns(10) value options(*nopass) ;
        End-Pr ;

        Dcl-Pr ReadFile int(10) extproc('read') ;
          *n int(10) value ;
          *n pointer value ;
          *n uns(10) value ;
        End-Pr ;

        Dcl-Pr CloseFile int(10) extproc('close') ;
           *n  int(10) value ;
        End-Pr;

        Dcl-Pr WriteSrcF  ExtPgm('WRITESRCF');
           *n  Char(400);
        End-Pr;

        Dcl-Pr SystemCmd int(10) extproc('system') ;
          *n pointer value options(*string) ;
        End-Pr ;

        Dcl-C O_RDONLY 1 ;           //Read only
        Dcl-C O_TEXTDATA 16777216 ;  //Open in text mode
        Dcl-C O_CCSID 32 ;           //CCSID
        Dcl-C S_IRGRP 32 ;           //Group authority

        Dcl-S FileDes int(10) ;
        Dcl-S Length int(10) ;
        Dcl-S Data char(100) ;
        Dcl-S Array char(100) dim(2000) ;
        Dcl-S Element packed(4:0) ;
        Dcl-S Start packed(4:0) ;
        Dcl-S End like(Start) ;
        Dcl-S EndStm like(Start) ;
        Dcl-S SqlSt  Char(400);
        Dcl-S SqlStm Char(400);
        Dcl-S AddStm Char(100);
        Dcl-S Number Char(4);
        Dcl-S Inx        Packed(3:0) Inz(1);
        Dcl-S SplitWord  Char(20);
        Dcl-S Split      Ind;
        Dcl-S SplitArray Char(20) Dim(50);
        Dcl-S InsertDta  Char(80);
        Dcl-S TableName  Char(10);

        Dcl-C Path '/home/pkumar/DDS_To_DDL.txt' ;

        FileDes = OpenFile(Path :
                  O_RDONLY + O_TEXTDATA + O_CCSID :
                  S_IRGRP :
                  37) ;

        If (FileDes < 0) ;
          dsply ('file ' + path + ' could not be open') ;
          *inlr = *on ;
          return ;
        Endif ;

        Dow (1 = 1) ;

          Length  = ReadFile(FileDes:%addr(Data):%size(Data)) ;
          if (Length = 0) ;
            leave ;
          elseif (Length < %size(Data)) ;
            %subst(Data:(length + 1)) = ' ' ;
          endif ;
          Start = 0 ;

          Dow (2 = 2) ;
            Element += 1 ;
            End = %scan(x'25':Data:(Start + 1)) ;
            If (End > 0) ;
              If (Array(Element) = ' ') ;
                Array(Element) = %subst(Data:(Start + 1):
                                       ((End - Start) - 2)) ;
              Else ;
                Array(Element) = %trimr(Array(Element)) +
                                 %subst(Data:(Start + 1):
                                       ((End - Start) - 2)) ;
              Endif ;

              Clear SqlSt;
              SqlSt = 'Create Or Replace Table ';

              ExSr ProcessDDL;
              ExSr ExecuteTbl;

              Start = End ;
            Else ;
              Array(Element) = %subst(Data:(Start + 1)) ;
              Element -= 1 ;
              Leave ;
            Endif ;
          Enddo ;
        Enddo ;

        CloseFile(FileDes) ;
        *InLr = *On ;

        BegSr ProcessDDL;

          SplitArray = %Split(Array(Element):',');
          Dow SplitArray(Inx) <> *Blank;
            If %Scan('DBF':SplitArray(Inx)) > *Zero;

              Clear TableName;
              TableName = SplitArray(Inx);

              ExSr AddMember;
              SqlSt = %Trim(SqlSt) + ' ' + %Trim(SplitArray(Inx)) + '(';

            ElseIf %Scan('Fld':SplitArray(Inx)) > *Zero;

              ExSr AddFldToStm;

            ElseIf %SubSt(SplitArray(Inx):1:3) <> 'Fld' or
                   %SubSt(SplitArray(Inx):1:3) <> 'DBF';

              If %Scan('.':%Trim(SplitArray(Inx))) > *Zero;
                SqlSt = %Trim(SqlSt) + ' Dec(';

                For-Each Number In %Split(SplitArray(Inx):'.');

                  If Split = *Off;
                    SqlSt = %Trim(SqlSt) + %Trim(Number)+ ',' ;
                    Split = *On;
                  Else;
                    SqlSt = %Trim(SqlSt) + %Trim(Number);
                    Split = *Off;
                  EndIf;

                EndFor;

                SqlSt = %Trim(SqlSt) + '),';
              Else;

                SqlSt = %Trim(SqlSt) + ' Char(' +
                         %Trim(SplitArray(Inx))+'),';
              EndIf;

            EndIf;

            Inx +=1;
          EndDo;

          If %ScanR(',':%Trim(SqlSt)) > *Zero;
            EndStm = %ScanR(',':%Trim(SqlSt));
            SqlSt = %ScanRpl(',':')':%Trim(SqlSt):EndStm);
            Reset EndStm;
          EndIf;

          Clear InsertDta;
          SqlStm = SqlSt;

          WriteSrcF(SqlStm);

          Clear SqlSt;
          Clear SqlStm;
          ReSet Inx;
        EndSr;
      *----------------------------------------------------------
      *  Add Member in source physical file
      *----------------------------------------------------------
        BegSr AddMember;

          Clear AddStm;
          AddStm = 'AddPfm Pkumar4/QSqlSrc Mbr('+
                          %Trim(SplitArray(Inx)) +')';
          SystemCmd(AddStm);

          AddStm = %Trim(AddStm) + ' SrcType(Text)';
          AddStm = %ScanRpl('Add':'Chg':AddStm);
          SystemCmd(AddStm);

          Clear AddStm;
          AddStm = 'OvrDbf File(QSqlSrc)'+
                   ' ToFile(Pkumar4/Qsqlsrc) Mbr(' +
                   %Trim(SplitArray(Inx)) +')' + ' OvrScope(*Job)';
          SystemCmd(AddStm);

        EndSr;

        BegSr AddFldToStm;

          SqlSt = %Trim(SqlSt) + %Trim(SplitArray(Inx));

        EndSr;
      *-----------------------------------------------------------
        BegSr ExecuteTbl;

          Clear AddStm;
          AddStm = 'DltOvr File(*All) Lvl(*Job)';
          SystemCmd(AddStm);

          Clear AddStm;
          AddStm = 'ChgCurLib Pkumar4';
          SystemCmd(AddStm);

          Clear AddStm;
          AddStm = 'RunSqlStm SrcFile(Pkumar4/Qsqlsrc) SrcMbr(' +
                   %Trim(TableName) + ')' +' Commit(*None)';
          SystemCmd(AddStm);

        EndSr;
