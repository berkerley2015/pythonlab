import os

print '1', os.getcwd()
print '2', os.path.basename(__file__)
print '3', os.path.abspath(__file__)
print '4', os.path.dirname(__file__)  #no significance
print '5', os.path.dirname(os.path.abspath(__file__))

print '6', __file__

#os.path.join(os.path.dirname(os.path.abspath(__file__))