from mamba import description, context, it
from expects import expect, equal


def split_street(fire):
    return fire.split('Y')

def split_fire(section, w):
    return len([section[i:i+w] for i in range(0, len(section), w)])

def waterbombs(fire, w):
    splitted_street = split_street(fire)
    waterbombs=0
    for section in splitted_street:
        waterbombs = waterbombs + split_fire(section, w)
    return waterbombs


with description("Aerial Firefighter"):
    with context("having NO fire"):
        with context("and no buildings"):
            with context("and width equal 1"):
                with it("extinghishes the fire"):
                    result = waterbombs("", 1)

                    expect(result).to(equal(0))

    with context("having 1 fire"):
        with context("and no buildings"):
            with context("and width equal 1"):
                with it("extinghishes the fire"):
                    result = waterbombs("x", 1)

                    expect(result).to(equal(1))

    with context("having 2 fires"):
        with context("and no buildings"):
            with context("and width equal 1"):
                with it("extinghishes the fire"):
                    result = waterbombs("xx", 1)

                    expect(result).to(equal(2))

            with context("and width equal 2"):
                with it("extinghishes the fire"):
                    result = waterbombs("xx", 2)

                    expect(result).to(equal(1))

    with context("having 6 fires"):
        with context("and two buildings"):
            with context("and width equal 4"):
                with it("extinghishes the fire"):
                    result = waterbombs("xxxxYxYx", 4)

                    expect(result).to(equal(3))
