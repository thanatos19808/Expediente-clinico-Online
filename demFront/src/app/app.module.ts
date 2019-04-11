import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { routing, RoutingProviders} from './app.routing';
import { DataTablesModule } from 'angular-datatables';

import { AppComponent } from './app.component';
import { ErrorComponent } from './view/error/error.component';
import { LoginComponent } from './view/login/login.component';
import { MenuAgendaComponent } from './view/menu-agenda/menu-agenda.component';
import { MenuAjustesComponent } from './view/menu-ajustes/menu-ajustes.component';
import { MenuInicioComponent } from './view/menu-inicio/menu-inicio.component';
import { MenuPacientesComponent } from './view/menu-pacientes/menu-pacientes.component';
import { MenuPagoComponent } from './view/menu-pago/menu-pago.component';
import { CalendarioComponent } from './component/calendario/calendario.component';
import { ListaComponent } from './component/lista/lista.component';
import { MenuComponent } from './component/menu/menu.component';
import { MenuRegistroComponent } from './view/menu-registro/menu-registro.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
//services
import { DataApiService }  from './services/data-api.service';

@NgModule({
  declarations: [
    AppComponent,
    ErrorComponent,
    LoginComponent,
    MenuAjustesComponent,
    MenuInicioComponent,
    MenuPacientesComponent,
    MenuPagoComponent,
    MenuAgendaComponent,
    CalendarioComponent,
    ListaComponent,
    MenuComponent,
    MenuRegistroComponent,
  ],
  imports: [
    BrowserModule,
    MDBBootstrapModule.forRoot(),
    routing,
    DataTablesModule,
    FormsModule,
  ],
  providers: [
    RoutingProviders,
    DataApiService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
