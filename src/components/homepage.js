import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
import axios from 'axios';
import Button from '@mui/material/Button';
import bg from '../bg.jpg';
import './homepage.css';
class HomePage extends Component{
    constructor(props)
    {
        super(props);
        this.state = {
            loggedIn :false,
        };
    }

    renderRedirect= () =>{
        if(this.state.loggedIn===true)
        {
            return <Redirect to={{pathname:'../dashboard'}}/>
        }
    }

    render(){
        return(
        <div className="container">
            {this.renderRedirect()}
                {/* <a href="https://internet.channeli.in/oauth/authorise/?client_id=z1T5401eydvctrKve1qOJpYBGdTrWSaMZWhAe98j&redirect_uri=http://127.0.0.1:3000/login&state=done">Login with Omniport</a> */}
                <Button style={{height:'50px', width:'500px', alignSelf:'center'}} content='Login with Omniport' icon='right arrow' labelPosition='right' primary
                    onClick={()=>{
                        window.location.href="https://channeli.in/oauth/authorise/?client_id=qxzf6ez39LBvOF6w9ghzvstlLXX3oiQRV35eqfW8&redirect_uri=http://localhost:8000/get_oauth_token/"
                    }}
                />
            }>


            </div>
        );
    }

    async componentDidMount(){

        const response= await axios({url:'http://127.0.0.1:8000/check_login/' ,method:'GET',withCredentials:true} ).then(console.log("done"));
        if(response.status==202){

            if(response.data['loggedin']==true){
                this.setState({loggedIn : true});
            }

        }

    }
}

export default HomePage;