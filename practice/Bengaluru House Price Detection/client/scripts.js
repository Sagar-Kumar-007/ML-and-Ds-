function getBHK(){
    var size=document.getElementsByName("size");
    for(i in size){
        //console.log(size[i]);
        if(size[i].checked){
            return parseInt(i)+1;
        }
        return -1;   // Invalid
    }
};

function getBalcony(){
    var balcony=document.getElementsByName("balcony");
    for(i in balcony){
        //console.log(size[i]);
        if(balcony[i].checked){
            return parseInt(i)+1;
        }
        return -1;   // Invalid
    }
};


function getPrice(){
    var total_sqft=document.getElementById("area_sqft");
    var area_type=document.getElementById("area1");
    var location=document.getElementById("main_locations");
    var ans=document.getElementById("ans");
    url="http://127.0.0.1:5000/get_estimated_price";
    $.post(url,{
        "total_sqft":total_sqft.value,
        "size":getBHK(),
        "balcony":getBalcony(),
        "area_type":area_type.value,
        "location":location.value
    },function(data,status){
        ans.innerHTML="<h3>"+data.estimated_price.toString()+" Rs"+"</h3>";
    });
};



function pageOnLoad(){
    url="http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data,status){   // jquery method to recieve data from the server. Since, data is in the form of json file, the variable data is also in json/object format.
        if(data){
            var location=data.location;
            var main_locations=document.getElementById("main_locations");
            $('#main_locations').empty();        // $('') is used to select a class or id or a tag.  .empty() is used to remove all the child nodes of the parent.
            for(var i in location){
                var opt= new Option(location[i]);  // we create a new object Option which will then be appended to the location tag as child nodes.
                $('#main_locations').append(opt);
            }
        }
    });
    // There is no need to get the get_area_type values from the server since there are only 3 columns which is already been added.
}

window.onload=pageOnLoad;