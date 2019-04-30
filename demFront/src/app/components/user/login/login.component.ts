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
    password: "",
    token: ""
  };

  ngOnInit() {}
    onLogin(){
      return this.authService.loginuser(this.user.email, this.user.password)
      .subscribe(
        data =>{
          console.log(this.user.email);
          console.log(this.user.password);
          this.user.token = data.key;
          this.authService.setInterface(this.user);
          this.router.navigate(['/inicio']);
        },
        error => console.log(error)
      );
  }
}
