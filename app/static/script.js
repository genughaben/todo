// Handle create
document.getElementById('form').onsubmit = function(e) {
    e.preventDefault() // would normally reload whole page!
    fetch('todo/create', {
        method: 'POST',
        body: JSON.stringify({
            'description': document.getElementById('description').value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(function(response) {
      return response.json();
    })
    .then(function(jsonResponse) {
      const li = document.createElement('li');
      const checkbox = document.createElement('input');
      checkbox.className = 'completed';
      checkbox.type = 'checkbox';
      checkbox.setAttribute('data-id', jsonResponse.id);
      li.appendChild(checkbox);

      const text = document.createTextNode(' ' + jsonResponse.description);
      li.appendChild(text);

      const deleteBtn = document.createElement('button');
      deleteBtn.className = 'close';
      deleteBtn.setAttribute('data-id', jsonResponse.id);
      deleteBtn.innerHTML = '&cross;';
      li.appendChild(deleteBtn);

      document.getElementById('todos').appendChild(li);
      document.getElementById('error').className = 'hidden';
    })
    .catch(function(e) {
      document.getElementById('error').className = 'error';
    });
}

// Handle update

const checkboxes = document.querySelectorAll('.check-completed');
for (let i = 0; i < checkboxes.length; i++){
    checkbox = checkboxes[i]
    checkbox.onchange = function(e) {
      const newCompletedState = e.target.checked;
      const todoId = e.target.dataset["id"];
      fetch('/todo/' + todoId + '/set-completed', {
        method: 'POST',
        body: JSON.stringify({
          'completed': newCompletedState
        }),
        headers: {
          'Content-Type': 'application/json'
      }
    })
    .then(function() {
      document.getElementById('error').className = 'hidden';
    })
    .catch(function() {
      document.getElementById('error').className = 'error';
    });
  }
}

// Handle delete

const closeSpans = document.querySelectorAll('.close');
for (let i = 0; i < closeSpans.length; i++){
    closeSpan = closeSpans[i]
    closeSpan.onclick = function(e) {
      const todoId = e.target.dataset["id"];
      console.log(todoId);
      fetch('/todo/' + todoId + '/delete', {
        method: 'DELETE',
      })
      .then(function(response) {
        return response.json();
      })
      .then(function(jsonResponse) {
        let success = jsonResponse['success'];
        if(success){
          let item = e.target.parentElement;
          item.remove();
        }
      })
      .catch(function(e) {
        document.getElementById('error').className = 'error';
      });
  }
}