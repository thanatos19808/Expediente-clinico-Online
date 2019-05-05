import { Component, OnInit } from '@angular/core';
import { AuthService } from "../../../services/auth.service";
import { UserInterface } from "../../../models/user-interface";
import { Router } from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private authService:AuthService, private router: Router) { }
  private user: UserInterface = {
    email: "",
    password: ""
  };

  ngOnInit() {
    localStorage.removeItem("currentUser");
    localStorage.removeItem("accessToken");
  }
    
  onLogin(){
    return this.authService.loginuser(this.user.email, this.user.password)
    .subscribe(
      data =>{
        this.authService.setInterface(this.user);
        this.authService.setToken(data.key);
        this.router.navigate(['/inicio']);
      },
        error => this.mensajeError(error)
    );
  }

  mensajeError(error){
    alert("Error durante el login: " + error.statusText);
    console.log(error.statusText);
  }
}
