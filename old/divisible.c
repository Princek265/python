#include<stdio.h>
int main(){
    int a;
    scanf("%d",&a);
    if (a%3==0){
        printf("%d is divisible by 3",a);
    }
    else if(a%5==0){
       printf("%d is divisible by 5",a);
    }
    return 0;
}