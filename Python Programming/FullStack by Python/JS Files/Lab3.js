// function birthday(nowyear , youryear){
//     var age  = nowyear - youryear;
//     return age;
// }
// console.log(birthday(2025, 2004)); 

// var student = {
//     name: "Abdallah",
//     age: 20,
//     city: "Shibin El Kom",
// }
// function appearinfo(){
//     console.log(student.name + " " + student.age + " " + student.city);
// }
// appearinfo();

// var arr = ["Play" , "Eat" , "Sleep"];
// function addtask(task){
//     arr.push(task);
//     console.log(arr);
// }
// addtask("Study");

// function removetask(task){
//     arr.splice(arr.indexOf(task), 1);
//     console.log(arr);
// }
// removetask("Eat");

// function showalltasks(){
//     console.log(arr);
// }
// showalltasks();
// var product = {
//     name: "Laptop",
//     price : 100000,
//     category: "Electronics",
//     discount: 0.1,
// }
// function calculatePrice(product) {
//     var finalPrice = product.price - (product.price * product.discount);
//     return finalPrice;
// }
// console.log(calculatePrice(product));

// var products = {
//     name: "Laptop",
//     price : 100000,
//     instockkeys : 5 ,
//     name2: "Mobile",
//     price2 : 50000,
//     instockkeys2 : 10 ,
//     name3: "Tablet",
//     price3 : 30000,
//     instockkeys3 : 15
// }

// function displayproducts(){
//     for (var key in products) {
//         console.log(key + ": " + products[key]);
// }}
// displayproducts();
// function buyproduct(produtname , key){
//     if (products["instockkeys" + key] > 0) {
//         products["instockkeys" + key]--;
//         console.log("You bought " + produtname + ". Remaining stock: " + products["instockkeys" + key]);
//     } else {
//         console.log("Sorry, " + produtname + " is out of stock.");
//     }
// }
// buyproduct("Laptop" , 1);
// buyproduct("Mobile" , 2);
// buyproduct("Tablet" , 3);
// console.log(products);

// function calculatetotalbill(products){
//     var total = 0;
//     for (var key in products) {
//         if (products[key] > 0) {
//             total += products[key];
//         }
//     }
//     return total;
// }
// console.log("Total is = " + calculatetotalbill(products));



var library = [
    {
        title: "Python",
        author: "Abdallah",
        year: 2025
    },
    {
        title: "JavaScript",
        author: "Abdallah",
        year: 2025
    }
]

function showAllBooks() {
      for(var i=0;i<library.length;i++){
        console.log("title: " + library[i].title +" " +"author: " + library[i].author + " "+ "year: " + library[i].year)
    }
}

function searchBook(title) {
    for(var i=0;i<library.length;i++){
        if(title.toLowerCase()===library[i].title.toLowerCase()){
            console.log("book found: "+library[i].title+" by "+library[i].author);
            return;
        }
    }
    console.log("book not found");
}

function addBook(title,author,year){
    var newBook={
        title:title,
        author:author,
        year:year
    }

    library.push(newBook);
    console.log("successfully added book")
}

searchBook("Python");
addBook("c#","abdallah",2025);
console.log(showAllBooks());




