import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import logo from '../logo.jpg';
import search from '../search.png';
import './login.css';
import Button from '@mui/material/Button';

class Login extends Component{
    constructor(props)
    {
        super(props);
        this.state = {
        done :"False",
        isAdmin : "False",
        isEnabled:"True",
        loggedIn:"False",
        error:false,
        failed:"False"
        };
    }

    renderRedirect= () =>{
        if(this.state.done==="True" || this.state.loggedIn==="True" )
        {
            return <Redirect to={{pathname:'http://127.0.0.1:8000/send_token_request/'}}/>
        }
        else if(this.state.failed==="True"){
            return <Redirect to={{pathname:'../'}}/>
        }
    }

    LoginRequest() {
    console.log("jdlsj")
  window.location.href = "https://channeli.in/oauth/authorise/?client_id=qxzf6ez39LBvOF6w9ghzvstlLXX3oiQRV35eqfW8&redirect_uri=http://localhost:3000/intermediate_page/"
}
CannotLogin() {
    console.log("jdlsj")
  window.location.href = "https://channeli.in/maintainer_site/";
}
    render(){
        return(
            <div className="container">
            {this.renderRedirect()}
            <div className="div1"><img src={logo} height="100%"/></div>
            <div className="div2">

  <h1><font size="50px">Welcome to TalentHunt <img src={search} className="image"/></font></h1>
  <Button variant="contained" size="large"  style={{fontSize:20}} onClick={() => this.LoginRequest()}>
      Sign in with Omniport
      </Button>
      <br/>
      <br/>
      <Button variant="contained" size="large" style={{fontSize:20}} onClick={()=> this.CannotLogin()}>
      Not in IMG
      </Button>
            </div>
            </div>
        );
    }

    async componentDidMount(){

//            // eslint-disable-next-line no-restricted-globals
//            const params= new URLSearchParams(location.search);
//            const auth= params.get("code");
//            console.log(auth);
//            const user1= await axios({url:'https://channeli.in/oauth/' ,method:'GET', params: {code:auth} , withCredentials:true} ).then(console.log("done"));
//
//            console.log(user1)
//            this.setState({done:"True"});


    }

}

Login.defaultProps = {
//    'message': "",
}

export default Login;