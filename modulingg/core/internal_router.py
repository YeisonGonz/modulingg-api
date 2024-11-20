from fastapi import APIRouter
from modulingg.controllers.autoload import Autoloader
from modulingg.controllers.config import DynamicConfig
from modulingg.core.Analytics import Analytics
from fastapi.responses import StreamingResponse,HTMLResponse

autoloader = Autoloader()
router = APIRouter()
config = DynamicConfig()
analytics_obj = Analytics()
analytics_manager = Analytics()
modulingg_prefix = config.get('modulingg_prefix')

# Simple internal router with the basic operations

@router.get('/')
async def main():
    return {"message": "Modulingg say Hello!"}

@router.get('/modules')
async def modules():
    return autoloader.search_modules()

@router.get('/health')
async def health():
    return {"status": "healthy"}

@router.get('/healthcheck')
async def health():
    return {"status": "healthy"}

@router.get('/analytics',response_class=HTMLResponse)
async def analytics():
    with open("modulingg/static/analytics.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content


@router.get('/graph')
async def analytics():
    graph = analytics_manager.make_graph_analytics_endpoints(analytics_manager.load_analytics())
    return StreamingResponse(graph, media_type="image/png")

@router.get('/graph_ip')
async def analytics():
    graph = analytics_manager.make_graph_analytics_by_ip(analytics_manager.load_analytics())
    return StreamingResponse(graph, media_type="image/png")

@router.get('/graph_lang')
async def analytics():
    graph = analytics_manager.make_graph_analytics_by_lang(analytics_manager.load_analytics())
    return StreamingResponse(graph, media_type="image/png")




def load_internal_router(app):
    app.include_router(router, prefix=modulingg_prefix)
