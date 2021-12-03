from django.http import HttpResponse

from .models import Member, Address, Vehicle


# Create your views here.
def get_all(request):
    members = Member.objects.all()
    response = HttpResponse()
    response.writelines('Members')
    response.writelines('<br/>')
    for member in members:
        data = member.__str__()
        response.writelines(data)
        response.writelines('<br/>')
    response.writelines(f'Total member: {len(members)}')
    return response


def insert_member_dummy(request):
    # create address
    try:
        address = Address.objects.get(district="12")
    except Address.DoesNotExist:
        address = Address.objects.create(district="12", address="Quang Trung")
        address.save()

    try:
        vehicle = Vehicle.objects.get(vehicle_id="XX-XX-9999")
    except Vehicle.DoesNotExist:
        vehicle = Vehicle.objects.create(vehicle_id="XX-XX-9999", vehicle_type="bike")
        vehicle.save()

    # create member
    try:
        member = Member.objects.get(first_name="Huy")
    except Member.DoesNotExist:
        member = Member()
        member.last_name = "Tran"
        member.first_name = "Huy"
        member.address = address
        member.vehicle = vehicle
        member.save()
    response = HttpResponse()
    data = member.__str__()
    response.writelines(data)
    response.writelines('<br/>')
    return response
