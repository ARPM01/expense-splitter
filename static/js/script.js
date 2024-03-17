
// Script for the modify expense modal
var modifyExpenseModal = document.getElementById('modifyExpense')
modifyExpenseModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    var id = button.getAttribute('id').split("modifyButton")[1]

    // Fetch the expense details
    fetch('/expense/' + id)
        .then(response => response.json())
        .then(expense => {
            // Fill the form inputs with the expense details
            document.querySelector('input[name="newName"]').value = expense.title;
            document.querySelector('input[name="newAmount"]').value = expense.amount;
            document.querySelector('select[name="newPaidBy"]').value = expense.paid_by;
            document.querySelector('input[name="newEquallysplit"]').checked = expense.equally_split;
        });

    // Link the modal form to the flask route
    var modalForm = modifyExpenseModal.querySelector('form')
    modalForm.action = '/modify/' + id
})

