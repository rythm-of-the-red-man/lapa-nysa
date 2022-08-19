import React, { useEffect, useState } from "react";
import leftArrow from "../../public/arrow-left.svg";
import rightArrow from "../../public/arrow-right.svg";
import placeholder from "../../public/placeholder.svg";

const AnimalGallery = () => {
  const splittedLocation = window.location.pathname.split("/");
  const animalId = splittedLocation[2];
  const [photos, setPhotos] = useState([]);
  useEffect(() => {
    const getAnimal = async () => {
      const response = await fetch(
        `http://localhost:8000/api/adoptions/${animalId}`
      );
      const data = await response.json();
      setPhotos(data.photos);
    };
    getAnimal();
  });
  const [currentPhoto, setCurrentPhoto] = useState(0)
  const incrementPhoto = () =>{
    if(currentPhoto !== photos.length-1){
      setCurrentPhoto(currentPhoto+1)
    }else{
      setCurrentPhoto(0)
    }
  }
  const decrementPhoto = () =>{
    if(currentPhoto !== 0){
      setCurrentPhoto(currentPhoto-1)
    }else{
      setCurrentPhoto(photos.length-1)
    }
  }
  return (
    <div className="d-flex flex-column align-items-center">
      {photos.length > 0 && (
        <>
          <div className="d-flex">
            <img onClick={decrementPhoto} src={leftArrow} />
            <img className="carousel-image ms-4 me-4" src={photos[currentPhoto].image} />
            <img onClick={incrementPhoto} src={rightArrow} />
          </div>
          <div
            className="d-flex"
            style={{ overflow: "auto", maxWidth: "400px" }}
          >
            {photos.map((photo, index) => (
              <img
              onClick={()=>setCurrentPhoto(index)}
                className="ms-3 me-3 mt-3"
                style={{ height: "100px" }}
                src={photo.image}
              />
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default AnimalGallery;
