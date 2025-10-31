document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.zoom').forEach(item => {
    item.addEventListener('click', function () {
      this.classList.toggle('image-zoom-large');
      this.parentElement.classList.toggle('image-backdrop');
      document.body.classList.toggle('hide');
    })
  });
});
