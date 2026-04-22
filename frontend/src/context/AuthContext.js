import { createContext, useState, useEffect } from "react";
import API from "../api/axios";
export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    const role = localStorage.getItem("role");

    if (token && role) {
      setUser({ role });
    }
  }, []);

  const login = (role) => {
    setUser({ role });
  };

  const logout = async () => {
  try {
    const refresh = localStorage.getItem("refresh_token");

    if (refresh) {
      await API.post("users/logout/", { refresh });  // 🔥 backend call
    }

  } catch (err) {
    console.log("Logout error:", err);
  } finally {
    localStorage.clear();
    setUser(null);
    window.location.href = "/login";
  }
};

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};