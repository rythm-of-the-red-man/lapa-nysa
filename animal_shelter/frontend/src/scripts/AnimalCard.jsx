import React from "react";
import placeholder from "../../public/placeholder.svg";
const AnimalCard = (props) => {
  const { animal } = props;
  const name = animal.name.length > 15 ? animal.name.slice(0,15)+"..." : animal.name
  return (
    <div className="my-carousel-wrapper p-4 mb-4 mt-5" style={{ maxWidth: "300px" }}>
      <div className="d-flex justify-content-center">
        <img
          className="animal-image"
          src={animal.photos[0]?.image || placeholder}
        />
      </div>
      <div className="d-flex justify-content-center mt-2">
        <h4>{name}</h4>
      </div>
      <div className="d-flex justify-content-center mt-2">
        <a className="btn btn-outline-primary"
                href={`/adopcje/${animal.id}`}
                role="button"
        >Dowiedz się więcej</a>
      </div>
    </div>
  );
};
export default AnimalCard;
