
speed=Speedkmh1(10:299);
subplot 211
stairs(speed)
title('speed')
ylabel('km/h')
xlabel('sampling')
xlim([1 length(speed)])


pm=table2array(PMrec20161114202846(82:end,3));
subplot 212
stairs(pm)
title('PM')
ylabel('ug/m^3')
xlabel('sampling')
xlim([1 length(pm)])