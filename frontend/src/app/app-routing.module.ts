import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GetTumblrComponent } from './components/get-tumblr/get-tumblr.component';

const routes: Routes = [
  { path: '', component: GetTumblrComponent },
  { path: 'tumblr/:id', component: GetTumblrComponent },];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
