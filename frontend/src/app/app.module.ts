import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { EditFormComponent } from './edit-form/edit-form.component';
import { TestFormComponent } from './test-form/test-form.component';
import { RouterModule } from '@angular/router';
import { Bootstrap4FrameworkModule } from '@ajsf/bootstrap4';
import { FrameworkComponent } from './commons/form-framework/form-framework.component';
import { ListFormsComponent } from './commons/list-forms/list-forms.component';
import { NavbarComponent } from './navbar/navbar.component';
import { HighlightModule, HIGHLIGHT_OPTIONS } from 'ngx-highlightjs';

@NgModule({
  declarations: [
    AppComponent,
    EditFormComponent,
    TestFormComponent,
    FrameworkComponent,
    ListFormsComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule.withServerTransition({ appId: 'serverApp' }),
    NgbModule,
    Bootstrap4FrameworkModule,
    HighlightModule,
    RouterModule.forRoot([
    { path: '', component: TestFormComponent },
    { path: 'edit/:formId', component: EditFormComponent },
], {
  initialNavigation: 'enabledBlocking'
})
  ],

  providers: [
    {
      provide: HIGHLIGHT_OPTIONS,
      useValue: {
        fullLibraryLoader: () => import('highlight.js')
      }
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
