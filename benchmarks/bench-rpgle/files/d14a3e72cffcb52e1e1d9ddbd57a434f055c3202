**Free
       ctl-opt option(*srcstmt:*nodebugio);
       ctl-opt dftActgrp(*no) actGrp(*caller);

       /copy qwebsrcn,POSTCLOB_C

       dcl-pi postClob_t;
         email  char(30);
         name   char(25);
         gender char(10);
         status char(10);
       end-pi;
       //*****************************************************
       // MainLine
       //*****************************************************
       POSTCLOBV(email: name: gender: status);

       *inlr = *on;
