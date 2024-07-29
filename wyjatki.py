# Zadanie 1
class CinemaHall:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = {chr(65 + r): ['O'] * seats_per_row for r in range(rows)}
        self.reservations = {}

    def print_seats(self):
        for row, seats in self.seats.items():
            print(row, ' '.join(seats))
        print()

    def reserve_seat(self, seat, user):
        row = seat[0]
        col = int(seat[1:]) - 1

        # Jeśli na seans nie ma już miejsc, zgłoś wyjątek
        if not any('O' in s for s in self.seats.values()):
            raise NoAvailableSeatsError("Brak wolnych miejsc.")

        # Jeśli użytkownik próbuje zarezerwować miejsce, które już jest zarezerwowane, zgłoś wyjątek
        if self.seats[row][col] != 'O':
            raise SeatAlreadyReservedError("To miejsce jest już zarezerwowane.")

        # Jeśli ten sam użytkownik próbuje ponownie zarezerwować miejsce, zgłoś wyjątek
        if user in self.reservations.values():
            raise UserAlreadyReservedError("Ten użytkownik ma już zarezerwowane miejsce.")

        # W przeciwnym razie zarezerwuj miejsce
        self.seats[row][col] = 'X'
        self.reservations[seat] = user
        print(f"Miejsce {seat} zostało zarezerwowane dla użytkownika {user}.")

    def cancel_reservation(self, seat, user):
        row = seat[0]
        col = int(seat[1:]) - 1

        # Jeśli zgadza się numer miejsca oraz użytkownik, anuluj rezerwację
        if self.seats[row][col] == 'X' and self.reservations.get(seat) == user:
            self.seats[row][col] = 'O'
            del self.reservations[seat]
            print(f"Rezerwacja miejsca {seat} dla użytkownika {user} została anulowana.")
        else:
            # W każdym innym przypadku, zgłoś wyjątek
            raise InvalidCancellationError("Nie możesz anulować tej rezerwacji.")

class SeatAlreadyReservedError(Exception):
    pass

class UserAlreadyReservedError(Exception):
    pass

class NoAvailableSeatsError(Exception):
    pass

class InvalidCancellationError(Exception):
    pass

# Przykładowe użycie:
hall = CinemaHall(5, 10)
hall.print_seats()

hall.reserve_seat("A2", "Mateusz M")  
hall.reserve_seat("A2", "Mateusz N"")  
hall.reserve_seat("B3", "Mateusz O") 

hall.print_seats()

hall.cancel_reservation("A2", "Mateusz M")  # Anulowanie rezerwacji
hall.cancel_reservation("B3", "Mateusz O")  # Powinien wyświetlić komunikat o błędzie

hall.print_seats()