# Python TODO 管理器

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

一个功能完整的命令行交互式 TODO 任务管理器，基于 Python 开发，支持任务增删改查、状态切换、持久化存储、导入导出、排序等核心功能，无需第三方依赖，开箱即用。

## 🌟 功能特性
- 📝 **任务新增**：自动记录创建时间，支持空输入校验
- 👀 **任务查看**：带状态/时间展示，自动统计完成/未完成数量
- 🗑️ **任务删除**：按序号精准删除，支持异常输入处理
- ✏️ **任务修改**：修改内容并记录修改时间
- ✅ **状态切换**：一键切换任务“完成/未完成”状态
- 🔍 **任务搜索**：关键词模糊搜索（不区分大小写）
- 💾 **持久化存储**：JSON 格式本地保存，退出自动存档
- 🧹 **批量清理**：一键清除所有已完成任务（需确认）
- 🔄 **任务排序**：支持按创建时间/内容/状态排序
- 📤/📥 **导入导出**：支持 TXT 格式任务导入导出

## 📋 快速开始

### 1. 环境要求
- Python 3.6 及以上版本（仅依赖内置库，无需额外安装）
- 兼容 Windows/macOS/Linux 所有系统

### 2. 克隆仓库
```bash
# 克隆仓库到本地
git clone https://github.com/你的GitHub用户名/python-todo-manager.git

# 进入项目目录
cd python-todo-manager
