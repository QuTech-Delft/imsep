const colorSchemeQueryList = window.matchMedia('(prefers-color-scheme: dark)');

const setColorScheme = e => {
  if (e.matches) {
    // Dark
    document.querySelector( 'label[for="__palette_1"]').click();
  } else {
    // Light
    document.querySelector( 'label[for="__palette_0"]').click();
  }
}

setColorScheme(colorSchemeQueryList);
document.activeElement.blur();
colorSchemeQueryList.addEventListener('change', setColorScheme);
all
