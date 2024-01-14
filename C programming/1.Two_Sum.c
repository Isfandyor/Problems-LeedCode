#include<stdio.h>
void two_sum(int n,int arr[n],int num){
      int arr2[2];
      for(int i=0;i<n;i++){
          for(int j=i+1;j<n;j++){
             if(arr[i]+arr[j]==num){
                 arr2[0]=i;
                 arr2[1]=j;
                 break;             
                 }
          }
      }
      for(int i=0;i<n;i++){
        printf("%d",arr[i]);
    }
} 
int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int num;
    scanf("%d",&num);
    two_sum(n,arr,num);
    return 0;
}

// #include<stdio.h>

// void two_sum(int n, int arr[n], int num) {
//     int arr2[2] = {-1, -1}; // Инициализируем массив arr2 значениями по умолчанию
//     for (int i = 0; i < n; i++) {
//         for (int j = i + 1; j < n; j++) {
//             if (arr[i] + arr[j] == num) {
//                 arr2[0] = i;
//                 arr2[1] = j;
//                 break;
//             }
//         }
//         if (arr2[0] != -1 && arr2[1] != -1) // Если пара найдена, прерываем цикл
//             break;
//     }
//     if (arr2[0] != -1 && arr2[1] != -1) { // Если пара найдена, выводим её
//         printf("Pair found at indices: %d, %d\n", arr2[0], arr2[1]);
//         printf("Numbers: %d and %d\n", arr[arr2[0]], arr[arr2[1]]);
//     } else {
//         printf("Pair not found\n");
//     }
// }

// int main() {
//     int n;
//     scanf("%d", &n);
//     int arr[n];
//     for (int i = 0; i < n; i++) {
//         scanf("%d", &arr[i]);
//     }
//     int num;
//     scanf("%d", &num);
//     two_sum(n, arr, num);
//     return 0;
// }
