var map = L.map( 'map', {
  center: [42.3391583, -3.71896111111111],
  maxZoom: 18,
  zoom: 18,
})

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo( map )

var myURL = jQuery( 'script[src$="cedroAtlas6.js"]' ).attr( 'src' ).replace( 'cedroAtlas6.js', '' )

var myIcon = L.icon({
  iconUrl: myURL + 'pin24.png',
  iconSize: [29, 24],
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
})

for ( var i=0; i < markers.length; ++i )
{

  if(i==60){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: </strong>" + markers[i].nombreComun )
     .addTo( map );
  }

}
