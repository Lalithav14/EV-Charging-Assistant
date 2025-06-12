import React,{useState,useEffect} from 'react';
import ROSLIB from 'roslib';
export default function App(){
  const [rul,set]=useState(0);
  useEffect(()=>{
    const ros=new ROSLIB.Ros({url:'ws://localhost:9090'});
    const sub=new ROSLIB.Topic({ros,name:'/health/rul',messageType:'std_msgs/Float32'});
    sub.subscribe(msg=>set(msg.data));
    return()=>sub.unsubscribe();
  },[]);
  return <div style={{color:'#0ff',background:'#101010',padding:20}}><h1>RUL</h1><p>{rul.toFixed(1)}</p></div>;
}
