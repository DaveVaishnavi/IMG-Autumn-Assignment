import React, {Component} from 'react';
import { render } from '@testing-library/react';
import { Redirect } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import axios from 'axios';
import logo from '../logo.jpg';
import './login.css';
import Button from '@mui/material/Button';

class Dashboard extends Component{
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
    render(){
        return(
            <div className="container">
           {/* {this.renderRedirect()} */}

            </div>
        );
    }

    // async componentDidMount(){
    //         const projects= await axios({url:'http://127.0.0.1:8000/season' ,method:'GET', withCredentials:true} ).then(console.log("done"));
    //         await this.setState({projectlist:projects.data});
    //         var ProjectDict = [];
    //         for(var key in this.state.projectlist){

    //             ProjectDict.push({
    //                 id:   this.state.projectlist[key]['id'],
    //                 name: this.state.projectlist[key]['Project_name'],
    //             });
    //         }

    //         // console.log(ProjectDict)
    //         await this.setState({projectlist_dict:ProjectDict});

    //     }
    // }

    async componentDidMount(){

        console.log("here")

        const response= await axios({url:'http://127.0.0.1:8000/season/' ,method:'GET',withCredentials:true} ).then(console.log("done"));
console.log(response)
//        console.log(this.state.loggedIn1);
//
//        if(response.status==202){
//
//            if(response.data['loggedin']==true){
//                await this.setState({loggedIn1 : true});
//            }
//            else{
//                alert("you are not logged in");
//                window.location.href = "http://localhost:3000/"
//            }
//        }
//        else{
//            alert("you are not logged in");
//            window.location.href = "http://localhost:3000/"
//
//        }
//
////        console.log(this.state.loggedIn1);
//
//        if(this.state.loggedIn1==true){
//
            const season= await axios({url:'http://127.0.0.1:8000/season/' ,method:'GET', withCredentials:true} ).then(console.log("done"));
            console.log(season)
            await this.setState({seasonlist:season.data});
            console.log(this.state.seasonlist);
             var SeasonDict = [];
             for(var key in this.state.seasonlist){

                 SeasonDict.push({
                     id:   this.state.seasonlist[key]['id'],
                     season_name: this.state.seasonlist[key]['season_name'],
                     year_of_season: this.state.seasonlist[key]['year_of_season'],
                 });
             }

//              console.log(SeasonDict)
             await this.setState({seasonlist_dict:SeasonDict});
             console.log(this.state.seasonlist);
    }
 }

//Dashboard.defaultProps = {
//    'message': "",
//}

export default Dashboard;