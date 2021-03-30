from rest_framework import routers
from employee_api.viewset import EmployeeViewset

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)