from flask import Flask
from config import Config
from routes import register_routes
from db_config import DatabaseConfig
import socket

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except:
        return "Could not determine IP address"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    print("\n=== Starting Application ===")
    try:
        # Initialize database
        db_config = DatabaseConfig()
        print("Database connection successful!")
        
        # Register routes
        register_routes(app)
        print("Routes registered successfully!")
        print("===========================\n")
        return app
    except Exception as e:
        print(f"Error during application startup: {e}")
        print("===========================\n")
        raise e

if __name__ == '__main__':
    try:
        app = create_app()
        ip_address = get_ip_address()
        port = 8080
        
        print("\n=== Flask Development Server ===")
        print(f"Local URL: http://localhost:{port}")
        print(f"Network URL: http://{ip_address}:{port}")
        print("===============================\n")
        
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as e:
        print("Failed to start the application. Please check the error messages above.")
        exit(1)