@bot.on(admin_cmd(pattern="repo"))
@bot.on(sudo_cmd(pattern="repo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    Repo = f"[Click Here](https://github.com/unknownforall1/YukkiSpamBot)"
    await edit_or_reply(
        event, f"**Indian Spam Bot Repo:** {Repo}"
    )
