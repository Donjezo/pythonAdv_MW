import streamlit as st

def kalkuloje(numer1, number2, operator):

    if operator=="mbledhe":
        rez=numer1 +number2
    elif operator =="zbtitje":
        rez =numer1-number2
    elif operator=="shumezim":
        rez = numer1*number2
    elif operator=="pjestim":
        try:
            rez=numer1/number2
        except ZeroDivisionError:
            rez="smundesh me pjestu me 0"
    return rez


def main():
    st.title("Kalkulatori")

    num1 = st.number_input("shenoje numrin e pare")

    num2 = st.number_input("shenoje numrin e dyte")

    operatori = st.radio("selektoje operatori",["mbledhe","zbtitje", "shumezim","pjestim"])

    rezultati = kalkuloje(num1,num2,operatori)
    st.write(rezultati)


if __name__ =="__main__":
    main()