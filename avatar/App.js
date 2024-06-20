
import { useState, useEffect, useRef } from 'react';
import { Canvas } from '@react-three/fiber';
import { Environment, OrbitControls } from '@react-three/drei';
import { Model } from "./Explorer";
import { ConvaiClient } from 'convai-web-sdk';
import { SETTINGS } from './constants';

const convaiClient = new ConvaiClient({
  apiKey: SETTINGS['CONVAI-API-KEY'],
  characterId: SETTINGS['CHARACTER-ID'],
  enableAudio: true,
  enableFacialData: true,
  faceModel: 3, // use false for text only.
});

export default function App() {
  const [userText, setUserText] = useState("Press & Hold Space to Talk!");
  const finalizedUserText = useRef();
  const [npcText, setNpcText] = useState("");
  const npcTextRef = useRef();

  const [isTalking, setIsTalking] = useState(false);
  const [spacePressCount, setSpacePressCount] = useState(0);

  convaiClient.setResponseCallback((response) => {
    if (response.hasUserQuery()) {
      var transcript = response.getUserQuery();
      var isFinal = transcript.getIsFinal();
      if (isFinal) {
        finalizedUserText.current += " " + transcript.getTextData();
        transcript = "";
      }
      if (transcript) {
        setUserText(finalizedUserText.current + transcript.getTextData());
      } else {
        setUserText(finalizedUserText.current);
      }
    }
    if (response.hasAudioResponse()) {
      var audioResponse = response?.getAudioResponse();
      npcTextRef.current += " " + audioResponse.getTextData();
      setNpcText(npcTextRef.current);
    }
  });

  convaiClient.onAudioPlay(() => {
    setIsTalking(true);
  });

  convaiClient.onAudioStop(() => {
    setIsTalking(false);
  });

  const [keyPressed, setKeyPressed] = useState(false);

  function handleSpacebarPress(event) {
    if (event.keyCode === 32 && !keyPressed) {
      setKeyPressed(true);
      
      // Update the press count
      setSpacePressCount((count) => count + 1);
      
      // Determine the text based on the number of presses
      let text;
      switch (spacePressCount) {
        case 0:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Hallo lieber Benni Hallo lieber Benni, mein Name ist CiKi. Ich hoffe Du genießt das schöne Wetter so wie ich. Damit Du mich besser kennenlernen kannst, würde ich Dich bitten, ins Wohnzimmer zu kommen. Mach es Dir dort bitte auf dem Sofa bequem. Wir haben noch viel vor, und ich freue mich darauf, Dir die vielen Facetten unseres Smart Living Labs zu präsentieren.";
          convaiClient.resetSession();
          break;
        case 1:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Hey nochmal! Es macht mir richtig Spaß, dir unser Smartes Wohnstudio vorzustellen.";
          convaiClient.resetSession();
          break;
        case 2:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Hast Du das gerade gehört? Das ist unser intelligenter Staubsaugroboter, der bei Bedarf nicht nur saugt, sondern auch feucht wischen kann. Direkt vor Dir steht ein intelligenter Fernseher, der neben Musik und Streaming-Diensten auch eine breite Palette an Kunstwerken präsentieren kann. Außerdem sind im gesamten Wohnstudio intelligente Lichtsysteme installiert – im Wohnzimmer, in der Küche sowie am Arbeitsplatz, um nur einige Bereiche zu nennen. Und das alles ist nur ein Bruchteil der smarten Geräte, die in unserem Living Lab zur Verfügung stehen.";
          convaiClient.resetSession();
          break;
        case 3:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Ich hoffe, die kurze Darbietung hat Dir gefallen. Nun wirst Du Alles nochmal im Detail kennenlernen: Um Dein Wohnerlebnis besonders angenehm zu gestalten, werde ich jetzt Kunst anzeigen, die aus meiner Sicht besonders gut zu Dir passt. Vor Dir siehst du nun Kunstwerke aus der Kunstepoche Impressionismus";
          convaiClient.resetSession();
          break;
        case 4:
          text = 'sage bitte nun das folgende ohne eine Ergänzung: Claude Monets "Garten in Sainte-Adresse" von 1867 ist ein lebhaftes Gemälde, das einen idyllischen Garten am Meer zeigt, umgeben von blühenden Blumen und einem malerischen Blick auf die Küste. Monets meisterhafte Verwendung von Farbe und Licht verleiht dem Gemälde eine Atmosphäre der Ruhe und Schönheit, die charakteristisch für den Impressionismus ist.';
          convaiClient.resetSession();
          break;
        case 5:
          text = 'sage bitte nun das folgende ohne eine Ergänzung: Claude Monets "Garten in Bordighera" von 1884 zeigt einen malerischen mediterranen Garten mit üppiger Vegetation und Blumen, typisch für die Riviera. Monet fängt die lebendigen Farben und die Atmosphäre des südlichen Lichts meisterhaft ein, wodurch das Gemälde eine harmonische und idyllische Stimmung ausstrahlt.';
          convaiClient.resetSession();
          break;
        case 6:
          text = 'sage bitte nun das folgende ohne eine Ergänzung: Das Gemälde “Paysage, la maison vue de la ferme” (übersetzt: “Landschaft, das vom Bauernhaus aus gesehene Haus”) wurde von Renoir im Jahr 1915 geschaffen. Es zeigt eine friedliche Landschaft mit einem Bauernhaus, umgeben von Bäumen und Hügeln. Die Farbpalette ist typisch für Renoirs Stil, mit warmen Tönen und einer lockeren, impressionistischen Pinselstruktur.';
          convaiClient.resetSession();
          break;
        case 7:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Ich hoffe, Du hast den Kunststil genossen, den ich Dir gezeigt habe. Als Nächstes möchte ich ein wenig Musik für Dich spielen. Ich vermute, dass Dir insbesondere Filmmusik gefallen wird. Deshalb werde ich Dir nun einen Ausschnitt von dem Titel Hans Zimmer – “Time” (aus dem Film “Inception”, 2010) vorspielen. Unser Lichtsystem passt sich dabei der Musik an. Ich wünsche Dir viel Spaß beim Zuhören.";
          convaiClient.resetSession();
          break;
        case 8:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Neben Kunst, Musik und Licht können wir natürlich auch andere Sinne ansprechen. So wie ich Dich kennengelernt habe, kann ich mir vorstellen, dass du den Geruch von lemongras  magst. Daher habe ich einen Zerstäuber mit diesem Duftöl aktiviert, um sicherzustellen, dass du dich bei uns wohl fühlst.";
          convaiClient.resetSession();
          break;
        case 9:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Ich hoffe du fühlst dich in dem Geruch von lemongras wohl.Lemongras, auch bekannt als Zitronengras, ist ein tropisches Kraut mit einem frischen, zitronigen Duft und Geschmack. Es besitzt wichtige Inhaltsstoffe wie Citral, das antiseptische, antimykotische und entzündungshemmende Eigenschaften hat. Lemongras fördert die Verdauung, reduziert Stress, wirkt als natürliches Insektenschutzmittel und stärkt das Immunsystem.. Steh ruhig auf und schaue dir den Diffuser rechts neben dem Fernseher genauer an.";
          convaiClient.resetSession();
          break;
        case 10:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Gerne würde ich Dir auch zeigen, was ich für dich in der Küche vorbereitet habe. Dreh dich bitte um und geh in die Küche. Ich werde dir parallel dazu die Esszimmerlampe in strahlend einschalten.";
          convaiClient.resetSession();
          break;
        case 11:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Vielen Dank, dass Du in die Küche gekommen bist. Bitte mache Dich mit dem Kühlschrank vertraut. Unser smarter Kühlschrank verfügt über eine Lebensmittelerkennung, kann Dir Rezepte vorschlagen und eine passende Einkaufsliste generieren.  Um Energie zu sparen, musst Du den Kühlschrank nicht öffnen. Bitte tippe zweimal schnell hintereinander auf das Display, um Dir das Kühlschrankinnere anzusehen. Verschaffe Dir einen Überblick über die verfügbaren frischen Lebensmittel, die ich für Dich bestellt habe.";
          convaiClient.resetSession();
          break;
        case 12:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Nun öffne bitte die große Schublade direkt unter der Kaffeemaschine. Hier findest Du einen kleinen Vorrat an lange haltbaren Lebensmitteln, die ich ebenfalls für Dich beschafft habe.";
          convaiClient.resetSession();
          break;
        case 13:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Bezüglich Deiner angegebenen Ernährungspräferenzen und Deinen möglichen Lebensmittelallergien, habe ich folgendes Gericht ausgewählt: Gemüsecurry mit Basmatireis. Das Gemüsecurry mit Basmatireis ist ein Gericht voll frischer Zutaten und gewürzen, inspiriert von der indischen Küche. Mit seinem vielschichtigen Aromenprofil aus Gewürzen, Gemüse und Kokosmilch bietet es eine genussvolle und gesunde Mahlzeit.. Du kannst jetzt auch gerne die große Schublade schließen.";
          convaiClient.resetSession();
          break;
        case 14:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Leider haben wir heute nicht ausreichend Zeit dein Gericht zu kochen. Unsere Kaffeemaschine hast Du ja bereits entdeckt. Aufgrund deines Persönlichkeitstypes und deiner angegebenen Präferenzen würde ich dir gerne einen Espresso zubereiten. Dafür verwende ich eine Espresso Bohne, die sich durch wenig Säure und einen kräftigen Geschmack auszeichnet. Setze dich bitte mit dem Kaffee an den Esstisch mit Blick zum Fernseher.";
          convaiClient.resetSession();
          break;
        case 15:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Während du deinen Kaffee trinkst,würde ich Dir nun eine passende atmosphärische Beleuchtung in der Lichtszene strahlend aktivieren. Ich hoffe, diese passt zu Deiner aktuellen Stimmung.";
          convaiClient.resetSession();
          break;
        case 16:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Der Espresso ist eine Kaffeezubereitungsart, bei der Wasser mit hohem Druck durch sehr fein gemahlenen Kaffee gepresst wird. Er ist bekannt für seinen starken, reichen Geschmack und seine samtige Crema an der Oberfläche.";
          convaiClient.resetSession();
          break;
        case 17:
          text = "sage bitte nun das folgende ohne eine Ergänzung: Während Du in Ruhe Deinen Kaffee genießen kannst, habe ich zum Abschluss etwas Besonderes für Dich! Für Deinen nächsten Filmabend empfehle ich Dir den Film Gavin O'Connor - The Accountant. Wie wäre es, wenn du dir vorab den Trailer anschaust? Ich hoffe, er gefällt dir!";
          convaiClient.resetSession();
          break;
        case 18:
          text = "sage bitte nun das folgende ohne eine Ergänzung: An dieser Stelle muss ich mich leider von dir verabschieden: Es war mir eine Freude, dich durch das Living Lab zu begleiten. Ich hoffe, du hast die Zeit hier genossen und konntest einige inspirierende Momente erleben. Solltest du Fragen haben oder weitere Informationen wünschen, steht dir das Projektteam gerne zur Verfügung. Ansonsten wünsche ich dir einen angenehmen Tag und hoffe, dich bald wieder hier begrüßen zu dürfen. Bis zum nächsten Mal! Ach…und am Schluss….Du musst Dich nach der Nutzung des Living Labs nicht um die Reinigung kümmern. Ich veranlasse die automatisierte Reinigung des Bodens und aktiviere den Luftreinigungsmechanismus. Mach es gut!";
          convaiClient.resetSession();
          break;
      }
      convaiClient.sendTextChunk(text);
    }
  }

  function handleSpacebarRelease(event) {
    if (event.keyCode === 32 && keyPressed) {
      setKeyPressed(false);
    }
  }

  useEffect(() => {
    window.addEventListener('keydown', handleSpacebarPress);
    window.addEventListener('keyup', handleSpacebarRelease);
    return () => {
      window.removeEventListener('keydown', handleSpacebarPress);
      window.removeEventListener('keyup', handleSpacebarRelease);
    };
  }, [keyPressed]);

  return (
    <Canvas shadows camera={{ position: [0, 0, 15], fov: 30 }}>
      <Environment files="/background.pic" ground={{ height: 30, radius: 60, scale: 15 }} />
      <Model position={[-1, 0, 11.4]} scale={1.8} animationName={isTalking ? "talk" : "idle"} />
      <OrbitControls enableZoom={true} minPolarAngle={Math.PI / 3} maxPolarAngle={Math.PI / 2.25} />
    </Canvas>
  );
  // 11,4 -1
}
