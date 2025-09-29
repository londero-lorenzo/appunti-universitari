class BlockCleanupParams:
    def __init__(
        self,
        inner_text_s_thresh=(None, 0.2),
        inner_text_v_thresh=(0.85, None),
        min_text_density=0.4,
        debug=False
    ):
        self.inner_text_s_thresh = inner_text_s_thresh
        self.inner_text_v_thresh = inner_text_v_thresh
        self.min_text_density = min_text_density
        self.debug = debug

    def to_kwargs(self):
        return {
            "inner_text_s_thresh": self.inner_text_s_thresh,
            "inner_text_v_thresh": self.inner_text_v_thresh,
            "min_text_density": self.min_text_density,
            "debug": self.debug,
        }

    def __repr__(self):
        return (
            f"BlockCleanupParams("
            f"s_thresh={self.inner_text_s_thresh}, "
            f"v_thresh={self.inner_text_v_thresh}, "
            f"density={self.min_text_density}, "
            f"debug={self.debug})"
        )
        
        
    def update_from_input(self):
        for attr in vars(self):
            val = input(f"{attr} = {getattr(self, attr)} → nuovo valore (ENTER per mantenere): ").strip()
            if not val:
                continue
            if attr.endswith("_thresh"):
                parsed = tuple(
                    float(x) if x.lower() != 'none' else None
                    for x in val.split(",")
                )
                setattr(self, attr, parsed)
            elif attr == 'debug':
                setattr(self, attr, val.lower() in ['1', 'true', 'yes'])
            else:
                setattr(self, attr, float(val))





class TextFinderParams:
    def __init__(
        self,
        inner_text_s_thresh=(None, 0.2),
        inner_text_v_thresh=(0.85, None),
        min_text_density=0.4,
        debug=False
    ):
        self.inner_text_s_thresh = inner_text_s_thresh
        self.inner_text_v_thresh = inner_text_v_thresh
        self.min_text_density = min_text_density
        self.debug = debug

    def to_kwargs(self):
        return {
            "inner_text_s_thresh": self.inner_text_s_thresh,
            "inner_text_v_thresh": self.inner_text_v_thresh,
            "min_text_density": self.min_text_density,
            "debug": self.debug
        }

    def update_from_input(self):
        for attr in vars(self):
            val = input(f"{attr} = {getattr(self, attr)} → nuovo valore (ENTER per mantenere): ").strip()
            if not val:
                continue
            if attr.endswith("_thresh"):
                parsed = tuple(
                    float(x) if x.lower() != 'none' else None
                    for x in val.split(",")
                )
                setattr(self, attr, parsed)
            elif attr == "debug":
                setattr(self, attr, val.lower() in ["1", "true", "yes"])
            else:
                setattr(self, attr, float(val))

    def __repr__(self):
        return f"TextFinderParams(s_thresh={self.inner_text_s_thresh}, v_thresh={self.inner_text_v_thresh}, min_density={self.min_text_density}, debug={self.debug})"



        