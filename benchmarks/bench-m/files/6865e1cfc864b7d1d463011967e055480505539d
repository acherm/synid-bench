
%********************consumption only
%********************no shares
% ===============================================================
% load 'Xshort','Xlong','u_country','u_cont'
% Xshort has
% country_all1 country_id2 years3 IC4 urban5 rural6 mean_dollar7 
% agPG8 gdpPG9 rain10 AgBorder11 NonBorder12 deciles(10c) 
% AgBorder & NonBorder are already in difference;
% Xlong has DCL13 and decile14 as last 2 columns
% ==============================================================

caption=['\\caption{'...
   'Second stage regression of the growth rate of decile expenditures '...
   'on the aggregate growth rates of agricultural and non-agricultural '...
   'income.  The annotations *, **, and *** indicate significance of '...
   'the corresponding coefficient estimate with levels of confidence '...
   'corresponding to 90\\%, 95\\%, and 99\\%.  In addition to the reported '...
   'variables, the (second stage) estimating equation includes fixed '...
   'effects for each country-decile, while the first stage includes '...
   'year effects.}'];

load ../Data/WBdata;

DR=sortrows(Xlong,[1 13 3]);
varlist={'country_all','country_id','years','IC','urban',...
    'rural','mean_dollar','ag','gdp','rain',...
    'AgBorder','NonBorder','DCL','dshares'};
for i=1:length(varlist);
    eval([varlist{i} '=DR(:,i);']);
end
deciles=mean_dollar.*dshares*0.1;
X=[country_all DCL years];
[D,I1,I2]=sdifference(X);
temp1=zeros(length(X),1); temp2=temp1;
temp1(I2)=AgBorder(I2); AgBorder=temp1;
temp2(I2)=NonBorder(I2); NonBorder=temp2;

includelist={'country_all','DCL','years','deciles',...
    'ag','gdp','AgBorder', 'NonBorder',...
    'country_id','IC','urban','rural'};
X=[];
for i=1:length(includelist);
    eval(['X=[X ' includelist{i} '];']);
end
idx=find(IC==0); %use only consumptions
X=X(idx,:);
sumX=sum(X')';
idx=find(~isnan(sumX));
X=X(idx,:); %delete obs with missing values;

% % get rid of the negative shares
index=find(X(:,4)<0);
this_obs=X(index,1); this_year=X(index,3);
for i=1:length(this_obs);
    index=find(X(:,1)==this_obs(i) & X(:,3)==this_year(i));
    X(index,:)=[];
end

% % get rid of data with leass than 3 years
u_X1=unique(X(:,1));
INDEX=[];
for i=1:length(u_X1);
    index=find(X(:,1)==u_X1(i));
    if length(index)>=30;
        INDEX=[INDEX;index];
    end
end
X=X(INDEX,:);
X=sortrows(X,[1 2 3]);

for i=1:length(includelist);
    eval([includelist{i} '=X(:,i);']);
end
%********************* end of data cleaning*******************
% =================================================================
% ***************start of data preparation*********************

[DD,I1,I2]=sdifference([country_all DCL years]); % only to get I & I2

% % % % get change rate
% % dAg=(ag(I2)./ag(I1)-1)./diff(DD')';
% % non=gdp-ag;
% % dNon=(non(I2)./non(I1)-1)./diff(DD')';
% % dWef=(deciles(I2)./deciles(I1)-1)./diff(DD')'; y=dWef;

% % get log change
dAg=(log(ag(I2))-log(ag(I1)))./diff(DD')';
non=gdp-ag;
dNon=(log(non(I2))-log(non(I1)))./diff(DD')';
dWef=(log(deciles(I2))-log(deciles(I1)))./diff(DD')'; y=dWef;

dInstrAg=AgBorder(I2)./diff(DD')';
dInstrNon=NonBorder(I2)./diff(DD')';

cinstr=size(dInstrAg,2);
rr=length(I1);

% % dummies
Qd=dummies(DCL(I1));
Cd=dummies(country_all(I1));
CQd=dummies([DCL(I1) country_all(I1)]);

u_year=unique(years);
yearmin=min(u_year);
yearmax=max(u_year);
Yd=zeros(rr,length(u_year)-1);
for i=1:length(u_year)-1;
    index=find(DD(:,1)<= u_year(i) & DD(:,2)>u_year(i));
    Yd(index,i)=1;
end
Yd=Yd./repmat(diff(DD')',1,size(Yd,2));
idx=find(sum(Yd)>0);
Yd=Yd(:,idx);

% generate interaction with DCL;
% generate 'dAgQ','dNonQ','dInstrAgQ','dInstrNonQ'
interlist={'dAg','dNon','dInstrAg','dInstrNon'};
for i=1:length(interlist);
    eval([interlist{i} 'Q=repmat(' interlist{i} ',1,size(Qd,2)).*Qd;']);
end

% ***************end of data preparations*********************
% ===============================================================
% *************start of Stage 1 analysis *********************
% 1st stage for Ag
putin1={[dInstrAg Yd]};
[B,E,T,R,P,Yhat,se1]=simplereg(dAg,putin1);
Aghat=Yhat{1}; % for use in deciles2.m
AghatQ=repmat(Aghat,1,size(Qd,2)).*Qd;

% 1st stage for Non
putin1={[dInstrNon Yd]};
[B,E,T,R,P,Yhat,se1]=simplereg(dNon,putin1);
Nonhat=Yhat{1};
NonhatQ=repmat(Nonhat,1,size(Qd,2)).*Qd;

% =================================================================
% ***************start of Stage 2 analysis**********************
y=dWef;
putin2={[AghatQ NonhatQ CQd]};
putin2_={[dAgQ dNonQ CQd]};
[B,E,T,R,P,Yhat,se1]=simplereg(y,putin2);
agB=B{1}(1:10);nonB=B{1}(11:20);

yhat=putin2_{1}*B{1};
E2sls=y-yhat;
T=B{1}./sqrt(diag(inv(putin2_{1}'*putin2_{1})*cov(E2sls)));
se2=full(sqrt(diag(inv(putin2_{1}'*putin2_{1})*cov(E2sls))));
agT=T(1:10);nonT=T(11:20);
agE=se2(1:10);nonE=se2(11:20);

% over-identification
putin3={[dInstrAgQ dInstrNonQ CQd]};
[B,E,T,R,P,Yhat]=simplereg(E2sls,putin3);
R2=sum(Yhat{1}.*Yhat{1})./sum(E2sls.*E2sls);

if ismatlab;
  p=1-chi2cdf(rr*R2,(size(putin1{1},2)+10-20));
else;
  p=1-chisquare_cdf(rr*R2,(size(putin1{1},2)+10-20));
end;
ovid=p;

% ==============================================================
% *********************start of table*********************
sAg=ag(I1)./gdp(I1);
shares=[mean(sAg) 1-mean(sAg)];
BB=[];BB(:,1)=agB; BB(:,2)=nonB;
TT=[];TT(:,1)=agT; TT(:,2)=nonT;
SSE=[]; SSE(:,1)=agE;SSE(:,2)=nonE;

BB,TT,SSE

tab=BB; 
title=['deciles2.tex'];

h=fopen(title,'w');
titlestr=['How Income Growth Affects Expenditures'];

cl=size(tab,2);
cname={'Deciles','Agriculture','Non-Agriculture'};
cname2={'','Income Growth','Income Growth'};
rname={'10','20','30','40','50','60','70','80','90','100'};
fmtstr=['l|' repmat('c',1,cl)];

fprintf(h,'\\begin{table}[h]\n\\centering\n');
fprintf(h,'\\begin{tabular}{%s}',fmtstr);
fprintf(h,['\\hline\\hline\n']);
% fprintf(h,['& \\multicolumn{' num2str(cl) '}{l}{\\textsl{%s}}\\\\\\hline\n'],titlestr);
fprintf(h,'%s',cname{1});
fprintf(h,'&\t%s',cname{2:end}); fprintf(h,'\\\\\n');
fprintf(h,'&\t%s',cname2{2:end}); fprintf(h,'\\\\\\hline\n');

fprintf(h,'Shares');
fprintf(h,'&\t $%5.3f$',shares);fprintf(h,'\\\\\\hline\n');

fprintf(h,'Std. Errors');
fprintf(h,'&\t $%5.3f$',SSE(1,:));fprintf(h,'\\\\\n');

for i=1:size(rname,2);
    fprintf(h,'%s\\%%',rname{i});
    plug=[BB(i,:);TT(i,:)];
    bplug
end

fprintf(h,'\\hline\\hline\n\\end{tabular}\n');

fprintf(h,'%s',caption);
fprintf(h,'\\label{tab:deciles2}\n');
fprintf(h,'\\end{table}\n');
