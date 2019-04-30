import { Component, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'menu-pacientes',
  templateUrl: './menu-pacientes.component.html',
  styleUrls: ['./menu-pacientes.component.css']
})
export class MenuPacientesComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    this.tabla();
  }
 
  tabla(){
    $(document).ready(function() {
      $('#lista').DataTable( {
        "language": {
          "sProcessing":     "Procesando...",
          "sLengthMenu":     "Mostrar _MENU_ pacientes",
          "sZeroRecords":    "No se encontraron resultados",
          "sEmptyTable":     "Ningún dato disponible en esta tabla",
          "sInfo":           "Mostrando pacientes del _START_ al _END_ de un total de _TOTAL_ pacientes",
          "sInfoEmpty":      "Mostrando pacientes del 0 al 0 de un total de 0 registros",
          "sInfoFiltered":   "(filtrado de un total de _MAX_ pacientes)",
          "sInfoPostFix":    "",
          "sSearch":         "Buscar:",
          "sUrl":            "",
          "sInfoThousands":  ",",
          "sLoadingRecords": "Cargando...",
          "oPaginate": {
              "sFirst":    "Primero",
              "sLast":     "Último",
              "sNext":     "Siguiente",
              "sPrevious": "Anterior"
          },
          "oAria": {
            "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        }
      }
        } );
    } );
  }

}