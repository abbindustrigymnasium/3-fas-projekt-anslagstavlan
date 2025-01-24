<script lang="ts">
    //Author Beni
    import Navbar from "../../components/Navbar.svelte";

    // Types
    interface Applicant {
        name: string;
        school: string;
        accepted: boolean;
    }

    let projects: string[] = ["Projekt 1", "Projekt 2", "Projekt 3", "Projekt 4", "Projekt 5", "Projekt 6"];

    let selectedProject: string = "";
    let showPopup: boolean = false;

    // Map to hold applicants for each project
    let projectApplicants: Record<string, Applicant[]> = {};

    // Initialize projectApplicants with default values
    projects.forEach(project => {
        projectApplicants[project] = [
            { name: "Elev Namn 1", school: "Hitachigymnasiet", accepted: false },
            { name: "Elev Namn 2", school: "Hitachigymnasiet", accepted: false },
            { name: "Elev Namn 3", school: "Hitachigymnasiet", accepted: false }
        ];
    });

    function openPopup(project: string): void {
        selectedProject = project;
        showPopup = true;
    }

    function closePopup(): void {
        showPopup = false;
    }

    function acceptApplicant(index: number): void {
        if (selectedProject) {
            projectApplicants[selectedProject][index].accepted = true;
        }
    }

    function removeApplicant(index: number): void {
        if (selectedProject) {
            projectApplicants[selectedProject][index].accepted = false;
        }
    }

    function getInterestCount(project: string): number {
        return projectApplicants[project]?.filter(applicant => applicant.accepted).length || 0;
    }
</script>

<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f5f5dc;
    }

    .container {
        display: flex;
        height: 100vh;
    }

    .content {
        flex: 3;
        padding: 20px;
        background-color: #f5f5dc;
    }

    .sidebar {
        flex: 1;
        padding: 20px;
        background-color: white;
        border-left: 2px solid #ccc;
    }

    .project-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin-top: 20px;
    }

    .project-card {
        background-color: #ffffff;
        padding: 20px;
        text-align: center;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        height: 200px;
    }

    .popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        width: 400px;
        padding: 20px;
        z-index: 1000;
    }

    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 999;
    }

    .popup-header {
        text-align: center;
        margin-bottom: 20px;
    }

    .popup-header h2 {
        font-size: 24px;
        margin: 0;
    }

    .applicant {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .applicant.accepted {
        background-color: #d4edda; /* Light green for accepted */
        border-color: #c3e6cb; /* Slightly darker green border */
    }

    .applicant:not(.accepted) {
        background-color: white;
        border-color: #ccc;
    }

    .close-button {
        display: block;
        margin: 20px auto 0;
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    .close-button:hover {
        background-color: #0056b3;
    }

    .action-button {
        cursor: pointer;
        font-size: 20px;
        margin: 0 5px;
    }

    .action-button.approve {
        color: green;
    }

    .action-button.deny {
        color: red;
    }

    h1 {
        font-style: italic;
        font-size: 36px;
        text-align: center;
    }

    .sidebar h2 {
        font-size: 24px;
        margin-bottom: 10px;
    }

    .sidebar ul {
        list-style: none;
        padding: 0;
    }

    .sidebar li {
        margin-bottom: 10px;
        font-size: 18px;
    }

    .sidebar li strong {
        display: block;
        margin-top: 4px;
        font-size: 14px;
        color: #555;
    }
</style>

<Navbar />

<div class="container">
    <div class="content">
        <h1>"företagsnamn" projekt</h1>
        <div class="project-grid">
            {#each projects as project}
                <div class="project-card" on:click={() => openPopup(project)}>
                    <p>{project}</p>
                </div>
            {/each}
        </div>
    </div>

    <div class="sidebar">
        <h2>Intressen</h2>
        <ul>
            {#each projects as project}
                <li>
                    {project}
                    <strong>{getInterestCount(project)} intresserade</strong>
                </li>
            {/each}
        </ul>
    </div>
</div>

{#if showPopup}
    <div class="overlay" on:click={closePopup}></div>
    <div class="popup">
        <div class="popup-header">
            <h2>{selectedProject}</h2>
            <p>{getInterestCount(selectedProject)}/{projectApplicants[selectedProject].length}</p>
        </div>
        {#each projectApplicants[selectedProject] as applicant, index}
            <div 
                class="applicant {applicant.accepted ? 'accepted' : ''}"
            >
                <div>
                    <strong>{applicant.name}</strong>
                    <p>{applicant.school}</p>
                </div>
                <div>
                    <span
                        class="action-button approve"
                        on:click={() => acceptApplicant(index)}
                    >
                        ✔
                    </span>
                    <span
                        class="action-button deny"
                        on:click={() => removeApplicant(index)}
                    >
                        ✘
                    </span>
                </div>
            </div>
        {/each}
        <button class="close-button" on:click={closePopup}>Stäng</button>
    </div>
{/if}
