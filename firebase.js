<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.8.4/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.8.4/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBRK-uO9b5RaqvJ-6Tg-Ta-EhPpK5AYkDA",
    authDomain: "tantorial-oauth.firebaseapp.com",
    projectId: "tantorial-oauth",
    storageBucket: "tantorial-oauth.appspot.com",
    messagingSenderId: "346462944607",
    appId: "1:346462944607:web:6b1e144562646eef2f0aea",
    measurementId: "G-2E64ZPNQYT"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>