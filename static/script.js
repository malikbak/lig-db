const leftSlider = document.getElementById("left-slider");
const rightSlider = document.getElementById("right-slider");
const leftValue = document.getElementById("left-value");
const rightValue = document.getElementById("right-value");

leftSlider.addEventListener("input", updateValues);
rightSlider.addEventListener("input", updateValues);

function updateValues() {
    leftValue.textContent = leftSlider.value;
    rightValue.textContent = rightSlider.value;
}
        // Function to update the table based on the row controller input
        function updateTable1() {
            var rowCount = parseInt(document.getElementById("row-count-left").value);
            var tableBody = document.getElementById("left-table-body");
            tableBody.innerHTML = ""; // Clear existing rows

            for (var i = 0; i < rowCount; i++) {
                var row = document.createElement("tr");
                for (var j = 0; j < 4; j++) {
                    var cell = document.createElement("td");
                    cell.textContent = "Row " + (i + 1) + ", Column " + (j + 1);
                    row.appendChild(cell);
                }
                tableBody.appendChild(row);
            }
        }

        // Initial table update
        updateTable1();
        function updateTable2() {
            var rowCount = parseInt(document.getElementById("row-count-right").value);
            var tableBody = document.getElementById("right-table-body");
            tableBody.innerHTML = ""; // Clear existing rows

            for (var i = 0; i < rowCount; i++) {
                var row = document.createElement("tr");
                for (var j = 0; j < 4; j++) {
                    var cell = document.createElement("td");
                    cell.textContent = "Row " + (i + 1) + ", Column " + (j + 1);
                    row.appendChild(cell);
                }
                tableBody.appendChild(row);
            }
        }

        // Initial table update
        updateTable2();

        function updateSliderValue(slider, outputId) {
            var output = document.getElementById(outputId);
            output.textContent = slider.value;
        }
        function updateSliderValue(slider, outputId) {
            var output = document.getElementById(outputId);
            output.textContent = slider.value;
        }


      