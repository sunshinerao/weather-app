import requests
import json

def get_weather(city_name, api_key):
    """
    获取指定城市的天气信息
    
    Args:
        city_name (str): 城市名称
        api_key (str): OpenWeatherMap API密钥
    
    Returns:
        dict: 包含温度和天气描述的字典
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # 使用摄氏度
        'lang': 'zh_cn'     # 中文描述
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure']
        }
        
        return weather_info
    
    except requests.exceptions.RequestException as e:
        return {'error': f'请求失败: {e}'}
    except KeyError as e:
        return {'error': f'数据解析失败: {e}'}

def main():
    # 替换为你的OpenWeatherMap API密钥
    API_KEY = "d6bcdff9f1d709396bc19576d20c1956"
    
    city = input("请输入城市名称: ")
    weather = get_weather(city, API_KEY)
    
    if 'error' in weather:
        print(weather['error'])
    else:
        print(f"城市: {weather['city']}")
        print(f"温度: {weather['temperature']}°C")
        print(f"天气: {weather['description']}")
        print(f"湿度: {weather['humidity']}%")
        print(f"气压: {weather['pressure']} hPa")

if __name__ == "__main__":
    main()

