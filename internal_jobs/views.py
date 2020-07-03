from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, _get_queryset
from django.views.decorators.http import require_POST

from .forms import JobRequirementForm, JobApplicantForm
from .models import JobRequirement, JobApplicant


@login_required(login_url='login')
def requirement_list(request):
    requirements = JobRequirement.objects.all()
    return render(request, "internal_jobs/requirement_list.html", {"requirements": requirements})


@login_required(login_url='login')
def requirement_create(request):
    if request.method == "POST":
        requirement_form = JobRequirementForm(request.POST)
        if requirement_form.is_valid():
            requirement_form.save()
            return redirect("jobs:jobs")
    else:
        requirement_form = JobRequirementForm()
    return render(request, "internal_jobs/create.html", {"requirement_form": requirement_form})


@login_required(login_url='login')
def requirement_edit(request, id):
    jobs = get_object_or_404(JobRequirement, pk=id)
    if request.method == "POST":
        jobs_form = JobRequirementForm(request.POST, instance=jobs)
        if jobs_form.is_valid():
            jobs_form.save()
            return redirect("jobs:jobs")
        else:
            jobs_form = JobRequirementForm(instance=jobs)
            return render(request, "internal_jobs/edit.html", {"requirement_form": jobs_form})
    else:
        jobs_form = JobRequirementForm(instance=jobs)
        return render(request, "internal_jobs/edit.html", {"requirement_form": jobs_form})


@login_required(login_url='login')
def requirement_details(request, id):
    job = get_object_or_404(JobRequirement, pk=id)
    return render(request, "internal_jobs/details.html", {"job": job})


@login_required(login_url='login')
def requirement_delete(request, id):
    job_id = int(id)
    try:
        job_sel = get_object_or_404(JobRequirement, pk=job_id)
    except JobRequirement.DoesNotExist:
        return redirect('jobs:jobs')
    job_sel.delete()
    return redirect('jobs:jobs')


@login_required(login_url='login')
def display_job_applications(request):
    job_applications = JobApplicant.objects.all()
    return render(request, "internal_jobs/job_applications.html", {"job_applications": job_applications})


@login_required(login_url='login')
def create_applicant(request):
    if request.method == "POST":
        job_form = JobApplicantForm(request.POST)
        if job_form.is_valid():
            job_form.save()
            return redirect("jobs:job_applications")
    else:
        job_form = JobApplicantForm()
    return render(request, "internal_jobs/create_applicant.html", {"job_form": job_form})


@login_required(login_url='login')
def edit_applicant(request, id):
    applicant = get_object_or_404(JobApplicant, pk=id)
    if request.method == "POST":
        job_form = JobApplicantForm(request.POST, instance=applicant)
        if job_form.is_valid():
            job_form.save()
            return redirect("jobs:jobs")
        else:
            job_form = JobApplicantForm(instance=applicant)
            return render(request, "internal_jobs/edit_applicant.html", {"job_form": job_form})
    else:
        job_form = JobApplicantForm(instance=applicant)
        return render(request, "internal_jobs/edit_applicant.html", {"job_form": job_form})


@login_required(login_url='login')
def delete_applicant(request):
    return render(request, "requirements/job_applications.html")


def apply_to_job(request, request_id):
    if request.method == "POST":
        job_form = JobApplicantForm(request.POST)
        if job_form.is_valid():
            job_form.save()
            return redirect("jobs:job_applications")
    else:
        job_form = JobApplicantForm()
    return render(request, "internal_jobs/create_applicant.html", {"job_form": job_form})


def job_reports(request):
    return render(request, "internal_jobs/reports.html")
