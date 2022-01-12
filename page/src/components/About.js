import { useState } from "react";
import AboutButton from "./AboutButton.js";
import AboutContent from "./AboutContent.js";

const About = () => {
  const [showContent, setShowContent] = useState(false);

  const expandAboutHandler = () => {
    setShowContent(true);
  }

  return (
    <footer className="footer">
      {!showContent && <AboutButton handleClick={expandAboutHandler} />}
      {showContent && <AboutContent />}
    </footer>
  );
}

export default About;

// Na página de boas-vindas: começa como um botão "Sobre" com uma setinha pra baixo
// Depois de clicar no Sobre, rola para baixo com quadros de:
// Sobre, Instruções, e "Fonte e Autores"
