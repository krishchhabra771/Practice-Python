#include<stdio.h>
#include<math.h>
int main(){
    int a,b,minh;
    float h;
    printf("enter the area and base");
    scanf("%d %d",&a,&b);
    h=(2.0*a)/b;
    printf("%f", h);
    minh=ceil(h);
    printf("the min height is %d",minh);
    return 0;
}