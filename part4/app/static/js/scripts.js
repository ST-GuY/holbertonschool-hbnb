// Détecte automatiquement l'URL du backend
const BASE_URL = (() => {
  // Si on est sur Go Live (port 5500), le backend est sur 127.0.0.1:3000
  if (window.location.port && window.location.port !== "3000") {
    return "http://127.0.0.1:3000";
  }
  return ""; // backend sur même serveur/port
})();

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const priceFilter = document.getElementById("price-filter");

  /* ------------------------------
        GESTION LOGIN
  ------------------------------ */
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;

      try {
        const response = await fetch(`${BASE_URL}/api/v1/auth/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password })
        });

        if (response.ok) {
          const data = await response.json();
          localStorage.setItem("token", data.access_token);

          // Redirection vers la page d'accueil
          window.location.href = "/";
        } else {
          alert('Échec de la connexion : vérifiez vos identifiants');
        }
      } catch (error) {
        console.error('Erreur lors du login:', error);
        alert('Une erreur est survenue. Veuillez réessayer.');
      }
    });
  }

  /* ------------------------------
        INIT FILTRE PRIX
  ------------------------------ */
  if (priceFilter) {
    priceFilter.innerHTML = `
      <option value="All">All</option>
      <option value="10">10</option>
      <option value="50">50</option>
      <option value="100">100</option>
    `;
    priceFilter.addEventListener("change", filterPlaces);
  }

  /* ------------------------------
        LISTENER FORM REVIEW
  ------------------------------ */
  const reviewForm = document.getElementById("review-form");
  if (reviewForm) reviewForm.addEventListener("submit", submitReview);

  /* ------------------------------
        AUTH + FETCH
  ------------------------------ */
  checkAuthentication();
});

/* -----------------------------
      AUTHENTIFICATION
----------------------------- */
function checkAuthentication() {
  const token = localStorage.getItem("token");
  const loginLink = document.querySelector(".login-button");

  if (loginLink) loginLink.style.display = token ? "none" : "block";

  // Page d'accueil → liste des places
  if (document.getElementById("places-list")) fetchPlaces(token);

  // Page des détails → afficher le lieu
  if (document.getElementById("place-details")) {
    const placeId = getPlaceIdFromURL();
    fetchPlaceDetails(placeId, token);
  }
}

/* -----------------------------
      FETCH LISTE DES PLACES
----------------------------- */
async function fetchPlaces(token) {
  try {
    const response = await fetch(`${BASE_URL}/api/v1/places/`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {}
    });
    if (!response.ok) return console.error("Erreur lors du fetch des places");

    const places = await response.json();
    displayPlaces(places);

  } catch (err) {
    console.error("Erreur réseau:", err);
  }
}

/* -----------------------------
      AFFICHER LES PLACES
----------------------------- */
function displayPlaces(places) {
  const list = document.getElementById("places-list");
  if (!list) return;

  list.innerHTML = "";
  places.forEach(place => {
    const div = document.createElement("div");
    div.classList.add("place-item");
    div.setAttribute("data-price", place.price);

    div.innerHTML = `
      <h3><a href="/place.html?place_id=${place.id}">${place.title}</a></h3>
      <p>${place.description || ""}</p>
      <p><strong>Prix :</strong> ${place.price} €</p>
    `;

    list.appendChild(div);
  });
}

/* -----------------------------
           FILTRE PRIX
----------------------------- */
function filterPlaces() {
  const selected = document.getElementById("price-filter").value;
  const items = document.querySelectorAll(".place-item");

  items.forEach(item => {
    const price = parseInt(item.getAttribute("data-price"));
    item.style.display = (selected === "All" || price <= parseInt(selected)) ? "block" : "none";
  });
}

/* -----------------------------
        PLACE DETAILS
----------------------------- */
function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get("place_id");
}

async function fetchPlaceDetails(placeId, token) {
  try {
    const headers = token ? { Authorization: `Bearer ${token}` } : {};
    const response = await fetch(`${BASE_URL}/api/v1/places/${placeId}`, { headers });

    if (!response.ok) return console.error("Erreur lors du fetch du lieu");

    const place = await response.json();
    displayPlaceDetails(place, token);

  } catch (err) {
    console.error("Erreur réseau:", err);
  }
}

function displayPlaceDetails(place, token) {
  const details = document.getElementById("place-details");
  if (!details) return;

  details.innerHTML = `
    <h2>${place.title}</h2>
    <p>${place.description || ""}</p>
    <p><strong>Prix :</strong> ${place.price} €</p>
    <p><strong>Commodités :</strong> ${
      place.amenities ? place.amenities.map(a => a.name).join(", ") : "Aucune"
    }</p>
  `;

  // Formulaire d'avis → visible seulement si connecté
  const reviewSection = document.getElementById("add-review");
  if (reviewSection) reviewSection.style.display = token ? "block" : "none";

  // Liste des reviews
  const reviewList = document.getElementById("reviews");
  reviewList.innerHTML = "<h3>Avis</h3>";

  if (place.reviews && place.reviews.length > 0) {
    place.reviews.forEach(r => {
      const div = document.createElement("div");
      div.classList.add("review-item");

      div.innerHTML = `
        <p><strong>${r.user_name || "Utilisateur inconnu"} :</strong> 
        ${r.text} (${r.rating}/5)</p>
      `;

      reviewList.appendChild(div);
    });
  } else {
    reviewList.innerHTML += "<p>Aucun avis pour ce lieu.</p>";
  }
}

/* -----------------------------
        AJOUT D'UN REVIEW
----------------------------- */
async function submitReview(event) {
  event.preventDefault();

  const token = localStorage.getItem("token");
  if (!token) {
    alert("Vous devez être connecté pour poster un avis.");
    return;
  }

  const text = document.getElementById("review-text").value;
  const rating = document.getElementById("review-rating").value;
  const placeId = getPlaceIdFromURL();

  try {
    const response = await fetch(`${BASE_URL}/api/v1/places/${placeId}/reviews`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify({
        text,
        rating: parseInt(rating)
      })
    });

    if (!response.ok) {
      alert("Erreur lors de l'ajout de l'avis");
      return;
    }

    alert("Avis ajouté avec succès !");
    // Recharge les détails pour afficher le nouvel avis
    fetchPlaceDetails(placeId, token);
    document.getElementById("review-form").reset();

  } catch (error) {
    console.error("Erreur réseau:", error);
  }
}
