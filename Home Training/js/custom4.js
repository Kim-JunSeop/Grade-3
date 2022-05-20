var params = {
  container: document.querySelector("#lottie4"),
  renderer: "canvas",
  loop: true,
  autoplay: true,
  path: "data/partner.json",
};

var anim;

anim = lottie.loadAnimation(params);
