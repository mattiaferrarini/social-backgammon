import axios from 'axios';
import { useAuthStore } from '@/stores/authStore';
import router from '@/router';

export const registerOrLogin = async (
	username: string,
	password: string,
	email: string | undefined,
	isRegistering: boolean,
) => {
	const data = {
		username: username,
		password: password,
	};
	const response = await axios.post(
		`http://localhost:8000/${isRegistering ? 'register' : 'token'}`,
		isRegistering ? { ...data, email: email } : data,
	);
	useAuthStore().setUserData(response.data.access_token, username);
};

export const requestPasswordRecovery = async (email: string) => {
  return await axios.post('http://localhost:8000/password-recovery', { email });
}

export const resetPassword = async (password: string, token: string) => {
  return await axios.post('http://localhost:8000/password-reset', { "new_password": password, token });
}

export const logout = async () => {
	useAuthStore().logout();
	await router.push({ name: 'register' });
};

export function isAuthenticated(): boolean {
	return useAuthStore().isAuthenticated();
}
