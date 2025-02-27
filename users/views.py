from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Artist, Producer

# Generate JWT Token Function
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh["user_type"] = "artist" if isinstance(user, Artist) else "producer"  # 🔥 Add user type to token
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user_type': refresh["user_type"]
    }

class SignupView(APIView):
    permission_classes = [AllowAny]  # ✅ Allow public access
    
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user_type = data.get('user_type')

        if user_type not in ['artist', 'producer']:
            return Response({"error": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)

        if Artist.objects.filter(email=email).exists() or Producer.objects.filter(email=email).exists():
            return Response({"error": "Email is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        if user_type == 'artist':
            user = Artist.objects.create(
                email=email,
                nom=data.get('nom', ''),
                prenom=data.get('prenom', ''),
                password=make_password(password)
            )
        else:
            user = Producer.objects.create(
                email=email,
                nom=data.get('nom', ''),
                prenom=data.get('prenom', ''),
                password=make_password(password)
            )

        return Response({"message": f"{user_type.capitalize()} account created successfully."}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [AllowAny]  # ✅ Allow public access

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = None
        user_type = None
        try:
            user = Artist.objects.get(email=email)
            user_type = "artist"
        except Artist.DoesNotExist:
            try:
                user = Producer.objects.get(email=email)
                user_type = "producer"
            except Producer.DoesNotExist:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        if not check_password(password, user.password):
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        tokens = get_tokens_for_user(user)
        return Response({
            "refresh": tokens["refresh"],
            "access": tokens["access"],
            "user_type": user_type
        }, status=status.HTTP_200_OK)
#  Protected API Example (Only Authenticated Users Can Access)
class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Welcome, {request.user.email}! You are authenticated."}, status=200)
