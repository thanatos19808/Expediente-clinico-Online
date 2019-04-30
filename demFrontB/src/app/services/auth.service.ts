import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs/internal/Observable';
import { map } from 'rxjs/operators';
import { isNullOrUndefined } from "util";

import {UserInterface } from "../models/user-interface";

@Injectable({
  providedIn: 'root'
})

export class AuthService {
  constructor(private http: HttpClient) {}
  headers : HttpHeaders = new HttpHeaders({
    "Content-Type": "application/json"
  });

  private currentUser: UserInterface = {
    name: "",
    password: "",
    email: ""
  };

  registerUser(password1: string, password2: string, email: string){
    const url_api = 'http://104.248.176.189:8000/rest-auth/registration/';
    return this.http
      .post(
        url_api, 
        {
          "password1": password1,
          "password2": password2,
          "email": email
        }
      )
      .pipe(map(data => data));
  }

  loginuser(email: string, password: string): Observable<any>{
    const url_api = 'http://104.248.176.189:8000/rest-auth/login/';
    return this.http
    .post<UserInterface>
    (url_api,
      {email, password},
      {headers: this.headers }
      ).pipe(map(data => data));
  }


  setEmail(email): void{
    localStorage.setItem("email", email);
  }


  getCurrentUser():UserInterface{
    let user_string = localStorage.getItem("currentUser");
    if (!isNullOrUndefined(user_string)) {
      let user: UserInterface= JSON.parse(user_string);
      return user;
    } else {
      return null;
    }
  }

  setToken(token): void{
    localStorage.setItem("key", token);
  }

  getToken(){
    return localStorage.getItem("key");
  }

  setPassword(password): void{
    localStorage.setItem("password", password);
  }

  getPassword(){
    return localStorage.getPassword("password");
  }

  setInterface(user: UserInterface): void {
    let user_string = JSON.stringify(user);
    localStorage.setItem("currentUser", user_string);
  }
  
  logoutUser(){
    let currentUser = localStorage.getItem("user");
    let currentPassword = localStorage.getItem("password");
    const url_api = 'http://104.248.176.189:8000/rest-auth/logout/';
    localStorage.removeItem("currentUser");
    return this.http
    .post<UserInterface>
    (url_api,
      {currentUser, currentPassword},
      {headers: this.headers }
      ).pipe(map(data => data));
  }



}

  
