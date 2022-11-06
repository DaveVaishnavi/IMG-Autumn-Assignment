import './App.css';
import Button from '@mui/material/Button';
import axios from "axios"
import React, {Component} from 'react';

import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Login from './components/login';
import HomePage from './components/homepage';
import Logout from './components/logout';
import Dashboard from './components/dashboard';
import IntermediatePage from './components/IntermediatePage'

class App extends Component{
  render(){
    return(
      <BrowserRouter>
        <Switch>
          <Route path="/login" component={Login}/>
          <Route path="/logout" component={Logout}/>
          <Route path="/dashboard" component={Dashboard}/>
          <Route path="/intermediate_page" component={IntermediatePage}/>
          <Route path="/" component={HomePage}/>
        </Switch>
      </BrowserRouter>

    );

  }
}

export default App;