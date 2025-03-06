import asyncio
import json
import aiohttp
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("CTF赛事播报", "orxiain", "带定时检测的CTF赛事插件", "1.1.0")
class CTFPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        # 初始化时启动后台任务
        self.check_task = asyncio.create_task(self.background_check())
        self.last_competitions = set()  # 用于跟踪已检测到的赛事

    @filter.command("赛事播报")
    async def ctf_events(self, event: AstrMessageEvent):
        """获取最新CTF赛事信息"""
        data = await self.fetch_data()
        if not data or not data.get("success"):
            yield event.plain_result("⛔ 暂时无法获取赛事信息")
            return
        
        formatted_text = self.format_competitions(data)
        yield event.plain_result(formatted_text)

    async def background_check(self):
        """后台定时检测任务"""
        try:
            while True:
                await asyncio.sleep(3600)  # 每小时检测一次
                if new_data := await self.fetch_data():
                    await self.process_new_competitions(new_data)
        except asyncio.CancelledError:
            logger.info("后台检测任务已终止")
        except Exception as e:
            logger.error(f"定时检测异常: {str(e)}")

    async def fetch_data(self):
        """通用数据获取方法"""
        url = "https://raw.githubusercontent.com/ProbiusOfficial/Hello-CTFtime/main/CN.json"
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
                async with session.get(url) as response:
                    return await self.parse_data(await response.text())
        except Exception as e:
            logger.error(f"数据获取失败: {str(e)}")
            return None

    async def parse_data(self, json_str):
        """通用数据解析方法"""
        try:
            return await asyncio.wait_for(
                asyncio.to_thread(self._parse_sync, json_str),
                timeout=5
            )
        except asyncio.TimeoutError:
            logger.warning("数据解析超时")
            return None
        except Exception as e:
            logger.error(f"解析失败: {str(e)}")
            return None

    def _parse_sync(self, json_str):
        """同步解析方法"""
        try:
            data = json.loads(json_str)
            return {
                "success": data.get("success", False),
                "competitions": [
                    {
                        "id": item.get("id"),
                        "name": item.get("name", "未命名赛事"),
                        "comp_time": {
                            "start": item.get("comp_time_start", "未知时间"),
                            "end": item.get("comp_time_end", "未知时间")
                        },
                        "link": item.get("link", "")
                    }
                    for item in data.get("data", {}).get("result", [])
                ],
                "total": data.get("data", {}).get("total", 0)
            }
        except json.JSONDecodeError as e:
            raise ValueError(f"无效JSON格式: {str(e)}")

    async def process_new_competitions(self, new_data):
        """处理新赛事检测"""
        if not new_data.get("success"):
            return

        current_competitions = {comp["id"] for comp in new_data["competitions"]}
        new_ids = current_competitions - self.last_competitions
        
        if new_ids:
            new_competitions = [comp for comp in new_data["competitions"] if comp["id"] in new_ids]
            message = "🎉 发现新CTF赛事！\n" + "\n".join(
                f"{comp['name']} ({comp['comp_time']['start']})"
                for comp in new_competitions
            )
            # 这里需要根据实际框架API实现消息发送
            # 示例：await self.context.broadcast(message)
            logger.info(f"检测到新赛事: {message}")
            
        self.last_competitions = current_competitions

    def format_competitions(self, data):
        """格式化输出"""
        if not data.get("success"):
            return "⚠️ 数据源异常，请稍后重试"

        competitions = data.get("competitions", [])[:5]
        return (
            "🌟 最新CTF赛事\n"
            "───────────\n" +
            "\n".join(
                f"🏆 {comp['name']}\n"
                f"⏰ {comp['comp_time']['start']} - {comp['comp_time']['end']}\n"
                f"🔗 {comp['link'] or '暂无'}\n"
                "───────────"
                for comp in competitions
            ) +
            f"\n🔍 共 {data['total']} 个赛事，更多请访问: https://hello-ctf.com/Event/#bot"
        )

    async def terminate(self):
        """清理资源"""
        if self.check_task and not self.check_task.done():
            self.check_task.cancel()
            try:
                await self.check_task
            except asyncio.CancelledError:
                pass
        logger.info("CTF插件已安全卸载")



