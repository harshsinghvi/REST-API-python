
// Replace ./data.json with your JSON feed

fetch('http://localhost:5000/db')
  .then((response) => {
    return response.json()
  })
  .then((data) => {
    // Work with JSON data here
    console.log(data.que)
    console.log(data)
    // document.write("Hello World!!");
    // document.write(data);
    // document.write(data.que);
    for(i in data)
    {
        document.write("<h1>"+i+". ");
        document.write(data[i]['que']+"</h1><br>");
        for(j in data[i]['choices'])
        {
            document.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+j+".&nbsp"+ data[i]['choices'][j]+"<br>");
        }
        document.write("<br><br>");


    }


  })
  .catch((err) => {
    // Do something for an error here
    document.write("ERROR");

  })

