import React, { useEffect, useState } from "react";
import Slider from "react-slick";
import leftArrow from "../../public/arrow-left.svg";
import rightArrow from "../../public/arrow-right.svg";
import placeholder from "../../public/placeholder.svg";
const AdoptionsCarousel = () => {
  const [animals, setAnimals] = useState([]);
  useEffect(() => {
    const getAnimals = async () => {
      const response = await fetch(
        "http://localhost:8000/api/adoptions/?page_size=5"
      );
      const data = await response.json();

      setAnimals(data.results.slice(0, 5));
    };
    getAnimals();
  }, []);
  let settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    className: "testslider",
    nextArrow: <img src={rightArrow} />,
    prevArrow: <img src={leftArrow} />,
  };
  return (
    <div>
    <Slider {...settings}>
      {animals.map((animal) => {
        const name =
          animal.name.length > 15
            ? animal.name.slice(0, 15) + "..."
            : animal.name;

        return (
          <div className="my-carousel-wrapper p-4">
            <div className="d-flex justify-content-center">
              <img
                className="carousel-image"
                src={animal.photos[0]?.image || placeholder}
              />
            </div>
            <div className="d-flex justify-content-center mt-2">
              <h4>{name}</h4>
            </div>
            <div className="d-flex justify-content-center mt-2">
              <a
                className="btn btn-outline-primary"
                role="button"
                href={`/adopcje/${animal.id}`}
              >
                Dowiedz się więcej
              </a>
            </div>
          </div>
        );
      })}
    </Slider>
    </div>
  );
};
export default AdoptionsCarousel;
