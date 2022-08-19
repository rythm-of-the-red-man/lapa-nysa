import '../styles/index.scss';
import "bootstrap/dist/js/bootstrap.bundle";

import ReactDOM from "react-dom/client";
import React from "react"; 
import AdoptionsCarousel from "./AdoptionsCarousel.jsx";
import AdoptionsSearch from "./AdoptionsSearch.jsx";
import AnimalGallery from "./AnimalGallery.jsx";
const e = React.createElement;


const domContainer = document.querySelector('#adoptions-container');
const searchContainer = document.querySelector('#adoptions-seach');
const galeryContainer = document.querySelector('#react-gallery');
if(domContainer){
    const carouselRoot = ReactDOM.createRoot(domContainer);
    carouselRoot.render(e(AdoptionsCarousel));
}
if(searchContainer){
const searchRoot = ReactDOM.createRoot(searchContainer);
searchRoot.render(e(AdoptionsSearch));   
}
if(galeryContainer){
    const galeryRoot = ReactDOM.createRoot(galeryContainer);
    galeryRoot.render(e(AnimalGallery));   
}