        // Elabora richiesta di chiamate http fatte da un programma esterno
        Ctl-Opt  DftActGrp(*no)
          ActGrp(*StgMdl)
          StgMdl(*SNGLVL)
          Bnddir('AL400MNUV2': 'WEBSCKDIR' : 'TESTBND')
          Thread(*Concurrent)
          Option(*NoUnRef :*SrcStmt :*NoDebugIo)
          DatFmt(*Iso) TimFmt(*Iso)
          Debug(*Constants)
          AlwNull(*UsrCtl)
          DftName(TESTWPOS1)
          Text('Test contattone');
        // ___________________________________________________________________
        /Include QSYSINC/QRPGLESRC,PTHREAD
        /Include Roberto/qrpglesrc,copy_pr
        /Include Roberto/qrpglesrc,copy_ds

        /copy Al400mnuv2/QRpgleSrc,UMiFunc_h
        // Prototipi
        Dcl-Pr TESTWPOS1 ExtPgm('TESTWPOS1');
        End-Pr TESTWPOS1;

        Dcl-Pi TESTWPOS1;
        End-Pi TESTWPOS1;

        Dcl-S ThreadId    Char(20);
        Dcl-S ThreadIdPt  Pointer Inz(%addr(threadid));

        // ____________________________________________________________________________

        *Inlr = *on;

      *           passa descrittore al thread, con pad x'00'
     c                   z-add     0             wpos              2 0    30
     c     loopxxx       tag
     c                   eval      wpos = %len(%trim(ThreadId))
     c                   if        wpos < 20
     c                   eval      %subst(ThreadId:wpos+1:1) = x'00'
     c                   goto      loopxxx
     c                   endif

        Return;
