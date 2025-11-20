const BASE_URL = "http://127.0.0.1:3000";
// -----------------------------
// DOMContentLoaded
// -----------------------------
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const priceFilter = document.getElementById("price-filter");

  /* ----- GESTION LOGIN ----- */
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
          document.cookie = `token=${data.access_token}; path=/; SameSite=Strict`;
          window.location.href = '/';
        } else {
          alert('Échec de la connexion : vérifiez vos identifiants');
        }
      } catch (error) {
        console.error('Erreur lors du login:', error);
        alert('Une erreur est survenue. Veuillez réessayer.');
      }
    });
  }

  /* ----- INIT FILTRE PRIX ----- */
  if (priceFilter) {
    priceFilter.innerHTML = `
      <option value="All">All</option>
      <option value="10">10</option>
      <option value="50">50</option>
      <option value="100">100</option>
    `;
    priceFilter.addEventListener("change", filterPlaces);
  }

  /* ----- AUTHENTIFICATION ET FETCH ----- */
  checkAuthentication();
});

// -----------------------------
// COOKIES
// -----------------------------
function getCookie(name) {
  const cookies = document.cookie.split("; ");
  for (let cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === name) return value;
  }
  return null;
}

// -----------------------------
// AUTHENTIFICATION
// -----------------------------
function checkAuthentication() {
  const token = getCookie("token");
  const loginLink = document.querySelector(".login-button");

  if (loginLink) loginLink.style.display = token ? "none" : "block";

  // Si l'utilisateur est sur la page principale
  if (document.getElementById("places-list")) {
    fetchPlaces(token);
  }

  // Si l'utilisateur est sur la page détails d'un lieu
  if (document.getElementById("place-details")) {
    const placeId = getPlaceIdFromURL();
    fetchPlaceDetails(placeId, token);
  }
}

// -----------------------------
// FETCH LISTE DES PLACES
// -----------------------------
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

// -----------------------------
// AFFICHER LES PLACES
// -----------------------------
function displayPlaces(places) {
  const list = document.getElementById("places-list");
  if (!list) return;

  list.innerHTML = "";
  places.forEach(place => {
    const div = document.createElement("div");
    div.classList.add("place-item");
    div.setAttribute("data-price", place.price);

    div.innerHTML = `
      <h3><a href="/place?place_id=${place.id}">${place.title}</a></h3>
      <p>${place.description || ""}</p>
      <p><strong>Prix :</strong> ${place.price} €</p>
      <p><strong>Lieu :</strong> ${place.city || ""}, ${place.country || ""}</p>
    `;
    list.appendChild(div);
  });
}

// -----------------------------
// FILTRE PRIX
// -----------------------------
function filterPlaces() {
  const selected = document.getElementById("price-filter").value;
  const items = document.querySelectorAll(".place-item");

  items.forEach(item => {
    const price = parseInt(item.getAttribute("data-price"));
    item.style.display = (selected === "All" || price <= parseInt(selected)) ? "block" : "none";
  });
}

// -----------------------------
// PLACE DETAILS
// -----------------------------
function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get("place_id");
}

async function fetchPlaceDetails(placeId, token) {
  try {
    const response = await fetch(`${BASE_URL}/api/v1/places/${placeId}`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {}
    });

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
    <p><strong>Lieu :</strong> ${place.city || ""}, ${place.country || ""}</p>
    <p><strong>Commodités :</strong> ${place.amenities ? place.amenities.join(", ") : ""}</p>
  `;

  // Afficher le formulaire d'avis seulement si l'utilisateur est connecté
  const reviewSection = document.getElementById("add-review");
  if (reviewSection) reviewSection.style.display = token ? "block" : "none";

  if (place.reviews) {
    const reviewList = document.getElementById("reviews");
    reviewList.innerHTML = "<h3>Avis</h3>";
    place.reviews.forEach(r => {
      const div = document.createElement("div");
      div.classList.add("review-item");
      div.innerHTML = `<p><strong>${r.user} :</strong> ${r.text} (${r.rating}/5)</p>`;
      reviewList.appendChild(div);
    });
  }
}
