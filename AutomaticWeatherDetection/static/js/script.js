const addCityButton = document.getElementById("add-city-button");
const cityForm = document.getElementById("city-form");
const cityFormInner = document.getElementById("city-form-inner");
const citiesContainer = document.getElementById("cities-container");
const emailid = document.getElementById("email");

// Variable to keep track of the form visibility
let isFormVisible = false;

addCityButton.addEventListener("click", () => {
    // Toggle the visibility of the city submission form
    cityForm.classList.toggle("hidden");
    
    // Toggle the button text between "Add City" and "X"
    isFormVisible = !isFormVisible;
    addCityButton.textContent = isFormVisible ? "X" : "Add City";
});

cityFormInner.addEventListener("submit", (e) => {
    e.preventDefault();
    const cityName = document.getElementById("city").value;
    const maxTemp = document.getElementById("max-temp").value;
    const minTemp = document.getElementById("min-temp").value;
    const emailid = document.getElementById("email").value;

    $.ajax({
        data:{
            location:cityName,
            min_temp:minTemp,
            max_temp:maxTemp,
            email:emailid,
        },
        type:"POST",
        url:"/adddata",
    }).done(function(data){
    });

    const cityCard = document.createElement("div");
    cityCard.classList.add("city-card");
    cityCard.innerHTML = `
        <div class="city-info">
            <span>${cityName}</span>
            <button class="info-button">+</button>
        </div>
        <div class="temp">
            <div class="info-box hidden">
                Info for ${cityName}: <br> Max Temp: ${maxTemp},<br> Min Temp: ${minTemp},<br> E-mail: ${emailid}
            </div>
        </div>
        
    `;

    // Add an event listener to the info button
    const infoButton = cityCard.querySelector(".info-button");
    infoButton.addEventListener("click", () => {
        // Toggle the visibility of the info box
        const infoBox = cityCard.querySelector(".info-box");
        infoBox.classList.toggle("hidden");
        cityCard.classList.toggle("show-info");
        infoButton.textContent = infoBox.classList.contains("hidden") ? "+" : "x";
    });

    citiesContainer.appendChild(cityCard);

    // Clear form fields
    document.getElementById("city").value = ""; // Clear city name
    document.getElementById("max-temp").value = ""; // Clear max temperature
    document.getElementById("min-temp").value = ""; // Clear min temperature

    // Hide the form
    cityForm.classList.add("hidden");
    // Reset the button text to "Add City"
    isFormVisible = false;
    addCityButton.textContent = "Add City";
});