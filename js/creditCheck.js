function creditCheck(str) {
  let arr = str.split('').reverse(); 
  for(let i = 1; i < arr.length; i+=2) { 
    arr[i] *= 2
    let temp = [];
    if(arr[i] > 9) {
       temp = arr[i].toString().split('');
       let sum = temp.reduce((a, b) => {
          return parseInt(a)+parseInt(b);
       });
       arr[i] = sum;
    }
  }
  let res = arr.reduce((a, b) => {
    return parseInt(a) + parseInt(b);
  })
  console.log(res);
  return (res % 10 === 0)
}

console.log(creditCheck('5541808923795240'));
console.log(creditCheck("6011797668867828"));
console.log(creditCheck("5541801923795240"));


