```

npm install ffmpeg-static
npm install ffmpeg-static是一个npm命令，用于安装ffmpeg-static包。ffmpeg-static是一个预编译的ffmpeg二进制文件，可以直接在Node.js中使用，无需手动安装ffmpeg。

const { exec } = require('child_process');
const ffmpegPath = require('ffmpeg-static').path;
 
exec(`"${ffmpegPath}" -version`, (error, stdout, stderr) => {
  if (error) {
    console.error(`执行出错: ${error}`);
    return;
  }
  console.log(stdout);
});
```