var table = $('#timesheet')
var tableBody = $("#tsdata")
var counter = 1;
var modal = $("#activityModal")
var form = $('#activityForm');
var submitBtn = $("modalSubmit");
var editFlag = false;

// Container binding for dynamically added edit row buttons.
$("#timesheet").on('click', '.editRow', function(){
  var id = this.attributes.id.value.match(/[0-9]/g)[0];
  var selector = '#row-' + id;
  var row = $(selector);
  var rowData = serializeRow(row);
  // Prefill the modal form with current data
  var inputs = form.find('.form-control');
  $.each(inputs, function(i, val){
    inputs[i].value = rowData[i];
  });
  editFlag = id;
  modal.modal('show');
});

// Container binding for dynamically added delete row buttons.
$("#timesheet").on('click', '.delRow', function(){
  var id = this.attributes.id.value.match(/[0-9]/g)[0];
  var selector = '#row-' + id;
  $(selector).remove();
});

// Function to add a row to the table using modal form data
var addRow = function(formData){
  var html = "<tr id=\"row-" + (counter) + "\">";
  for(var i = 0; i < formData.length; i++){
    html += "<td>"+formData[i].value+"</td>";
  }
  html += "<td><button id=\"edit-" + counter + "\" class=\"btn editRow btn-primary btn-sm\"><span class=\"glyphicon glyphicon-pencil\"></span></button> <button id=\"delete-" + counter + "\" class=\"btn delRow btn-danger btn-sm\"><span class=\"glyphicon glyphicon-remove\"</span></button></td>"
  html += "</tr>";
  
  // Update selectors and increment counter
  counter++;
  tableBody.append(html);
}

// Submission of activity via modal
form.on('submit',function(event){
  event.preventDefault();
  var formData = form.serializeArray();
  // If the edit flag is set, change a row instead of adding.
  if(editFlag){
    var selector = '#row-' + editFlag;
    var row = $(selector);
    var cells = row.find('td');
    for(var i = 0; i < (cells.length) - 1; i++){
      cells[i].firstChild.data = formData[i].value;
    }
    editFlag = false;
  }
  else{
    addRow(formData);
  }
  form.trigger('reset');
  modal.modal('hide');
});

// Serializes a table into an object using headers as object properties.
var serializeTable = function(table){
  var TableObj = {};
  var headers = table.find('th');
  var rows = table.find('tbody').find('tr');
  for(var i = 0; i < rows.length; i++){
    TableObj[i] = {};
    // Subtract 1 from headers.length because of the hidden button       column.
    for(var j = 0; j < (headers.length)-1; j++){ 
      TableObj[i][headers[j].firstChild.data] = rows.children()[j].firstChild.data;
    }
  }
  return TableObj;
}

// Serialize a single row into an array
var serializeRow = function(row){
  var cells = row.find('td');
  var data = [];
  for(var i = 0; i < (cells.length)-1; i++){
    data.push(cells[i].firstChild.data);
  }
  return data;
}

//Set close button to turn off edit flag.
$('#modalClose').on('click', function(){
  editFlag = false;
  form.trigger('reset');
})