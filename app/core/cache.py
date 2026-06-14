from app.core.redis import redis_client

def invalidate_reports_cache():
    redis_client.delete("report:low_stock")
    redis_client.delete("repost:top_selling")
    redis_client.delete("report:monthly_sales")