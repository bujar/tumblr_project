import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GetTumblrComponent } from './get-tumblr.component';

describe('GetTumblrComponent', () => {
  let component: GetTumblrComponent;
  let fixture: ComponentFixture<GetTumblrComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GetTumblrComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GetTumblrComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
