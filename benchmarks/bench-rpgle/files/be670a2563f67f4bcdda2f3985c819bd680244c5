      /If Defined(*CRTBNDRPG)
     H DFTACTGRP(*NO) bnddir('U6') actgrp('AG6')
      /endif
     FJRNENTWWd CF   E             WORKSTN SFILE(SFL1:SFlRRN1) InfDS(wsDS)

      /copy cpy,u6ibm_h
      /copy cpy,u6env_h
      /copy cpy,u6filter_h
      /copy cpy,u6file_h
      /copy cpy,u6fmt_h
      /copy cpy,u6grid_h
      /copy cpy,u6ifs_h
      /copy cpy,u6int_h
      /copy cpy,u6jrn_h
      /copy cpy,u6msg_h
      /copy cpy,u6screen_h
      /copy cpy,u6screen_s
      /copy cpy,u6stat_h
      /copy cpy,u6tree_h
      /copy cpy,u6xml_h
      /copy cpy,u6xview_h
      /copy cpy,u6yview_h

      //˜Anchors
     D A               DS                  qualified
     d  lOpts                          *
     d  lFKs                           *
     d  lXViews                        *
     d  lFmts                          *
     d  lGrids                         *
     d  lYViews                        *
     d  lForms                         *
      //˜Global fields
     D G               DS                  qualified
     d  pScreen                        *   procptr
     d  lVariant1                      *
     d  lVariant1_b4                   *
     d  lVariant9                      *
     d  lVariant9_b4                   *
     d  fRefresh                       n
     d  Item                               dim(20) likeds(tItem)
     d  anzJrnPath                  255a   varying
     d  lJournal                       *
     d  lFiles                         *
     d  lEntries                       *
     d  lStats                         *
     d  lFilters                       *
     d  hdta                         10i 0
     d  error                          n
     d  CanTabRight                    n   inz(*off)
     d  CanTabLeft                     n   inz(*on)
     d  freePartWidth                 3u 0
     d  lVariant_last                  *
     d  fSubEntries                    n
      *
     d  jrnXView       ds                  likeDs(tXView) based(pJrnXView)
     d  lJrnXView      s               *
     d  margin         c                   const(4)
      *
     d  tItem          ds                  qualified
     d   lXView                        *
     d   lYView                        *
     d   lVariant                      *
      *
     d  journal        ds                  likeDs(tJournal) based(pJournal)
     d filters         ds                  likeds(tFilters) based(pFilters)
      //‚--------------------------------------------------------------------
      //‚main
      //‚--------------------------------------------------------------------
     d JRNENTWW        pi
     d   rtncode                      3i 0
     d   AnzID                       35
      *
     d lColumn         s               *
     d lFmtEntry       s               *
     d Column          ds                  likeDs(tColumn) based(pColumn)
       //‚get path for journal analysis
       g.anzJrnPath=env_getjournalPath()+%trim(anzID)+'.jrn';
       //‚welcome message
       msg_SndPM(pgmID:env_getWelcomeMessage());
       //‚Load special procedure
       int_loadprocs();
       //‚Load journal
       g.lJournal=tree_xml2tree(g.anzJrnPath:%paddr(jrn_xmlinput));
       pJournal=tree_getItem(g.lJournal);
       g.lEntries=tree_getLinkFromList(g.lJournal:kEntries);
       g.lFilters=tree_getLinkFromList(g.lJournal:kFilters);
       if g.lFilters=*null;
         g.lFilters=
         tree_getNewLink(tree_getNewItem(%addr(tFilters):%size(tFilters)));
         tree_linkToparent(g.lJournal:g.lFilters:g.lEntries);
       endIf;
       pFilters=tree_getItem(g.lFilters);
       jrn_tieEntries(g.lEntries);
       //‚load view for journal (fixed part)
       lJrnXView=xview_getXView(a.lXViews:a.LGrids:a.lfmts:'JRNENTRY':'Y');
       pJrnXView=tree_getItem(lJrnXView);
       lFmtEntry=jrnXView.lFmt;
       jrnXView.hdrColor=x'22';
       xview_posToMostLeft(jrnXView:%len(xFil)/2);
       xview_sethdrs(jrnXView:0);

       g.freePartWidth=%len(xFil)-%len(jrnxView.hdrs)-2;

       //‚get handle on data journal
       G.hDta=ifs_openForRead(env_getJournalPath()+%trim(AnzID)+'.dta');
       //‚load other views (free part)
       EntriesLoad();
       //‚load models
       ModelsLoad();
       //‚position on the left
       f18();
       //‚Load function keys
       screen_setFK(A.lFKs:x'31':'1':%pAddr(f1));
       screen_setFK(A.lFKs:x'32':'1':%pAddr(f2):'F2=Filters');
       screen_setFK(A.lFKs:x'33':'0':%pAddr(F3):'F3=Exit');
       screen_setFK(A.lFKs:x'36':'1':%pAddr(f6):'F6=To left');
       screen_setFK(A.lFKs:x'37':'1':%pAddr(f7):'F7/F19=Left/all');
       screen_setFK(A.lFKs:x'38':'1':%pAddr(f8):'F8/F20=Right/all');
       screen_setFK(A.lFKs:x'3a':'1':%pAddr(f10):'F10=To top');

       screen_setFK(A.lFKs:x'3b':'1':%pAddr(f11):'F11=Filtered   '
                                                :'F11=Display all');
       screen_setFKcontext(a.lFKs:x'3b':%char(%int(filters.activated)));

       screen_setFK(A.lFKs:x'b7':'1':%pAddr(f19));
       screen_setFK(A.lFKs:x'b8':'1':%pAddr(f20));
       screen_setFK(A.lFKs:x'bc':'1':%pAddr(f24):'F24=Grid');
       screen_setFK(A.lFKs:x'f1':'1':%pAddr(Enter));
       screen_setFK(A.lFKs:x'f4':'1':%pAddr(rollUP));
       screen_setFK(A.lFKs:x'f5':'1':%pAddr(rolldown));
       //‚Load options
       screen_SetOption(A.lOpts:'5':'5=Data');
       screen_SetOption(A.lOpts:'j':'j=Journal');
       if g.fSubEntries;
         screen_SetOption(A.lOpts:'d':'d=develop');
         screen_SetOption(A.lOpts:'r':'r=reduce');
       endIf;
       zCH=screen_getChoicesEntitle(A.lOpts);
       //‚Title display
       zTL='Work with analysis '
          +journal.text
          +' ['+journal.ID+']';
       //‚work screens
       g.pScreen=%pAddr(screen1);
       g.lVariant1=tree_getFirst(g.lEntries);
       wrkScreens();
       //‚end of program
       ifs_Close(g.hDta);
       tree_dealloc(a.lFKs);
       tree_dealloc(g.lJournal);
       *inlr=*on;
      //‚--------------------------------------------------------------------
      //‚loop on screens
      //‚--------------------------------------------------------------------
     pwrkScreens       b
     d wrkScreens      pi
      *
     d Screen          pr                  extproc(g.pScreen)
       //‚loop on screens
       dow g.pScreen<>*null;
         screen();
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Screen 1 - list of entries about journal analysis
      //‚--------------------------------------------------------------------
     p Screen1         b
     d  Screen1        pi
     d fkProcess       pr                  extproc(pAction)
      *
     d pAction         s               *   procptr
     d fcontrol        s               n
       //‚refresh the work area
       if g.lVariant1<>g.lVariant1_b4
       or g.fRefresh
       or screen_toRefresh();
         zFK=screen_getfkentitle(A.lFKs);
         loadLabel();
         loadwa1();
       endif;
       //‚refresh the subfile
       if g.lVariant1<>g.lVariant1_b4
       or g.fRefresh
       or screen_toRefresh();
         loadSfl1();
       endIf;
       //‚display the limits
       displayLimits();
       //‚display activation
       write msgCtl;
       write hdr1;
       sflDsp=*on;
       sflClr=*off;
       exfmt ctl1;
       msg_rmvPM(pgmID);
       csrtorow=0;
       csrtocol=0;
       g.error=*off;
       //‚get/launch function key
       screen_processFK(pgmID:A.lFKs:wsds.kp:%pAddr(control));
     p                 e
      //‚--------------------------------------------------------------------
      //‚display the limits
      //‚--------------------------------------------------------------------
     p displayLimits   b
     d lXView          s               *
     d  XView          ds                    likeDS(tXView) based(pXView)
     d  leftColumn     ds                    likeDs(tColumn) based(pLeftcolumn)
     d  rightColumn    ds                    likeDs(tColumn) based(pRightColumn)
       lXView=tree_getfirst(a.lXViews);
       dow lXView<>*null;
         pXView=tree_getItem(lXView);
         pleftColumn=tree_getItem(XView.left.lColumn);
         prightColumn=tree_getItem(XView.right.lColumn);

         lXView=tree_getNext(lXView);
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Load label
      //‚--------------------------------------------------------------------
     p loadLabel       b
       if filters.activated;
         zLabel=x'2b'+' FILTER ACTIVATED ';
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Load screen work area
      //‚--------------------------------------------------------------------
     p loadwa1         b
      *
     d lVariant        s               *
     d NO              s              3u 0 inz(0)
     d lXview          s               *
     d lYview          s               *
     d lXview$         s               *
       clear g.Item;
       lVariant=tree_getCurrent(g.lVariant1:%pAddr(filterValidator));
       dow lVariant<>*null;
         //‚Check if enought row remains
         if NO=20;
           leave;
         endif;
         //‚store view+entry
         NO+=1;
         g.lVariant9=lVariant;
         if breakOnXView(lXView:lYView:lXView$:lVariant);
           g.Item(no).lVariant=lXView;
           g.Item(no).lXView=lXView;
         else;
           g.Item(no).lVariant=lVariant;
           g.Item(no).lXView=lXView$;
           g.Item(no).lYView=lYView;
           lVariant=
           tree_getNextToDisplay(g.lEntries:lVariant:%pAddr(filterValidator));
         endIf;
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚break on XView
      //‚--------------------------------------------------------------------
     pbreakOnXView     b
     d breakOnXView    pi              n
     d  lXView                         *
     d  lYView                         *
     d  lXView$                        *
     d  lVariant                       *   const
      *
     d entry           ds                  likeDS(tEntry)    based(pEntry)
     d subEntry        ds                  likeDS(tSubEntry) based(pSubEntry)
       if tree_isofthekind(kEntry:lVariant:pEntry);
         lYView=Entry.lYView;
         lXView$=Entry.lXView;
       elseif tree_isofthekind(kSubEntry:lVariant:pSubEntry);
         lYView=SubEntry.lYView;
         lXView$=SubEntry.lXView;
       endIf;
       if lXView$<>*null and lXView<>lXView$;
         lXView=lXView$;
         return *on;
       endIf;
       return *off;
     p                 e
      //‚--------------------------------------------------------------------
      //‚filter validator  0=Skip 1=Take it
      //‚--------------------------------------------------------------------
     pfilterValidator  b
     dfilterValidator  pi             3i 0
     d  lVariant                       *   const
      *
     d entry           ds                  likeDs(tEntry)    based(pEntry)
     d lJrnEntryFmt    s               *
     d  JrnEntryFmt    ds                  likeDs(tFormat)based(pJrnEntryFmt)
     d lFilter         s               *
     d filters         ds                  likeDs(tFilters) based(pFilters)
     d filter          ds                  likeDs(tFilter) based(pFilter)
     d lStat           s               *
     d stat            ds                  likeDs(tStat) based(pStat)
     d val             s             50a   varying
       //‚No filter input
       if g.lFilters=*null;
         return 1;
       endIf;
       //‚Entry only taken in account for the filter
       if tree_isofthekind(kSubEntry:lVariant);
         return 1;
       else;
         pEntry=tree_getItem(lVariant);
       endif;
       //‚filter is activated?
       pFilters=tree_getItem(g.lFilters);
       if not Filters.activated;
         return 1;
       endif;
       //‚load journal entry format
       lJrnEntryFmt=fmt_getFormat(a.lFmts:'JRNENTRY':'Y');
       pjrnEntryFmt=tree_getItem(lJrnEntryFmt);
       JrnEntryFmt.pBuffer1=%addr(Entry.det);
       //‚loop on filters
       lFilter=tree_getFirst(g.lFilters);
       dow lFilter<>*null;
         pFilter=tree_getItem(lFilter);
         lStat=tree_getLinkFromList(g.lStats:kStat:filter.ID);
         pStat=tree_getItem(lStat);
         val=int_formulaExec(stat.lFormula);
         if tree_getLinkFromList(lFilter:kOmit:val)<>*null;
           return 0;
         endif;
         lFilter=tree_getNext(lFilter);
       endDo;
       return 1;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Load lines of subfile
      //‚--------------------------------------------------------------------
     ploadSFl1         b
     d loadSFl1        pi
      *
     d lVariant        s               *
     d lXView          s               *
     d fCase           s              3i 0
       //‚clear subfile
       sflDsp=*off;
       sflClr=*on;
       WRITE ctl1;
       g.cantabRight=*off;
       g.cantabLeft =*off;
       if g.item(1).lVariant=*null;
         sflRrn1=1;
         *in01=*on;
         xFil1=x'20'+'(No entries displayable)';
         write sfl1;
       endif;
       //‚load the subfile according to the work table
       for sflRrn1=1 to 20;
         //‚Leave if no item
         lVariant=g.Item(sflRrn1).lVariant;
         if lVariant=*null;
           leave;
         endif;
         lXView=g.Item(sflRrn1).lXView;
         if tree_isofthekind(kXView:lVariant);
           //‚1) Load headers
           *in01=*on;
           loadSFL1A(lVariant);
         else;
           *in01=*off;
           //‚2) Load option
           loadSFL1B(lVariant);
           //‚3) Determine if the current entry is linked to another
           fCase=getCase(lVariant);
           //‚4) journal part
           loadSFL1c(lVariant:fCase);
           //‚5) data part
           loadSFL1d(lXView:lVariant:fCase);
           //‚6) To avoid no displayable characters
           xfil=int_chkDisplay(Min+Maj+num+spec+spec2+colors+' '
                              :xfil);
           //‚7) Sub-format?
           *in03=tree_getFirst(lVariant)<>*null;
         endIf;
         write sfl1;
       endFor;
       //
       g.lVariant1_b4=g.lVariant1;
       g.lVariant9_b4=g.lVariant9;
       g.fRefresh=*off;
       //‚more item or bottom of list
       screen_setSflEnd(mySflEnd:
        tree_getNextToDisplay(g.lEntries:g.lVariant9:%pAddr(filterValidator))
                       =*null);
     p                 e
      //‚--------------------------------------------------------------------
      //‚Load lines of subfile / headers
      //‚--------------------------------------------------------------------
     ploadSFl1A        b
     d loadSFl1A       pi
     d  lVariant                       *   const
      *
     d xView           ds                  likeDs(tXView)  based(pXView)
       //‚Load line according to the kind of corresponding item
       if not tree_isofthekind(kXView:lVariant:pXView);
         return;
       endIf;
       //‚header
       xFil1='';
       if sflrrn1=1;
         xFil1='Opt'+jrnXView.hdrs;
       endif;
       %subst(xfil1:%len(jrnXView.hdrs)+4)=x'22'+'|';
       %subst(xfil1:%len(jrnXView.hdrs)+6)
       =xview_setHdrs(XView:%len(jrnXView.hdrs)+2);
       g.canTabRight=g.canTabRight or not XView.right.most;
       g.canTabLeft =g.canTabLeft  or not XView.Left.most;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Load lines of subfile / option
      //‚--------------------------------------------------------------------
     ploadSFl1B        b
     d loadSFl1B       pi
     d  lVariant                       *   const
      *
       xCho=tree_getOption(lVariant);
       if g.lVariant_last=lVariant;
         csrToCol=3;
         csrToRow=sflRrn1+6-1;
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Load journal part
      //‚--------------------------------------------------------------------
     ploadSFl1C        b
     d loadSFl1C       pi
     d  lVariant                       *   const
     d  fCase                         3i 0 const
      *
     d fmt             ds                  likeds(tFormat) based(pFmt)
     d entry           ds                  likeDs(tEntry) based(pEntry)
     d entry0          ds                  likeDs(tEntry) based(pEntry0)
       xFil='';
       if tree_isofthekind(kEntry:lVariant:pEntry);
         pFmt=tree_getitem(jrnXView.lFmt);
         fmt.pBuffer1=%addr(entry.det);
         if entry.pEntry0<>*null;
           pEntry0=entry.pEntry0;
           fmt.pBuffer0=%addr(entry0.det);
         endif;
         loadSFC1(jrnXView:xFil:fCase);
       endIf;
       %subst(xfil:%len(jrnXView.hdrs)+1)=x'22'+'|';
     p                 e
      //‚--------------------------------------------------------------------
      //‚Load data part
      //‚--------------------------------------------------------------------
     ploadSFl1D        b
     d loadSFl1D       pi
     d  lXView                         *   const
     d  lVariant                       *   const
     d  fCase                         3i 0 const
      *
     d XView           ds                  likeDs(tXView) based(pXView)
     d fmt             ds                  likeds(tFormat) based(pFmt)
     d entry           ds                  likeDs(tEntry) based(pEntry)
     d entry0          ds                  likeDs(tEntry) based(pEntry0)
     d subEntry        ds                  likeDs(tSubEntry) based(pSubEntry)
     d pos             s             10u 0
       if lXView=*null;
         return;
       endIf;
       pXView=tree_getItem(g.Item(sflRrn1).lXView);
       pFmt=tree_getItem(xView.lFmt);
       if tree_isofthekind(kEntry:lVariant:pEntry);
         pos=0;
       elseif tree_isofthekind(kSubEntry:lVariant:pSubEntry);
         pEntry=tree_getItem(tree_getParent(lVariant));
         pos=subEntry.pos;
       endIf;
       ifs_lseek(g.hDta:entry.det.apos+pos:0);
       ifs_read(g.hDta:Fmt.pBuffer1:Fmt.len);
       if Entry.pEntry0<>*null;
         pEntry0=Entry.pEntry0;
         ifs_lseek(g.hDta:entry0.det.apos+pos:0);
         ifs_read(g.hDta:Fmt.pBuffer0:Fmt.len);
       endif;
       loadSFC1(XView:xFil:fCase);
     p                 e
      //‚--------------------------------------------------------------------
      //‚case -1=Deleted,0=Not changed,1=Changed
      //‚--------------------------------------------------------------------
     pgetCase          b
     d getCase         pi             3i 0
     d  lVariant                       *   const
      *
     d  entry          ds                  likeds(tEntry) based(pEntry)
       //‚validate the entry
       if not tree_isofthekind(kEntry:lVariant:pEntry);
         pEntry=tree_getItem(tree_getParent(lVariant));
       endif;
       //‚4) to setup the color
       if entry.det.ENTT='DL'
       or entry.det.ENTT='DR';
         return -1;
       else;
         return %int(entry.pEntry0<>*null);
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Load subfile columns
      //‚--------------------------------------------------------------------
     ploadSFC1         b
     d loadSFC1        pi
     d XView                               likeDs(tXView) const
     d xFil                         128
     d fCase                          3i 0 const
      *
     d lColumn         s               *
     d Column          ds                  likeDs(tColumn) based(pColumn)
     d string          s          32000a
       //‚Loop on each cell
       lColumn=XView.left.lColumn;
       dow 1=1;
         pColumn=tree_getItem(lColumn);
         string=int_FormulaExec(column.lFormula);
         //‚1) Attribut of the cell
         if fCase=0;
           //‚no change on the record
           %subst(xFil:Column.pos-1:1)=XView.Detcolor;
         elseif fCase=-1;
           //‚record deleted
           %subst(xFil:Column.pos-1:1)=x'2b';
         elseif int_FormulaExec(column.lFormula:0)<>string;
           //‚field has been changed
           %subst(xFil:Column.pos-1:1)=XView.ChgColor;
         else;
           //‚no change on the field
           %subst(xFil:Column.pos-1:1)=XView.Detcolor;
         endIf;
         //‚2) Fill the value of the field
         if lColumn=XView.right.lColumn;
           //‚right column
           %subst(xFil:Column.pos:XView.right.width)
           =%subst(String:XView.right.pos:XView.right.width);
           if Column.pos+XView.right.width<%len(xFil);
             //‚right attribut
             %subst(xFil:Column.pos+XView.right.width:1)=x'20';
           endif;
           return;
         elseif lColumn=XView.left.lColumn;
           //‚left column
           %subst(xFil:Column.pos:XView.left.width)
           =%subst(String:XView.left.pos:XView.left.width);
         else;
           //‚mid column
           %subst(xFil:Column.pos)=%subst(String:1:column.maxWidth);
         endif;
         lColumn=tree_getNext(lColumn);
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚control input
      //‚--------------------------------------------------------------------
     pControl          b
     d Control         pi              n
      *
     d lVariant        s               *
     d entry           ds                  likeDS(tEntry)    based(pEntry)
     d subEntry        ds                  likeDS(tSubEntry) based(pSubEntry)
       readc sfl1;
       dow not %eof();
         *in02=*off;
         if %scan(xCho:' 5jdr')=0;
           msg_SndPM(pgmID:'Option "'+xCho+'" is not valid');
           g.error=*on;
           *in02=*on;
         elseif %scan(xCho:'dr')>0
         and tree_getfirst(g.Item(sflRrn1).lVariant)=*null;
           msg_SndPM(pgmID:'Option "'+xCho
                          +'" is only valid on entry with sub-format');
           g.error=*on;
           *in02=*on;
         elseif xCho='5'
         and    g.item(sflrrn1).lYView=*null;
           msg_SndPM(pgmID:'Option "'+xCho+'" is not valid');
           g.error=*on;
           *in02=*on;
         endif;
         *in03=tree_getFirst(g.Item(sflRrn1).lVariant)<>*null;
         update sfl1;
         tree_setOption(g.Item(sflRrn1).lVariant:xCho);
         readc sfl1;
       enddo;
       return g.error;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Roll-UP
      //‚--------------------------------------------------------------------
     pRollUp           b
     d RollUp          pi
      *
     d lVariant        s               *
     d lXView          s               *
     d lYView          s               *
     d lXView$         s               *
     d NO              s              3u 0 inz(0)
       if tree_getPrevToDisplay(g.lEntries:g.lVariant1:%pAddr(filterValidator))
       =*null;
         msg_SndPM(pgmID:'You have reached the top of the list');
         return;
       endIf;
       lVariant
       =tree_getPrevtoDisplay(g.lEntries:g.lVariant1:%pAddr(filterValidator));
       dow lVariant<>*null;
         if no=20;
           return;
         endif;
         g.lVariant1=lVariant;
         if breakOnXView(lXView:lYView:lXView$:lVariant);
           no+=1;
         else;
           no+=1;
           lVariant
           =tree_getPrevtoDisplay(g.lEntries:lVariant:%pAddr(filterValidator));
         endif;
       enddo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Roll-down
      //‚--------------------------------------------------------------------
     pRollDown         b
     d RollDown        pi
       if mySflEnd='Bottom';
         msg_SndPM(pgmID:'You have reached the bottom of the list');
       else;
         g.lVariant1=
         tree_getNextToDisplay(g.lEntries:g.lVariant9:%pAddr(filterValidator));
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Enter
      //‚--------------------------------------------------------------------
     pEnter            b
     d Enter           pi
      *
     d lVariant        s               *
     d rtnCode         s              3i 0
     d option          s              1a
      *
      /copy cpy,jrnentdp_h
       //‚loop on each entry
       lVariant=tree_getFirst(g.lEntries);
       dow lVariant<>*null;
         option=tree_getOption(lVariant);
         if option='r';
           tree_closeLink(lVariant);
           g.fRefresh=*on;
           tree_setOption(lVariant:'');
           g.lVariant_last=lVariant;
         elseif option='d';
           tree_openLink(lVariant);
           g.fRefresh=*on;
           tree_setOption(lVariant:'');
           g.lVariant_last=lVariant;
         elseif %scan(option:'5j')>0;
           g.fRefresh=*on;
           jrnEntDp(rtncode:option
                   :ztl
                   :lVariant
                   :g.hDta
                   :a.lYViews:a.lFmts:a.lForms);
           g.lVariant_last=lVariant;
           if rtnCode>0;
             tree_setOption(lVariant:'');
           elseif rtnCode=0;
             leave;
           else;
             leave;
           endIf;
         endIf;
         lVariant=tree_getNexttoDisplay(g.lEntries:lVariant);
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F1=Where am I?
      //‚--------------------------------------------------------------------
     pf1               b
     d f1              pi
      *
     d lColumn         s               *
     d column          ds                  likeds(tColumn) based(pColumn)
     d posOnColumn     s              5u 0
       csrtorow=wsds.csrfromrow;
       csrtocol=wsds.csrfromcol;
       if SFLCSRRRN=0
       or wsds.CsrFromCol<=margin
       or  wsds.CsrFromCol>margin+%len(jrnxView.hdrs)
       and wsds.CsrFromCol<margin+%len(jrnxView.hdrs)+3;
         msg_SndPM(pgmID:'Wrong cursor position');
       elseif wsds.CsrFromCol-margin<=%len(jrnxView.hdrs);
         xview_getColumnAtPos(lJrnXView
                             :wsds.CsrFromCol-margin
                             :lColumn
                             :posOnColumn);
         pColumn=tree_getItem(lColumn);
         msg_SndPM(pgmID:'You are on the column '+%trim(column.formula)
                        +' '+%char(posOnColumn));
       elseif xview_getColumnAtPos(g.Item(sflcsrrrn).lXView
                                  :wsds.CsrFromCol-margin
                                  :lColumn
                                  :posOnColumn);
         pColumn=tree_getItem(lColumn);
         msg_SndPM(pgmID:'You are on the column '+%trim(column.formula)
                        +' '+%char(posOnColumn));
       else;
         msg_SndPM(pgmID:'No displayed column at the specified position');
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F2=Filters
      //‚--------------------------------------------------------------------
     pf2               b
     d f2              pi
     d rtnCode         s              3i 0
      /copy cpy,filterup_h
       filterUP(rtncode:g.lStats:g.lFilters);
       g.fRefresh=*on;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F3=Exit
      //‚--------------------------------------------------------------------
     pf3               b
     d f3              pi
       G.pScreen=*null;
       xml_tree2xml(g.anzJrnPath:g.lJournal:%paddr(jrn_xmloutput));
     p                 e
      //‚--------------------------------------------------------------------
      //‚F6=to left
      //‚--------------------------------------------------------------------
     pf6               b
     d f6              pi
      *
     d lColumn         s               *
     d posOnColumn     s              5u 0
     d XView           ds                  likeDS(tXView) based(pXView)
       csrtorow=wsds.csrfromrow;
       csrtocol=wsds.csrfromcol;
       if SFLCSRRRN>0
       and xview_getColumnAtPos(g.Item(sflcsrrrn).lXView
                               :wsds.CsrFromCol-margin
                               :lcolumn
                               :posOnColumn);
         pXView=tree_getItem(g.Item(sflcsrrrn).lXView);
         xview_posAtLeft(XView
                        :g.freePartWidth
                        :lcolumn
                        :posOnColumn);
         csrtocol=3;
         g.fRefresh=*on;
       else;
         msg_SndPM(pgmID:'No displayed column at the specified position');
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F7=Left tab
      //‚--------------------------------------------------------------------
     pf7               b
     d f7              pi
      *
     d XView           ds                  likeDs(tXView) based(pXView)
       csrtorow=wsds.csrfromrow;
       csrtocol=wsds.csrfromcol;
       if SFLCSRRRN=0 or g.Item(1).lVariant=*null;
         msg_SndPM(pgmID:'Wrong cursor position');
       else;
         csrtocol=3;
         pXView=tree_getItem(g.item(SFLCSRRRN).lXView);
         if XView.left.most;
           msg_SndPM(pgmID:'Format is on the most left position');
         else;
           xview_TabLeft(XView:g.freePartWidth);
           g.fRefresh=*on;
         endIf;
       endif;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F8=Right tab
      //‚--------------------------------------------------------------------
     pf8               b
     d f8              pi
      *
     d XView           ds                  likeDs(tXView) based(pXView)
       csrtorow=wsds.csrfromrow;
       csrtocol=wsds.csrfromcol;
       if SFLCSRRRN=0 or g.Item(1).lVariant=*null;
         msg_SndPM(pgmID:'Wrong cursor position');
       else;
         csrtocol=3;
         pXView=tree_getItem(g.item(SFLCSRRRN).lXView);
         if XView.Right.most;
           msg_SndPM(pgmID:'Format is on the most right position');
         else;
           xview_TabRight(XView:g.freePartWidth);
           g.fRefresh=*on;
         endIf;
       endif;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F10=Move to top
      //‚--------------------------------------------------------------------
     pf10              b
     d f10             pi
       if SFLCSRRRN=0 or g.Item(1).lVariant=*null;
         msg_SndPM(pgmID:'Wrong cursor position');
       elseif tree_getKind(g.Item(sflcsrrrn).lVariant)=kXView;
         g.lVariant1=g.Item(sflcsrrrn+1).lVariant;
       else;
         g.lVariant1=g.Item(sflcsrrrn).lVariant;
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F11=display all/apply filter
      //‚--------------------------------------------------------------------
     pf11              b
     d f11             pi
      *
     d filters         ds                  likeDS(tFilters) based(pFilters)
       pFilters=tree_getItem(g.lFilters);
       filters.activated=not filters.activated;
       zLabel='';
       g.fRefresh=*on;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F18=Position all views on the left
      //‚--------------------------------------------------------------------
     pf18              b
     d f18             pi
      *
     d lXView          s               *
     d XView           ds                  likeDs(tXView) based(pXView)
       if g.canTabLeft;
         lXView=tree_getFirst(a.lXViews);
         dow lXView<>*null;
           if lXView<>lJrnXView;
             pXView=tree_getItem(lXView);
             xview_posToMostLeft(XView:g.freePartWidth);
           endIf;
           lXView=tree_getNext(lXView);
         endDo;
         g.fRefresh=*on;
       else;
         msg_SndPM(pgmID:'Formats displayed are on the most left position');
       endif;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F19=Left tab on all
      //‚--------------------------------------------------------------------
     pf19              b
     d f19             pi
      *
     d lXView          s               *
     d XView           ds                  likeDs(tXView) based(pXView)
       if g.canTabLeft;
         lXView=tree_getFirst(a.lXViews);
         dow lXView<>*null;
           pXView=tree_getItem(lXView);
           xview_TabLeft(XView:g.freePartWidth);
           lXView=tree_getNext(lXView);
         endDo;
         g.fRefresh=*on;
       else;
         msg_SndPM(pgmID:'Formats displayed are on the most left position');
       endif;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F20=Right
      //‚--------------------------------------------------------------------
     pf20              b
     d f20             pi
      *
     d lXView          s               *
     d XView           ds                  likeDs(tXView) based(pXView)
       if g.canTabRight;
         lXView=tree_getFirst(a.lXViews);
         dow lXView<>*null;
           pXView=tree_getItem(lXView);
           xview_tabRight(XView:g.freePartWidth);
           lXView=tree_getNext(lXView);
         endDo;
         g.fRefresh=*on;
       else;
        msg_SndPM(pgmID:'Formats displayed are on the most right position');
       endif;
     p                 e
      //‚--------------------------------------------------------------------
      //‚F24=Grid
      //‚--------------------------------------------------------------------
     pf24              b
     d f24             pi
      /copy cpy,gridup_h
     d lXView          s               *
     d  XView          ds                  likeDs(tXView) based(pXView)
     d lGrid           s               *
     d  Grid           ds                  likeDs(tGrid) based(pGrid)
     d  gridID         s             10a   varying
     d  Column         ds                  likeDs(tColumn) based(pColumn)
     d  columnID       s             10a   varying
       if SFLCSRRRN=0;
         msg_SndPM(pgmID:'Wrong cursor position');
       else;
         lXView=g.item(sflcsrrrn).lXview;
         pXView=tree_getItem(lXView);
         lGrid=XView.lGrid;
         pGrid=tree_getItem(lGrid);
         gridID=grid.ID;
         gridUP(rtnCode:grid.ID);
         if rtnCode=fContinue;
           xview_reloadGrid(xview:a.lGrids:lGrid:grid.ID:g.freePartWidth);
           g.fRefresh=*on;
         endIf;
       endIf;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Entries load
      //‚--------------------------------------------------------------------
     pEntriesLoad      b
     d EntriesLoad     pi
     d lEntry          s               *
     d Entry           ds                  likeDs(tEntry) based(pEntry)
     d lFile           s               *
     d File            ds                  likeDs(tFile) based(pFile)
     d lFmt            s               *
       //‚Files are loaded from analysis
       lEntry=tree_getFirst(g.lEntries);
       dow lEntry<>*null;
         pEntry=tree_getItem(lEntry);
         if entry.det.code='R' and entry.det.entt<>'IL';
           //‚Files are loaded from object
           lFile=file_getFile(g.lFiles:%trim(entry.det.obj));
           //‚Load the corresponding XVIew
           if lFile<>*null;
             pFile=tree_getItem(lFile);
             lFmt=fmt_getFormat(a.lFmts:File.format);
            entry.lXView=xview_getXView(a.lXViews:a.lGrids:a.lFmts:File.format);
            entry.lYView=yview_getYView(a.lYViews:a.lForms:a.lFmts:File.format);
             SubEntriesLoad(lEntry:lFmt:0);
           endif;
         endif;
         lEntry=tree_getNext(lEntry);
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚load models
      //‚--------------------------------------------------------------------
     pModelsLoad       b
     d ModelsLoad      pi
      *
     d lJrnEntryFmt    s               *
     d  JrnEntryFmt    ds                  likeDs(tFormat)based(pJrnEntryFmt)
     d lEntry          s               *
     d Entry           ds                  likeDs(tEntry) based(pEntry)
     d lStat           s               *
     d stat            ds                  likeDS(tStat) based(pStat)
       //‚load journal entry format
       lJrnEntryFmt=fmt_getFormat(a.lFmts:'JRNENTRY':'Y');
       pjrnEntryFmt=tree_getItem(lJrnEntryFmt);
       //‚load formulas for stat
       g.lStats=tree_Xml2Tree(env_getAppliPath+'jrnAnzStat.xml'
                                   :%pAddr(stat_XmlInput));
       lStat=tree_getFirst(g.lStats);
       dow lStat<>*null;
         pStat=tree_getItem(lStat);
         stat.lFormula=int_FormulaLoad(stat.formula:lJrnEntryFmt);
         lStat=tree_getNextToDisplay(g.lStats:lStat);
       endDo;
       //‚loop on each entries
       lEntry=tree_getFirst(g.lEntries);
       dow lEntry<>*null;
         pEntry=tree_getItem(lEntry);
         JrnEntryFmt.pBuffer1=%addr(Entry.det);
         ModelsLoad2(*null:g.lStats);
         lEntry=tree_getNext(lEntry);
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚load models (part 2)
      //‚--------------------------------------------------------------------
     pModelsLoad2      b
     d ModelsLoad2     pi
     d  lModels_                       *   const
     d  lStats                         *   const
      *
     d  lModels        s               *
     d  lModel         s               *
     d  lStat          s               *
     d  stat           ds                  likeDS(tStat)  based(pStat)
     d  model          ds                  likeDS(tModel) based(pModel)
     d  modelID        s             50a   varying
       lStat=tree_getFirst(lStats);
       dow lStat<>*null;
         pStat=tree_getItem(lStat);
         if lModels_<>*null;
           lModels=lModels_;
         elseif Stat.lModels<>*null;
           lModels=Stat.lModels;
         else;
           stat.lModels=tree_getNewLink(*null);
           lModels=Stat.lModels;
         endIf;
         modelID=int_formulaExec(stat.lFormula);
         lModel=tree_getLinkFromList(lModels:kModel:modelID);
         if lModel=*null;
           pModel=tree_getNewItem(%addr(tModel):%size(tModel));
           model.ID=modelID;
           model.statID=Stat.ID;
           tree_linkToParent(lModels:tree_getNewLink(pModel));
         else;
           pModel=tree_getItem(lModel);
         endIf;
         model.count+=1;
         modelsLoad2(stat.lModels:lStat);
         lStat=tree_getNext(lStat);
       endDo;
     p                 e
      //‚--------------------------------------------------------------------
      //‚Sub-Entries load
      //‚--------------------------------------------------------------------
     pSubEntriesLoad   b
     d SubEntriesLoad  pi
     d  lEntry                         *   const
     d  lParentFmt                     *   const
     d  pos                          10u 0 value
      *
     d  entry          ds                  likeDs(tEntry)  based(pEntry)
     d  ParentFmt      ds                  likeDs(tFormat) based(pParentFmt)
     d  lSubFormats    s               *
     d  lSubFormat     s               *
     d  SubFormat      ds                  likeDs(tSubFormat) based(pSubFormat)
     d  formatID       s             10A   varying
     d  lFormat        s               *
     d  SubEntry       ds                  likeDs(tSubEntry) based(pSubEntry)
      *
       lSubFormats=tree_getLinkFromList(lParentFmt:kSubFormats);
       if lSubFormats=*null;
         return;
       endif;
       pEntry=tree_getItem(lEntry);
       pParentFmt=tree_getItem(lParentFmt);
       ifs_lseek(g.hDta:entry.det.aPos+pos:0);
       ifs_read(g.hDta:ParentFmt.pBuffer1:ParentFmt.len);
       lSubFormat=tree_getFirst(lSubformats);
       dow lSubFormat<>*null;
         pSubFormat=tree_getItem(lSubFormat);
         formatID=int_FormulaExec(SubFormat.lFormula);
         lFormat=fmt_getFormat(a.lFmts:formatID);
         if lFormat<>*null;
          if tree_getLinkFromList(lFormat:kFields)<>*null;
            g.fSubEntries=*on;
            pSubEntry=tree_getNewItem(%addr(tSubEntry):%size(tSubEntry));
            SubEntry.lXView=xview_getXView(a.lXViews:a.lGrids:a.lfmts:formatID);
            SubEntry.lYView=yview_getYView(a.lYViews:a.lForms:a.lfmts:formatID);
            SubEntry.pos=subFormat.pos+pos;
            SubEntry.fmtID=formatID;
            tree_linktoparent(lEntry:tree_getnewlink(pSubEntry));
            tree_closeLink(lEntry);
          endIf;
          SubEntriesLoad(lEntry:lFormat:subFormat.pos+pos);
         endIf;
         lSubFormat=tree_getNext(lSubformat);
       endDo;
     p                 e
