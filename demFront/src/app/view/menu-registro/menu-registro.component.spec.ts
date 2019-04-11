import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuRegistroComponent } from './menu-registro.component';

describe('MenuRegistroComponent', () => {
  let component: MenuRegistroComponent;
  let fixture: ComponentFixture<MenuRegistroComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MenuRegistroComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MenuRegistroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
