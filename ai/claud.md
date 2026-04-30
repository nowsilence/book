
```shell
# 安装
npm install -g @anthropic-ai/claude-code

# 配置deepseek
# 临时生效，仅当前终端
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="sk-077c5b4053a64dd2b645b3ddc204974b" # 你的DeepSeek API Key
export ANTHROPIC_MODEL="deepseek-v4-pro" # deepseek-v4-flash
export ANTHROPIC_SMALL_FAST_MODEL="deepseek-v4-flash"

# 永久写入
# zsh
echo '# DeepSeek API Configuration for Claude Code' >> ~/.zshrc
echo 'export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"' >> ~/.zshrc
echo 'export ANTHROPIC_AUTH_TOKEN="sk-077c5b4053a64dd2b645b3ddc204974b"' >> ~/.zshrc
echo 'export ANTHROPIC_MODEL="deepseek-v4-pro"' >> ~/.zshrc
echo 'export ANTHROPIC_SMALL_FAST_MODEL="deepseek-v4-flash"' >> ~/.zshrc

source ~/.zshrc # rc run commands

# bash
echo '# DeepSeek API Configuration for Claude Code' >> ~/.bash_profile
echo 'export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"' >> ~/.bash_profile
echo 'export ANTHROPIC_AUTH_TOKEN="sk-077c5b4053a64dd2b645b3ddc204974b"' >> ~/.bash_profile
echo 'export ANTHROPIC_MODEL="deepseek-v4-pro"' >> ~/.bash_profile
echo 'export ANTHROPIC_SMALL_FAST_MODEL="deepseek-v4-flash"' >> ~/.bash_profile

source ~/.bash_profile
```