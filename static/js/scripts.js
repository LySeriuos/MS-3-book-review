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

    const container = document.querySelector('.rating');
    const items = container.querySelectorAll('.rating-item')
    container.onclick = e => {
    const elClass = e.target.classList;
// change the rating if the user clicks on a different star
    if (!elClass.contains('active')) {
    items.forEach( // reset the active class on the star
    item => item.classList.remove('active')
    );
    console.log(e.target.getAttribute("data-rate"));
    elClass.add('active'); // add active class to the clicked star
    }
    };
    


  
});
