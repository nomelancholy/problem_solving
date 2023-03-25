#include <stdio.h>
int main(void)
{
 
 int n,input;
 int max = 0;
 double answer = 0;
 
 scanf("%d",&n);
 double arr[n];
 
 for(int i=0; i<n;i++){
     scanf("%d",&input);
     arr[i] = input;
     if(arr[i]>max){
         max = arr[i];
     }
 }
 
 for(int i=0; i<n;i++){
     arr[i] = arr[i]/max*100;
     answer = answer + arr[i];
 }
 
 answer = answer / n;
 printf("%f",answer);
 
}