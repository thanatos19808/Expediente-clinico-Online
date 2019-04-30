import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CalendarModule, DateAdapter } from 'angular-calendar';
import { adapterFactory } from 'angular-calendar/date-adapters/date-fns';


import { routing, RoutingProviders} from './app.routing';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { LoginComponent } from './components/user/login/login.component';
import { RegisterComponent } from './components/user/register/register.component';
import { Page404Component } from './components/page404/page404.component';
import { MenuAjustesComponent } from './components/menu-ajustes/menu-ajustes.component';
import { MenuPacientesComponent } from './components/menu-pacientes/menu-pacientes.component';
import { MenuPagoComponent } from './components/menu-pago/menu-pago.component';
import { CalendarioComponent } from './components/calendario/calendario.component';
import { ListaComponent } from './components/lista/lista.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

//services
import { DataApiService } from 'src/app/services/data-api.service';



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavbarComponent,
    LoginComponent,
    RegisterComponent,
    Page404Component,
    MenuAjustesComponent,
    MenuPacientesComponent,
    MenuPagoComponent,
    CalendarioComponent,
    ListaComponent
  ],
  imports: [
    BrowserModule,
    routing,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    CalendarModule.forRoot({
      provide: DateAdapter,
      useFactory: adapterFactory
    })
  ],
  providers: [
    DataApiService,
    RoutingProviders
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
