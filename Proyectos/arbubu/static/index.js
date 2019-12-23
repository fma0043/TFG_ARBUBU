var map = L.map( 'map', {
  center: [42.3509, -3.688],
  minZoom: 1,
  maxZoom: 20,
  zoom: 18,
})

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo( map )

var myURL = jQuery( 'script[src$="index.js"]' ).attr( 'src' ).replace( 'index.js', '' )

var myIcon = L.icon({
  iconUrl: myURL + 'pin24.png',
  iconSize: [29, 24],
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
})

for ( var i=0; i < markers.length; ++i )
{
  if(i==0){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cirueloRojo4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==1){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinsapo4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==2){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= olivo></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==3){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= acebo2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==4){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abetoRojo8></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==5){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= hiedra2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==6){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= sauceLloron4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==7){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= nogal2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==8){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= laurelCerezo2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==9){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tuyaGigante2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==10){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= catalpa></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==11){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= taray2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==12){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= lilo2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==13){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= platanoSombra7></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==14){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= falsaAcacia2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==15){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= olmoSiberiano2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==16){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= chopoCanadiense4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }


  if(i==17){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= hayaPurpura></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==18){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= falsoEbano></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==19){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= arbolAmor></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==20){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= arbolTulipanes></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==21){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= encina></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==22){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= quejigo></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==23){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= sauceLloron2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==24){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= aligustreJapon1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==25){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= aligustreJapon2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==26){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= aligustreJapon3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==27){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cipresLeyland></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==28){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= moral></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==29){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cirueloRojo3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==30){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abetoRojo6></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==31){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abetoRojo7></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==32){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= madreselva></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==33){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= sauceLloron3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==34){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinsapo3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==35){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tuyaOriental></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==36){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= taray1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==37){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tejo2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==38){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= nogal1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==39){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= falsaAcacia1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==40){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= lilo1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==41){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= alamoBlanco2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==42){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tilo2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }


  if(i==43){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinoPinonero1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==44){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinoPinonero2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==45){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinoPinonero3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==46){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinoPinonero4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==47){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinoPinonero5></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==48){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tejo1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==49){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tuyaCanada1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==50){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tuyaCanada2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==51){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tuyaCanada3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==52){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abetoRojo1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==53){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abetoRojo2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==54){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abetoRojo3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==55){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abetoRojo4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==56){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abetoRojo5></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==57){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAtlas3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==58){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAtlas4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==59){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAtlas5></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==60){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAtlas6></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==61){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAtlas7></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==62){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAtlas8></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==63){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroHimalaya3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==64){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tilo1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==65){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinsapo2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==66){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= laurelCerezo1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==67){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cirueloRojo2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }


  if(i==68){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= platanoSombra2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==69){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= platanoSombra3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==70){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= platanoSombra4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==71){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= platanoSombra5></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==72){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= platanoSombra6></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==73){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= tuyaGigante1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==74){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= hiedra1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==75){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= pinsapo1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==76){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAtlas2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==77){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abeto1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==78){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= abeto2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==79){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= chopo></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==80){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= peral></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==81){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= chopoCanadiense2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==82){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= chopoCanadiense3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==83){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= olmoSiberiano1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==84){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= sauco></strong>" + markers[i].nombreComun )
     .addTo( map );
  }


  if(i==85){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroHimalaya1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==86){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroHimalaya2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==87){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAtlas1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==88){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cedroAzul></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==89){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cipresArizona1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==90){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cipresArizona2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==91){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= alamoChino1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==92){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= alamoChino2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==93){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= alamoChino3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==94){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= alamoChino4></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==95){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= higuera></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==96){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= rosaDeSiria></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==97){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= ailanto1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==98){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= ailanto2></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==99){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= ailanto3></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==100){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= platanoSombra1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==101){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= alamoBlanco1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==102){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= sauceLloron1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==103){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= cirueloRojo1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==104){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= secuoyaGigante></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==105){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= chopoCanadiense1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==106){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= moribundo></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==107){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= haya></strong>" + markers[i].nombreComun )
     .addTo( map );
  }
  if(i==108){
    L.marker( [markers[i].latitud, markers[i].longitud], {icon: myIcon} )
     .bindPopup(  "<strong>Motivo Singular: </strong>"+markers[i].motivoSingular   + "<br/><strong>Explicación Singularidad: </strong>" + markers[i].explicacionMotivoSingular + "<br/><strong>Nombre Árbol: <a href= acebo1></strong>" + markers[i].nombreComun )
     .addTo( map );
  }

}
