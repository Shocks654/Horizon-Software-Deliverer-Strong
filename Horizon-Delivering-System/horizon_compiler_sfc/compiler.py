import os
import json

class HorizonSFCCompiler:
    def __init__(self):
        self.compiled_blocks = {}
        self.is_ready = True

    def parse_sfc_template(self, raw_source):
        if not raw_source:
            return ""
        parsed_data = {}
        try:
            if "<template>" in raw_source and "</template>" in raw_source:
                start = raw_source.find("<template>") + len("<template>")
                end = raw_source.find("</template>")
                parsed_data["template"] = raw_source[start:end].strip()
            if "<script>" in raw_source and "</script>" in raw_source:
                start = raw_source.find("<script>") + len("<script>")
                end = raw_source.find("</script>")
                parsed_data["script"] = raw_source[start:end].strip()
            return parsed_data
        except Exception:
            return {}

    def deliver_compiled_sfc(self, parsed_matrix, state_variables):
        template = parsed_matrix.get("template", "")
        if not template:
            return ""
        for key, value in state_variables.items():
            token = "{{" + str(key) + "}}"
            if token in template:
                template = template.replace(token, str(value))
        return template
