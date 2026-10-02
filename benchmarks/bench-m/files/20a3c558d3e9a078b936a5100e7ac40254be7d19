%% stroke max

figure
subplot(3,2,1)
title('stroke min')
hold on
subplot(3,2,2)
title('strokemin mod coefficient')
hold on
subplot(3,2,3)
hold on
subplot(3,2,4)
hold on
subplot(3,2,5)
hold on
subplot(3,2,6)
hold on

n_loc = round(Rds_steady_meanCIstd(1)*size(pitch_wb_L_bins,1));

subplot(3,2,1)
% plot((M_axis1_mean_wb),stroke_wb_L_bins(n_loc,:),'.k')
plot((M_axis1_mean_wb),stroke_wb_R_bins(n_loc,:),'.k')
plot(M_axis1_TorqueAxis1UP,stroke_wb_R_TorqueAxis1UP_bins(n_loc,:),'.b')

% plot trend
RC = strokeMOD_wb_R_TorqueAxis1UP_bins_meanCIstd(n_loc,1)/M_axis1_norm;
var0 = stroke_wb_steady_bins_meanCIstd(n_loc,1);
x0 = 0;
x1 = max(M_axis1_TorqueAxis1UP);
var1 = var0 + RC * (x1-x0);
xmin1 = min(M_axis1_TorqueAxis1UP);
varmin1 = var0 + RC * (xmin1-x0);
plot([xmin1 x1],[varmin1 var1],'-r','linewidth',2)
% xlabel('rotR Torque','fontsize',10)
ylabel('right wing','fontsize',10)

ang_min = -90;
ang_max = 0;
axis([xmin xmax ang_min ang_max])
set(gca,'YTick',ang_min:(ang_max-ang_min)/2:ang_max) 

subplot(3,2,3)
plot((M_axis1_mean_wb),stroke_wb_L_bins(n_loc,:),'.k')
% plot((M_axis1_mean_wb),stroke_wb_R_bins(n_loc,:),'.k')
plot((M_axis1_TorqueAxis1UP),stroke_wb_L_TorqueAxis1UP_bins(n_loc,:),'.b')

% plot trend
RC = strokeMOD_wb_L_TorqueAxis1UP_bins_meanCIstd(n_loc,1)/M_axis1_norm;
var0 = stroke_wb_steady_bins_meanCIstd(n_loc,1);
x0 = 0;
x1 = max(M_axis1_TorqueAxis1UP);
var1 = var0 + RC * (x1-x0);
xmin1 = min(M_axis1_TorqueAxis1UP);
varmin1 = var0 + RC * (xmin1-x0);
plot([xmin1 x1],[varmin1 var1],'-r','linewidth',2)
% xlabel('rotR Torque','fontsize',10)
ylabel('left wing','fontsize',10)

ang_min = -90;
ang_max = 0;
axis([xmin xmax ang_min ang_max])
set(gca,'YTick',ang_min:(ang_max-ang_min)/2:ang_max) 

subplot(3,2,5)
plot((M_axis1_mean_wb),Dstroke_wb_bins(n_loc,:),'.k')
% plot((M_axis1_mean_wb),stroke_wb_R_bins(n_loc,:),'.k')
plot((M_axis1_TorqueAxis1UP),Dstroke_wb_TorqueAxis1UP_bins(n_loc,:),'.b')

% plot trend
RC = DstrokeMOD_wb_TorqueAxis1UP_bins_meanCIstd(n_loc,1)/M_axis1_norm;
var0 = 0;
x0 = 0;
x1 = max(M_axis1_TorqueAxis1UP);
var1 = var0 + RC * (x1-x0);
xmin1 = min(M_axis1_TorqueAxis1UP);
varmin1 = var0 + RC * (xmin1-x0);
plot([xmin1 x1],[varmin1 var1],'-r','linewidth',2)
xlabel('rotR Torque','fontsize',10)
ylabel('R - L','fontsize',10)

ang_min = -45;
ang_max = 45;
axis([xmin xmax ang_min ang_max])
set(gca,'YTick',ang_min:(ang_max-ang_min)/2:ang_max) 

%% coeff
% right
subplot(3,2,2)
plot((M_axis1_TorqueAxis1UP),strokeMOD_wb_R_TorqueAxis1UP_bins(n_loc,:),'.b')

RC = strokeMOD_wb_R_TorqueAxis1UP_bins_meanCIstd(n_loc,1);
var0 = 0;
x0 = 0; 
x1 = max(M_axis1_TorqueAxis1UP); 
var1 = RC
xmin1 = min(M_axis1_TorqueAxis1UP); 
varmin1 = RC
plot([xmin1 x1],[varmin1 var1],'-r','linewidth',2)
% xlabel('rotR Torque','fontsize',10)
% ylabel('strokemax mod coefficient','fontsize',10)

ang_min = -45;
ang_max = 45;
axis([xmin xmax ang_min ang_max])
set(gca,'YTick',ang_min:(ang_max-ang_min)/2:ang_max) 

% Left
subplot(3,2,4)
plot((M_axis1_TorqueAxis1UP),strokeMOD_wb_L_TorqueAxis1UP_bins(n_loc,:),'.b')

RC = strokeMOD_wb_L_TorqueAxis1UP_bins_meanCIstd(n_loc,1);
var0 = 0;
x0 = 0; 
x1 = max(M_axis1_TorqueAxis1UP); 
var1 = RC
xmin1 = min(M_axis1_TorqueAxis1UP); 
varmin1 = RC
plot([xmin1 x1],[varmin1 var1],'-r','linewidth',2)
% xlabel('rotR Torque','fontsize',10)
% ylabel('strokemax mod coefficient','fontsize',10)

ang_min = -45;
ang_max = 45;
axis([xmin xmax ang_min ang_max])
set(gca,'YTick',ang_min:(ang_max-ang_min)/2:ang_max) 

% right-Left
subplot(3,2,6)
plot((M_axis1_TorqueAxis1UP),DstrokeMOD_wb_TorqueAxis1UP_bins(n_loc,:),'.b')

RC = DstrokeMOD_wb_TorqueAxis1UP_bins_meanCIstd(n_loc,1);
var0 = 0;
x0 = 0; 
x1 = max(M_axis1_TorqueAxis1UP); 
var1 = RC
xmin1 = min(M_axis1_TorqueAxis1UP); 
varmin1 = RC
plot([xmin1 x1],[varmin1 var1],'-r','linewidth',2)
xlabel('rotR Torque','fontsize',10)
% ylabel('strokemax mod coefficient','fontsize',10)

ang_min = -45;
ang_max = 45;
axis([xmin xmax ang_min ang_max])
set(gca,'YTick',ang_min:(ang_max-ang_min)/2:ang_max) 


