import React from "react";

class Mode extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isToggleOn: true };

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState((prevState) => ({
        isToggleOn: !prevState.isToggleOn
    }));
  }

  render() {
    return (
      <button className="mode-toggle" onClick={this.handleClick}>
        {this.state.isToggleOn ? "PvC" : "PvP"}
      </button>
    );
  }
}

export default Mode;
