        ctl-opt NOMAIN option(*nodebugio:*srcstmt);

        Dcl-Proc Cities Export;
          Dcl-Pi *n Char(10);
            C_Val Char(3) Value;
          End-Pi;

          If C_Val = 'Kan';
            Return 'Kanpur';
          ElseIf C_Val = 'Del';
            Return 'Delhi';
          ElseIf C_Val = 'Lko';
            Return 'Lucknow';
          ElseIf C_Val = 'Noi';
            Return 'Noida';
          ElseIf C_Val = 'Kol';
            Return 'Kolkata';
          ElseIf C_Val = 'Che';
            Return 'Chennai';
          ElseIf C_Val = 'Mum';
            Return 'Mumbai';
          ElseIf C_Val = 'Var';
            Return 'Varanasi';
          EndIf;
        End-Proc;

        dcl-proc addprc export;
          dcl-pi *n packed(5:2);
            p_fld1 packed(5:2);
            p_fld2 packed(5:2);
          end-pi;
          dcl-s p_result packed(5:2);

          p_result = p_fld1 + p_fld2 + 5;
          p_fld1 = p_result;
          return p_result;
        end-proc;

        dcl-proc subtract export;
          dcl-pi *n packed(5:2);
            p_fld1 packed(5:2);
            p_fld2 packed(5:2);
          end-pi;
          dcl-s p_result packed(5:2);
          p_result = p_fld1 - p_fld2;
          return p_result;
        end-proc;

        Dcl-Proc Division Export;
          Dcl-Pi *n packed(5:2);
            p_fld1 packed(5:2);
            p_fld2 packed(5:2);
          End-Pi;
          Dcl-S P_Result packed(5:2);

          Monitor;
            p_result = p_fld1 / p_fld2;
          On-Error;
            p_result = *zero;
          EndMon;
            return p_result;
        End-proc;

        Dcl-proc Test1 export;
          dsply 'Hello';
        End-Proc;
