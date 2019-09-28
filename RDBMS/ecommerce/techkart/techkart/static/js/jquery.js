$(".toggle-password").click(function () {

    $(this).toggleClass("fa-eye fa-eye-slash");
    var input = document.getElementById("pass");
    if (input.type === "password") {
        input.type = "text";
    } else {
        input.type = "password";
    }
});
// Set the date we're counting down to
var countDownDate = new Date("Oct 5, 2019 24:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    
  // Find the distance between now and the count down date
  var distance = countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="demo"
  document.getElementById("days").innerHTML = days;
  
  document.getElementById("hours").innerHTML = hours;
  
  document.getElementById("mins").innerHTML = minutes;
  
  document.getElementById("secs").innerHTML = seconds;
    
   //If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    //document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);
let html =`<span style="margin-left:40%;">Free</span>`;
let tip = `<span data-toggle="tooltip" title="Maximum 10 products can be Ordered by a User!"></span>`;
let val = parseInt(document.getElementById("proPrice").value, 10);
//document.getElementById("totalPrice").value = val;
let delCharge = 50;

if(val >= 500)
{
    $(document).ready(function () {
            $(this).find('#deliveryIcon').replaceWith(html);
    });
} else
{
    document.getElementById("delivery").value = delCharge;
  }
document.getElementById("priceItem").value = val;
function increaseValue() {
  let value = parseInt(document.getElementById("number").value, 10);
  value = isNaN(value) ? 0 : value;
  value++;
  if(value > 10)
  {
      value = 10;
      document.getElementById('number').value = value;
  }
  else
  {
      document.getElementById('number').value = value;
  }
  document.getElementById("decrease").disabled = false;
  let price = parseInt(document.getElementById("proPrice").value, 10);
  price =val;
  document.getElementById("proPrice").value = price;
  document.getElementById("itemVal").value = value;
  document.getElementById("priceItem").value = (price*value);
  if(val < 500)
  {
    document.getElementById("delivery").value = (value * delCharge);
    document.getElementById("totalPrice").value = (price*value) + (value * delCharge);
  }
  else
  {
    document.getElementById("totalPrice").value = (price*value);
  }
}
if(val<500)
{
    document.getElementById("totalPrice").value = val+delCharge;
}
else
{
    document.getElementById("totalPrice").value = val;
}

function decreaseValue() {
  let value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 0 : value;
  value < 1 ? value = 1 : '';
  value--;
  document.getElementById('number').value = value;
  let price = parseInt(document.getElementById("proPrice").value, 10);
  price =val;
  document.getElementById("proPrice").value = price;
  if(value < 2)
      document.getElementById("decrease").disabled = true;
  document.getElementById("itemVal").value = value;
  document.getElementById("priceItem").value = (price*value);
  let delCharge = 50;
//  document.getElementById("totalPrice").value = price + delCharge;
  if(val < 500)
  {
    document.getElementById("delivery").value = (value * delCharge);
    document.getElementById("totalPrice").value = (price*value) + (value * delCharge);
  }
  else
  {
    document.getElementById("totalPrice").value = (price*value);
  }
}