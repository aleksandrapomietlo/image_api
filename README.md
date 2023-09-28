Image Upload API with Django REST Framework

This project is a Django application that provides an API for users to upload images in PNG or JPG format. It also supports different account tiers with varying features related to image thumbnails and expiring links.
Setup
Requirements

    Python 3.x
    Docker and Docker Compose (optional)

Installation

    1. Clone the repository
    2. Create a virtual environment and install dependencies
    3. Apply migrations
    4. Create a superuser
    5. Run the development server
    
    Alternatively you can use Docker Compose for easier setup

    Access the API at http://localhost:8000


Account Tiers

    Admins can create and manage account tiers with configurable features like thumbnail sizes, presence of original file link, and ability to generate expiring links via the Django admin panel.


Account Tiers Features

    Basic Tier
        Thumbnail: 200px height

    Premium Tier
        Thumbnail 1: 200px height
        Thumbnail 2: 400px height
        Original File Link

    Enterprise Tier
        Thumbnail 1: 200px height
        Thumbnail 2: 400px height
        Original File Link
        Expiring Links (configurable duration, between 300 and 30000 seconds)


Considerations

    The project follows Django REST Framework (DRF) best practices for building APIs.
    Uploaded images are stored in the media directory.
    Performance has been considered for handling a large number of images and frequent API access.
    Validation checks are in place to ensure data integrity and security.
    Admin UI is accessible via the Django admin panel.