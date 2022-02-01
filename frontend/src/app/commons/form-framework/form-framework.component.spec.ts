import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FrameworkComponent } from './form-framework.component';

describe('AppFormFrameworkComponent', () => {
  let component: FrameworkComponent;
  let fixture: ComponentFixture<AppFormFrameworkComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [FrameworkComponent]
    })
      .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FrameworkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
