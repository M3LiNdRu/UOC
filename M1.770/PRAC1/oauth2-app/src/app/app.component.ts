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

  constructor(private route: ActivatedRoute,
    private http: HttpClient) {

  }

  ngOnInit(): void {
    this.route.queryParams
    .subscribe(params => {
        console.log(params); 
        this.code = params['code'];
    });
  }
  
  signIn(): void {
    this.getChallengeCode();
    window.location.href='https://www.linkedin.com/oauth/native-pkce/authorization?response_type=code&client_id=78412qx611f4v7&redirect_uri=https://localhost:4200&state=DCEeFWf45A53sdfKef424&scope=r_liteprofile&code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM&code_challenge_method=S256';
  }

  getChallengeCode(): void {
    getPkce(43, (error: any, { verifier, challenge }: any) => {
      if (!error) {
        this.verifier = verifier;
        this.challenge = challenge;
        console.log(verifier, challenge);
      }
    });
  }

  requestAccessToken(): void {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/x-www-form-urlencoded'
      })
    };
    const body = new URLSearchParams();
    body.set('grant_type','authorization_code');
    body.set('code', this.code);
    body.set('client_id', '78412qx611f4v7');
    body.set('code_verifier', 'dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk');
    body.set('redirect_uri', 'https://localhost:4200');

    this.http.post<any>('https://localhost:4200/oauth/v2/accessToken', body, httpOptions)
        .subscribe(data => {
          console.log(data);
          this.access_token = data.access_token;
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
        });
  }
}
