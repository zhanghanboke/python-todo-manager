import json
import os
from datetime import datetime

class TodoManager:
    """TODO管理器类"""

    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self):
        """添加新任务"""
        task = input("请输入要添加的任务: ").strip()

        if not task:
            print("❌ 任务不能为空")
            return

        # 添加时间戳
        task_data = {
            "content": task,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False
        }

        self.tasks.append(task_data)
        print(f"✅ 任务 '{task}' 已添加")

    def view_tasks(self, show_completed=False):
        """查看所有任务"""
        if not self.tasks:
            print("📋 当前没有任务")
            return

        print("\n📋 任务列表:")
        print("-" * 50)

        for i, task in enumerate(self.tasks, 1):
            status = "✅" if task["completed"] else "⭕"
            completed_str = " [已完成]" if task["completed"] else ""
            created_str = f" (创建于: {task['created_at']})"

            print(f"{i}. {status} {task['content']}{completed_str}{created_str}")

        print("-" * 50)

        # 显示统计信息
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])
        print(f"📊 统计: 总共 {total} 个任务, 已完成 {completed} 个, 待完成 {total - completed} 个")

    def delete_task(self):
        """按序号删除任务"""
        if not self.tasks:
            print("📋 没有任务可删除")
            return

        self.view_tasks()

        try:
            index = int(input("请输入要删除的任务序号: ")) - 1

            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"✅ 任务 '{removed['content']}' 已删除")
            else:
                print("❌ 序号无效，请输入1到", len(self.tasks), "之间的数字")

        except ValueError:
            print("❌ 请输入有效的数字")

    def modify_task(self):
        """修改任务内容"""
        if not self.tasks:
            print("📋 没有任务可修改")
            return

        self.view_tasks()

        try:
            index = int(input("请输入要修改的任务序号: ")) - 1

            if 0 <= index < len(self.tasks):
                old_task = self.tasks[index]["content"]
                new_task = input("请输入新的任务内容: ").strip()

                if new_task:
                    self.tasks[index]["content"] = new_task
                    self.tasks[index]["modified_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"✅ 任务 '{old_task}' 已修改为 '{new_task}'")
                else:
                    print("❌ 任务内容不能为空")
            else:
                print("❌ 序号无效")

        except ValueError:
            print("❌ 请输入数字")

    def toggle_task_status(self):
        """切换任务完成状态"""
        if not self.tasks:
            print("📋 没有任务可操作")
            return

        self.view_tasks()

        try:
            index = int(input("请输入要切换状态的任务序号: ")) - 1

            if 0 <= index < len(self.tasks):
                task = self.tasks[index]
                task["completed"] = not task["completed"]

                status = "已完成" if task["completed"] else "未完成"
                print(f"✅ 任务 '{task['content']}' 状态已更新为: {status}")
            else:
                print("❌ 序号无效")

        except ValueError:
            print("❌ 请输入数字")

    def search_tasks(self):
        """搜索任务"""
        if not self.tasks:
            print("📋 没有任务可搜索")
            return

        keyword = input("请输入搜索关键词: ").strip().lower()

        if not keyword:
            print("❌ 关键词不能为空")
            return

        results = []
        for i, task in enumerate(self.tasks, 1):
            if keyword in task["content"].lower():
                results.append((i, task))

        if results:
            print(f"\n🔍 找到 {len(results)} 个匹配的任务:")
            print("-" * 50)
            for index, task in results:
                status = "✅" if task["completed"] else "⭕"
                print(f"{index}. {status} {task['content']}")
            print("-" * 50)
        else:
            print(f"❌ 没有找到包含 '{keyword}' 的任务")

    def save_tasks(self):
        """保存任务到文件"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
            print(f"✅ 任务已保存到 {self.filename}")
        except Exception as e:
            print(f"❌ 保存失败: {e}")

    def load_tasks(self):
        """从文件读取任务"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
                print(f"✅ 从 {self.filename} 加载了 {len(self.tasks)} 个任务")
            else:
                print("📋 未找到任务文件，创建新列表")
                self.tasks = []
        except Exception as e:
            print(f"❌ 加载失败: {e}")
            self.tasks = []

    def clear_completed_tasks(self):
        """清除已完成的任务"""
        if not self.tasks:
            print("📋 没有任务可清除")
            return

        completed_count = sum(1 for task in self.tasks if task["completed"])

        if completed_count == 0:
            print("📋 没有已完成的任务")
            return

        confirm = input(f"确认清除 {completed_count} 个已完成的任务吗? (y/n): ").strip().lower()

        if confirm == 'y':
            self.tasks = [task for task in self.tasks if not task["completed"]]
            print(f"✅ 已清除 {completed_count} 个已完成的任务")
        else:
            print("❌ 操作已取消")

    def sort_tasks(self, by="created"):
        """排序任务"""
        if not self.tasks:
            print("📋 没有任务可排序")
            return

        if by == "created":
            # 按创建时间排序（最新的在前）
            self.tasks.sort(key=lambda x: x["created_at"], reverse=True)
            print("✅ 任务已按创建时间排序（最新在前）")
        elif by == "content":
            # 按内容字母顺序排序
            self.tasks.sort(key=lambda x: x["content"])
            print("✅ 任务已按内容字母顺序排序")
        elif by == "status":
            # 未完成的在前，已完成的在后
            self.tasks.sort(key=lambda x: x["completed"])
            print("✅ 任务已按状态排序（未完成在前）")
        else:
            print("❌ 无效的排序方式")

    def export_tasks(self):
        """导出任务到文本文件"""
        if not self.tasks:
            print("📋 没有任务可导出")
            return

        filename = input("请输入导出文件名 (默认: tasks_export.txt): ").strip()
        if not filename:
            filename = "tasks_export.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"任务列表 - 导出时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 50 + "\n\n")

                for i, task in enumerate(self.tasks, 1):
                    status = "✅" if task["completed"] else "⭕"
                    completed_str = " [已完成]" if task["completed"] else ""
                    created_str = f" (创建: {task['created_at']})"

                    f.write(f"{i}. {status} {task['content']}{completed_str}{created_str}\n")

                f.write("\n" + "=" * 50 + "\n")
                f.write(f"总计: {len(self.tasks)} 个任务\n")

            print(f"✅ 任务已导出到 {filename}")
        except Exception as e:
            print(f"❌ 导出失败: {e}")

    def import_tasks(self):
        """从文件导入任务"""
        filename = input("请输入要导入的文件名: ").strip()

        if not filename:
            print("❌ 文件名不能为空")
            return

        if not os.path.exists(filename):
            print(f"❌ 文件 '{filename}' 不存在")
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # 简单的文本解析（假设是txt格式）
            lines = content.strip().split('\n')
            imported_count = 0

            for line in lines:
                line = line.strip()
                if line and not line.startswith('=') and not line.startswith('任务列表') and not line.startswith('总计'):
                    # 提取任务内容（去掉序号和状态符号）
                    if line and line[0].isdigit():
                        # 找到第一个非数字字符的位置
                        start = 0
                        while start < len(line) and line[start].isdigit():
                            start += 1
                        # 跳过点号和空格
                        while start < len(line) and line[start] in ['.', ' ']:
                            start += 1
                        # 跳过状态符号
                        while start < len(line) and line[start] in ['✅', '⭕']:
                            start += 1

                        task_content = line[start:].strip()
                        # 去掉可能的 [已完成] 标记
                        if task_content.endswith('[已完成]'):
                            task_content = task_content[:-5].strip()

                        if task_content:
                            task_data = {
                                "content": task_content,
                                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                "completed": False
                            }
                            self.tasks.append(task_data)
                            imported_count += 1

            if imported_count > 0:
                print(f"✅ 成功导入 {imported_count} 个任务")
            else:
                print("❌ 未找到可导入的任务")

        except Exception as e:
            print(f"❌ 导入失败: {e}")

def main_menu():
    """主菜单"""
    print("\n" + "="*60)
    print("🎯 TODO 管理器 - 功能完整版")
    print("="*60)
    print("1.  📝 添加任务")
    print("2.  👀 查看所有任务")
    print("3.  🗑️  删除任务")
    print("4.  ✏️  修改任务")
    print("5.  ✅ 切换任务状态（完成/未完成）")
    print("6.  🔍 搜索任务")
    print("7.  💾 保存到文件")
    print("8.  📂 从文件读取")
    print("9.  🧹 清除已完成的任务")
    print("10. 🔄 排序任务")
    print("11. 📤 导出任务到文本")
    print("12. 📥 导入任务从文本")
    print("0.  🚪 退出程序")
    print("="*60)

def main():
    """主程序"""
    manager = TodoManager()

    while True:
        main_menu()
        choice = input("请选择操作 (0-12): ").strip()

        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.delete_task()
        elif choice == '4':
            manager.modify_task()
        elif choice == '5':
            manager.toggle_task_status()
        elif choice == '6':
            manager.search_tasks()
        elif choice == '7':
            manager.save_tasks()
        elif choice == '8':
            manager.load_tasks()
        elif choice == '9':
            manager.clear_completed_tasks()
        elif choice == '10':
            print("\n排序方式:")
            print("1. 按创建时间（最新在前）")
            print("2. 按内容字母顺序")
            print("3. 按状态（未完成在前）")
            sort_choice = input("请选择排序方式 (1-3): ").strip()
            if sort_choice == '1':
                manager.sort_tasks("created")
            elif sort_choice == '2':
                manager.sort_tasks("content")
            elif sort_choice == '3':
                manager.sort_tasks("status")
            else:
                print("❌ 无效的选择")
        elif choice == '11':
            manager.export_tasks()
        elif choice == '12':
            manager.import_tasks()
        elif choice == '0':
            # 退出前自动保存
            manager.save_tasks()
            print("\n👋 感谢使用TODO管理器！再见！")
            break
        else:
            print("❌ 无效选择，请重新输入 (0-12)")

        # 按回车继续
        if choice != '0':
            input("\n按回车键继续...")

# 程序入口
if __name__ == "__main__":
    main()
