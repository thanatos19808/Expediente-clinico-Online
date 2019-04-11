// modulos de router de angular
import {ModuleWithProviders} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';

//componentes
import { LoginComponent} from './view/login/login.component';
import { MenuAgendaComponent} from './view/menu-agenda/menu-agenda.component';
import { MenuAjustesComponent} from './view/menu-ajustes/menu-ajustes.component';
import { MenuInicioComponent} from './view/menu-inicio/menu-inicio.component';
import { MenuPacientesComponent} from './view/menu-pacientes/menu-pacientes.component';
import { MenuPagoComponent} from './view/menu-pago/menu-pago.component';
import { ErrorComponent} from './view/error/error.component';
import { MenuRegistroComponent} from './view/menu-registro/menu-registro.component';

//Array de Rutas
const appRoutes: Routes = [
    {path: '', component: LoginComponent},
    {path: 'login', component: LoginComponent},
    {path: 'registro', component: MenuRegistroComponent},
    {path: 'inicio', component: MenuInicioComponent},
    {path: 'inicio/agenda', component: MenuAgendaComponent},
    {path: 'inicio/ajustes', component: MenuAjustesComponent},
    {path: 'inicio/paciente', component: MenuPacientesComponent},
    {path: 'inicio/pago', component: MenuPagoComponent},
    {path: 'inicio/registro', component: MenuRegistroComponent},
    {path: '**', component: ErrorComponent}
];

// exportar modulo de router
export const RoutingProviders: any[] = [];
export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);


