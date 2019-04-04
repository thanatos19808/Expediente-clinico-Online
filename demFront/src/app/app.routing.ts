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

//Array de Rutas
const appRoutes: Routes = [
    {path: '', component: MenuInicioComponent},
    {path: 'login', component: LoginComponent},
    {path: 'inicio', component: MenuInicioComponent},
    {path: 'agenda', component: MenuAgendaComponent},
    {path: 'ajustes', component: MenuAjustesComponent},
    {path: 'paciente', component: MenuPacientesComponent},
    {path: 'pago', component: MenuPagoComponent},
    {path: '**', component: ErrorComponent}
];

// exportar modulo de router
export const RoutingProviders: any[] = [];
export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);


