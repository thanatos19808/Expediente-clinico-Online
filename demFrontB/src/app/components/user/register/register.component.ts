
import { Component, OnInit } from '@angular/core';
import { AuthService } from "../../../services/auth.service";
import { UserInterface } from "../../../models/user-interface";
import { Router } from "@angular/router";

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor(private authService: AuthService, private router: Router) { }
  private user: UserInterface = {
    name: "",
    password: "",
    email: ""
  };

  ngOnInit() {
  }

  onRegister():void{
    let token = this.authService.registerUser(
      this.user.password,
      this.user.password2,
      this.user.email
    )
    .subscribe(user =>{
      //mensaje registro exito
      this.router.navigate(['/login']);
    });
  }

}