import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const baseUrl = 'http://127.0.0.1:8000/api/tumblr';

@Injectable({
  providedIn: 'root'
})
export class TumblrService {

 constructor(private http: HttpClient) { }
  get(name) {
    return this.http.get(`${baseUrl}/${name}`);
  }
}