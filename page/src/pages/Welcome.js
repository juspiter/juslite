import SearchBox from "../components/SearchBox";
import About from "../components/About.js";
import AboutContent from "../components/AboutContent.js";
// import "../partials/Welcome.scss";

const Welcome = () => {
  return (
    <div id="welcome_">
      <div id="landing_">
        <img src="/image/logo.svg" alt="Imagem vetorial do planeta jupiter com uma lupa na parte inferior" />
        <h1>Juslite</h1>
        <div><SearchBox /></div>
      </div>
      <AboutContent />
    </div>
  );
}

export default Welcome;
