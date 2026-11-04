(() => {
  const root = document.documentElement;
  const buttons = document.querySelectorAll('[data-theme-choice]');

  function updateButtons() {
    buttons.forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.themeChoice === root.dataset.theme));
    });
  }

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const theme = button.dataset.themeChoice;
      root.dataset.theme = theme;
      try {
        localStorage.setItem('color-theme', theme);
      } catch (error) {}
      updateButtons();
    });
  });

  updateButtons();
})();
