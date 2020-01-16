import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)




@pytest.fixture(scope="function")
def calculator():
    return Calculator()


@pytest.mark.parametrize(
                        ["operator",
                        "arg1",
                        "arg2",
                        "expected"],
                       [("+",0,1,1),
                        ("-",2,3,-1),
                        ("*",1,2,2),
                        ("/",3,1,3)
                        ])
def test_run_fun(operator, arg1, arg2, expected, calculator):
    result = calculator.run(operator, arg1, arg2)
    assert result == expected


@pytest.mark.parametrize(
                        ["operator",
                        "arg1",
                        "arg2",
                        "expected"],
                        [("%",0,1,WrongOperation),
                        ("-",".","i",NotNumberArgument),
                        ("-",1,"i",NotNumberArgument),
                        ("-","f",2,NotNumberArgument),
                        ("/",1,0,CalculatorError),
                        ("/", 7, None, EmptyMemory)
                        ])
def test_run_exep(operator, arg1, arg2, expected, calculator):
    with pytest.raises(expected):
        calculator.run(operator, arg1, arg2)


