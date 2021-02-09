async function main(){
    var url = "localhost:5000/api-auth-test";
    const response = await fetch(url);
    var data = await response.json();
    document.getElementById("size").innerHTML="test = "+data['test'];
    console.log(data);
}