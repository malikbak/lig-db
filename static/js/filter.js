function filterTable() {
    // Variables
    let dropdown, table, rows, cells, country, filter;
    dropdown = document.getElementById("countriesDropdown");
    table = document.getElementById("myTable");
    rows = table.getElementsByTagName("tr");
    filter = dropdown.value;
  
    // Loops through rows and hides those with countries that don't match the filter
    for (let row of rows) { // `for...of` loops through the NodeList
      cells = row.getElementsByTagName("td");
      country = cells[0] || null; // gets the 2nd `td` or nothing
      // if the filter is set to 'All', or this is the header row, or 2nd `td` text matches filter
      if (filter === "All" || !country || (filter === country.textContent)) {
        row.style.display = ""; // shows this row
      }
      else {
        row.style.display = "none"; // hides this row
      }
    }
  }
  const options = []

  document.querySelectorAll('#countriesDropdown > option').forEach((option) => {
      if (options.includes(option.value)) option.remove()
      else options.push(option.value)
  })
  // Select the table and the dropdown
  const table = document.getElementById("myTable");
  const dynamicDropdown = document.getElementById("dynamicDropdown");

  // Get all the values from the table and add them to the dropdown
  const rows = table.getElementsByTagName("tr");
  for (let i = 1; i < rows.length; i++) {
      const cell = rows[i].getElementsByTagName("td")[2];
      const option = document.createElement("option");
      option.text = cell.textContent;
      dynamicDropdown.add(option);
  }
  const optionsp = []

  document.querySelectorAll('#dynamicDropdown > option').forEach((option) => {
      if (optionsp.includes(option.value)) option.remove()
      else optionsp.push(option.value)
  })
  function filterTablef() {
    // Variables
    let dropdown, table, rows, cells, country, filter;
    dropdown = document.getElementById("dynamicDropdown");
    table = document.getElementById("myTable");
    rows = table.getElementsByTagName("tr");
    filter = dropdown.value;
  
    // Loops through rows and hides those with countries that don't match the filter
    for (let row of rows) { // `for...of` loops through the NodeList
      cells = row.getElementsByTagName("td");
      country = cells[2] || null; // gets the 2nd `td` or nothing
      // if the filter is set to 'All', or this is the header row, or 2nd `td` text matches filter
      if (filter === "All" || !country || (filter === country.textContent)) {
        row.style.display = ""; // shows this row
      }
      else {
        row.style.display = "none"; // hides this row
      }
    }
  }
  function alertInnerHTML(e)
    {
        e = e || window.event;//IE
        alert(this.innerHTML);
    }

    var theTbl = document.getElementById('myTable');
    for(var i=0;i<theTbl.length;i++)
    {
        for(var j=0;j<theTbl.rows[i].cells.length;j++)
        {
            theTbl.rows[i].cells[j].onclick = alertInnerHTML;
        }
    }
 // Select the table and other elements
 const uniqueValueCount = document.getElementById("uniqueValueCount");
const countButton = document.getElementById("countButton");

// Function to count unique values from comma-separated values
function countUniqueValues(columnIndex) {
    const values = new Set();
    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) { // Start at index 1 to skip the header row
        const cell = rows[i].getElementsByTagName("td")[columnIndex];
        const cellValues = cell.textContent.split(',').map(value => value.trim());

        cellValues.forEach(value => {
            values.add(value);
        });
    }

    return values.size;
}

// Add an event listener to the button
countButton.addEventListener("click", function () {
    const uniqueCount = countUniqueValues(1); // Use index 1 for Column 2
    uniqueValueCount.textContent = `Number of unique values: ${uniqueCount}`;
});

document.addEventListener("DOMContentLoaded", function () {
    const filterDropdown = document.getElementById("countriesDropdown");  // "Filter by Bacteria" dropdown
    const tablef = document.getElementById("myTable").getElementsByTagName("tbody")[0]; // Table body

    // Function to filter the table based on the selected value
    function filterTable(selectedValue) {
        const rows = tablef.getElementsByTagName("tr");
        for (let i = 0; i < rows.length; i++) {
            const cell = rows[i].getElementsByTagName("td")[0]; // Assuming the first column is the "Bacteria" column
            const cellValue = cell.textContent;

            if (selectedValue === "All" || cellValue === selectedValue) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }

    // Add an event listener to the "Filter by Bacteria" dropdown
    filterDropdown.addEventListener("change", function () {
        const selectedValue = filterDropdown.value;
        filterTable(selectedValue);
    });

    // Initialize the table filtering
    filterTable("All"); // Show all rows initially
});
