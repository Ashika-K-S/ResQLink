import { useEffect, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";

const SocialLoginSuccess = () => {
  const navigate = useNavigate();
  const { login } = useContext(AuthContext);

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const access = params.get("access");
    const refresh = params.get("refresh");
    const role = params.get("role");

    if (access && refresh) {
    
      localStorage.setItem("access_token", access);
      localStorage.setItem("refresh_token", refresh);

      if (!role) {
        navigate("/select-role");
      } else {
        localStorage.setItem("role", role);

      
        login(role);

        navigate("/dashboard");
      }
    } else {
      navigate("/login");
    }
  }, [navigate, login]);

  return <p>Logging you in...</p>;
};

export default SocialLoginSuccess;