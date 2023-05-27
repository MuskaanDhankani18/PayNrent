$(document).ready(function()
{
    //****on load **/
    $.getJSON("http://localhost:8000/api/displayvehicleforuser", {param:'all'}, function(data)
    {
        var htm = `<div class="rightbartemplate">
        <img src="/static/Subscription.png" width="85%" style="display: flex; margin-left: 7%; margin-top: 7%;">
         </div>`;
        data.map((item)=>{
            htm+=`<a href='http://localhost:8000/api/displayselectedvehicle/?vehicle=${JSON.stringify(item)}' style="text-decoration:none; cursor:pointer; color:#000;">
            <div class="rightbartemplate" style="margin-left: 3%;">
            <img src="/${item.icon}" width="60%" style="display: flex; margin-left: 20%; margin-top: 4%;">
            <div style="margin-left: 8%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 1%;">
                ${item.brandname}
            </div>
            <div style="margin-left: 8%; font-family: Poppins; font-size: 16; font-weight: 600;">
                ${item.subcategoryname}
            </div>
            <div style="margin-left: 5%; font-family: Poppins; font-size: 10; font-weight: 600;">
                <img src="/static/iconDiesel.svg" width="4%"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 600;">${item.fuel_type}</span>
                <img src="/static/iconTransmission.svg" width="11%" style="padding-left: 6%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 10; font-weight: 500;">${item.transmission_type}</span>
                <img src="/static/iconSeat.svg" width="10%" style="padding-left: 5%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.no_of_seats} Seats</span>
            </div>
            <div style="margin-left: 8%;">
                <div style="font-size: 20px; margin-top: 4%; display: flex; justify-content: space-between;">
                    <div style="display: flex; margin-left: 1%; margin-top: 1%; ">
                        &#8377<span style="font-family: Poppins; font-size: 20px; font-weight: bold;">
                           ${item.price}
                        </span>
                    </div>
                    <div class="button_style" style="display: flex; margin-right: 7%; margin-top: 1%;">
                        <div style="display: flex; align-items: center; font-size: 15; color: #fff; font-weight: bold;">Book  ></div>
                    </div>
                </div>
            </div>
            <div style="margin-left: 8%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 5%;">
                288 kms | Price <b>exclude</b> fuel cost 
            </div>
            </a>
        </div>`
});
        $('#listvehicle').html(htm);
        });
/*****/


    function searching(value)
    {
        $.getJSON("http://localhost:8000/api/displayvehicleforuser", {param:value}, function(data)
    {
        var htm = `<div class="rightbartemplate">
        <img src="/static/Subscription.png" width="85%" style="display: flex; margin-left: 7%; margin-top: 7%;">
         </div>`;
        data.map((item)=>{
            htm+=`<a href='http://localhost:8000/api/displayselectedvehicle/?vehicle=${JSON.stringify(item)}' style="text-decoration:none; cursor:pointer; color:#000;">
            <div class="rightbartemplate" style="margin-left: 3%;">
            <img src="/${item.icon}" width="60%" style="display: flex; margin-left: 20%; margin-top: 4%;">
            <div style="margin-left: 8%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 1%;">
                ${item.brandname}
            </div>
            <div style="margin-left: 8%; font-family: Poppins; font-size: 16; font-weight: 600;">
                ${item.subcategoryname}
            </div>
            <div style="margin-left: 5%; font-family: Poppins; font-size: 10; font-weight: 600;">
                <img src="/static/iconDiesel.svg" width="4%"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 600;">${item.fuel_type}</span>
                <img src="/static/iconTransmission.svg" width="11%" style="padding-left: 6%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 10; font-weight: 500;">${item.transmission_type}</span>
                <img src="/static/iconSeat.svg" width="10%" style="padding-left: 5%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.no_of_seats} Seats</span>
            </div>
            <div style="margin-left: 8%;">
                <div style="font-size: 20px; margin-top: 4%; display: flex; justify-content: space-between;">
                    <div style="display: flex; margin-left: 1%; margin-top: 1%; ">
                        &#8377<span style="font-family: Poppins; font-size: 20px; font-weight: bold;">
                           ${item.price}
                        </span>
                    </div>
                    <div class="button_style" style="display: flex; margin-right: 7%; margin-top: 1%;">
                        <div style="display: flex; align-items: center; font-size: 15; color: #fff; font-weight: bold;">Book  ></div>
                    </div>
                </div>
            </div>
            <div style="margin-left: 8%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 5%;">
                288 kms | Price <b>exclude</b> fuel cost 
            </div>
            </a>
        </div>`
});

        $('#listvehicle').html(htm);
    });
}
$(".brand").click(function () 
{
    var sb=''
    $(".brand").map(function (i, item) 
    {  
      if ($(this).prop("checked"))  
      {sb+="'"+$(this).val()+"',"}
    });
    sb=sb.substring(0,sb.length-1)
    if(sb=='')
      searching('all')
    else
      searching(sb)
    });
});
