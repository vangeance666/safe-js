from app import create_app

def main():
	my_app = create_app()
	my_app.run(debug=True, port=5000)


if __name__ == '__main__':
	main()