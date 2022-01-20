const nav = document.querySelector('nav');

function updateNavbar() {
  if (scrollY > 100) {
    nav.classList.add('bg-gray-900');
  } else {
    nav.classList.remove('bg-gray-900');
  }
}

document.addEventListener('scroll', (e) => updateNavbar());

// const nav = document.querySelector('nav');

// document.addEventListener('scroll', (e) => {
//   if (scrollY > 100) {
//     nav.classList.add('bg-gray-900');
//     console.log('teste');
//   } else {
//     nav.classList.remove('bg-gray-900');
//   }
// });
