<script lang="ts">
	import { Button, Card } from 'flowbite-svelte';
	import { createClient } from '@supabase/supabase-js';

	let registrationType = 'personal';
	let email = '';
	let password = '';

	const supabase = createClient(
		'https://viyiiculbbsxmsjmswiv.supabase.co',
		'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZpeWlpY3VsYmJzeG1zam1zd2l2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIwMTY0OTIsImV4cCI6MjA0NzU5MjQ5Mn0.gKrMsCWeUCfRRjk9lYSpgDXq_TTTTg_PHU2iF-U6_mg'
	);

	function handleSubmit(e: Event) {
		e.preventDefault();
		// Add form submission logic here
		console.log('Form submitted:', { registrationType, email, password });
	}

	async function handleMicrosoftSignIn() {
     const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'azure',
  options: {
    redirectTo: 'https://example.com/welcome'
  }
})

		console.log('Microsoft sign-in clicked');
	}
</script>

<div class="flex min-h-screen flex-col items-center justify-center bg-gray-50">
	<div class="w-[450px] rounded-lg border border-gray-200 bg-white p-8 shadow-md">
		<h1 class="mb-6 text-center text-3xl font-bold text-gray-900">Logga in</h1>

		<form class="space-y-4" on:submit={handleSubmit}>
			<div>
				<label for="registrationType" class="mb-2 block text-sm font-medium text-gray-900">
					Registreringstyp
				</label>
				<select
					id="registrationType"
					bind:value={registrationType}
					class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-blue-500 focus:ring-blue-500"
					required
				>
					<option value="personal">Personlig</option>
					<option value="lärare">Lärare</option>
					<option value="företag">Företag</option>
				</select>
			</div>

			{#if registrationType === 'företag'}
				<button
					type="button"
					on:click={handleMicrosoftSignIn}
					class="mt-4 flex w-full items-center justify-center gap-2 rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm font-medium text-gray-900 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
				>
					<svg class="h-5 w-5" viewBox="0 0 21 21" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M10 0H0V10H10V0Z" fill="#F25022" />
						<path d="M21 0H11V10H21V0Z" fill="#7FBA00" />
						<path d="M10 11H0V21H10V11Z" fill="#00A4EF" />
						<path d="M21 11H11V21H21V11Z" fill="#FFB900" />
					</svg>
					Logga in med Microsoft
				</button>
			{:else}
				<div>
					<label for="email" class="mb-2 block text-sm font-medium text-gray-900">Email</label>
					<input
						type="email"
						id="email"
						bind:value={email}
						class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-blue-500 focus:ring-blue-500"
						required
					/>
				</div>

				<div>
					<label for="password" class="mb-2 block text-sm font-medium text-gray-900">Lösenord</label
					>
					<input
						type="password"
						id="password"
						bind:value={password}
						class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-blue-500 focus:ring-blue-500"
						required
					/>
				</div>

				<Button type="submit" class="w-full" href="/home"><p class="text-black">Logga in</p></Button
				>
			{/if}
		</form>
	</div>
</div>
