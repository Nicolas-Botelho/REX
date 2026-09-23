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
import Project from '@/pages/Project.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', component: Home},
    {path: '/project/:p_id', component: Project},
    {path: '/project/:p_id/generate', component: Generate},
    {path: '/project/:p_id/json_data', component: Export},
    {path: '/project/:p_id/markdown', component: Markdown},
    {path: '/project/:p_id/classes', component: Classes},
    {path: '/project/:p_id/classes/:id', component: ClassDetail},
    {path: '/project/:p_id/usecases', component: UseCases},
    {path: '/project/:p_id/usecases/:id', component: UseCaseDetail},
    {path: '/project/:p_id/requirements', component: Requirements},
    {path: '/project/:p_id/narrative', component: DomainNarrative},
  ],
})

export default router
