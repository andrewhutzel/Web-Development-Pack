function dailyAccounting(moneyMade, moneyLost){
    if(moneyMade <= moneyLost){
        finances.checking+=moneyMade-moneyLost;
        console.log("Today's total amount of money lost is: $"+ (Math.abs((moneyMade - moneyLost))) + "\nRemaining balance in checking account:" + ( finances.checking) )
    }else{
        finances.checking+=moneyMade-moneyLost;
        console.log("Today's total amount of money made is: $" + (moneyMade - moneyLost) + "\nBalance in checking account:" + (finances.checking) )
    }

}

function multi(){
    var num1 = prompt("Enter first number to multiply:");
    var num2 = prompt("Enter second number to multiply:");
    alert("The sum of "+ num1 + "*" + num2+ "="+num1*num2);
    return (num1 * num2);
}

function becomeMember(){
    console.log("Member button pressed")
}

var list = ["jim", "bob", "cat"]
function friends_check(person){
    if(list.includes(person)){
        return alert("You're on the list")
    }else{
        return alert("You're not on the list")
    }
}


//Breaklist practice
const person = {
    break_list: [],
    time_worked: 0,
    time_breaked: 0
}

function pomo(){

        if((person.break_list.length+1)%4 !=0){
            person.break_list.push(5)
        }else{
            person.break_list.push(15)
        }

    return console.log(person.break_list);
}
//End Breaklist Practice

//Function that prints all even numbers in any given list
//Function that finds if in an array all even indexs contain even numbers and all odd indexes contain odd numbers. I pull random values every time to test the functionality.
function find_specials(){
    var test_arr=[];
    for(let i=0;i<Math.floor(Math.random() *10);i++){
        test_arr.push(Math.floor(Math.random() *10));
    }

    console.log(test_arr);

    for(let i=0;i<test_arr.length;i++){
        if(test_arr[i]%2 == 0 && i%2 == 0){
            continue;
        }else if((test_arr[i]%2) == 1 && (i%2) == 1){
            continue;
        }else{
            return false;
        }
    }
    return true;

}

//DOM var object manipulation
var obj = document.querySelector('.product_cards')
console.log(obj)

const shoe = {
    color: "Yellow",
    size: 40,
    price: 124.95,
    bestSeller: true
}

const car = {
    working: false,
    wheels: "Flat",
    price: 10
}

const finances = {
    savings: 1000,
    checking: 100,
    debt: 35000
}

//More document manipulation

var mem = document.getElementById("member-bt").style.boxShadow = "10px 20px 30px blue"
console.log(mem)

function hideNav() {
    document.querySelector(".main-nav").style.display = "none";
}



//Show / Hide Events

//Realistically you just eneed showreview, hidereview is redundant. For future updates remove hideReview()
//Function takes event, which is the caad that is triggered by the mouseover event.
//Assign the current target card to variable card then query the review & product_img.
function showReview(event){
    var card =event.currentTarget;
    card.querySelector(".review").classList.toggle("hover-review");
    card.querySelector(".product_img").classList.toggle("hover-img");
}

function hideReview(event){
    var card =event.currentTarget;
    card.querySelector('.review').classList.toggle("hover-review");
    card.querySelector(".product_img").classList.toggle("hover-img");
}


//Pull all the cards dynamically
var card_img = document.querySelectorAll(".product_cards");

//Traverse all cards and add an event listener for showing / hiding
card_img.forEach(function(card){
    card.addEventListener("mouseover",showReview)
    card.addEventListener("mouseout",hideReview)
});






//Check for when video ends and write to the console
function vid_end(){
    console.log("The video has ended!")
}

var vid = document.querySelector("video")
vid.addEventListener("ended",vid_end)


//Light and Dark Mode 
var sun= document.getElementById("sun-icon");
var moon= document.getElementById("moon-icon");
var body = document.getElementsByTagName("body")[0]
var introTxt = document.querySelector("#intro p")


function darkMode(){
    sun.style.display="none"
    moon.style.display="block"
    body.classList.toggle("body-dark")
    introTxt.style.color="#d3d3d3"
}

function lightMode(){
    sun.style.display="block"
    moon.style.display="none"
    body.classList.toggle("body-dark")
    introTxt.style.color="black"
}