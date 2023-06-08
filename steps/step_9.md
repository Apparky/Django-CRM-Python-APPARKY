## Step 9:
Let's set up `Delete` and `Update` section

Go to `crm/views.py` and create function for the same as this
```commandline
def delete_cst(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()

        messages.success(request, 'Records has been deleted Successfully')
        return redirect('home')

    else:
        messages.error(request, 'Something went Wrong..!!')
        return redirect('home')


def update_cst(request, pk):
    if request.user.is_authenticated:
        the_record = Record.objects.get(id=pk)
        datas = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=the_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update.html', {'form': form})

    else:
        messages.error(request, 'Something went Wrong....!!')
        return redirect('home')


```

Go to `cmr/urls.py` to create ulr for the same like this :
```commandline
path('delete/<int:pk>', views.delete_cst, name='delete'),
path('update/<int:pk>', views.update_cst, name='update'),
```

Now create `update.html` in `templates` directory. The code for that is given billow :
```commandline
{% extends 'base.html' %}

{% block body %}
<div class="col-md-6 offset-md-3">
    <h1>Update Record</h1>
    <br/>
    
    <form method="POST">
        {% csrf_token %}
    
        {{ form.as_p }}
    
    <br/>
      <button type="submit" class="btn btn-danger">Update Record</button>
        
      <a href="{% url 'home' %}" class="btn btn-secondary">Back</a>

    
    </form>
    
    
    </div>
    
{% endblock body %}
```

This is how it looks like..

![DjangoUpdate](../ss/ss10.PNG)

The url for that is [http://localhost/update/1](http://localhost/update/1) .

On pressing `Delete` button, the web page will look like this.

![DjangoDelete](../ss/ss11.PNG)


