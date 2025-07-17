/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  const priceFilter = document.getElementById('price-filter');
  const options = [
    { value: '', text: "All"},
    { value: '100', text: "100$"},
    { value: '150', text: "150$"},
    { value: '200', text: "200$"},
    { value: '250', text: "250$"},
    { value: '300', text: "300$"}
  ];

  for (const opt of options) {
    const option = document.createElement('option');
    option.value = opt.value;
    option.textContent = opt.text;
    priceFilter.appendChild(option);
  }
});

  /*---------------------------------*/