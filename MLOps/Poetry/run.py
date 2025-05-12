import argparse

def run():
    argparser = argparse.ArgumentParser(description="Run a script with specified arguments.")
    argparser.add_argument(
        "--train",
        action="store_true",
        help="Run the training script.",)
    argparser.add_argument(
        "--predict",
        action="store_true",
        help="Run the test script.",
    )

    args = argparser.parse_args()
    
    if args.train:
        from iris.main import train_model
        train_model.run()
    elif args.predict:
        from iris.main import predict
        prediction = predict.predict()
        print(f"Predicted class: {prediction}")

    else:
        print("Please specify --train or --test to run the respective script.")

if __name__ == "__main__":
    run()