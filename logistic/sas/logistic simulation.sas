DM  "log;clear;output;clear;";
options nodate;

data a;

proc iml;

beta0=0.5;
beta1=2;
beta2=1.5;
beta3=0.2;
observation=100;

start covariates(x1,x2,x3,y);
    if (ranuni(0)>0.5) then x1=1; else x1=0;
    if (ranuni(0)>0.5) then x2=1; else x2=0;
    if (ranuni(0)>0.5) then x3=1; else x3=0;
    y=beta0+beta1*x1+beta2*x2+beta3*x3;
finish;

 do i=1 to observation;
 
      dataset= j(observation,4,.); 
     
           call covariates(x1,x2,x3,y);
           dataset=[i,1]=x1;
           dataset=[i,2]=x2;
           dataset=[i,3]=x3;
           dataset=[i,4]=y;
 end;

quit;



