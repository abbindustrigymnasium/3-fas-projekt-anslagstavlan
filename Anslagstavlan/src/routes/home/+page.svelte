<script lang="ts">
    //Author Beni
    import Navbar from "../../components/Navbar.svelte";
    import { onMount } from 'svelte';
    import { Card, Button, GradientButton } from 'flowbite-svelte';
    import { ArrowRightOutline } from 'flowbite-svelte-icons';
    
    interface Project {
        id: number;
        isTaken: boolean;
        title: string;
        companyName: string;
        time: number;
        projectType: string;
        additionalInfo: string;
        contactPerson: string;
        canApply?: boolean; // Add this field
    }

    let user = {
        id: 1,
        name: "beni"
    }

    let projects: Project[] = [];
    let error: string | null = null;
    let selectedProject: Project | null = null;
    let showModal = false;
<<<<<<< Updated upstream

    // Function to update apply status for all projects
    async function updateApplyStatus() {
        const interests = await checkInterest();
        projects.forEach(project => {
            project.canApply = !interests.some((interest: any) => interest.project === project.id);
        });
        projects = [...projects]; // Trigger reactivity
    }

=======
    let filters = {
        status: {
            available: false,
            taken: false
        },
        types: {
            thesis: false,
            internship: false,
            project: false
        }
    };
    let showFilters = false;

    const toggleFilters = () => {
        showFilters = !showFilters;
    }
  
>>>>>>> Stashed changes
    onMount(async () => {
        try {
            const response = await fetch('api/data');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            projects = await response.json();
            await updateApplyStatus(); // Check interests on load
        } catch (err) {
            error = (err as Error).message;
            console.error('Failed to fetch projects:', err);
        }
        document.body.style.overflow = 'auto';
    });

    async function openModal(project: Project) {
        selectedProject = project;
        showModal = true;
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        showModal = false;
        selectedProject = null;
        document.body.style.overflow = 'auto';
    }

    async function checkInterest() {
        const response = await fetch(`api/check_interest?user=${user.id}`);
        return response.json();
    }

    async function apply(project: Project) {
        let headersList = {
            "Content-Type": "application/json"
        }

        let bodyContent = {
            "user": user.id,
            "project": project.id
        };

        let response = await fetch("/api/submit/apply", { 
            method: "POST",
            body: JSON.stringify(bodyContent),
            headers: headersList
        });

        let data = await response.text();
        console.log(data);
        await updateApplyStatus(); // Update status after applying
        closeModal();
    }
</script>


    <Navbar />
    <div class="flex flex-col h-full items-center justify-center mt-16 no-sc">
        <div class="flex flex-row items-center">
            <div class="w-[300px]">
                <h1 class="font-Inter font-extrabold text-5xl">Projekt</h1>
                <p class="italic">Utforska en rad olika företagsidéer och hitta inspiration för ditt nästa stora projekt!</p>
            </div>
            <img src="Penna.png" alt="penna">
        </div>

 

     
            <div class="bg-white p-4 rounded-lg shadow-md mb-4 transition-all duration-300">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <!-- Add your filter options here -->
                    <div class="form-control">
                        <label class="label">Kategori</label>
                        <select class="select select-bordered w-full">
                            <option value="">Alla Kategorier</option>
                            <option value="teknik">Teknik</option>
                            <option value="design">Design</option>
                            <option value="marknadsföring">Marknadsföring</option>
                            <option value="försäljning">Försäljning</option>
                       
                        </select>
                    </div>
                    
                    <div class="form-control">
                        <label class="label" for="time">Time</label>
                        <select id="status" class="select select-bordered w-full">
                            <option value="">Alla</option>
                            <option value="available">Under 20h</option>
                            <option value="taken">20 - 30h</option>
                            <option value="taken">30 - 40h</option>
                            <option value="taken">+40h</option>
                        </select>
                    </div>
                    <div class="form-control">
                        <label class="label" for="time">Företag</label>
                        <select id="status" class="select select-bordered w-full">
                            <option value="">Alla</option>
                            <!-- Hitta alla företag -->

                        </select>
                    </div>
                </div>
            </div>
       
    
        </div>
    
        {#if error}
            <p class="text-red-500">Error: {error}</p>
        {:else}
            <div class="grid grid-cols-3 gap-4 p-4 items-center">
                {#each projects as project}
                    <div class="bg-gray-100 p-4 rounded-lg">
                        <div class="w-full flex flex-col justify-between">
                            <div>
                                <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 line-clamp-1">{project.title}</h5>
    
                                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight line-clamp-2">{project.companyName}</p>
                                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight line-clamp-2">Typ: {project.projectType}</p>
                                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight line-clamp-2">Tid: {project.time} timmar</p>
                            </div>
                            <Button  color="light" class="w-fit mt-auto" on:click={() => openModal(project)}>
                                Read more <ArrowRightOutline class="w-6 h-6 ms-2 text-white" />
                            </Button>
                        </div>
                    </div>
                {/each}
            </div>
        {/if}
    
        {#if showModal && selectedProject}
            <button class="fixed inset-0 bg-black bg-opacity-50 backdrop-blur-sm flex items-center justify-center z-50 cursor-default" on:click={closeModal}>
                <div class="bg-white p-6 rounded-lg shadow-lg w-1/2 relative text-left" on:click|stopPropagation>
                    <a class="text-3xl  absolute top-2 right-5 text-gray-500 hover:text-gray-700 cursor-pointer" on:click={closeModal}>
                        &times;
                    </a>
                    <h2 class="text-2xl font-bold mb-4">{selectedProject.title}</h2>
                    <p class="mb-2"><strong>Company:</strong> {selectedProject.companyName}</p>
                    <p class="mb-2"><strong>Type:</strong> {selectedProject.projectType}</p>
                    <p class="mb-2"><strong>Time:</strong> {selectedProject.time} hours</p>
                    <p class="mb-2"><strong>Additional Info:</strong> {selectedProject.additionalInfo}</p>
                    <p class="mb-2"><strong>Contact:</strong> {selectedProject.contactPerson}</p>
                    <p class="mb-2"><strong>Status:</strong> {selectedProject.isTaken ? 'Taken' : 'Available'}</p>

                    <GradientButton
                        color={selectedProject.canApply ? "green" : "gray"}
                        size="xl"
                        class="absolute bottom-2 right-5"
                        disabled={!selectedProject.canApply}
                        on:click={() => selectedProject && selectedProject.canApply && apply(selectedProject)}
                    >
                        {selectedProject.canApply ? 'Ansök' : 'Ansökt'}
                    </GradientButton>
                </div>
                
            </button>
        {/if}
