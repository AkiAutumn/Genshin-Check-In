allCookies = document.cookie.split("; ");
_MHYUUID = allCookies.find((row) => row.startsWith("_MHYUUID="))
  ?.split("=")[1];
ltoken = allCookies.find((row) => row.startsWith("ltoken="))
  ?.split("=")[1];
ltuid = allCookies.find((row) => row.startsWith("ltuid="))
  ?.split("=")[1];

url = window.location.href;
act_id = url.split("act_id=")[1];
act_id = act_id.split("&")[0];

function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

download('Genshin Check-In.bat', 'start /min cmd /c genshin-check-in.exe ' + act_id + ' ' + _MHYUUID + ' ' +  ltoken + ' ' + ltuid)

console.warn("Do NOT share the downloaded file with anyone. It contains login information for your Genshin account! Run it to launch genshin-check-in.exe with correct parameters")