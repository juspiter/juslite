const AboutButton = (props) => {
  return (
    <>
      <button
        className="input-group-text input-button"
        onClick={props.handleClick}>Sobre
      </button>
    </>
  );
}

export default AboutButton;
