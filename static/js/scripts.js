$(document).ready(function(){
    var today = new Date();
    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    document.getElementById("currentDate").value = date;
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    document.getElementById("currentTime").value = time;
    let xxx = document.getElementById("getBookId").textContent;
    console.log(xxx);
    let bookName = document.getElementById("getBookName").textContent;
    document.getElementById("currentBookName").value = bookName;
    let bookAuthor = document.getElementById("getAuthor").textContent;
    document.getElementById("currentAuthor").value = bookAuthor;
    
});
