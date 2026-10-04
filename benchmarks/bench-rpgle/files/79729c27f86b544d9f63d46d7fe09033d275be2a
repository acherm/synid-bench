
**FREE
//--------------------------------------------------------------------------------------------------
// MIT License
// Copyright (c) 2020 Ghost +
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//-------------------------------------------------------------------------------------------------- 
ctl-opt option(*srcstmt: *nodebugio) datfmt(*iso) nomain;

/include QRPGLESRC,UTILITY_P

//--------------------------------------------------------------------------------------------------
// Procedure  : Utility_getSystemName
// Purpose    : Use ibm retrieval to get the name of the system.
// Returns    : systemName => The retrieved system name.
// Parameter/s: N/A
//--------------------------------------------------------------------------------------------------
dcl-proc Utility_getSystemName export;
  dcl-pi *n char(8) end-pi;

  dcl-pr QWCRNETA extpgm('QWCRNETA');
   *n char(32766) options(*varsize); 
   *n int(10) const; 
   *n int(10) const; 
   *n char(10) const;
   *n char(256); 
  end-pr;

  // Error code structure
  dcl-ds apiError len(256) end-ds;

  // Receiver variable for QWCRNETA
  dcl-ds apiData;
   filler char(32) inz;
   returnSystem char(8) inz;
  end-ds;

  dcl-c SYSTEM_NAME const('SYSNAME');

  QWCRNETA(apiData
         : %size(apiData)
         : 1
         : SYSTEM_NAME
         : apiError);

  return returnSystem;
end-proc;     

//--------------------------------------------------------------------------------------------------
// Procedure  : Common_getLastSpooledFileCreated
// Purpose    : Retrieves the job name, number, user and the spooled file name for the most recent
//              spooled file created within this job.
// Returns    : spooledFileDetails => Contains all response values of the job details.
// Parameter/s: N/A
//--------------------------------------------------------------------------------------------------
dcl-proc Common_getLastSpooledFileCreated export;
  dcl-pi *n likeDS(dt_spooledFileDetails);
  end-pi;

  dcl-pr getLastSpooledFile extpgm('QSPRILSP');
    receiver char(32767) options(*varsize);
    receiverLength int(10:0) const;
    formatName char(8)  const;
    error char(32767) options(*varsize);
  end-pr; 

  dcl-ds details likeDS(dt_spooledFileDetails) inz;

  dcl-ds SPRL0100 qualified;
    bytesReturned int(10:0) inz;
    bytesAvailable int(10:0) inz;
    spooledFileName char(10) inz;
    jobName char(10) inz;
    userName char(10) inz;
    jobNumber char(6) inz;
    spooledFileNumber int(10:0) inz;
    jobSystemName char(8) inz;
    spooledFileCreatedDate char(7) inz;
    *n char(1) inz;
    spooledFileCreatedTime char(6) inz;
  end-ds;

  dcl-ds apiError qualified;
    bytesProvided int(10:0) inz(%size(apiError));
    bytesAvailable int(10:0) inz;
    messageID char(7);
    *n char(1);
    messageData char(128);
  end-ds;

  getLastSpooledFile(SPRL0100 : %size(SPRL0100) : 'SPRL0100' : apiError);
  details.spooledFileName = %trim(SPRL0100.spooledFileName);
  details.spooledFileNumber = SPRL0100.spooledFileNumber;
  details.jobDetails.jobName = SPRL0100.jobName;
  details.jobDetails.userName = SPRL0100.userName;
  details.jobDetails.jobNumber = SPRL0100.jobNumber;

  return details;
end-proc;
