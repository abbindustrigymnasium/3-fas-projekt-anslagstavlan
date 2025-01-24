<script lang="ts">
    import Navbar from "../../components/Navbar.svelte";
    let companyName: string = "";
    let orgNumber: string = "";
    function createCompany(): void {
        if (companyName && orgNumber) {
            alert(`Företag "${companyName}" med organisationsnummer "${orgNumber}" har skapats!`);
            companyName = "";
            orgNumber = "";
        } else {
            alert("Vänligen fyll i alla fält.");
        }
    }
</script>

<style>
    .wrapper {
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #d3d3d3;
        font-family: Arial, sans-serif;
    }
    .container {
        background-color: white;
        padding: 20px 30px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        text-align: center;
        width: 300px;
    }
    h1 {
        font-size: 24px;
        margin-bottom: 20px;
    }
    input[type="text"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 16px;
        box-sizing: border-box;
    }
    button {
        width: 100%;
        padding: 10px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 16px;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
</style>

<div class="wrapper">
    <div class="container">
        <h1>Företagsinformation</h1>
        <input
            type="text"
            placeholder="Företag"
            bind:value={companyName}
        />
        <input
            type="text"
            placeholder="Org nr."
            bind:value={orgNumber}
        />
        <button on:click={createCompany}>Skapa Företag</button>
    </div>
</div>