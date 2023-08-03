import utils
import read_csv
import charts

# data = [
#    {
#      'Country':'Colombia',
#      'Population':500
#    },
#    {
#      'Country':'Bolivia',
#      'POpulation':300
#    }
#  ]
def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data,country)
  
  if len(result) > 0:
    country = result[0]
    labels,values=utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels,values)
  labels,values = utils.get_world_percentages(data)
  charts.generate_pie_chart(country['Country/Territory'],labels,values)
    
  #print(result)

if __name__ == '__main__':
  run()