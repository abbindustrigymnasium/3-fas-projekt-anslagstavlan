<script>
	import { Section, News, HeroHeader, HeroBody } from 'flowbite-svelte-blocks';
	import { Button } from 'flowbite-svelte';
	import { ArrowRightOutline } from 'flowbite-svelte-icons';
</script>

<div class="h-screen flex-grow flex justify-center items-center">
  <div class="flex w-full flex-grow flex-row items-center justify-center">
    <HeroHeader
      h1Class=" mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl dark:text-dark"
      pClass="max-w-2xl mb-6 font-light text-gray-500 lg:mb-8 md:text-lg lg:text-xl dark:text-gray-400"
    >
      <svelte:fragment slot="h1">Från förslag till verklighet</svelte:fragment>
      <svelte:fragment slot="paragraph"
        >Anslagstavlan är en plattform där företag delar idéer och projekt som elever kan ta sig an.
        Här skapas nya möjligheter för lärande, kreativitet och samarbete. En mötesplats för
        framtidens innovation!</svelte:fragment
      >
      <a href="/login"
        ><Button size="xl" color="red" class="mr-3 inline-flex items-center justify-center"
          >Get started<ArrowRightOutline size="md" class="-mr-1 ml-2" /></Button
        >
      </a>
      <a href="/"
        ><Button color="light" size="xl" class="inline-flex items-center justify-center"
          >Speak to Sales</Button
        >
      </a>
    </HeroHeader>
  
    <img src="Logo.svg" class="size-48" alt="mockup" />
  </div>
</div>
