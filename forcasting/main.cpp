#include <iostream>
#include <math.h>
using namespace std;

int main()
{

    //Forcasting
    //3MA
    cout << "            3 MA"<<'\n';
    int a,j=0;
    double sum=0 , sumPow=0 ,sumDev=0, b;
    double arr2[200];
    double arr1[100];
    ///Enter the number what you want
    cout << "Please Enter The Number Of Digits : ";
    cin >> a ;
    ///Enter them
    for(int i=0;i<a;i++)
    {
        cin>>arr1[i];
    }
    ///calculate 3MA and the error
    for(int i=0;i<(a-3);i++)
    {
        double z = (arr1[i]+arr1[i+1]+arr1[i+2])/3;
        b = abs(arr1[i+3]-z);
        arr2[j]=b;
        j++;
    }
    ///for calculate MAE
    for(int i=0;i<j;i++)
    {
       sum+=arr2[i];
    }
    double mae=sum/j;
    cout << "MAE = " << mae<<'\n';
    ///For calculate MSE
    for(int i=0;i<j;i++)
    {
       sumPow+=pow(arr2[i],2);
    }
    double mse=sumPow/j;
    cout <<"MSE = " <<mse<<'\n';
    ///For calculate MAPE
    double ccc=0;
    for(int i=0;i<j;i++)
    {
        ccc = arr2[i]/arr1[i+3];
        sumDev+=ccc;
    }
    double mape= (sumDev/j)*100;
    cout << "MAPE = "<<mape;

    return 0;
}
