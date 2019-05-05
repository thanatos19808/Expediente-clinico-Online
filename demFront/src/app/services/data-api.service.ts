import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from "rxjs/internal/Observable";
import { map } from "rxjs/operators";

import {PacienteInterface} from "../models/paciente-interface";
import {AuthService} from "./auth.service";

@Injectable({
  providedIn: 'root'
})

export class DataApiService {
  constructor(private http:HttpClient, private AuthService: AuthService) { }
  paciente: Observable<any>;
  pacientes: Observable<any>;

  headers: HttpHeaders = new HttpHeaders({
    "Content-Type": "aplication/json",
    Authorization: this.AuthService.getToken()
  });

  getAllPacientes(){
    const url_api = 'http://104.248.176.189:8000/PacientesList/';
    return this.http
      .post<PacienteInterface>(url_api, {headers: this.headers}) 
      .pipe(map(data => data));
  }
}
