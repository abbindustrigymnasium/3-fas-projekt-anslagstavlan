<script lang="ts">
import Navbar from "../../components/Navbar.svelte";
import { onMount } from 'svelte';  
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
        id: 2,
        name: "beni"
    }
let projects: Project[] = [];
let error: string | null = null;
let selectedProject: Project | null = null;
let loading = true;

<<<<<<< Updated upstream
onMount(async () => {
    loading = true;
    try {
        const response = await fetch(`/api/user_projects?user=${user.id}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        projects = await response.json();
    } catch (err) {
        error = (err as Error).message;
        console.error('Failed to fetch projects:', err);
    } finally {
        loading = false;
    }
});
=======
	let projects: Project[] = [];
	let error: string | null = null;
	let selectedProject: Project | null = null;
	let loading = true;
	let isModalOpen = false;

	function openProjectModal(project: Project) {
		selectedProject = project;
		isModalOpen = true;
	}

	function closeModal() {
		isModalOpen = false;
		selectedProject = null;
	}
>>>>>>> Stashed changes

</script>

<Navbar />
<div class="right-0 fixed h-full bg-gray-200 w-[50vh] flex flex-col pt-9">
	<div class="flex flex-col items-center justify-center">
		<h1 class="font-Inter  text-5xl">Ansökningar</h1>
</div>
</div>

<<<<<<< Updated upstream
<div class="p-4">
    {#if loading}
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {#each Array(6) as _}
                <div class="bg-white rounded-lg border border-gray-200 shadow-sm p-5 animate-pulse">
                    <div class="h-4 bg-gray-200 rounded w-3/4 mb-4"></div>
                    <div class="h-3 bg-gray-200 rounded w-full mb-2"></div>
                    <div class="h-3 bg-gray-200 rounded w-2/3"></div>
                </div>
            {/each}
        </div>
    {:else if projects.length > 0}
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
            {#each projects as project}
                <div class="bg-white rounded-lg border border-gray-200 shadow-sm hover:shadow-md transition-shadow">
                    <div class="p-5">
                        <h5 class="mb-3 text-xl font-bold tracking-tight text-gray-900">
                            {project.title}
                        </h5>
                        <p class="text-gray-600">
                            {project.additionalInfo}
                        </p>
                    </div>
                </div>
            {/each}
        </div>
    {:else}
        <p class="text-center text-gray-600">No projects available</p>
    {/if}
</div>
=======
<div class="p-16">
	{#if loading}
		<div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3 ">
			{#each Array(6) as _}
				<div class="animate-pulse rounded-lg border border-gray-200 bg-white p-5 shadow-sm">
					<div class="mb-4 h-4 w-3/4 rounded bg-gray-200"></div>
					<div class="mb-2 h-3 w-full rounded bg-gray-200"></div>
					<div class="h-3 w-2/3 rounded bg-gray-200"></div>
				</div>
			{/each}
		</div>
	{:else if projects.length > 0}
	
			<div class="">
				<p class="text-4xl pb-9 font-bold">Aktiva projekt</p>
				<div class="grid gap-4 md:grid-cols-2 lg:grid-cols-2 w-fit">
					{#each projects as project (project.id)}
						<div
							class="rounded-lg border border-gray-200 bg-white p-5 shadow-sm cursor-pointer hover:shadow-md transition-shadow"
							on:click={() => openProjectModal(project)}
						>
							<h5 class="mb-3 text-xl font-bold tracking-tight text-gray-900">
								{project.title}
							</h5>
							<p class="text-gray-600">
								{project.additionalInfo}
							</p>
						</div>
					{/each}
					
				</div>
		
				
		</div>
	{:else}
		<p class="text-center text-gray-600">No projects available</p>
	{/if}
	
	{#if isModalOpen && selectedProject}
		<div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div class="bg-white p-8 rounded-lg shadow-xl max-w-2xl w-full m-4">
				<div class="flex justify-between items-center mb-4">
					<h2 class="text-2xl font-bold">{selectedProject.title}</h2>
					<button on:click={closeModal} class="text-gray-500 hover:text-gray-700">
						✕
					</button>
				</div>
				<div class="space-y-4">
					<p><strong>Company:</strong> {selectedProject.companyName}</p>
					<p><strong>Time:</strong> {selectedProject.time} hours</p>
					<p><strong>Project Type:</strong> {selectedProject.projectType}</p>
					<p><strong>Contact:</strong> {selectedProject.contactPerson}</p>
					<p><strong>Additional Info:</strong> {selectedProject.additionalInfo}</p>
				</div>
			</div>
		</div>
	{/if}
</div>
>>>>>>> Stashed changes
