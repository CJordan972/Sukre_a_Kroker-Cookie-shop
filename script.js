/* Maison Miette — JavaScript débutant : un petit panier fictif, sans paiement. */

// 1. Voici les données de notre catalogue. Les prix sont en centimes.
const products = {
  chocolat: { name: "Le Cacao Royal", detail: "Chocolat noir · Fleur de sel", price: 450, image: 'assets/cookie-chocolat.svg' },
  pistache: { name: 'Le Précieux', detail: 'Pistache · Chocolat blanc', price: 450, image: 'assets/cookie-pistache.svg' },
  caramel: { name: 'Le Fondant', detail: 'Caramel beurre salé · Noix', price: 450, image: 'assets/cookie-caramel.svg' },
  framboise: { name: 'Le Rosé', detail: 'Framboise · Vanille', price: 450, image: 'assets/cookie-framboise.svg' }
};

// 2. Notre panier est un objet : { chocolat: 2, pistache: 1 }, par exemple.
const cart = {};
const cartDrawer = document.querySelector('#cart-drawer');
const cartOverlay = document.querySelector('#cart-overlay');
const cartItems = document.querySelector('#cart-items');
const toast = document.querySelector('#toast');
let toastTimeout;
let previousFocus = null;

function euros(cents) {
  return (cents / 100).toLocaleString('fr-FR', { style: 'currency', currency: 'EUR' });
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add('visible');
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => toast.classList.remove('visible'), 2700);
}

// 3. Ajouter, retirer et compter les cookies.
function changeQuantity(id, amount) {
  if (!products[id]) return;
  const next = (cart[id] || 0) + amount;
  if (next <= 0) delete cart[id];
  else cart[id] = next;
  updateCart();
}

function updateCart() {
  const entries = Object.entries(cart);
  const count = entries.reduce((sum, [, quantity]) => sum + quantity, 0);
  const total = entries.reduce((sum, [id, quantity]) => sum + products[id].price * quantity, 0);
  document.querySelector('#cart-count').textContent = count;
  document.querySelector('#drawer-count').textContent = `(${count})`;
  document.querySelector('#cart-total').textContent = euros(total);

  if (entries.length === 0) {
    cartItems.innerHTML = '<p class="empty-cart">Votre panier est encore vide.<br>Et si vous choisissiez un cookie ? ♡</p>';
    return;
  }

  // Les noms et chemins viennent de notre catalogue écrit ci-dessus, pas d'une saisie utilisateur.
  cartItems.innerHTML = entries.map(([id, quantity]) => {
    const product = products[id];
    return `<div class="cart-item">
      <img src="${product.image}" alt="" />
      <div class="cart-item-info"><strong>${product.name}</strong><small>${product.detail}</small>
        <div class="quantity-control">
          <button type="button" data-change="-1" data-id="${id}" aria-label="Retirer un ${product.name}">−</button>
          <span>${quantity}</span>
          <button type="button" data-change="1" data-id="${id}" aria-label="Ajouter un ${product.name}">+</button>
        </div>
      </div><span class="cart-item-price">${euros(product.price * quantity)}</span>
    </div>`;
  }).join('');
}

function openCart() {
  previousFocus = document.activeElement;
  cartDrawer.hidden = false;
  cartOverlay.hidden = false;
  document.body.classList.add('no-scroll');
  document.querySelector('#close-cart').focus();
}

function closeCart() {
  cartDrawer.hidden = true;
  cartOverlay.hidden = true;
  document.body.classList.remove('no-scroll');
  if (previousFocus && typeof previousFocus.focus === 'function') previousFocus.focus();
}

// 4. On écoute les clics sur les boutons.
document.querySelectorAll('.add-button').forEach(button => {
  button.addEventListener('click', () => {
    const id = button.dataset.product;
    changeQuantity(id, 1);
    showToast(`${products[id].name} ajouté au panier !`);
  });
});

cartItems.addEventListener('click', event => {
  const button = event.target.closest('button[data-change]');
  if (button) changeQuantity(button.dataset.id, Number(button.dataset.change));
});

document.querySelector('#open-cart').addEventListener('click', openCart);
document.querySelector('#close-cart').addEventListener('click', closeCart);
document.querySelector('#keep-shopping').addEventListener('click', closeCart);
cartOverlay.addEventListener('click', closeCart);
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !cartDrawer.hidden) closeCart();
  // Maintenir la navigation clavier dans la fenêtre de panier.
  if (event.key === 'Tab' && !cartDrawer.hidden) {
    const focusable = [...cartDrawer.querySelectorAll('button:not([disabled])')];
    if (!focusable.length) return;
    const first = focusable[0], last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  }
});

updateCart();
