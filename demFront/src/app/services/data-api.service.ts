import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from "rxjs/internal/Observable";
import { map } from 'rxjs/operators';

import { AuthService } from "./auth.service";

@Injectable({
  providedIn: 'root'
})
export class DataApiService {
  doctors: Observable<any>;
  doctor: Observable<any>;
  paciente: Observable<any>;
  pacientes: Observable<any>;

  constructor(private http: HttpClient, private authService: AuthService) { }
  
  headers: HttpHeaders = new HttpHeaders({
    'Content-Type': 'application/json',
    Authorization: this.authService.getToken()
  });
  
  getAllBooks() {
    const url_api = `http://localhost:3000/api/doctor`;
    return this.http.get(url_api);
  }

  getDoctorById(id: string){
    const url_api= `http://localhost:3000/api/doctor/${id}`;
    return (this.doctor = this.http.get(url_api));
  }

  savePaciente(paciente){
    // token
    // not null
    let token = this.authService.getToken();
    const url_api= `http://localhost:3000/api/paciente?acess_token=${token}`;
    return this.http
      .post(url_api, paciente,{headers: this.headers})
      .pipe(map(data => data));
  }

  updateDoctor(doctor){
    // token
    // not null
    let token = this.authService.getToken();
    const url_api= `http://localhost:3000/api/doctor?acess_token=${token}`;
    return this.http
      .put(url_api, doctor,{headers: this.headers})
      .pipe(map(data => data));
  }

  deletePaciente(id: string){
    // token
    // not null
    let token = this.authService.getToken();
    const url_api= `http://localhost:3000/api/paciente?acess_token=${token}`;
    return this.http
      .delete(url_api,{headers: this.headers})
      .pipe(map(data => data));
  }
}
  