from tensorflow.keras.layers import Dense , Add ,Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import PIL

from tensorflow.keras.models import Model
from tensorflow.keras import Input

from tensorflow.keras.applications import NASNetMobile

train_dir_path = 'Known faces/train'
test_dir_path = 'Known faces/test'



input_shape = (224, 224, 3)

nasa_net_model =NASNetMobile (input_shape , include_top=False  ,weights='imagenet')

for layer in nasa_net_model.layers :
    layer.trainable = False


X = Flatten()(nasa_net_model.output)
X= Dense(1000 , activation= 'relu')(X)
prediction = Dense( 1  ,activation= 'softmax')(X)

model = Model(inputs =nasa_net_model.input , outputs = prediction)

model.summary()


train_gen = ImageDataGenerator( rescale= 1./255 , shear_range= 0.2 , zoom_range= 0.2 , horizontal_flip= True)

test_gen = ImageDataGenerator (rescale= 1./255)


train_data = train_gen.flow_from_directory("Known faces/train" , batch_size= 32 , target_size= (224,224) , class_mode= 'categorical')
test_data = test_gen.flow_from_directory("Known faces/validation", batch_size= 32 , target_size= (224,224) , class_mode= 'categorical')




model.compile( optimizer = 'adam',loss = 'categorical_crossentropy'  , metrics= ['accuracy'])

model.fit(train_data , validation_data= test_data , epochs= 5 ,steps_per_epoch= len(train_data ) ,  validation_steps= len(test_data))





