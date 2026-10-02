rng(42)
addpath('utils/');
addpath('NNLS-0/solver');
addpath('NNLS-0/PROPACKmod/');
close all;
clc;clear;clear global;

funcSimulation=@runSMCSimulation;
outfile='resultSMC';

niter=3;
dim_iter={{100,100,5},{250,250,5}};

c=2:2:10;
giter = cell(0);
giter{1}=@(a) a;
for ci=1:length(c)   
    giter{ci+1}=@(a) 1.0./(1+exp(-c(ci)*a));
end
f={'spearman_rho', 'kendall_tau', 'NDCG'};

result=cell(niter*length(dim_iter),1);

parfor ix=1:niter*length(dim_iter)
    [n,i]=ind2sub([niter,length(dim_iter)],ix);
    [d1,d2,r]=dim_iter{i}{:};
    result{ix}=funcSimulation(d1,d2,r,giter,f);
end
save(outfile,'result')


fprintf('DONE COMPUTING\n')
