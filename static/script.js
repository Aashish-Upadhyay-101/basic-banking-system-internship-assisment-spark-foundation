function tableRowClickHandler(customer_id) {
  console.log(customer_id);
  window.location.href = `https://aashish101.pythonanywhere.com/customer/${customer_id}/`;
}
