
class Vertex(object):
	def __init__(self,label):
		self._label=label

	def __str__(self):
		output='%s' % (self._label)
		return output

	def element(self):
		return self._label


class Edge(object):
	def __init__(self, vertex1,vertex2,weight):
		self._weight=weight
		self._vertex1=vertex1
		self._vertex2=vertex2
		self._vertices=(vertex1,vertex2)

	def __str__(self):
		output='%s %s %s'%(self._vertex1,self._vertex2,self._weight)
		return output

	def vertices(self):
		return self._vertex1,self._vertex2

	def opposite(self,x):
		if self._vertex1==x:
			return self._vertex2
		elif self._vertex2==x:
			return self._vertex1
		else:
			return None


	def weight(self):
		return self._weight
class Graph(object):
	def __init__(self):
		self._dic={}
		self._edgeList=[]
	def __str__(self):
		return str(self._dic)

	def vertices(self):
		return self._dic.keys()

	def edges(self):
		return self._edgeList

	def num_vertices(self):
		return len(self._dic.keys())

	def num_edges(self):
		return len(self._edgeList)

	def get_edge(self,x,y):
		return self._dic[x][y]

	def degree(self,x):
		return len(self._dic[x])

	def get_edges(self,x):
		return self._dic[x].values()

	def add_vertex(self,elt):
		elt=Vertex(elt)
		if elt.element() not in self._dic:
			self._dic[elt.element()]={}

	def add_edge(self,x,y,elt):
		elt=Edge(x,y,elt)
		self._edgeList.append(elt)
		for item in elt.vertices():
			#print(item,' opposite = ',elt.opposite(item))
			self._dic[item][elt.opposite(item)]=elt

	def remove_vertex(self,x):
		for item in self.get_edges(x):
			print(item)
			print(self._edgeList)
			self._edgeList.remove(item)
		self._dic.pop(x)
		#self._dic.pop(x)
		for item in self._dic:
			try:
				self._dic[item].pop(x)
			except KeyError:
				pass #Not in dictionary

	def remove_edge(self,e):
		self._edgeList.remove(e)
		for item in self._dic:
			for this in self._dic[item]:
				if self._dic[item][this]==e:
					self._dic[item].pop(this)
					break

	def max_degrees(self):
		state=''
		most=0
		for item in self._dic:
			if len(self._dic[item])>most:
				most=len(self._dic[item])
				state=item
		return state,most

	def get_vertex_by_label(self,element):
		for v in self._dic:
			if v.element()==element:
				return v
		return None

	def depthfirstsearch(self,v):
		marked={v:None}
		self._depthfirstsearch(v,marked)
		return marked

	def _depthfirstsearch(self,v,marked):
		for e in self.get_edges(v):
			w=e.opposite(v)
			if w not in marked:
				marked[w]=e
				self._depthfirstsearch(w,marked)

	def breadthfirstsearch(self,v):
		marked={v:None}
		level=[v]
		hops=0
		#print('\n')
		while len(level)>0:
			nextlevel=[]
			#print(hops,level)
			hops+=1
			for w in level:
				for e in self.get_edges(w):
					x=e.opposite(w)
					if x not in marked:
						marked[x]=(hops,w)#e
						nextlevel.append(x)
			level=nextlevel
		#print('here:')
		return marked

	def breadthfirst(self,dic):
		print(dic)
		for item in dic:
			print(dic[item])
			#return dic[item]


	def path(self,tree):
		for item in self.vertices():
			if tree[item]==None:
				root=item
		for item in self.vertices():
			asscend=item
			l=[asscend]
			while asscend!=root:
				asscend=tree[asscend][1]
				l.append(asscend)
			l.reverse()
			distance=tree[item]
			if distance!=None:
				distance=distance[0]
			print(item, ' : ',l,' Distance: ',distance)

	def central(self):
		l=[]
		for item in self.vertices():
			print(item)
			dic=self.breadthfirstsearch(item)
			print(dic)
			max=(0,'')
			for vertex in dic:
				#print(item,dic[item])
				if dic[vertex]!=None:
					if dic[vertex][0]>max[0]:
						max=(dic[vertex][0],item)
			l.append(max)
		central=min(l)
		print('Most central vertex:',central[1],'Distance of:',central[0])


class Element:
#A key, value and index.
	def __init__(self, k, v, i):
		self._key = k
		self._value = v
		self._index = i
	def __eq__(self, other):
		if self._key:
			return self._key == other._key
		return False
	def __lt__(self, other):
		return self._key < other._key
	def _wipe(self):
		self._key = None
		self._value = None
		self._index = None

class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0
		self.heapdic={}

	def __str__(self):
		l=[]
		for element in self.heapList:
			l.append(l)
		return str(l)

	def get_heap(self):
		for item in range(1,self.currentSize+1):
			print(self.heapList[item]._key,self.heapList[item]._value,self.heapList[item]._index)

	def percUp(self,i):
		while i // 2 > 0:
			if self.heapList[i]._key < self.heapList[i // 2]._key:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
				tmp1 = self.heapList[i // 2]._index
				self.heapList[i // 2]._index = self.heapList[i]._index
				self.heapList[i]._index = tmp1
			i = i // 2

	def insert(self,key,value):
		index=self.currentSize
		k = Element(key,value,index)
		self.heapdic[value]=k
		#print(k._index)
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)
		return k

	def percDown(self,i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i]._key > self.heapList[mc]._key:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
				tmp1 = self.heapList[i]._index
				self.heapList[i]._index = self.heapList[mc]._index
				self.heapList[mc]._index = tmp1
			i = mc

	def minChild(self,i):
		print(i)
		if i * 2 + 1 >= self.currentSize: #Changed to >=
			return i * 2
		else:
			if self.heapList[i*2]._key < self.heapList[i*2+1]._key:
				return i * 2
			else:
				return i * 2 + 1

	def delMin(self):
		minimum=self.min()
		last=self.heapList[self.currentSize]
		print('last',last._key)
		tmp = self.heapList[self.currentSize]
		self.heapList[self.currentSize]=minimum
		self.heapList[1]=tmp
		tmp1 = self.heapList[self.currentSize]._index
		self.heapList[self.currentSize]._index=minimum._index
		self.heapList[1]._index=tmp1
		removed=self.heapList.pop()
		self.currentSize-=1
		self.percDown(1)
		return removed

	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1

	def min(self):
		return self.heapList[1]


	def find(self,element):
		obj = self.heapdic[element]
		return obj #Todo: Edit delete

	def update_key(self,element,newkey):
		#print('\n')
		element=self.find(element)
		index=element._index+1
		#print('Indexed:',self.heapList[index]._value)
		self.heapList[index]._key=newkey
		#element._key=newkey
		#print(element._value,newkey)
		#print(self.heapList)
		self.percUp(index)
		self.percDown(index)

	def get_key(self,element):
		element=self.find(element)
		index=element._index+1
		return self.heapList[index]._key

	def remove(self,element):
		last=self.heapList[self.currentSize]
		print('last',last._key)
		tmp = self.heapList[self.currentSize]
		self.heapList[self.currentSize]=element
		self.heapList[1]=tmp
		tmp1 = self.heapList[self.currentSize]._index
		self.heapList[self.currentSize]._index=element._index
		self.heapList[1]._index=tmp1
		removed=self.heapList.pop()
		self.currentSize-=1
		self.percDown(1)
		return removed

def dijkstra(s):
	open=BinHeap()
	open.buildHeap([])
	locs={}
	closed={}
	preds={s:None}
	returned=open.insert(0,s)
	locs[s]=returned
	print('Open:')
	open.get_heap()	

	print('\nLocs:',locs)
	print('\nClosed', closed)
	print('\nPreds',preds)
	while open.currentSize>0:
		#remove the min element v and its cost (key) from open
		element=open.delMin()
		cost=element._key
		elt=element._value
		print(cost,elt)
		#remove the entry for v from locs and preds (which returns predecessor)
		print(locs.pop(elt))
		predecessor=preds.pop(elt)
		#add an entry for v :(cost, predecessor) into closed
		closed[elt]=(cost,predecessor)
		#for each edge e from v
		print('Edges:',graph.get_edges(elt))
		for edge in graph.get_edges(elt):
			#w is the opposite vertex to v in e
			opposite=edge.opposite(elt)
			print(opposite)
			#if w is not in closed
			if opposite not in closed:
				#print('Cost:',edge._weight)
				#newcost is v's key plus e's cost 
				newcost=cost+edge._weight
				print(newcost)
				if opposite not in locs:
					#preds[w]=v
					#open[w]=newcost
					#locs[w]=elt returned from open
					preds[opposite]=elt
					returned=open.insert(newcost,opposite)
					#open[opposite]=newcost
					locs[opposite]=returned
				
				#else if newcost is better than w's oldcost
				elif newcost<open.get_key(opposite):
					open.update_key(opposite,newcost)
					preds[opposite]=elt
					#update w:v in preds, update w's cost in open to newcost
	

	#print(returned)

	print('\nLocs:',locs)
	print('\nClosed', closed)
	print('\nPreds',preds)
	return closed


graph=Graph()
#graph.add_element('element1')
print(graph)


class RouteMap:
	def __init__(self):
		self._route_map={}

	def __str__(self):
		#return str(self._route_map)
		if graph.num_edges()>100 or graph.num_vertices()>100:
			return 'Graph to big to represent'
		else:
			return str(self._route_map)

	def add_vertex(self,vertex, x,y):
		self._route_map[vertex]=(x,y)
		graph.add_vertex(vertex)


	def sp(self,v,w):
		shortest=dijkstra(v)
		print(shortest)
		parents=[]
		time=[]
		time.append(shortest[w][0])
		parent=shortest[w][1]
		parents.append(parent)
		print('Time:',time)
		while parent!=v:
			time.append(shortest[parent][0])
			parent=shortest[parent][1]
			parents.append(parent)
		parents.reverse()
		time.append(0)
		time.reverse()
		parents.append(w)
		return time,parents
	def get_routemap(self):
		return self._route_map

def read_file():
	fh = open('simplegraph2.txt')
	wordlist=[]
	for line in fh:
		wordlist.append(line.split())
		print(line)
	fh.close()

	edges=[]
	for index in wordlist:
		if index[0]=='id:':
			graph.add_vertex(index[1])
		elif index[0]=='from:':
			edges.append(index[1])
		elif index[0]=='to:':
			edges.append(index[1])
		elif index[0]=='length:':
			edges.append(index[1])
	print(len(edges))

	edgelist=[]

	while len(edges)!=0:
		l=[]
		l.append(edges.pop(0))
		l.append(edges.pop(0))
		l.append(edges.pop(0))
		edgelist.append(l)

	print(edgelist)
	for l in edgelist:
		graph.add_edge(l[0],l[1],int(l[2]))
	print('Vertices :',graph.vertices())
	print('Num edges :',graph.num_edges())
	print('Num vertices :',graph.num_vertices())


#ead_file()

def read_map():
	fh = open('simpleroute1.txt')
	wordlist=[]
	for line in fh:
		wordlist.append(line.split())
		#print(line)
	fh.close()

	edges=[]
	coordinates=[]
	nodes=[]
	for index in wordlist:
		gps=[]
		if index[0]=='id:':
			coordinates.append(index[1])
			#nodes.append(index[1])
			#graph.add_vertex(index[1])
		elif index[0]=='gps:':
			coordinates.append((index[1],index[2]))
			#coordinates.append(gps)
		elif index[0]=='from:':
			edges.append(index[1])
		elif index[0]=='to:':
			edges.append(index[1])
		elif index[0]=='time:':
			edges.append(index[1])
	#print(len(edges))
	#print('Coordinates:',coordinates)
	#print(nodes)

	edgelist=[]

	while len(edges)!=0:
		l=[]
		l.append(edges.pop(0))
		l.append(edges.pop(0))
		l.append(edges.pop(0))
		edgelist.append(l)
	#print('Edges',edgelist)

	gpslist=[]
	while len(coordinates)!=0:
		l=[]
		l.append(coordinates.pop(0))
		l.append(coordinates.pop(0))
		gpslist.append(l)
	#print('GPS List:',gpslist)
	return gpslist,edgelist


	'''
	for l in edgelist:
		graph.add_edge(l[0],l[1],int(l[2]))
	print('Vertices :',graph.vertices())
	print('Num edges :',graph.num_edges())
	print('Num vertices :',graph.num_vertices())
'''
routemap=RouteMap()

vertices,edges=read_map()
print('Vertices:',vertices)
print('Edges:',edges)
for element in vertices:
	routemap.add_vertex(element[0],element[1][0],element[1][1])


for element in edges:
	graph.add_edge(element[0],element[1],float(element[2]))


#routemap.add_vertex('a',123.33,234.333)
#print(routemap)
print('\n',graph)
time,path=routemap.sp('1','4')
print(time)
print(path)
timer=0
for index in path:
	print('W',routemap.get_routemap()[index],index,time[timer])
	timer+=1


#print(dijkstra("3"))




