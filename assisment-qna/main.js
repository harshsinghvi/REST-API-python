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


function httpGet()
{
    theUrl='http://localhost:5000/questions';
    console.log("in function")
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log(xmlHttp.responseText);
    var x = JSON.parse(xmlHttp.responseText);
    for(i in x)
    {
      console.log(i);
    }

    return xmlHttp.responseText;
    return 0;
}


function sendJSON(){ 
               
  let result = document.querySelector('.result'); 
  let name = document.querySelector('#name'); 
  let email = document.querySelector('#email'); 
  // var timestamp = new Date(year, month, day, hours, minutes, seconds, milliseconds);
  // console.log(timestamp)
  // Creating a XHR object 
  let xhr = new XMLHttpRequest(); 
  let url = "http://localhost:5000/db-in"; 

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

  // Converting JSON data to string 
  var data = JSON.stringify({ "name": name.value, "email": email.value,  }); 

  // Sending data with the request 
  xhr.send(data); 
}