<template>
	<div class="col-4">
		<div class="h-100 card">
			<b-img :src="preview" class='w-100 card-img-top'></b-img>
			<div class="card-body">
				<h2 class="card-title">{{title}}</h2>
				<a :href="'/projects/' + id" class="btn btn-primary text-white">Подробнее</a>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'ProjectItem',
	props: ['id', 'title', 'preview', 'description', 'project_url', 'code_url']
}
</script>

<style>

</style>
