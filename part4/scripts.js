document.addEventListener('DOMContentLoaded', () => {

  /* ----- GESTION LOGIN ----- */
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      try {
        const response = await fetch("http://127.0.0.1:3000/api/v1/places/", {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password })
        });

        if (response.ok) {
          const data = await response.json();
          document.cookie = `token=${data.access_token}; path=/; Secure; SameSite=Strict`;
          window.location.href = 'index.html';
        } else {
          alert('Échec de la connexion : vérifiez vos identifiants');
        }

      } catch (error) {
        console.error('Erreur lors du login:', error);
        alert('Une erreur est survenue. Veuillez réessayer.');
      }
    });
  }

  /* ----- AUTHENTIFICATION + FETCH PLACES ----- */
  checkAuthentication();

  /* ----- FILTRE PRIX ----- */
  const priceFilter = document.getElementById("price-filter");
  if (priceFilter) {
    priceFilter.innerHTML = `
      <option value="All">All</option>
      <option value="10">10</option>
      <option value="50">50</option>
      <option value="100">100</option>
    `;
    priceFilter.addEventListener("change", filterPlaces);
  }
});
