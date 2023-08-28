import folium
import webbrowser

latitude = 35.19023118026066
longitude = 128.12735035794333

# 지도 생성
m = folium.Map(location=[latitude, longitude], zoom_start=18)

tooltip = "Click me!"

folium.Marker(
    [35.19023118026066, 128.12735035794333],
    popup="한국폴리텍대학 진주캠퍼스",
    tooltip=tooltip      
).add_to(m)

# 지도를 HTML 파일로 저장
# map_file = 'map.html'
m.save('map.html')

# 웹 브라우저로 HTML 파일 열기
webbrowser.open("map.html")
