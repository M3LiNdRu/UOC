import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import getPkce from 'oauth-pkce'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'oauth2-app';
  code: string = "";
  access_token: string = "";
  verifier: string = "";
  challenge: string = "";
  pkce: boolean = false;

  author: string = "";
  message: string = "";
  message_id: string = "";
  authorFullName: string = "";

  constructor(private route: ActivatedRoute,
    private http: HttpClient) {

  }

  ngOnInit(): void {
    this.access_token = localStorage.getItem('token') ?? "";
    this.generateChallenge();
    this.route.queryParams
    .subscribe(params => {
        console.log(params); 
        this.code = params['code'];
    });
  }
  
  signInWithPKCE(): void {
    window.location.href='https://www.linkedin.com/oauth/native-pkce/authorization?response_type=code&client_id=78412qx611f4v7&redirect_uri=https://localhost:4200&state=DCEeFWf45A53sdfKef424&scope=r_liteprofile%20w_member_social&code_challenge=' + this.challenge + '&code_challenge_method=S256';
    this.pkce = true;
  }

  generateChallenge(): void {
    getPkce(43, (error: any, { verifier, challenge }: any) => {
      if (!error) {
        this.verifier = verifier;
        this.challenge = challenge;
        //TODO: save values in local storage 
        //console.log(verifier, challenge);
      }
    });
  }

  requestAccessTokenWithPKCE(): void {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/x-www-form-urlencoded'
      })
    };
    const body = new URLSearchParams();
    body.set('grant_type','authorization_code');
    body.set('code', this.code);
    body.set('client_id', '78412qx611f4v7');
    body.set('code_verifier', this.verifier);
    body.set('redirect_uri', 'https://localhost:4200');

    this.http.post<any>('https://localhost:4200/oauth/v2/accessToken', body, httpOptions)
        .subscribe(data => {
          console.log(data);
          this.access_token = data.access_token;
          localStorage.setItem('token', data.access_token);
        });
  }

  signIn(): void {
    window.location.href='https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=78412qx611f4v7&redirect_uri=https://localhost:4200&state=DCEeFWf45A53sdfKef424&scope=r_liteprofile%20w_member_social';
  }

  requestAccessToken(): void {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    };
    const body = { 'code': this.code }
    this.http.post<any>('https://localhost:4200/oauth/v2/accessToken', body, httpOptions)
        .subscribe(data => {
          console.log(data);
          this.access_token = data.access_token;
          if (data.access_token) 
            localStorage.setItem('token', data.access_token);
        });
  }

  requestPersonalInfo(): void {
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization':  'Bearer ' + this.access_token
      })
    };

    this.http.get<any>('https://localhost:4200/api/v2/me', httpOptions)
        .subscribe(data => {
          console.log(data);
          this.author = "urn:li:person:" + data.id;
          this.authorFullName = data.localizedFirstName + " " + data.localizedLastName
        });
  }

  shareMessage(): void {
    const httpOptions = {
      headers: new HttpHeaders({
        'X-Restli-Protocol-Version':  '2.0.0',
        'Content-Type':  'application/json',
        'Authorization':  'Bearer ' + this.access_token
      })
    };
    const body = {
      'author': this.author,
      'lifecycleState': 'PUBLISHED',
      'specificContent': {
        'com.linkedin.ugc.ShareContent': {
            'shareCommentary': {
              'text': this.message
            },
            'shareMediaCategory': 'NONE'
        }
      },
      'visibility': {
        'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
      }
    }

    this.http.post<any>('https://localhost:4200/api/v2/ugcPosts', body, httpOptions)
        .subscribe(data => {
          console.log(data);
          this.message_id = data.id;
        });
  }
}
