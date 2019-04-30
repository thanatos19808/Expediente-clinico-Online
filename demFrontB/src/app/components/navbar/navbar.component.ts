import { Component, OnInit } from '@angular/core';
import { AuthService } from "../../services/auth.service";
declare var $: any;

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(private authService: AuthService) { }

  ngOnInit() {
    this.dashboard();
  }

  onLogout():void{   
    this.authService.logoutUser();
  }

  dashboard(){
    var Dashboard = function () {
      var global = {
        menuClass: ".c-menu"
      };
  
      var menuChangeActive = function menuChangeActive(el) {
        var hasSubmenu = $(el).hasClass("has-submenu");
        $(global.menuClass + " .is-active").removeClass("is-active");
        $(el).addClass("is-active");
  
        if (hasSubmenu) {
        $(el).find("ul").slideDown();
        }
      };
  
      var sidebarChangeWidth = function sidebarChangeWidth() {
        var $menuItemsTitle = $("li .menu-item__title");
  
        $("body").toggleClass("sidebar-is-reduced sidebar-is-expanded");
        $(".hamburger-toggle").toggleClass("is-opened");
      };
  
      return {
        init: function init() {
          $(".js-hamburger").on("click", sidebarChangeWidth);
  
          $(".js-menu li").on("click", function (e) {
            menuChangeActive(e.currentTarget);
          });
        }
      };
    }();

    Dashboard.init();
  }

}
