function [soilCommonStateParams, soilInnerStateParams]...
                           = mergeInnerOuter(fractSoil, fractPlant,...
                                             simulationSettings,...
                                             soilConsParams,...
                                             soilCommonStateParams,...
                                             soilInnerStateParams,...
                                             soilOuterStateParams)
                                             
t = simulationSettings.t;

%% Determine field situation and set corresponding values
if simulationSettings.flag_double_sim == 1
    
    % Soil organic matter
    soilCommonStateParams.soil_om =  soilOuterStateParams.soil_om*fractSoil +...
        soilInnerStateParams.soil_om*fractPlant;
    
    % Water content
    soilCommonStateParams.wcmo =  soilOuterStateParams.wcmo*fractSoil + ...
        soilInnerStateParams.wcmo*fractPlant;
    
    % Solute content
    soilCommonStateParams.tcsolo =  soilOuterStateParams.tcsolo*fractSoil +....
        soilInnerStateParams.tcsolo*fractPlant;
    
    %Store temperature data
    soilCommonStateParams.temp =  soilOuterStateParams.temp*fractSoil +...
        soilInnerStateParams.temp*fractPlant;
    
    % Mineralised organic matter
    soilCommonStateParams.minerm =  soilOuterStateParams.minerm(:,2)*fractSoil +...
        soilInnerStateParams.minerm(:,2)*fractPlant;
    
    % water balance
    if soilCommonStateParams.water_balance
        soilCommonStateParams.water_balance(1,end+1) = soilOuterStateParams.water_balance(1, end);
        soilCommonStateParams.water_balance(2:4,end) = soilCommonStateParams.water_balance(2:4, end-1) +...
                                                          (soilInnerStateParams.water_balance(2:4, end) -...
                                                           soilInnerStateParams.water_balance(2:4, end-1)) * fractPlant +...
                                                          (soilOuterStateParams.water_balance(2:4, end) -...
                                                           soilOuterStateParams.water_balance(2:4, end-1)) * fractSoil;
    else
        soilCommonStateParams.water_balance(1,end+1) = soilOuterStateParams.water_balance(1, end);
        soilCommonStateParams.water_balance(2:4,end) =  soilInnerStateParams.water_balance(2:4, end) * fractPlant +...
                                                          soilOuterStateParams.water_balance(2:4, end) * fractSoil;

    end
    
elseif simulationSettings.flag_double_sim == 0
    % Soil organic matter
    soilCommonStateParams.soil_om =  soilOuterStateParams.soil_om*fractSoil;
    
    % Water content
    soilCommonStateParams.wcmo =  soilOuterStateParams.wcmo*fractSoil;
    
    % Solute content
    soilCommonStateParams.tcsolo =  soilOuterStateParams.tcsolo*fractSoil;
    
    %Store temperature data
    soilCommonStateParams.temp =  soilOuterStateParams.temp*fractSoil;
    
    % Mineralised organic matter
    soilCommonStateParams.minerm =  soilOuterStateParams.minerm(:,2)*fractSoil;
    
    % water balance
    if soilCommonStateParams.water_balance % if soilCommonState.water_balance is not empty
        soilCommonStateParams.water_balance(1,end+1) = soilOuterStateParams.water_balance(1, end);
        soilCommonStateParams.water_balance(2:4,end) = soilCommonStateParams.water_balance(2:4, end-1) +...
                                                          (soilOuterStateParams.water_balance(2:4, end) -...
                                                           soilOuterStateParams.water_balance(2:4, end-1)) * fractSoil;
        
    else % if soilCommonState.water_balance is empty
        soilCommonStateParams.water_balance(1,end+1) = soilOuterStateParams.water_balance(1, end);
        soilCommonStateParams.water_balance(2:4,end) = soilOuterStateParams.water_balance(2:4, end) * fractSoil;                                                       
    end
    
    % Zeros should be added to balance variables such that after planting
    % the balance is calculated correctly 
    SoluteFields = {"UreumBalance_log", "NH4Balance_log", "NO3Balance_log"};
    
    for i = 1:numel(SoluteFields)
       [nRow, ~] = size(soilOuterStateParams.(SoluteFields{1}(1)));
       soilInnerStateParams.(SoluteFields{i}(1))(:,end+1) = [t; soilInnerStateParams.(SoluteFields{i}(1))(2:end,end)];
    end
   
    [nRow, ~] = size(soilOuterStateParams.N_reaction_balance);
    soilInnerStateParams.N_reaction_balance(:,end+1) = [t; zeros(nRow-1, 1)];

end
%% merge inner state parameters & outer state parameters in common state parameters


soilCommonStateParams.water_storage(end+1) = sum(soilCommonStateParams.wcmo.*simulationSettings.dx); %Wcmo calculated at end of a day dependent on fractions
soilCommonStateParams.WCSoil_log(:,end+1) = soilCommonStateParams.wcmo';

soilCommonStateParams.UreumSoil_log(:,end+1) = soilCommonStateParams.tcsolo(:,1);
soilCommonStateParams.NH4Soil_log(:,end+1) = soilCommonStateParams.tcsolo(:,2);
soilCommonStateParams.NO3Soil_log(:,end+1) = soilCommonStateParams.tcsolo(:,3);

% save solute balance
SoluteFields = {["UreumBalance_log", "UreumSoil_log"],...
                ["NH4Balance_log", "NH4Soil_log"],...
                ["NO3Balance_log", "NO3Soil_log"]};

% loop over cell array
for i = 1:numel(SoluteFields)
    
    % time
    soilCommonStateParams.(SoluteFields{i}(1))(1,end+1)= soilOuterStateParams.(SoluteFields{i}(1))(1,end);
    if simulationSettings.t == datenum(2009, 1, 1) + 60
        disp('')
    end
    %Inflow (2) & outflow (3)
    soilCommonStateParams.(SoluteFields{i}(1))(2:3,end)= soilCommonStateParams.(SoluteFields{i}(1))(2:3,end-1)+...
        (soilOuterStateParams.(SoluteFields{i}(1))(2:3,end) -...
        soilOuterStateParams.(SoluteFields{i}(1))(2:3,end-1))*fractSoil + ...
        (soilInnerStateParams.(SoluteFields{i}(1))(2:3,end) -...
        soilInnerStateParams.(SoluteFields{i}(1))(2:3,end-1))*fractPlant; 
    
    %Solute change in profiile
    soilCommonStateParams.(SoluteFields{i}(1))(4,end) = sum(soilCommonStateParams.(SoluteFields{i}(2))(:,end)) -...
        sum(soilConsParams.tcsolo_ini(:,i)); 
    
    %Sink term
    soilCommonStateParams.(SoluteFields{i}(1))(6,end)= soilCommonStateParams.(SoluteFields{i}(1))(6,end-1)+...
        (soilOuterStateParams.(SoluteFields{i}(1))(6,end) -...
        soilOuterStateParams.(SoluteFields{i}(1))(6,end-1))*fractSoil + ...
        (soilInnerStateParams.(SoluteFields{i}(1))(6,end) -...
        soilInnerStateParams.(SoluteFields{i}(1))(6,end-1))*fractPlant;
    
    %Balance error
    soilCommonStateParams.(SoluteFields{i}(1))(5,end) = soilCommonStateParams.(SoluteFields{i}(1))(4,end)-....
        (soilCommonStateParams.(SoluteFields{i}(1))(2,end)+....
        soilCommonStateParams.(SoluteFields{i}(1))(3,end)+...
        soilCommonStateParams.(SoluteFields{i}(1))(6,end)); 
    
end

% Nitrogen reaction balance
soilCommonStateParams.N_reaction_balance(:,end+1) =...
                        soilCommonStateParams.N_reaction_balance(:,end) +...
                        (soilOuterStateParams.N_reaction_balance(:,end) -...
                        soilOuterStateParams.N_reaction_balance(:,end-1)) * fractSoil +...
                        (soilInnerStateParams.N_reaction_balance(:,end) -...
                        soilInnerStateParams.N_reaction_balance(:,end-1)) * fractPlant;


soilCommonStateParams.daily_mineral(:,end+1) = soilCommonStateParams.minerm;


soilCommonStateParams.TSoil = soilCommonStateParams.temp';

