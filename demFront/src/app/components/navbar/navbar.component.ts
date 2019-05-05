import { Component, OnInit } from '@angular/core';
import { AuthService } from "../../services/auth.service";
import { UserInterface } from "../../models/user-interface";
import { Router } from "@angular/router";


@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(private authService: AuthService,private router: Router) { }

  ngOnInit() {
  }

  myFunction() {
    var element = document.getElementById("body");
    element.classList.toggle("sidebar-is-reduced");
    element.classList.toggle("sidebar-is-expanded");
    var element2 = document.getElementById("hamburger");
    element2.classList.toggle("is-opened");
 }
 
  onLogout(){   
    return this.authService.logoutuser()
    .subscribe(
      data =>{
        this.router.navigate(['/login']);
      },
      error => console.log(error)
    );
    
  }

  

}
