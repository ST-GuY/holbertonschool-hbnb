document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault(); // Empêche le comportement par défaut du formulaire

      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      // Appel API pour la connexion
      try {
        const response = await fetch('http://127.0.0.1:3000/api/v1/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
        });

        if (response.ok) {
          const data = await response.json();
          // Stocker le token JWT dans un cookie
          document.cookie = `token=${data.access_token}; path=/; Secure; SameSite=Strict`;
          // Rediriger vers la page principale
          window.location.href = 'index.html';
        } else {
          // Afficher erreur
          alert('Échec de la connexion : vérifiez vos identifiants');
        }
      } catch (error) {
        console.error('Erreur lors de la tentative de login:', error);
        alert('Une erreur est survenue. Veuillez réessayer.');
      }
    });
  }
});
