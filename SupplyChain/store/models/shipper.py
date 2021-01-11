from django.db import models

class Shipping_Route(models.Model):
    From = models.CharField(max_length=15) 
    To = models.CharField(max_length=15)
    Days = models.IntegerField()

    @staticmethod
    def get_days(from_city, address):

        city_no = {
            'Jammu': 0,
            'Delhi': 1,
            'Mumbai': 2,
            'Bangalore': 3,
            'Chennai': 4,
            'Andaman': 5,
            'Hyderabad': 6,
            'Kanpur': 7,
            'Patna': 8,
            'Guwahati': 9,
            'Nagpur': 10,
        }

        objs = Shipping_Route.objects.all()

        class Graph:  
  
            def __init__(self, vertices):  
                self.V = vertices 
                self.graph = []  

            def addEdge(self, u, v, w):  
                self.graph.append([u, v, w])  
      
            def BellmanFord(self, src):  
                
                dist = [float("Inf")] * self.V  
                dist[src] = 0
        
                for _ in range(self.V - 1):   
                    for u, v, w in self.graph:  
                        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                                print("u ",u)  
                                dist[v] = dist[u] + w  

                for u, v, w in self.graph:  
                        if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                                print("Graph contains negative weight cycle") 
                                return False
                                
                return dist[city_no[address]]
    
        g = Graph(11)  
        
        for obj in objs:
             g.addEdge(city_no[obj.From], city_no[obj.To], obj.Days) 

        return g.BellmanFord(city_no[from_city])   
