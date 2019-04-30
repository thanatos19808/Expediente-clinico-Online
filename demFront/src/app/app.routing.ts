// modulos de router de angular
import {ModuleWithProviders} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
  
//componentes
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/user/login/login.component';
import { RegisterComponent } from './components/user/register/register.component';
import { Page404Component } from './components/page404/page404.component';
import { MenuAjustesComponent } from './components/menu-ajustes/menu-ajustes.component';
import { MenuPacientesComponent } from './components/menu-pacientes/menu-pacientes.component';
import { MenuPagoComponent } from './components/menu-pago/menu-pago.component';
import { AuthGuard } from './guards/auth.guard';

//Array de Rutas
const appRoutes: Routes = [
    {path: '', component: LoginComponent},
    {path: 'login', component: LoginComponent},
    {path: 'registro', component: RegisterComponent},
    {path: 'inicio', component: HomeComponent, canActivate: [AuthGuard]},
    {path: 'inicio/agenda', component: HomeComponent, canActivate: [AuthGuard]},
    {path: 'inicio/ajustes', component: MenuAjustesComponent, canActivate: [AuthGuard]},
    {path: 'inicio/paciente', component: MenuPacientesComponent, canActivate: [AuthGuard]},
    {path: 'inicio/pago', component: MenuPagoComponent, canActivate: [AuthGuard]},
    {path: '**', component: Page404Component}
];


// exportar modulo de router
export const RoutingProviders: any[] = [];
export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);

