def petrol_countries_build(country):
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    url = "https://countryeconomy.com/energy/prices-gasoline-gas-oil-heating/{}".format(country)
    country_data = requests.get(url)
    soup = BeautifulSoup(country_data.text, 'lxml')
    numbers = soup.find('div', {'class': "table-responsive"})
    df = pd.read_html(str(numbers))
    df = pd.DataFrame(df[0])
    df.to_excel('petrolpricesof{}2.xlsx'.format(country))
def building_petrol_dates(country):
    import pandas as pd
    petrol_data=pd.read_excel(r'C:\Users\Batu1\PycharmProjects\pythonProject1\Quizzes\OOP\project4_petrol\petrolpricesof{}.xlsx'.format(country))
    dates=petrol_data["Date"].tolist() #tarıhler ıcın ayrı bır lıste olusturdum
    del dates[-1] # sondakı eleman 2022ye don dıye gosterıyordu
    return dates
def building_gas_oil_prices(country):
    import pandas as pd
    petrol_data=pd.read_excel(r'C:\Users\Batu1\PycharmProjects\pythonProject1\Quizzes\OOP\project4_petrol\petrolpricesof{}.xlsx'.format(country))
    gas_oil=petrol_data["Gas oil"].tolist()
    del gas_oil[-1]
    return gas_oil
def building_super_95_prices(country):
    import pandas as pd
    petrol_data = pd.read_excel(r'C:\Users\Batu1\PycharmProjects\pythonProject1\Quizzes\OOP\project4_petrol\petrolpricesof{}.xlsx'.format(country))
    super_95=petrol_data["Super 95"].tolist()
    del super_95[-1]
    return super_95
def building_graph(petrol_type,dates):
    import matplotlib.pyplot as plt
    petrol_price=[]
    for i in petrol_type:   #€ işaretini yok etmek ıcın yapıldı cunku grafıkte karsılastırma yapılamayıp yanlıs graphn draw edılıyorudu
        p=list(i)
        e = ''.join(p[1:6])   #1. sattırdan 6.satıra kadar olan elemanları yanyana getiriyor
        c=float(e)
        print(c)
        petrol_price.append(c)
    print(petrol_price)
    plt.plot(dates,petrol_price,marker="*",markersize=15,color='red')
    # naming the x axis
    plt.ylabel('Prices')
    # naming the y axis
    plt.xlabel('Date')
    plt.xticks(rotation=90)
    # giving a title to my graph
    plt.title('Change of prices')
    # function to show the plot
    plt.show()
def building_graph_all(petrol_type,petrol_type_2,dates):
    import matplotlib.pyplot as plt
    petrol_price=[]
    for i in petrol_type:   #€ işaretini yok etmek ıcın yapıldı cunku grafıkte karsılastırma yapılamayıp yanlıs graphn draw edılıyorudu
        p=list(i)
        e = ''.join(p[1:6])   #1. sattırdan 6.satıra kadar olan elemanları yanyana getiriyor
        c=float(e)
        print(c)
        petrol_price.append(c)
    petrol_price_2=[]
    for i in petrol_type_2:   #€ işaretini yok etmek ıcın yapıldı cunku grafıkte karsılastırma yapılamayıp yanlıs graphn draw edılıyorudu
        d=list(i)
        f = ''.join(d[1:6])   #1. sattırdan 6.satıra kadar olan elemanları yanyana getiriyor
        k=float(f)
        print(k)
        petrol_price_2.append(k)
    plt.subplot(1,2,1)
    plt.xticks(rotation=90)
    plt.plot(dates,petrol_price,marker=".",markersize=15,color='magenta')
    plt.subplot(1,2,2)
    plt.xticks(rotation=90)
    plt.plot(dates,petrol_price_2,marker=".",markersize=15,color='green')
    plt.show()