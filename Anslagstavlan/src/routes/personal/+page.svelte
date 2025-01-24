<script lang="ts">
//Author Beni
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

</script>

<Navbar />
<div class="right-0 fixed h-full bg-gray-200 w-[50vh] flex flex-col pt-9">
	<div class="flex flex-col items-center justify-center">
		<h1 class="font-Inter  text-5xl">Ansökningar</h1>
</div>
</div>

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
