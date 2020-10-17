import React from 'react';
import '../App.css';


function BasicInfo(props) {
    const sayHello = () => {
        console.log("hello");
      };
      
    return (
        <div className = "box">
            <h1 className = "playFont">Financial Education Class</h1>
            
            <button className = "playButton">Play!</button>
            {/* <h1>Basic Information</h1>
            <div>

            </div>
            <h1>{props.name}</h1>
            <button onClick= {sayHello()}> Button </button> 
            <p>Random styff</p>
            <h3>stfsdfsd</h3> */}
        </div>
    );
}

export default BasicInfo;