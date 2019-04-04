import { Component, OnInit } from '@angular/core';
declare var $: any;



@Component({
  selector: 'menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    this.dashboard();
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
