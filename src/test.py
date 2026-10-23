import asyncio,sys
from playwright.async_api import async_playwright
U='http://localhost:8765/alex-cave-rescue/'
async def run(p,w,h,tag):
  b=await p.webkit.launch();c=await b.new_context(viewport={'width':w,'height':h},has_touch=True,is_mobile=True);pg=await c.new_page()
  errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type=='error' and errs.append(m.text))
  await pg.goto(U);await pg.evaluate('localStorage.clear()');await pg.reload();await pg.wait_for_timeout(800)
  await pg.screenshot(path=f'/tmp/cv/{tag}-title.png')
  await pg.evaluate('__C.tap()');await pg.wait_for_timeout(500);await pg.screenshot(path=f'/tmp/cv/{tag}-story.png');await pg.evaluate('__C.tap()')
  # hold right with touch-free keyboard for a bit + jumps
  await pg.keyboard.down('ArrowRight')
  for i in range(8):
    await pg.wait_for_timeout(350);await pg.keyboard.press('ArrowUp')
  await pg.keyboard.up('ArrowRight');await pg.screenshot(path=f'/tmp/cv/{tag}-z0.png');print(tag,'z0 walk',await pg.evaluate('__C.state().x'),await pg.evaluate('__C.state().gems'))
  for z in range(5):
    await pg.evaluate(f'__C.unlock({z});__C.start({z})');await pg.wait_for_timeout(600);await pg.screenshot(path=f'/tmp/cv/{tag}-lv{z}.png')
    await pg.evaluate(f'__C.toBoss({z})');await pg.wait_for_timeout(200)
    await pg.keyboard.down('ArrowRight');await pg.wait_for_timeout(300);await pg.keyboard.up('ArrowRight')
    await pg.wait_for_timeout(3500);await pg.screenshot(path=f'/tmp/cv/{tag}-boss{z}.png')
    st=await pg.evaluate('[__C.boss(),__C.state().hp]');print(tag,'boss',z,st)
    if z==4:
      await pg.evaluate('__C.hitBoss(5)');await pg.wait_for_timeout(3500);await pg.screenshot(path=f'/tmp/cv/{tag}-boss4p2.png');print(' p2',await pg.evaluate('__C.boss()'))
      await pg.evaluate('__C.hitBoss(5)');await pg.wait_for_timeout(3500);await pg.screenshot(path=f'/tmp/cv/{tag}-boss4p3.png');print(' p3',await pg.evaluate('__C.boss()'))
    for i in range(20):
      await pg.evaluate('__C.hitBoss(1)');await pg.wait_for_timeout(500)
      if not await pg.evaluate('__C.boss()') or (await pg.evaluate('__C.boss()'))['hp']<=0: break
    await pg.wait_for_timeout(2800);await pg.screenshot(path=f'/tmp/cv/{tag}-win{z}.png');print(' after',await pg.evaluate('__C.state()'))
    await pg.wait_for_timeout(2500);await pg.screenshot(path=f'/tmp/cv/{tag}-win{z}b.png')
  await pg.evaluate('__C.start(4)');await pg.evaluate('__C.chicken()');await pg.wait_for_timeout(400);await pg.screenshot(path=f'/tmp/cv/{tag}-chicken.png');print('chicken hp',await pg.evaluate('__C.state().hp'))
  await pg.evaluate("__C.start(0)");await pg.evaluate('__C.tele(52)');await pg.wait_for_timeout(1200);await pg.screenshot(path=f'/tmp/cv/{tag}-quiz.png')
  await pg.reload();await pg.wait_for_timeout(600);print('saved',await pg.evaluate('__C.state().save'));await pg.screenshot(path=f'/tmp/cv/{tag}-title2.png')
  print(tag,'ERRS',errs[:5]);await b.close()
async def main():
  async with async_playwright() as p:
    for w,h,t in [(1180,820,'ipad'),(390,844,'phone')]: await run(p,w,h,t)
asyncio.run(main())
