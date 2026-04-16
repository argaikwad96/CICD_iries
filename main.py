from src.train import train
from src.predict import predict

if __name__== "__main__":
    train()

    sample = [5.1,3.5,0.2,1.4]
    result  =predict(sample)

    print("Prediction:",result)

