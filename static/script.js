function tableRowClickHandler(customer_id) {
  console.log(customer_id);
  window.location.href = `http://127.0.0.1:8000/customer/${customer_id}/`;
}
