import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { routing, RoutingProviders} from './app.routing';

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

@NgModule({
  declarations: [
    AppComponent,
    ErrorComponent,
    LoginComponent,
    MenuAgendaComponent,
    MenuAjustesComponent,
    MenuInicioComponent,
    MenuPacientesComponent,
    MenuPagoComponent,
    CalendarioComponent,
    ListaComponent,
    MenuComponent
  ],
  imports: [
    BrowserModule,
    MDBBootstrapModule.forRoot(),
    routing
  ],
  providers: [
    RoutingProviders
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
