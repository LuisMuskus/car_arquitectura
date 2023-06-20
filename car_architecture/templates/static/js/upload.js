/*const dropArea = document.querySelector(".drop_box"),
  button = dropArea.querySelector("button"),
  dragText = dropArea.querySelector("header"),
  input = dropArea.querySelector("input");
let file;
var filename;

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function (e) {
  var fileName = e.target.files[0].name;
  let filedata = `
    <form method="post" action="{% url 'process_file' %}" enctype="multipart/form-data">
    <input type="hidden" name="csrfmiddlewaretoken" value="{% csrf_token %}">
    <div class="form">
    <h4>${fileName}</h4>
    <br>
    <input class="btn" type="submit" value="Enviar" style="display: flex;justify-content: center;">
    </div>
    </form>`;
  dropArea.innerHTML = filedata;
});*/
/* <input type="email" placeholder="Enter email upload file"></input> 
<button class="btn" type="submit" style="display: flex;justify-content: center;">Subir</button>
{% csrf_token %}
*/