import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import Generate from '@/pages/Generate.vue'

import Classes from '@/pages/class_pages/Classes.vue'
import ClassDetail from '@/pages/class_pages/ClassDetail.vue'
import ClassNew from '@/pages/class_pages/ClassNew.vue'

import Enums from '@/pages/enum_pages/Enums.vue'
import EnumDetail from '@/pages/enum_pages/EnumDetail.vue'
import EnumNew from '@/pages/enum_pages/EnumNew.vue'

import UseCases from '@/pages/usecase_pages/UseCases.vue'
import UseCaseDetail from '@/pages/usecase_pages/UseCaseDetail.vue'
import UseCaseNew from '@/pages/usecase_pages/UseCaseNew.vue'

import Actors from '@/pages/actor_pages/Actors.vue'
import ActorDetail from '@/pages/actor_pages/ActorDetail.vue'
import ActorNew from '@/pages/actor_pages/ActorNew.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', component: Home},
    {path: '/generate', component: Generate},
    {path: '/classes', component: Classes},
    {path: '/classes/:id', component: ClassDetail},
    {path: '/classes/new', component: ClassNew},
    // {path: '/classes/:id/update', component: ClassNew},
    {path: '/enums', component: Enums},
    {path: '/enums/:id', component: EnumDetail},
    {path: '/enums/new', component: EnumNew},
    {path: '/usecases', component: UseCases},
    {path: '/usecases/:id', component: UseCaseDetail},
    {path: '/usecases/new', component: UseCaseNew},
    {path: '/actors', component: Actors},
    {path: '/actors/:id', component: ActorDetail},
    {path: '/actors/new', component: ActorNew},
  ],
})

export default router
