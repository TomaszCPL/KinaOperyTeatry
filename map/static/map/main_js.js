function map_init_basic (map, options)
        {
        $.ajax
            ({
	        url:'http://localhost:8000/api/places/',
	        type:'GET',
	        data:'json',
            }).done(
                    function(response)
                        {
                        var date = new Date();
                        var today = '0'+date.getDate() +"." +Number(date.getMonth()+1)+"." +date.getFullYear();

                        $.each(response, function(i,place)
                            {
                            $(place.shows).each(function(index){
                                if (place.shows[index].date == today){
                                    $('#accordion').append('<h3></h3><div><p></p></div>')
                                    var marker = L.marker([place.lat,place.long])
                                    $("#accordion").accordion("refresh");
                                    $("h3").eq(i).text(place.name);
                                      var div = $("h3").eq(i).next();
                                       var title = place.shows[index].title;
                                       var time = place.shows[index].time;
                                       var date = place.shows[index].date;
                                       var titled = title.substr(0,1).toUpperCase()+title.substr(1);
                                       div.append('<strong>' + titled + '</strong>' + '</br>' + date + ' ' + time +'<hr>')

                                    marker.setBouncingOptions({
                                    bounceHeight : 10,
                                    bounceSpeed  : 80,
                                    exclusive    : true,
                                        }).on('click', function() {
                                    this.toggleBouncing();
                                        $("h3").eq(i).click()
                                     });
                                    marker.addTo(map);
                                   return false}else{}

                                });
                            })
                        }
                    );
             };




