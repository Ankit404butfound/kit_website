def render_custom_template(function_info):
    func_desp = ""
    for function, arg_type, req, func_description in function_info["func_info"]:
        func_desp += f"<li><b>{function}</b> [{arg_type}]<i> ({req})</i>: {func_description}</li>\n"
    
    error_info = ""
    for error_type, error_description in function_info["error_info"]:
        error_info += f"<li><b>{error_type}</b>: {error_description}</li>\n"
    
    return f"""
<style>
    li{{
        margin-top: 0.5em;
    }}

</style>
<center>
    <h1>{function_info["title"]}</h1>
    <br>
    <h2>{function_info["description"]}</h2>
</center>
<div style="margin-top: 7%;">
    <script src="static/js/embedder.js?target={function_info["url"]}&style=night-owl&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on&fetchFromJsDelivr=on')"></script>
</div>
<div class=parameter-container>
    <h2>The following parameters can be passed</h2>
    <br>
    <ul style="margin-left: 20px;">
    
        {func_desp}
    
    </ul>
    <br><br>
    <h2>The following are some common errors</h2>
    <br>
    <ul style="margin-left: 20px;">
        {error_info}
    </ul>
</div>
<br><br>
<div style="display:inline;">
    <button data-inline="true" onclick="location.href='{function_info["previous_function"]}'">Previous</button>
</div>
<div style="display:inline; float: right;">
    <button data-inline="true" onclick="location.href='{function_info["next_function"]}'">Next</button>
</div>"""