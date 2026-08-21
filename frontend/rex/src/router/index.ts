import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import Generate from '@/pages/Generate.vue'
import Export from '@/pages/Export.vue'
import Markdown from '@/pages/Markdown.vue'

import Classes from '@/pages/class_pages/Classes.vue'
import ClassDetail from '@/pages/class_pages/ClassDetail.vue'

import UseCases from '@/pages/usecase_pages/UseCases.vue'
import UseCaseDetail from '@/pages/usecase_pages/UseCaseDetail.vue'

import DomainNarrative from '@/pages/DomainNarrative.vue'
import Requirements from '@/pages/Requirements.vue'

import Actors from '@/pages/Actors.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', component: Home},
    {path: '/generate', component: Generate},
    {path: '/json_data', component: Export},
    {path: '/markdown', component: Markdown},
    {path: '/classes', component: Classes},
    {path: '/classes/:id', component: ClassDetail},
    {path: '/usecases', component: UseCases},
    {path: '/usecases/:id', component: UseCaseDetail},
    {path: '/actors', component: Actors},
    {path: '/requirements', component: Requirements},
    {path: '/narrative', component: DomainNarrative},
  ],
})

export default router
