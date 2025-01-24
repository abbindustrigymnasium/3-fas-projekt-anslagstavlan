<script>
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
	import { Avatar, Dropdown, DropdownHeader, DropdownItem, DropdownDivider } from 'flowbite-svelte';
	var authenticated = false;
</script>

<Navbar class="justify-items-stretch">
	<NavBrand href="/">
		<img src="/LogoStor.svg" class="size-16" alt="Anslagstavla Logo" />
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white"
			>Anslagstavlan</span
		>
	</NavBrand>
	<div class="flex flex-row flex-wrap justify-center">
    <div class="flex flex-row items-center md:order-2 align-middle justify-center ">
      {#if authenticated}
        <Avatar id="user-drop" src="/Logo.svg" class="cursor-pointer" size="sm" />
      {:else}
        <a href="/login">Logga in</a>
      {/if}
      <NavHamburger class="w-full md:order-1 md:hidden md:w-auto" />
    </div>
      <Dropdown triggeredBy="#user-drop" class="">
        <DropdownHeader>
          <span class="block text-sm">Bonnie Green</span>
          <span class="block truncate text-sm font-medium">name@flowbite.com</span>
        </DropdownHeader>
        <DropdownItem href="/">Sign out</DropdownItem>
      </Dropdown>
    <NavUl>
      <NavLi href="/home">Hem</NavLi>
      <NavLi href="/personal">Personlig sida</NavLi>
      <NavLi href="/contact">Contact</NavLi>
    </NavUl>
  </div>
</Navbar>
