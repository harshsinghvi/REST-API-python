// function main(){
//     const Http = new XMLHttpRequest();
//     const url='http://localhost:5000/questions';
//     Http.open("GET", url);
//     Http.send();
    
//     Http.onreadystatechange = (e) => {
//       console.log(Http.responseText)
//     }
//     return HtmlService.createHtmlOutput('Hii Harsh');
// }

var delayInMilliseconds = 1000; //1 second

setTimeout(function() {
  //your code to be executed after 1 second
//   console.log("Delay");
  return 0;
}, delayInMilliseconds);








// function httpGet()
// {
//     theUrl='http://localhost:5000/questions';
//     console.log("in function")
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
//     xmlHttp.send( null );
//     console.log(xmlHttp.responseText);
//     var x = JSON.parse(xmlHttp.responseText);
//     for(i in x)
//     {
//       console.log(i);
//     }

//     return xmlHttp.responseText;
//     return 0;
// }


function put(){ 
               
  let result = document.querySelector('.result'); 
  let put_data = document.querySelector('#put_data'); 
//   let email = document.querySelector('#email'); 
  // var timestamp = new Date(year, month, day, hours, minutes, seconds, milliseconds);
  // console.log(timestamp)
  // Creating a XHR object 
  let xhr = new XMLHttpRequest(); 
  let url = "http://localhost:5000/put?data="+put_data.value; 
  console.log(url)
  // open a connection 
  xhr.open("POST", url, true); 

  // Set the request header i.e. which type of content you are sending 
  xhr.setRequestHeader("Content-Type", "application/json"); 

  // Create a state change callback 
  xhr.onreadystatechange = function () { 
      if (xhr.readyState === 4 && xhr.status === 200) { 

          // Print received data from server 
          result.innerHTML = this.responseText; 

      } 
  }; 
    // console.log(put_data.value)
  // Converting JSON data to string 
  var data = JSON.stringify({ "put_data": put_data.value  }); 

  // Sending data with the request 
  xhr.send(data); 
  setTimeout(300);
  window.location.replace("index.html");
}

function get(){
    // let xhr = new XMLHttpRequest(); 
    // let url = "http://localhost:5000/pop";
    // xhr.open("GET", url, true); 
    // xhr.send(); 


    
    fetch('http://localhost:5000/get')
    .then((response) => {
    return response.json()
    })
    .then((data) => {
    // Work with JSON data here 
    })
    .catch((err) => {
    // Do something for an error here
    // document.write("ERROR");

    })


    setTimeout(300);
    window.location.replace("index.html");
 
}

function filesave(){
    // let xhr = new XMLHttpRequest(); 
    // let url = "http://localhost:5000/pop";
    // xhr.open("GET", url, true); 
    // xhr.send(); 


    
    fetch('http://localhost:5000/filesave')
    .then((response) => {
    return response.json()
    })
    .then((data) => {
    // Work with JSON data here 
    })
    .catch((err) => {
    // Do something for an error here
    // document.write("ERROR");

    })


    setTimeout(2000);
    window.location.replace("index.html");
 
}