import { Component, OnInit } from '@angular/core';
import { TumblrService } from 'src/app/services/tumblr.service';
import { ActivatedRoute, Router } from '@angular/router';
@Component({
  selector: 'app-get-tumblr',
  templateUrl: './get-tumblr.component.html',
  styleUrls: ['./get-tumblr.component.css']
})
export class GetTumblrComponent implements OnInit {

  tumblr_posts = [];
  tumblrName = null;
  message = '';
  error = '';

  constructor(
    private tumblrService: TumblrService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit() {
    this.message = '';
  }

  getTumblr() {
    this.tumblrService.get(this.tumblrName)
      .subscribe(
        data => {
          this.loadData(data);
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  loadData(data) {
  	this.tumblr_posts = []
    if (data["json_response"].length === 0){
      this.error = "Not Found"
      return;
    }
    this.error = '';
    let posts = data["json_response"]["posts"]
    for (let i = 0; i < posts.length; i++) {
      if (posts[i]["type"] == "photo") {
        this.tumblr_posts.push({id:posts[i]["id"], photo_link:posts[i]["photo-url-500"], url:posts[i]["url"]})
      }
  }


}}
