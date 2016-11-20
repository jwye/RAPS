clc
clear
load testday2
%==============================
%open sheild taped mouth 
pm=table2cell(PMrec20161114202846(2:end,1:4));
pm25=cell2mat(pm(:,3));
pm25meanR1=mean(pm25(250:450));
pmtime=table2cell(PMrec20161114202846(2:end,1));
speedtime=table2cell(R12(2:end,2));
speed=table2array(R12(2:end,6));
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
zerospeed=find(~speed(ch(:,2)));
pm25meanR1zs=mean(pm25(zerospeed));
figure(1)
[hAx,hLine1,hLine2]=plotyy((1:length(pm25)),pm25,...
    ch(:,1),speed(ch(:,2)),'stairs','stairs'); 
hold on;
title('open sheild taped mouth (PM & speed)')
ylabel(hAx(1),'ug/m^3') % left y-axis
ylabel(hAx(2),'km/hr') % right y-axis
ylim(hAx(1),[0 300])
ylim(hAx(2),[-10 200])
xlabel('sec')
xlim([1 length(pm25)])

hold off
    


%==============================
%close sheild taped mouth 
pm=table2cell(PMrec20161114203620(2:end,1:4));
pm25=cell2mat(pm(:,3));
pm25meanR2=mean(pm25(345:485));
pmtime=table2cell(PMrec20161114203620(2:end,1));
speedtime=table2cell(R12(2:end,2));
speed=table2array(R12(2:end,6));
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
zerospeed=find(~speed(ch(:,2)));
pm25meanR2zs=mean(pm25(zerospeed));
figure(2)
[hAx,hLine1,hLine2]=plotyy((1:length(pm25)),pm25,...
    ch(:,1),speed(ch(:,2)),'stairs','plot'); 
hold on;
title('close sheild taped mouth (PM & speed)')
ylabel(hAx(1),'ug/m^3') % left y-axis
ylabel(hAx(2),'km/hr') % right y-axis
%ylim(hAx(1),[0 300])
%ylim(hAx(2),[-10 200])
xlabel('sec')
xlim([1 length(pm25)])

hold off



%==============================
%open sheild RAPS OFF 
pm=table2cell(PMrec20161114205034(2:end,1:4));
pm25=cell2mat(pm(:,3));
pm25meanR3=mean(pm25(40:340));
pmtime=table2cell(PMrec20161114205034(2:end,1));
speedtime=table2cell(R345(2:end,2));
speed=table2array(R345(2:end,6));
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
zerospeed=find(~speed(ch(:,2)));
pm25meanR3zs=mean(pm25(zerospeed));
pm25meanR3zse=mean(pm25(12:57));
figure(3)
[hAx,hLine1,hLine2]=plotyy((1:length(pm25)),pm25,...
    ch(:,1),speed(ch(:,2)),'stairs','plot'); 
hold on;
title('open sheild RAPS off (PM & speed)')
ylabel(hAx(1),'ug/m^3') % left y-axis
ylabel(hAx(2),'km/hr') % right y-axis
ylim(hAx(1),[0 330])
ylim(hAx(2),[-10 200])
xlabel('sec')
xlim([1 length(pm25)])

hold off


% %==============================
% %close sheild RAPS OFF 
pm=table2cell(PMrec20161114205553(2:end,1:4));
pm25=cell2mat(pm(:,3));
pm25meanR4=mean(pm25(5:220));
pmtime=table2cell(PMrec20161114205553(2:end,1));
speedtime=table2cell(R345(2:end,2));
speed=table2array(R345(2:end,6));
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
zerospeed=find(~speed(ch(:,2)));
pm25meanR4zs=mean(pm25(zerospeed));
figure(4)
[hAx,hLine1,hLine2]=plotyy((1:length(pm25)),pm25,...
    ch(:,1),speed(ch(:,2)),'stairs','plot'); 
hold on;
title('close sheild RAPS off (PM & speed)')
ylabel(hAx(1),'ug/m^3') % left y-axis
ylabel(hAx(2),'km/hr') % right y-axis
ylim(hAx(1),[0 300])
ylim(hAx(2),[-10 200])
xlabel('sec')
xlim([1 length(pm25)])

hold off
    

%==============================
%close sheild RAPS on 
pm=table2cell(PMrec20161114210017(2:end,1:4));
pm25=cell2mat(pm(:,3));
pm25meanR5=mean(pm25(150:484));
pmtime=table2cell(PMrec20161114210017(2:end,1));
speedtime=table2cell(R345(2:end,2));
speed=table2array(R345(2:end,6));
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
zerospeed=find(~speed(ch(:,2)));
pm25meanR5zs=mean(pm25(zerospeed));
pm25meanR5zsr=mean(pm25(zerospeed(15:end)));
pm25meanR5zse=mean(pm25(zerospeed(1:8)));
figure(5)
[hAx,hLine1,hLine2]=plotyy((1:length(pm25)),pm25,...
    ch(:,1),speed(ch(:,2)),'stairs','plot'); 
hold on;
title('close sheild RAPS on (PM & speed)')
ylabel(hAx(1),'ug/m^3') % left y-axis
ylabel(hAx(2),'km/hr') % right y-axis
ylim(hAx(1),[0 300])
ylim(hAx(2),[-10 200])
xlabel('sec')
xlim([1 length(pm25)])

hold off
    