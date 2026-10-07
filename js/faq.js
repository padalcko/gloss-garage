/* Progressive FAQ enhancement. All questions/answers remain in source HTML. */
(() => {
  document.querySelectorAll('.pdr-faq').forEach((faq) => {
    const buttons = [...faq.querySelectorAll('.pdr-faq__trigger')];
    const setExpanded = (button, panel, expanded) => {
      button.setAttribute('aria-expanded', String(expanded));
      panel.setAttribute('aria-hidden', String(!expanded));
      panel.inert = !expanded;
    };

    buttons.forEach((button, index) => {
      const panel = document.getElementById(button.getAttribute('aria-controls'));
      if (!panel || !faq.contains(panel)) return;
      setExpanded(button, panel, false);
      button.addEventListener('click', () => {
        setExpanded(button, panel, button.getAttribute('aria-expanded') !== 'true');
      });
      // Enter/Space use native button behavior; arrows/Home/End are optional shortcuts.
      button.addEventListener('keydown', (event) => {
        let target;
        if (event.key === 'ArrowDown') target = (index + 1) % buttons.length;
        if (event.key === 'ArrowUp') target = (index + buttons.length - 1) % buttons.length;
        if (event.key === 'Home') target = 0;
        if (event.key === 'End') target = buttons.length - 1;
        if (target === undefined) return;
        event.preventDefault();
        buttons[target].focus();
      });
    });
    faq.classList.add('pdr-faq--ready');
  });
})();
