import { tsParticles } from "https://cdn.jsdelivr.net/npm/@tsparticles/engine@3.2.2/+esm";
import { loadAll } from "https://cdn.jsdelivr.net/npm/@tsparticles/all@3.2.2/+esm";

import {options} from "./animationJson.js";

(async () => {
    await loadAll(tsParticles);
    await tsParticles.load({ id: "tsparticles", options });
  })();