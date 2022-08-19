import React, { useEffect, useState } from "react";
import AnimalCard from "./AnimalCard.jsx";
import Button from "./common/Button.jsx";
import Filters from "./Filters.jsx";
const AdoptionsCarousel = () => {
  const [animals, setAnimals] = useState([]);
  const [count, setCount] = useState(0);
  const [nextPage, setNextPage] = useState(false);
  const [prevPage, setPrevPage] = useState(false);
  const [page, setPage] = useState(1);
  const [allCount, setAllCount] = useState(0);
  const getAnimals = async () => {
    const params = `?page=${page}&spice=${filters.spice}&size=${filters.size}&sex=${filters.sex}&age_lte=${filters.age[1]}&age_gte=${filters.age[0]}`;
    const response = await fetch(
      `http://localhost:8000/api/adoptions/${params}`
    );
    const data = await response.json();
    setAnimals(data.results);
    setNextPage(data.next !== null);
    setPrevPage(data.previous !== null)
    setCount(data.count);
    const responseAll = await fetch(`http://localhost:8000/api/adoptions/`);
    const allData = await responseAll.json();
    setAllCount(allData.count);
  };
  const [filters, setFilters] = useState({
    spice: [],
    size: [],
    age: [0, 99],
    sex: [],
  });

  useEffect(() => {
    getAnimals();
  }, [filters, page]);
  return (
    <>
      <Filters filters={filters} setFilters={setFilters} />
      {(count > 0 || allCount > 0) && (
        <div className="row serif-font ms-2">
          Wybrano {count} z {allCount}
        </div>
      )}
      <div className="d-flex flex-wrap justify-content-around">
        {animals.map((animal) => (
          <AnimalCard key={animal.id} animal={animal}></AnimalCard>
        ))}
      </div>
        <div className="d-flex justify-content-center" lg>
          {prevPage && <Button className="me-3" onClick={() => setPage(page - 1)}>Poprzednia strona</Button>}
          {nextPage && <Button onClick={() => setPage(page + 1)}>Następna strona</Button>}
        </div>
    </>
  );
};
export default AdoptionsCarousel;
