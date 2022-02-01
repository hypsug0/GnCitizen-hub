import { Component, OnInit } from '@angular/core';
import { FrameworkComponent } from '../commons/form-framework/form-framework.component';

@Component({
  selector: 'app-test-form',
  templateUrl: './test-form.component.html',
  styleUrls: ['./test-form.component.css']
})
export class TestFormComponent implements OnInit {
  jsonFormSchema: object | undefined;
  sampleData: object | undefined;
  data: object | undefined;
  active: 1 | undefined;
  submittedFormData: any = null;
  liveFormData: any = {};
  formOptions: any = {
    loadExternalAssets: true,
    debug: false,
    returnEmptyFields: false,
    addSubmit: false,
  };
  FrameworkComponent: any = {
    framework: FrameworkComponent,
  };
  constructor() { }

  ngOnInit(): void {
    this.sampleData = {
      "schema": {
        "type": "object",
        "title": "Comment",
        "properties": {
          "number": {
            "title": "number",
            "type": "integer"
          },
          "boolean": {
            "title": "bool",
            "type": "boolean"
          },
          "email": {
            "title": "Email",
            "type": "string",
            "pattern": "^\\S+@\\S+$",
            "description": "Email will be used for evil."
          },
          "comment": {
            "title": "Comment",
            "type": "string",
            "maxLength": 20,
            "validationMessage": "Don't be greedy!"
          }
        },
        "required": [
          "number",
          "email",
          'boolean',
          "comment"
        ]
      },
      "form": [
        "number",
        "boolean",
        "email",
        {
          "key": "comment",
          "type": "textarea",
          "placeholder": "Make a comment"
        }
      ]
    }


  }

  populateSchema() {
    console.log('test');
    this.jsonFormSchema = this.sampleData;
  }
  // onSubmit(data: any) {
  //   this.submittedFormData = data;
  // }

  onChanges(data: any) {
    this.liveFormData = data;
  }


}
