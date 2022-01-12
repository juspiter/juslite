import SearchBox from "../components/SearchBox";
// import "../partials/Welcome.scss";

const Welcome = () => {
  return (
    <div id="welcome_">
      <img src="/image/juspiter.png" alt="Imagem vetorial do planeta jupiter com uma lupa na parte inferior" />
      <h1>Juslite</h1>
      <div>
        <SearchBox />
      </div>
    </div>
  );
}

export default Welcome;
