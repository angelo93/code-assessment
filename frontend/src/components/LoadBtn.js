import React from "react";

class LoadBtn extends React.Component {
  handleClick = () => {};

  render() {
    return (
      <button className="load-btn-game" onClick={this.handleClick}>
      </button>
    );
  }
}

export default LoadBtn;