import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuPagoComponent } from './menu-pago.component';

describe('MenuPagoComponent', () => {
  let component: MenuPagoComponent;
  let fixture: ComponentFixture<MenuPagoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MenuPagoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MenuPagoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
