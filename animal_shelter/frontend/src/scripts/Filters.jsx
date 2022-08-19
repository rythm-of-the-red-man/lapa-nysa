import React from "react";
import Button from "./common/Button.jsx";
const Filters = (props) => {
  const { filters, setFilters } = props;
  const applyFilter = (val, key) => {
    const newState = { ...filters };
    if (Array.isArray(val)) {
      newState[key] = val;
      return setFilters(newState);
    }
    if (newState[key].includes(val)) {
      newState[key] = newState[key].filter((item) => item !== val);
    } else {
      newState[key].push(val);
    }
    setFilters(newState);
  };
  const arrEquals = (arr1, arr2) => {
    return arr1.sort().toString() === arr2.sort().toString();
  };
  return (
    <div class="row mb-5" style={{ margin: "auto" }}>
      <div className="col-12 col-lg-5">
        <div className="d-flex justify-content-center mb-2 mt-4">
          <h4>Jakiego przyjaciela szukasz?</h4>
        </div>
        <div className="d-flex justify-content-between">
          <Button
            onClick={() => applyFilter("dog", "spice")}
            outline={!filters.spice.includes("dog")}
            lg
            className="me-3"
          >
            Pies
          </Button>
          <Button
            onClick={() => applyFilter("cat", "spice")}
            outline={!filters.spice.includes("cat")}
            lg
            className="me-3 filter"
          >
            Kot
          </Button>
          <Button
            onClick={() => applyFilter("other", "spice")}
            outline={!filters.spice.includes("other")}
            lg
          >
            Inne
          </Button>
        </div>
        <div className="d-flex justify-content-center mb-2 mt-4">
          <h4>Jak duży ma być zwierzak?</h4>
        </div>
        <div className="d-flex justify-content-between">
          <Button
            onClick={() => applyFilter("small", "size")}
            outline={!filters.size.includes("small")}
            lg
            className="me-3"
          >
            Małe
          </Button>
          <Button
            onClick={() => applyFilter("medium", "size")}
            outline={!filters.size.includes("medium")}
            lg
            className="me-3"
          >
            Średnie
          </Button>
          <Button
            onClick={() => applyFilter("big", "size")}
            outline={!filters.size.includes("big")}
            lg
          >
            Duże
          </Button>
        </div>
      </div>
      <div className="col-12 offset-lg-2 col-lg-5">
        <div className="d-flex justify-content-center mb-2 mt-4">
          <h4>Wiek</h4>
        </div>
        <div className="d-flex justify-content-between">
          <Button
            onClick={() => applyFilter([0, 1], "age")}
            outline={!arrEquals(filters.age, [0, 1])}
            lg
            className="me-3"
          >
            0-1
          </Button>
          <Button
            onClick={() => applyFilter([1, 4], "age")}
            outline={!arrEquals(filters.age, [1, 4])}
            lg
            className="me-3"
          >
            1-4
          </Button>
          <Button
            onClick={() => applyFilter([4, 7], "age")}
            outline={!arrEquals(filters.age, [4, 7])}
            lg
            className="me-3"
          >
            4-7
          </Button>
          <Button
            onClick={() => applyFilter([7, 99], "age")}
            outline={!arrEquals(filters.age, [7, 99])}
            lg
          >
            7+
          </Button>
        </div>
        <div className="d-flex justify-content-center mb-2 mt-4">
          <h4>Płeć</h4>
        </div>
        <div className="d-flex justify-content-between">
          <Button
            onClick={() => applyFilter("female", "sex")}
            outline={!filters.sex.includes("female")}
            lg
            className="me-3"
          >
            Samica
          </Button>
          <Button
            onClick={() => applyFilter("male", "sex")}
            outline={!filters.sex.includes("male")}
            lg
          >
            Samiec
          </Button>
        </div>
      </div>
    </div>
  );
};
export default Filters;
