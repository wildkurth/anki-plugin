from anki.hooks import addHook
from aqt.editor import Editor
from aqt.qt import *

addon_path = os.path.dirname(__file__)

def hide_text(editor:Editor):
    selected_text = editor.web.selectedText()
    html = '<span class="hideText" style="color: #BFB500;"><span class="hideTextFront"></span><span class="hideTextBack">{}</span></span>'.format(selected_text)
    editor.web.eval("document.execCommand('insertHTML', false, '{}');".format(html))

def add_hide_button(buttons, editor):
    button = editor.addButton(
        icon=os.path.join(addon_path, "image", "hide_button.svg"),
        cmd='replace_selection_with_html',
        func=lambda ed=editor: hide_text(ed),
        tip='Replace Selection with HTML'
    )
    buttons.append(button)
    return buttons

addHook("setupEditorButtons", add_hide_button)
