
//Remove before moving to next branch
function dailyAccounting(moneyMade, moneyLost){
    if(moneyMade <= moneyLost){
        finances.checking+=moneyMade-moneyLost;
        console.log("Today's total amount of money lost is: $"+ (Math.abs((moneyMade - moneyLost))) + "\nRemaining balance in checking account:" + ( finances.checking) )
    }else{
        finances.checking+=moneyMade-moneyLost;
        console.log("Today's total amount of money made is: $" + (moneyMade - moneyLost) + "\nBalance in checking account:" + (finances.checking) )
    }

}
//Remove before moving to next branch
function multi(){
    var num1 = prompt("Enter first number to multiply:");
    var num2 = prompt("Enter second number to multiply:");
    alert("The sum of "+ num1 + "*" + num2+ "="+num1*num2);
    return (num1 * num2);
}

function becomeMember(){
    console.log("Member button pressed")
}

//Remove before moving to next branch
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

//Function that simply gives 3 breaks of 5 minutes then on the 4th break you get 15.
//Add one to the length to account for array slot 0.
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
    //Randomly generates numbers so I don't have to populate manually each time.
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

//Remove before moving to next branch
const shoe = {
    color: "Yellow",
    size: 40,
    price: 124.95,
    bestSeller: true
}
//Remove before moving to next branch
const car = {
    working: false,
    wheels: "Flat",
    price: 10
}
//Remove before moving to next branch
const finances = {
    savings: 1000,
    checking: 100,
    debt: 35000
}

//More document manipulation for the "become a memeber" button on the main page. Gives a blue background,
//purely for testing and should be removed before changing branches.

var mem = document.getElementById("member-bt").style.boxShadow = "10px 20px 30px blue"


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

//High Order Function -- Testing

function sum(n1,n2){
    return console.log(n1+n2);
}

function calc(n1,n2,op){
    op(n1,n2);
}


//Constuctors

var art;

function createUser(first,last){
    this.first=first;
    this.last=last;
    this.greeting = function(){
        console.log("WE're in create user")
    }
}

function signup(first,last) {
 art = new createUser(first,last);
    var overit = document.getElementById("changeme");

    overit.textContent = art.first + ' ' + art.last;
}


var user2 = {
    name:"Yeee",
    display: function(){
        return console.log("test");
    }
}

var arr= [true,false,true,false,false]
var total=0;
function calcArr(){
    arr.forEach(function(bool,i){
        if(bool){
            total++;
        }
    });
    return total;
}

function fibonacci(n){
    var arr = [0,1];
    var sum=0;

    for(i=0;i<8;i++){
        sum=arr[i]+arr[i+1];
        arr.push(sum);
    }
    console.log(arr);
}

const obj_2 ={
    vowels:0,
    consonants:0
};

var tiddies="mah gawd those are the biggest knockers I've ever seen. I do declare."

function countVowelsAndConsonants(arg1){
    arg1=arg1.toUpperCase();
    arg1=arg1.replaceAll(' ', '');
    console.log(arg1);
    var i=0;

    for(i=0;i<arg1.length;i++){
        console.log("Arg["+i+"]="+arg1[i]+"\n");
        if(arg1[i]==='A' || arg1[i]==='E' || arg1[i]==='I'|| arg1[i]==='O' || arg1[i]==='U' ){
            obj_2.vowels++;
        }else{
            obj_2.consonants++;
        }
    }

    return obj_2;
}
