import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { routing, RoutingProviders} from './app.routing';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './view/login/login.component';
import { CalendarioComponent } from './component/calendario/calendario.component';
import { ListaComponent } from './component/lista/lista.component';
import { MenuInicioComponent } from './view/menu-inicio/menu-inicio.component';
import { MenuAgendaComponent } from './view/menu-agenda/menu-agenda.component';
import { MenuPacientesComponent } from './view/menu-pacientes/menu-pacientes.component';
import { MenuAjustesComponent } from './view/menu-ajustes/menu-ajustes.component';
import { MenuPagoComponent } from './view/menu-pago/menu-pago.component';
import { MenuComponent } from './component/menu/menu.component';
import { ErrorComponent } from './view/error/error.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    CalendarioComponent,
    ListaComponent,
    MenuInicioComponent,
    MenuAgendaComponent,
    MenuPacientesComponent,
    MenuAjustesComponent,
    MenuPagoComponent,
    MenuComponent,
    ErrorComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    routing
  ],
  providers: [
    RoutingProviders
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
