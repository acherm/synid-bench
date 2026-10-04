    ctl-opt dftactgrp(*no) ;                         
                                                     
    dcl-pr OpenFile int(10) extproc('open') ;        
      *n pointer value options(*string) ;            
      *n int(10) value ;                             
      *n uns(10) value options(*nopass) ;            
      *n uns(10) value options(*nopass) ;            
      *n uns(10) value options(*nopass) ;            
     end-pr ;                                        
                                                     
     dcl-pr ReadFile int(10) extproc('read') ;       
       *n int(10) value ;                            
       *n pointer value ;                            
       *n uns(10) value ;                            
     end-pr ;                                        
                                                     
     dcl-pr WriteFile int(10) extproc('write') ;     
       *n int(10) value ;                            
       *n pointer value ;                            
       *n pointer value ;                                 
       *n uns(10) value ;                                 
     end-pr ;                                             
                                                          
     dcl-pr CloseFile int(10) extproc('close') ;          
       *n  int(10) value ;                                
     end-pr ;                                             
                                                          
     dcl-c O_RDONLY 1 ;           //Read only             
     dcl-c O_WRONLY 2 ;           //Writing               
     dcl-c O_CREAT  8 ;           //Create                
     dcl-c O_TRUNC 64 ;           //truncate              
     dcl-c O_TEXTDATA 16777216 ;  //Open in text mode     
     dcl-c O_CCSID 32 ;           //CCSID                 
                                                          
    // owner authority                                    
    dcl-c S_IRUSR 256 ;                                   
    dcl-c S_IWUSR 128 ;                                   
    dcl-c S_IXUSR 64  ;                                   
    dcl-c S_IRWXU 448 ;                                   
    dcl-c S_IRWXU 448 ;               
    // group authority                
    dcl-c S_IRGRP 32  ;               
    dcl-c S_IWGRP 16  ;               
    dcl-c S_IXGRP 8   ;               
    dcl-c S_IRWXG 56  ;               
    // other people                   
    dcl-c S_IROTH 4   ;               
    dcl-c S_IWOTH 2   ;               
    dcl-c S_IXOTH 1   ;               
    dcl-c S_IRWXO 7   ;               
                                      
                                      
     dcl-s fd int(10) ;               
     dcl-s Length int(10) ;           
     dcl-s Data char(100) ;           
     dcl-s Array char(100) dim(20) ;  
     dcl-s Element packed(3) ;        
     dcl-s Start packed(3) ;          
     dcl-s End like(Start) ;          
     dcl-s End like(Start) ;                                      
     dcl-s Mode uns(10);                                          
     dcl-s Flags uns(10);                                         
     dcl-c Path '/tmp/tmp22.txt' ;                                
                                                                  
     mode  = S_IRUSR + S_IWUSR  + S_IRGRP + S_IROTH ;             
                                                                  
     fd = OpenFile(Path :                                         
                   O_WRONLY + O_CREAT + O_TRUNC :                 
                   mode :                                         
                   37) ;                                          
     if (fd < 0) ;                                                
       dsply ('IFS file ' + path + ' could not be opened') ;      
       *inlr = *on ;                                              
       return ;                                                   
     endif ;                                                      
                                                                  
     data = 'Hi from RPG!';                                       
                                                                  
     WriteFile(fd: %addr(data): %size(data));                     
     WriteFile(fd: %addr(data): %size(data));      
                                                   
                                                   
    CloseFile(fd) ;                                
    *inlr = *on ;                                  
                                                                        