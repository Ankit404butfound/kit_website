function loadDoc() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
      document.getElementById("code_area").innerHTML =
      this.responseText;
      console.log(this.responseText);
    }
    xhttp.open("GET", "https://raw.githubusercontent.com/Ankit404butfound/kit_website/main/html/sendwhatmsg.html");
    xhttp.send();
  }