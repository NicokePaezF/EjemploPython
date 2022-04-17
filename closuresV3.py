def make_division_by(n):
    def division(numero):
        assert type(numero) == int, "El ingreso debe ser sólo número."
        return numero / n

    return division


def run():
    div_3 = make_division_by(3)
    print(div_3(18))


if __name__ == '__main__':
    run()
