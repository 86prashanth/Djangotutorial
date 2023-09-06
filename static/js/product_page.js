const plusButton = document.getElementById("plus");
const minusButton = document.getElementById("minus");

const inputData = document.getElementById("input");
plusButton.addEventListener('click',()=>{
    inputValue = parseInt(inputData.value);
    inputValue = inputValue + 1;
    inputData.value = inputValue;
})


minusButton.addEventListener('click',()=>{
    inputValue = parseInt(inputData.value);
    if(inputValue > 1 ){
        inputValue = inputValue - 1;
        inputData.value = inputValue;
    }
})



const stars=document.querySelectorAll('.p-star-rating');
const current_rating=document.getElementById("current-rating");

stars.forEach((star,index)=>{
  star.addEventListener('click',()=>{

    let current_star=index+1;
    current_rating.innerText=`${current_star} of 5`;

    stars.forEach((star,i)=>{
        if(current_star>=i+1){
          star.innerHTML='&#9733;';
        }else{
          star.innerHTML='&#9734;';
        }
    });

  });
});