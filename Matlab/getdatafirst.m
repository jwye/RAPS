clc
clear
load testday1
%==============================
%Testday1
pm=table2cell(PMrecRealTest20161113203617(2:end,1:4));
pm25=cell2mat(pm(:,3));

pmtime=table2cell(PMrecRealTest20161113203617(2:end,1));
speedtime=table2cell(RealTest(2:end,2));
speed=table2array(RealTest(2:end,6));
ch=[0 0];k=0;
for i=1:length(pmtime)
    for j=1:length(speedtime)-10
        checking=sum(pmtime{i}==speedtime{j});
        if checking == 16 && speed(j) <= 75
            k=k+1;
            ch(k,:)=[i j];
        end
    end
end

figure(1)
[hAx,hLine1,hLine2]=plotyy((1:length(pm25)),pm25,...
    ch(:,1),speed(ch(:,2)),'stairs','stairs'); 
hold on;
title('Testday 1 (PM & speed)')
ylabel(hAx(1),'ug/m^3') % left y-axis
ylabel(hAx(2),'km/hr') % right y-axis
xlabel('sec')
xlim([1 length(pm25)])
hold off
    
