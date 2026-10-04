h datedit(*ymd.)                                               
 *                                                             
d i               s              3  0                          
d literal         s              8                             
 *                                                             
 /free                                                         
   clear i;                                                    
   dow 1 = 1;                                                  
     i += 1;                                                   
     if i > 100;                                               
       leave;                                                  
     endif;                                                    
                                                               
     if %rem(i:15) = *zeros;        // Divisible entre 3 y 5   
       literal = 'FIZZBUZZ';                                   
     else;                                                     
       if %rem(i:3) = *zeros;       // Divisible entre 3       
         literal = 'FIZZ';                                     
       else;                                                   
               if %rem(i:5) = *zeros;     // Divisible entre 5   
          literal = 'BUZZ';                               
        else;                                             
          literal = %editc(i:'X');                        
        endif;                                            
      endif;                                              
    endif;                                                
                                                          
    dsply %trim(literal);                                 
                                                          
  enddo;                                                  
  *inlr = *on;                                            
/end-free                                                 
*                                                         
