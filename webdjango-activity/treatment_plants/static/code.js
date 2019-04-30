import { csv } from 'd3-request';
import url from 'C:/Users/Usuario/Desktop/django/mysite/treatment_plants/templates/treatment_plants/enbio.csv';
$(document).ready(function(){
	$('#bAnadirCSV').click(console.log("a"))
    function cargarDeCSV(){
	    console.log("aaa");
        csv(url, function(err, data) {
         console.log(data);
        })
    }
    function printPrueba(){
	    console.log("aaa");
    }
    });