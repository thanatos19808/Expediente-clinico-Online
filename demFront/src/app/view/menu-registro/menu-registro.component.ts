import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { UserInterface } from '../../models/user-interface';
import { Router } from '@angular/router';

@Component({
  selector: 'app-menu-registro',
  templateUrl: './menu-registro.component.html',
  styleUrls: ['./menu-registro.component.css']
})
export class MenuRegistroComponent implements OnInit {

  constructor(private authService: AuthService, private router: Router){}
  private user: UserInterface = {
    name: "",
    email: "",
    password: ""
  }; 
  
  ngOnInit() {
  }

  onRegister(): void{
    this.authService.registerUser(
      this.user.name,
      this.user.email,
      this.user.password
      )
      .subscribe( user =>{
        this.authService.setUser(user);
        let token = user.id;
        this.authService.setToken(token);
        this.router.navigate(['/user/profile']);
      });
  }
}
