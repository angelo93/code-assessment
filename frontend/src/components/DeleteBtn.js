import React from "react";

class DeleteBtn extends React.Component {
  handleClick = () => {};

  render() {
    return (
      <button className="del-btn" onClick={this.handleClick}>
      </button>
    );
  }
}

export default DeleteBtn;