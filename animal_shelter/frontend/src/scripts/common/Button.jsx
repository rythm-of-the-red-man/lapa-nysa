import React from "react";

const Button = (props) => {
  const { onClick, children, outline = false, lg = false, className="" } = props;
  return (
    <button
      onClick={onClick}
      className={`btn ${outline ? "btn-outline-primary" : "btn-primary"} ${
        lg ? "btn-lg" : ""
      } ${className}`}
    >
      {children}
    </button>
  );
};
export default Button;
