var params = {
  container: document.querySelector("#lottie2"),
  renderer: "canvas",
  loop: true,
  autoplay: true,
  path: "data/Feature1.json",
};

var anim;

anim = lottie.loadAnimation(params);
