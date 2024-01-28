from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ToDoList, ToDoItem
from .forms import ToDoItemForm, ToDoListForm


class ListListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

    permission_required = ('todo_list.view_todo_list',)
    permission_denied_message = "Você não tem permissão para listar TODO"

class ItemListView(LoginRequiredMixin, ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    permission_required = ('todo_item.view_item_list',)
    permission_denied_message = "Você não tem permissão para listar items"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
    
class ListCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ToDoList
    form_class = ToDoListForm

    permission_required = ('todo_list.add_list',)
    permission_denied_message = "Você não tem permissão para criar TODO"

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Adicionar nova lista"
        return context

class ItemCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ToDoItem
    form_class = ToDoItemForm
    
    permission_required = ('todo_item.add_item',)
    permission_denied_message = "Você não tem permissão para criar Item"

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ToDoItem
    form_class = ToDoItemForm

    permission_required = ('todo_item.change_item',)
    permission_denied_message = "Você não tem permissão para editar Item"

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])
    
class ListDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

    permission_required = ('todo_list.delete_todo_list')
    permission_denied_message = "Você não tem permissão para excluir TODO list"

class ItemDelete(DeleteView):
    model = ToDoItem

    permission_required = ('todo_item.delete_todo_item')
    permission_denied_message = "Você não tem permissão para excluir TODO item"

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context