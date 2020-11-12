filename = 'settings (2).txt';
A = importdata(filename)
B = importdata("data (4).txt")
dU = A(1)
dT = A(2)
D = (B*3.3)/256
T = 0:dT:dT*(size(B)-1)
LT = 1:5:size(T)
figure('name','Александр Брага Б03-004')
p = plot(T,D,"r-*","LineWidth",2,"MarkerIndices",1:10:length(T))
title({"Capacitor voltage";"versus time"})
xlabel("Time, c")
ylabel("Voltage, V")
grid on
legend("Voltage changing")
saveas(gcf,'Capacitor1.png',"epsc")
Index=find(B == 247)
Time1 = T(Index)
Index1 = size(B)
Time2 = T(end)-Time1


