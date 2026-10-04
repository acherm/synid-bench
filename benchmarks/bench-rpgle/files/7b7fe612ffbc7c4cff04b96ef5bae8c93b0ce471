      /If Defined(*CRTBNDRPG)
     H DFTACTGRP(*NO) bnddir('U6') actgrp('AG6')
      /endif
     Fjrnanzwwd CF   E             WORKSTN SFILE(SFL1:SF1RRN) InfDS(wsDS)
      /copy cpy,u6Ibm_h
      /copy cpy,u6env_h
      /copy cpy,u6ifs_h
      /copy cpy,u6index_h
      /copy cpy,u6jrn_h
      /copy cpy,u6msg_h
      /copy cpy,u6screen_h
      /copy cpy,u6tree_h
      /copy cpy,u6xml_h

      //˜Global fields
     D G               DS                  qualified
     d  screen                        3u 0 inz(1)
     D  change                         N
     D  error                          N
     D  lAnzs                          *
     d  lAnz                           *   dim(18) inz(*null)
     d  lAnz1                          *   inz(*null)
     d  lAnz1_b4                       *   inz(*null)
     d  lAnz9                          *   inz(*null)
     d  lAnz9_B4                       *   inz(*null)
     d  lOpts                          *   inz(*null)
     d  lFKs                           *   inz(*null)
     d  jrnExt                       10a   varying
     d  jrnPath                      80a   varying
     d  indexPath                    80a   varying
     d  fToSort                        n
      //‚--------------------------------------------------------------------
      //‚main
      //‚--------------------------------------------------------------------
     d JRNANZWW        pi
     d  index          ds                  likeDs(tIndex) based(pIndex)
       //‚welcome message
       msg_SndPM(pgmID:env_getWelcomeMessage());
       //‚Title
       ZTL='Work with Journals analysis';
       //‚Load function keys
       screen_setFK(g.lFKs:x'33':'0':%pAddr(F3):'F3=Exit');
       screen_setFK(g.lFKs:x'36':'1':%pAddr(f6):'F6=Save');
       screen_setFK(g.lFKs:x'3a':'1':%pAddr(f10):'F10=Move to top');
       screen_setFK(g.lFKs:x'b8':'1':%pAddr(f20):'F20=Renumber');
       screen_setFK(g.lFKs:x'f1':'1':%pAddr(Enter));
       screen_setFK(g.lFKs:x'f4':*ON :%pAddr(rollUP));
       screen_setFK(g.lFKs:x'f5':*ON :%pAddr(rolldown));
       zFK=screen_getfkentitle(g.lFKs);
       //‚Load options
       screen_SetOption(g.lOpts:'E':'E=Entries');
       screen_SetOption(g.lOpts:'X':'X=XML');
       screen_SetOption(g.lOpts:'x');
       zCH=screen_getChoicesEntitle(g.lOpts);
       //‚load index
       g.jrnPath=env_getpath(cJournal);
       g.jrnExt=env_getExt(cJournal);
       g.indexPath=g.jrnPath+g.jrnExt+'.index';
       g.lAnzs=tree_xml2tree(g.indexPath
                            :%pAddr(index_XMLinput));
       if g.lAnzs=*null;
         pIndex=Tree_getNewItem(%addr(tIndex):%size(tIndex));
         g.lAnzs=tree_getNewLink(pIndex);
       endIf;
       //‚browse files from folder
       ifs_browseFiles(g.jrnPath:%paddr(procFile));
       //‚Sort elements
       tree_Sort(g.lAnzs:%paddr(index_comparator));
       g.lAnz1=tree_getFirst(g.lAnzs);
       wrkScreen();
       *inlr=*on;
      //‚--------------------------------------------------------------------
      //‚work screen
      //‚--------------------------------------------------------------------
     pwrkScreen        b
       dow g.screen>0;
         if G.screen=1;
           Screen1();
         endif;
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Screen 1 - display form
      //‚--------------------------------------------------------------------
     p Screen1         b
     d fkProcess       pr                  extproc(pAction)
      *
     d pAction         s               *   procptr
     d fcontrol        s               n
       if g.lAnz9<>g.lAnz9_b4;
         sync();
       endIf;
       if g.lAnz1<>g.lAnz1_b4;
         loadWA1();
         loadSf1();
         //‚more item or bottom of list
         if tree_getNext(g.lAnz9)=*null;
           mySflEnd='Bottom';
         else;
           mySflEnd='More...';
         endIf;
       endIf;
       //‚display activation
       write msgCtl;
       write hdr1;
       *in88=*on;
       *in89=*off;
       exfmt ctl1;
       msg_rmvPM(pgmID);
       //‚get/launch function key
       screen_processFK(pgmID:g.lFKs:wsds.kp:%pAddr(Control));
     p                 e
      //‚--------------------------------------------------------------------
      //‚to process file in directory
      //‚--------------------------------------------------------------------
     pControl          b
     d Control         pi              n
      *
     d Anz             ds                  likeDs(tElement) based(pAnz)
     d pCheckProc      s               *   procptr
     d checkProc       pr              n   extproc(pCheckProc)
     d  lAnz                           *
     d lOption         s               *
     d error           s               n   inz(*off)
       readc sfl1;
       dow not %eof();
         *in01=*off;
         pAnz=tree_getitem(g.lAnz(sf1rrn));
         if anz.seq<>xSeq;
           anz.seq=xSeq;
           g.fToSort=*on;
         endIf;
         tree_SetOption(g.lAnz(sf1rrn):xChoice);
         if xChoice<>'';
           lOption=tree_getLinkFromList(g.lOpts:'o':xChoice);
           if lOption=*null;
             g.error=*on;
             msg_SndPM(pgmID:'Option '''+xChoice+''' is not valid');
             *in01=*on;
           endif;
         endif;
         update sfl1;
         readc sfl1;
       enddo;
       return error;
     p                 e
      //‚--------------------------------------------------------------------
      //‚to process file in directory
      //‚--------------------------------------------------------------------
     pProcFile         b
     d procFile        pi
     d  wPAth                       255a   const varying
      *
     d lAnz            s               *
     d Anz             ds                  likeDs(tElement) based(pAnz)
       //‚Only take "*.jrn"
       if %scan('.'+g.jrnExt:wPath)=0;
         return;
       endIf;
       lAnz=tree_getLinkFromList(g.lAnzs:kElement:wPath);
       if lAnz<>*null;
         pAnz=tree_getItem(lAnz);
       //‚Case of a new analysis not yet listed
       else;
         pAnz=Tree_getNewItem(%addr(tElement):%size(tElement));
         anz.ID=wPath;
         anz.seq=0;
         tree_linkToParent(g.lAnzs:tree_getNewLink(pAnz));
       endIf;
       //‚to confirm existance of analysis
       anz.exists=*on;
       xml_read(g.jrnPath+wPath:%paddr(ProcNode):pAnz);
     p                 e
      //‚--------------------------------------------------------------------
      //‚Procedure node
      //‚--------------------------------------------------------------------
     pProcNode         b
     d ProcNode        pi              n
     d    ND                               likeDs(xml_NodeDefine)
     d    pAnz_                        *   const
      *
     d anz             ds                  likeDs(tElement) based(pAnz)
       if ND.ID='JOURNAL';
         pAnz=pAnz_;
         anz.text=ND.text;
         return *on;
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Loadind work area
      //‚--------------------------------------------------------------------
     p loadWA1         b
      *
     d lAnz            s               *
     d i               s              3u 0
       clear g.lAnz;
       lAnz=g.lAnz1;
       for i=1 to 18;
         g.lAnz(i)=lAnz;
         g.lAnz9=lAnz;
         lAnz=tree_getNext(lAnz);
       endFor;
     p                 e
      //‚-----------------------------------------------------------------------
      //‚Loadind subfile
      //‚-----------------------------------------------------------------------
     p loadSF1         b
      *
     d Anz             ds                  likeDs(tElement) based(pAnz)
       //‚clear subfile
       *in88=*off;
       *in89=*on;
       WRITE ctl1;
       //‚Reload subfile
       for sf1rrn=1 to 18;
         if g.lAnz(sf1rrn)=*null;
           leave;
         endIf;
         xChoice=tree_getOption(g.lAnz(sf1rrn));
         pAnz =tree_getItem(g.lAnz(sf1rrn));
         xSeq =anz.seq;
         xID  =anz.ID;
         xTitle=anz.text;
         write sfl1;
       endFor;
       g.lanz1_b4=g.lanz1;
       g.lanz9_b4=g.lanz9;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Roll-UP
      //‚--------------------------------------------------------------------
     pRollUp           b
     d Rollup          pi
       if G.lAnz1=tree_GetFirst(G.lAnzs);
         msg_SndPM(pgmID:'You have reached the top of the list');
       else;
         g.lAnz9=tree_getPrev(g.lAnz1);
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Roll-down
      //‚--------------------------------------------------------------------
     pRollDown         b
     d RollDown        pi
       if mySflEnd='Bottom';
         msg_SndPM(pgmID:'You have reached the bottom of the list');
       else;
         g.lAnz1=tree_getNext(g.lAnz9);
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Enter
      //‚--------------------------------------------------------------------
     pEnter            b
     d Enter           pi
     d lAnz            s               *
     d Choice          s              1a
     d pOption         s               *
   86d Anz             ds                  likeDs(tElement) based(pAnz)
     d cmd             s             80a   varying
      /copy cpy,jrnentww_h
       if g.fToSort;
         g.fToSort=*off;
         //‚Sort elements
         tree_Sort(g.lAnzs:%paddr(index_comparator));
         g.lAnz1_b4=*null;
         return;
       endIf;
       //
       lAnz=tree_getFirst(g.lAnzs);
       dow lAnz<>*null;
         choice=tree_getOption(lAnz);
         if choice<>'';
           pAnz=tree_getItem(lAnz);
           if choice='X';
             cmd='dspf '''+g.jrnPath+anz.ID+'''';
             qcmdexc(cmd:%len(cmd));
           elseif choice='x';
             cmd='edtf '''+g.jrnPath+anz.ID+'''';
             qcmdexc(cmd:%len(cmd));
           elseif choice='E';
             jrnentww(0:%scanrpl('.jrn':'':anz.ID));
           endIf;
           g.lAnz1_b4=*null;
           tree_setOption(lAnz:'');
         endIf;
         lAnz=tree_getNext(lAnz);
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F3=Exit
      //‚--------------------------------------------------------------------
     pf3               b
     d f3              pi
       G.screen=0;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F6=Save
      //‚--------------------------------------------------------------------
     pf6               b
     d f6              pi
       f20();
       xml_tree2xml(g.indexPath:g.lAnzs:%paddr(index_XmlOutput));
       g.screen=0;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F10=Move to top
      //‚--------------------------------------------------------------------
     pf10              b
     d f10             pi
       if SFLCSRRRN=0;
         msg_SndPM(pgmID:'Wrong cursor position');
       else;
         g.lAnz1=g.lAnz(sflcsrrrn);
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F20=Renumber
      //‚--------------------------------------------------------------------
     pf20              b
     d f20             pi
      *
     d Seq             s             10u 0 inz(0)
     d lAnz            s               *
     d Anz             ds                  likeDs(tElement) based(pAnz)
       //‚Resequence elements                                                -
       lAnz=tree_getFirst(g.lAnzs);
       dow lAnz<>*null;
         pAnz=tree_getItem(lAnz);
         if Anz.seq=0;
           leave;
         else;
           Seq+=10;
           Anz.seq=seq;
         endIf;
         lAnz=tree_getNext(lAnz);
       endDo;
       g.lAnz1_b4=*null;
     p                 e
      //‚-----------------------------------------------------------------------
      //‚Synch
      //‚-----------------------------------------------------------------------
     pSync             b
     d Sync            pi
      *
     d i               s              3u 0
     d lX              s               *
       for i=1 to 18;
         lX=tree_getPrev(G.lAnz1);
         if lX=*null;
           leave;
         endIf;
         G.lAnz1=lX;
       endFor;
     p                 e
