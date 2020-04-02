from abc import ABC, abstractmethod


class SelfDrivingVehicle(ABC):

    def driveToDestionation(self) -> None:
        self.steer()
        self.accelerate()
        self.brake()
        self.reachDestionation()

    def reachDestionation(self) -> None:
        print("Made it to destination")


    @abstractmethod
    def steer(self) -> None:
        pass

    @abstractmethod
    def brake(self) -> None:
        pass

    @abstractmethod
    def accelerate(self) -> None:
        pass


class SelfDrivingMotorcycle(SelfDrivingVehicle):

    def accelerate(self) -> None:
        print("twist the throttle")

    def steer(self) -> None:
        print("Turning handlebars")

    def brake(self) -> None:
        print("Pull brake levers")


class SelfDrivingCar(SelfDrivingVehicle):

    def accelerate(self) -> None:
        print("push the accelerating pedal")

    def steer(self) -> None:
        print("Turning steering wheel")

    def brake(self) -> None:
        print("Pull brake pedal")


SelfDrivingMotorcycle().driveToDestionation()
print()
SelfDrivingCar().driveToDestionation()
