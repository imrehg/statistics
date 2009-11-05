DM  "log;clear;output;clear;";
options nodate;

data a;
* Generate test data;
beta0=0.5;
beta1=2;
beta2=1.5;
beta3=0.2;
observation=100;


do i=1 to observation;

   if (ranuni(0)>0.5) then x1=1; else  x1=0;
   if (ranuni(0)>0.5) then x2=1; else  x2=0;
   if (ranuni(0)>0.5) then x3=1; else  x3=0;
   p=beta0+beta1*x1+beta2*x2+beta3*x3;

   if ranuni(0)< (exp(p)/(1+exp(p))) then y=1;else y=0;

   output;
end;
proc print ;
run;


data b;
* Calculate conditional counts;
set a;

  if (x2=1& x3=1) then do;
    if  (y=1 & x1=1)  then f1111=1; else f1111=0;
    if  (y=1 & x1=0)  then f1011=1; else f1011=0;
    if  (y=0 & x1=1)  then f0111=1; else f0111=0;
    if  (y=0 & x1=0)  then f0011=1; else f0011=0;
  end;

  if (x2=1& x3=0) then do;
    if  (y=1 & x1=1)  then f1110=1; else f1110=0;
    if  (y=1 & x1=0)  then f1010=1; else f1010=0;
    if  (y=0 & x1=1)  then f0110=1; else f0110=0;
    if  (y=0 & x1=0)  then f0010=1; else f0010=0;
  end;

  if (x2=0 & x3=1) then do;
    if  (y=1 & x1=1)  then f1101=1; else f1101=0;
    if  (y=1 & x1=0)  then f1001=1; else f1001=0;
    if  (y=0 & x1=1)  then f0101=1; else f0101=0;
    if  (y=0 & x1=0)  then f0001=1; else f0001=0;
  end;

  if (x2=0& x3=0) then do;
    if  (y=1 & x1=1)  then f1100=1; else f1100=0;
    if  (y=1 & x1=0)  then f1000=1; else f1000=0;
    if  (y=0 & x1=1)  then f0100=1; else f0100=0;
    if  (y=0 & x1=0)  then f0000=1; else f0000=0;
  end;


proc print ;
run;

proc iml;
* Calculate sums;
use b;

read all var {x1 x2 x3 
              f0000 f0001 f0010 f0011 f0100 f0101 f0110 f0111
              f1000 f1001 f1010 f1011 f1100 f1101 f1110 f1111};

n0000 = sum(f0000);
n0001 = sum(f0001);
n0010 = sum(f0010);
n0011 = sum(f0011);
n0100 = sum(f0100);
n0101 = sum(f0101);
n0110 = sum(f0110);
n0111 = sum(f0111);
n1000 = sum(f1000);
n1001 = sum(f1001);
n1010 = sum(f1010);
n1011 = sum(f1011);
n1100 = sum(f1100);
n1101 = sum(f1101);
n1110 = sum(f1110);
n1111 = sum(f1111);

print n0000 n0001 n0010 n0011 n0100 n0101 n0110 n0111;
print n1000 n1001 n1010 n1011 n1100 n1101 n1110 n1111;
run;
quit;

/*
data b;
set a;
proc logistic  descending;
model y=x1 x2 x3;
run;
*/ 
