# Anslagstavlan 
## Skapare
Gustav Ström, Beni och lukas
## Syfte
Anslagstavlan är en webbaserad plattform där företag kan lägga upp projekt som kan genomföras av elever.

## Techstack

### Svelte
**Varför Svelte?**
</br>
Svelte är ett modernt Javascript ramverk som är lightweight och lättanvändlig.
</br>
</br>
**Viktiga funktioner i detta projekt:**
</br>
UI-rendering och API-anrop till Flask-backend.
### Flask
**Varför Flask?**
</br>
Flask är ett lightweight och flexibelt web ramverk för python, dens minimalistiska design gör det lätt att använda och anpassa.
</br>
</br>
**Viktiga funktioner i detta projekt:**
</br>
RESTful API för att hantera klientförfrågningar från Svelte-frontenden, JSON-svar för dynamisk innehållsleverans.
### Supabase
**Varför Supabase?**
</br>
Byggt på PostgreSQL för tillförlitlighet och skalbarhet, inbyggd autentisering
</br>
</br>
**Viktiga funktioner i detta projekt:**
</br>
Autentisering med e-post och Microsoft, persistent lagring för användardata

### Integrations översikt

**Svelte-frontenden kommunicerar med Flask-backenden via RESTful API:er.**
</br>
</br>
**Flask-backenden interagerar med Supabase-databasen för CRUD-operationer.**
</br>
</br>
**Supabase-realtidsprenumerationer tillhandahåller liveuppdateringar till frontenden som data ändringar**
</br>
</br>


## Planering
### Flödesschema 
![bild](https://github.com/user-attachments/assets/4ddc0b8a-da0d-42ab-a6bd-82b90d7868a0)

### Funktionsspecifikation för controller
![bild](https://github.com/user-attachments/assets/ff251987-c52f-41e6-b720-031676270936)

## Installationsinstruktioner

### Krav
Node.js v22+
Python 3.8+
Supabase konto

### Installering
1. Klona repository
   </br>
 `git clone https://github.com/abbindustrigymnasium/3-fas-projekt-anslagstavlan.git `
2. Setup av Frontend
   </br>
`cd Anslagstavlan`
   </br>
`npm install`
   </br>
`npm run dev`

3. Setup av Flask
   </br>
`cd ..`
   </br>
`cd Controller`
   </br>
`flask run`

## Vidareutveckling
**För att förbättra projektets funktionalitet och tillgodose fler användarbehov kan följande vidareutveckling övervägas:**
</br>
1. Tillägg av lärarfunktionalitet
2. Tillägg av projektmallar 
