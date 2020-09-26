#include <stdio.h>

int main() {
    int counter;
    float gallons, miles, tankAverage, overallAverage, total;
    counter = 0;
    total = 0;
    printf("Enter the gallons used, (-1 to end): \n");
    scanf("%f", &gallons);
    while(gallons!=-1) {
        
        printf("Enter the miles driven: \n");
        scanf("%f", &miles);
        
        tankAverage = miles / gallons;
        printf("The miles per gallon for this tank was %f\n", tankAverage);
        
        total += tankAverage;
        counter +=1;
        printf("Enter the gallons used, (-1 to end): \n");
        scanf("%f", &gallons);
    }
    overallAverage = total / counter;
    printf("The overall average miles/gallon was %f\n", overallAverage);
    return 0;
    }

