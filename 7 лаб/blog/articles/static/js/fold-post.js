var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
  foldBtns[i].addEventListener("click", function(e) {
    var element = e.target.parentNode; // находим родительский элемент кнопки
      if (element.className == "one-post folded") {
      e.target.innerHTML = "свернуть";
      element.className = "one-post";; // удаляем класс folded
    } else {
      e.target.innerHTML = "развернуть";
      element.className = "one-post folded";; // добавляем класс folded
    }
  });
};

