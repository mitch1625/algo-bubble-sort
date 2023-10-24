var sequence = [4, 3, 5, 0, 1]
var swaps = 0

function bubbleSort(arr){
    let swapCount = 0
    for (let i = 0; i < arr.length;i++) {
        for (let j = 0; j < arr.length-1; j++){
            if (arr[j] > arr[j+1]){
                let current = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = current
                console.log(arr)
            }
            swapCount+=1;
        }
    }
    // let result = arr
    console.log(arr)
}


bubbleSort(sequence)
// console.log("Final result: " + result)
// console.log("Swaps: " + swaps)
