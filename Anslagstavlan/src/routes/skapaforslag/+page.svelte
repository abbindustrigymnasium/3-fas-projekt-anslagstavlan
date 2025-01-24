<script lang="ts">
   import Navbar from "../../components/Navbar.svelte";

   // Lista med timmar och typer av projekt
   let timmar = [
       "1 timme", "2 timmar", "3 timmar", "4 timmar", "5 timmar", "6 timmar", "7 timmar", "8 timmar"
   ];
   let typer = [
       "Webbutveckling", "Design", "Marknadsföring", "Övrigt"
   ];

   // Valda värden
   let valdTimme = "";
   let valdTyp = "";
   let projektInfo = "";
   let kontaktPerson = "";
</script>

<style>
   body {
       font-family: Arial, sans-serif;
       margin: 0;
       padding: 0;
       background-color: #f3f3f3;
   }

   .container {
       max-width: 600px;
       margin: 50px auto;
       padding: 20px;
       background-color: #ffffff;
       border-radius: 8px;
       box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
   }

   .header {
       text-align: center;
   }

   .header h1 {
       margin: 0;
       font-size: 24px;
   }

   .header p {
       font-size: 14px;
       color: #666;
   }

   .form-group {
       margin-bottom: 20px;
   }

   .form-group label {
       display: block;
       margin-bottom: 8px;
       font-weight: bold;
   }

   .form-group select,
   .form-group input {
       width: 100%;
       padding: 10px;
       border: 1px solid #ccc;
       border-radius: 4px;
       font-size: 14px;
   }

   .submit-button {
       display: block;
       width: 100%;
       padding: 15px;
       background-color: #007bff;
       color: white;
       font-size: 16px;
       font-weight: bold;
       text-align: center;
       border: none;
       border-radius: 4px;
       cursor: pointer;
       text-transform: uppercase;
   }

   .submit-button:hover {
       background-color: #0056b3;
   }
</style>

<Navbar />

<div class="container">
   <div class="header">
       <h1>Börja här</h1>
       <p>Skriv in detaljer för företagets projekt</p>
   </div>

   <div class="form-group">
       <label for="timmar">Timmar</label>
       <select bind:value={valdTimme} id="timmar">
           <option value="" disabled selected>Välj antal timmar</option>
           {#each timmar as timme}
               <option value={timme}>{timme}</option>
           {/each}
       </select>
   </div>

   <div class="form-group">
       <label for="typ">Typ</label>
       <select bind:value={valdTyp} id="typ">
           <option value="" disabled selected>Välj typ av projekt</option>
           {#each typer as typ}
               <option value={typ}>{typ}</option>
           {/each}
       </select>
   </div>

   <div class="form-group">
       <input
           type="text"
           placeholder="Övrig info om projektet"
           bind:value={projektInfo}
       />
   </div>

   <div class="form-group">
       <input
           type="email"
           placeholder="Kontaktperson@företag.com"
           bind:value={kontaktPerson}
       />
   </div>

   <button class="submit-button">Lägg upp projekt</button>
</div>
