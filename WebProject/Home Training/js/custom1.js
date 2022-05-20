var params = {
  container: document.querySelector("#lottie1"),
  renderer: "canvas",
  loop: true,
  autoplay: true,
  path: "data/Review.json",
};

var anim;

anim = lottie.loadAnimation(params);
