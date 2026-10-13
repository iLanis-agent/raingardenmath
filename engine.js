(function (root) {
  "use strict";
  var RUNOFF_COEF = 0.9; // labeled hard-surface runoff coefficient
  var BED_PCT = 15;      // labeled bed area as percent of drainage area
  var MULCH_CM = 8;      // labeled mulch depth, cm
  var BAG_L = 50;        // labeled mulch bag, liters

  function round1(x) { return Math.round(x * 10) / 10; }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function catchPlan(areaM2, rainCm) {
    if (!(areaM2 > 0) || !(rainCm > 0)) return { error: "the area and the rain must be positive" };
    var liters = round1(areaM2 * rainCm * 10 * RUNOFF_COEF);
    var verdict;
    if (liters <= 500) verdict = "barrel scale";
    else if (liters <= 3000) verdict = "garden scale";
    else verdict = "swale territory";
    return { liters: liters, verdict: verdict };
  }

  function bedPlan(areaM2) {
    if (!(areaM2 > 0)) return { error: "the area must be positive" };
    var bed = round1(areaM2 * BED_PCT / 100);
    var verdict;
    if (bed <= 4) verdict = "a planter box";
    else if (bed <= 15) verdict = "a weekend dig";
    else verdict = "a landscaper's job";
    return { bed: bed, verdict: verdict };
  }

  function mulchPlan(bedM2) {
    if (!(bedM2 > 0)) return { error: "the bed must be positive" };
    var liters = round1(bedM2 * MULCH_CM * 10);
    var bags = Math.ceil(liters / BAG_L);
    var verdict;
    if (bags <= 4) verdict = "a car-trunk haul";
    else if (bags <= 16) verdict = "a few trips";
    else verdict = "a delivery load";
    return { liters: liters, bags: bags, verdict: verdict };
  }

  function renderCatch(r, areaM2, rainCm) {
    return "A " + rainCm + " cm rain on your " + areaM2 + " m2 roof sends " + r.liters
      + " L your way at a labeled " + RUNOFF_COEF + " runoff coefficient - " + r.verdict + ".";
  }

  function renderBed(r, areaM2) {
    return "Your " + areaM2 + " m2 roof at a labeled " + BED_PCT + " percent rule names a " + r.bed
      + " m2 bed - " + r.verdict + ".";
  }

  function renderMulch(r, bedM2) {
    return "Your " + bedM2 + " m2 bed at a labeled " + MULCH_CM + " cm of mulch asks " + r.liters
      + " L - " + plural(r.bags, "bag") + " of labeled " + BAG_L + " L, " + r.verdict + ".";
  }

  var api = { catchPlan: catchPlan, bedPlan: bedPlan, mulchPlan: mulchPlan, renderCatch: renderCatch, renderBed: renderBed, renderMulch: renderMulch };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.RainGardenMath = api;
})(this);
