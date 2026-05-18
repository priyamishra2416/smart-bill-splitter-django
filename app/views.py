from django.shortcuts import render, redirect
from .models import Friend, Expense

def home(request):

    search = request.GET.get('search')

    expenses = Expense.objects.all().order_by('-created_at')

    if search:

        expenses = expenses.filter(
            title__icontains=search
        )


    # Dashboard Summary

    total_expenses = Expense.objects.count()

    total_friends = Friend.objects.count()

    total_amount = 0

    for expense in expenses:

        total_amount += expense.amount


    # Who Owes Whom Logic

    owes_data = []

    for expense in expenses:

        split = expense.split_amount()

        for person in expense.participants.all():

            if person != expense.paid_by:

                owes_data.append({

                    'person': person.name,

                    'paid_to': expense.paid_by.name,

                    'amount': split

                })


    context = {

        'expenses': expenses,

        'total_expenses': total_expenses,

        'total_friends': total_friends,

        'total_amount': total_amount,

        'owes_data': owes_data

    }

    return render(
        request,
        'app/home.html',
        context
    )


def add_friend(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        Friend.objects.create(name=name)

        return redirect('home')

    return render(
        request,
        'app/add_friend.html'
    )


def add_expense(request):

    friends = Friend.objects.all()

    if request.method == 'POST':

        title = request.POST.get('title')

        amount = request.POST.get('amount')

        paid_by_id = request.POST.get('paid_by')

        participants = request.POST.getlist(
            'participants'
        )

        paid_by = Friend.objects.get(
            id=paid_by_id
        )

        expense = Expense.objects.create(
            title=title,
            amount=amount,
            paid_by=paid_by
        )

        expense.participants.set(
            participants
        )

        return redirect('home')

    context = {
        'friends': friends
    }

    return render(
        request,
        'app/add_expense.html',
        context
    )
def delete_expense(request, id):

    expense = Expense.objects.get(id=id)

    expense.delete()

    return redirect('home')


def update_expense(request, id):

    expense = Expense.objects.get(id=id)

    friends = Friend.objects.all()

    if request.method == 'POST':

        expense.title = request.POST.get('title')

        expense.amount = request.POST.get('amount')

        paid_by_id = request.POST.get('paid_by')

        expense.paid_by = Friend.objects.get(
            id=paid_by_id
        )

        participants = request.POST.getlist(
            'participants'
        )

        expense.save()

        expense.participants.set(
            participants
        )

        return redirect('home')

    context = {
        'expense': expense,
        'friends': friends
    }

    return render(
        request,
        'app/update_expense.html',
        context
    )