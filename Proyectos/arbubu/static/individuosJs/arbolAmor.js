var map = L.map( 'map', {
  center: [42.3409139, -3.72716944444444],
  maxZoom: 18,
  zoom: 18,
})

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo( map )

var myURL = jQuery( 'script[src$="arbolAmor.js"]' ).attr( 'src' ).replace( 'arbolAmor.js', '' )

var myIcon = L.icon({
  iconUrl: myURL + 'pin24.png',
  iconSize: [29, 24],
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
})

for ( var i=0; i < markers.length; ++i )
{

  if(i==19){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: </strong>" + markers[i].nombreComun )
     .addTo( map );
  }

}
