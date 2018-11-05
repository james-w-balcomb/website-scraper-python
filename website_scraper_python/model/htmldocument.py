# import bs4
from bs4 import BeautifulSoup
from bs4 import Comment
from bs4 import Doctype


class HtmlDocument(object):

    # requests_response_text = None
    #
    # # soup = bs4.BeautifulSoup
    # # soup = BeautifulSoup
    # soup = None
    #
    # pre_html_tag_contents = None
    # post_html_tag_contents = None
    # html_tag_contents = None
    # head_tag_contents = None
    # head_meta_tag_contents = None
    # head_title_tag_contents = None
    # body_tag_contents = None
    # body_script_tag_contents = None
    # body_footer_tag_contents = None
    # div_tag_contents = None
    #
    # comment_tags_contents = None
    # doctype_tags_contents = None
    # a_tags_contents = None
    # abbr_tags_contents = None
    # acronym_tags_contents = None
    # address_tags_contents = None
    # applet_tags_contents = None
    # area_tags_contents = None
    # article_tags_contents = None
    # aside_tags_contents = None
    # audio_tags_contents = None
    # b_tags_contents = None
    # base_tags_contents = None
    # basefont_tags_contents = None
    # bdi_tags_contents = None
    # bdo_tags_contents = None
    # big_tags_contents = None
    # blockquote_tags_contents = None
    # body_tags_contents = None
    # br_tags_contents = None
    # button_tags_contents = None
    # canvas_tags_contents = None
    # caption_tags_contents = None
    # center_tags_contents = None
    # cite_tags_contents = None
    # code_tags_contents = None
    # col_tags_contents = None
    # colgroup_tags_contents = None
    # data_tags_contents = None
    # datalist_tags_contents = None
    # dd_tags_contents = None
    # del_tags_contents = None
    # details_tags_contents = None
    # dfn_tags_contents = None
    # dialog_tags_contents = None
    # dir_tags_contents = None
    # div_tags_contents = None
    # dl_tags_contents = None
    # dt_tags_contents = None
    # em_tags_contents = None
    # embed_tags_contents = None
    # fieldset_tags_contents = None
    # figcaption_tags_contents = None
    # figure_tags_contents = None
    # font_tags_contents = None
    # footer_tags_contents = None
    # form_tags_contents = None
    # frame_tags_contents = None
    # frameset_tags_contents = None
    # h1_tags_contents = None
    # h2_tags_contents = None
    # h3_tags_contents = None
    # h4_tags_contents = None
    # h5_tags_contents = None
    # h6_tags_contents = None
    # head_tags_contents = None
    # header_tags_contents = None
    # hr_tags_contents = None
    # html_tags_contents = None
    # i_tags_contents = None
    # iframe_tags_contents = None
    # img_tags_contents = None
    # input_tags_contents = None
    # ins_tags_contents = None
    # kbd_tags_contents = None
    # label_tags_contents = None
    # legend_tags_contents = None
    # li_tags_contents = None
    # link_tags_contents = None
    # main_tags_contents = None
    # map_tags_contents = None
    # mark_tags_contents = None
    # meta_tags_contents = None
    # meter_tags_contents = None
    # nav_tags_contents = None
    # noframes_tags_contents = None
    # noscript_tags_contents = None
    # object_tags_contents = None
    # ol_tags_contents = None
    # optgroup_tags_contents = None
    # option_tags_contents = None
    # output_tags_contents = None
    # p_tags_contents = None
    # param_tags_contents = None
    # picture_tags_contents = None
    # pre_tags_contents = None
    # progress_tags_contents = None
    # q_tags_contents = None
    # rp_tags_contents = None
    # rt_tags_contents = None
    # ruby_tags_contents = None
    # s_tags_contents = None
    # samp_tags_contents = None
    # script_tags_contents = None
    # section_tags_contents = None
    # select_tags_contents = None
    # small_tags_contents = None
    # source_tags_contents = None
    # span_tags_contents = None
    # strike_tags_contents = None
    # strong_tags_contents = None
    # style_tags_contents = None
    # sub_tags_contents = None
    # summary_tags_contents = None
    # sup_tags_contents = None
    # svg_tags_contents = None
    # table_tags_contents = None
    # tbody_tags_contents = None
    # td_tags_contents = None
    # template_tags_contents = None
    # textarea_tags_contents = None
    # tfoot_tags_contents = None
    # th_tags_contents = None
    # thead_tags_contents = None
    # time_tags_contents = None
    # title_tags_contents = None
    # tr_tags_contents = None
    # track_tags_contents = None
    # tt_tags_contents = None
    # u_tags_contents = None
    # ul_tags_contents = None
    # var_tags_contents = None
    # video_tags_contents = None
    # wbr_tags_contents = None

    def __init__(self, requests_response_text):
        self.requests_response_text = requests_response_text

        # <class 'bs4.BeautifulSoup'>
        # markup, features, builder, parse_only, from_encoding, exclude_encodings
        self.soup = BeautifulSoup(markup = self.requests_response_text, features = "lxml")
        # soup = BeautifulSoup(markup = requests_response_text, features = 'html.parser')
        # self.soup = BeautifulSoup()

        # self.comment_tags_contents = self.soup.find_all("comment")
        # self.doctype_tags_contents = self.soup.find_all("doctype")
        # self.a_tags_contents = self.soup.find_all("a")
        # self.abbr_tags_contents = self.soup.find_all("abbr")
        # self.acronym_tags_contents = self.soup.find_all("acronym")
        # self.address_tags_contents = self.soup.find_all("address")
        # self.applet_tags_contents = self.soup.find_all("applet")
        # self.area_tags_contents = self.soup.find_all("area")
        # self.article_tags_contents = self.soup.find_all("article")
        # self.aside_tags_contents = self.soup.find_all("aside")
        # self.audio_tags_contents = self.soup.find_all("audio")
        # self.b_tags_contents = self.soup.find_all("b")
        # self.base_tags_contents = self.soup.find_all("base")
        # self.basefont_tags_contents = self.soup.find_all("basefont")
        # self.bdi_tags_contents = self.soup.find_all("bdi")
        # self.bdo_tags_contents = self.soup.find_all("bdo")
        # self.big_tags_contents = self.soup.find_all("big")
        # self.blockquote_tags_contents = self.soup.find_all("blockquote")
        # self.body_tags_contents = self.soup.find_all("body")
        # self.br_tags_contents = self.soup.find_all("br")
        # self.button_tags_contents = self.soup.find_all("button")
        # self.canvas_tags_contents = self.soup.find_all("canvas")
        # self.caption_tags_contents = self.soup.find_all("caption")
        # self.center_tags_contents = self.soup.find_all("center")
        # self.cite_tags_contents = self.soup.find_all("cite")
        # self.code_tags_contents = self.soup.find_all("code")
        # self.col_tags_contents = self.soup.find_all("col")
        # self.colgroup_tags_contents = self.soup.find_all("colgroup")
        # self.data_tags_contents = self.soup.find_all("data")
        # self.datalist_tags_contents = self.soup.find_all("datalist")
        # self.dd_tags_contents = self.soup.find_all("dd")
        # self.del_tags_contents = self.soup.find_all("del")
        # self.details_tags_contents = self.soup.find_all("details")
        # self.dfn_tags_contents = self.soup.find_all("dfn")
        # self.dialog_tags_contents = self.soup.find_all("dialog")
        # self.dir_tags_contents = self.soup.find_all("dir")
        # self.div_tags_contents = self.soup.find_all("div")
        # self.dl_tags_contents = self.soup.find_all("dl")
        # self.dt_tags_contents = self.soup.find_all("dt")
        # self.em_tags_contents = self.soup.find_all("em")
        # self.embed_tags_contents = self.soup.find_all("embed")
        # self.fieldset_tags_contents = self.soup.find_all("fieldset")
        # self.figcaption_tags_contents = self.soup.find_all("figcaption")
        # self.figure_tags_contents = self.soup.find_all("figure")
        # self.font_tags_contents = self.soup.find_all("font")
        # self.footer_tags_contents = self.soup.find_all("footer")
        # self.form_tags_contents = self.soup.find_all("form")
        # self.frame_tags_contents = self.soup.find_all("frame")
        # self.frameset_tags_contents = self.soup.find_all("frameset")
        # self.h1_tags_contents = self.soup.find_all("h1")
        # self.h2_tags_contents = self.soup.find_all("h2")
        # self.h3_tags_contents = self.soup.find_all("h3")
        # self.h4_tags_contents = self.soup.find_all("h4")
        # self.h5_tags_contents = self.soup.find_all("h5")
        # self.h6_tags_contents = self.soup.find_all("h6")
        # self.head_tags_contents = self.soup.find_all("head")
        # self.header_tags_contents = self.soup.find_all("header")
        # self.hr_tags_contents = self.soup.find_all("hr")
        # self.html_tags_contents = self.soup.find_all("html")
        # self.i_tags_contents = self.soup.find_all("i")
        # self.iframe_tags_contents = self.soup.find_all("iframe")
        # self.img_tags_contents = self.soup.find_all("img")
        # self.input_tags_contents = self.soup.find_all("input")
        # self.ins_tags_contents = self.soup.find_all("ins")
        # self.kbd_tags_contents = self.soup.find_all("kbd")
        # self.label_tags_contents = self.soup.find_all("label")
        # self.legend_tags_contents = self.soup.find_all("legend")
        # self.li_tags_contents = self.soup.find_all("li")
        # self.link_tags_contents = self.soup.find_all("link")
        # self.main_tags_contents = self.soup.find_all("main")
        # self.map_tags_contents = self.soup.find_all("map")
        # self.mark_tags_contents = self.soup.find_all("mark")
        # self.meta_tags_contents = self.soup.find_all("meta")
        # self.meter_tags_contents = self.soup.find_all("meter")
        # self.nav_tags_contents = self.soup.find_all("nav")
        # self.noframes_tags_contents = self.soup.find_all("noframes")
        # self.noscript_tags_contents = self.soup.find_all("noscript")
        # self.object_tags_contents = self.soup.find_all("object")
        # self.ol_tags_contents = self.soup.find_all("ol")
        # self.optgroup_tags_contents = self.soup.find_all("optgroup")
        # self.option_tags_contents = self.soup.find_all("option")
        # self.output_tags_contents = self.soup.find_all("output")
        # self.p_tags_contents = self.soup.find_all("p")
        # self.param_tags_contents = self.soup.find_all("param")
        # self.picture_tags_contents = self.soup.find_all("picture")
        # self.pre_tags_contents = self.soup.find_all("pre")
        # self.progress_tags_contents = self.soup.find_all("progress")
        # self.q_tags_contents = self.soup.find_all("q")
        # self.rp_tags_contents = self.soup.find_all("rp")
        # self.rt_tags_contents = self.soup.find_all("rt")
        # self.ruby_tags_contents = self.soup.find_all("ruby")
        # self.s_tags_contents = self.soup.find_all("s")
        # self.samp_tags_contents = self.soup.find_all("samp")
        # self.script_tags_contents = self.soup.find_all("script")
        # self.section_tags_contents = self.soup.find_all("section")
        # self.select_tags_contents = self.soup.find_all("select")
        # self.small_tags_contents = self.soup.find_all("small")
        # self.source_tags_contents = self.soup.find_all("source")
        # self.span_tags_contents = self.soup.find_all("span")
        # self.strike_tags_contents = self.soup.find_all("strike")
        # self.strong_tags_contents = self.soup.find_all("strong")
        # self.style_tags_contents = self.soup.find_all("style")
        # self.sub_tags_contents = self.soup.find_all("sub")
        # self.summary_tags_contents = self.soup.find_all("summary")
        # self.sup_tags_contents = self.soup.find_all("sup")
        # self.svg_tags_contents = self.soup.find_all("svg")
        # self.table_tags_contents = self.soup.find_all("table")
        # self.tbody_tags_contents = self.soup.find_all("tbody")
        # self.td_tags_contents = self.soup.find_all("td")
        # self.template_tags_contents = self.soup.find_all("template")
        # self.textarea_tags_contents = self.soup.find_all("textarea")
        # self.tfoot_tags_contents = self.soup.find_all("tfoot")
        # self.th_tags_contents = self.soup.find_all("th")
        # self.thead_tags_contents = self.soup.find_all("thead")
        # self.time_tags_contents = self.soup.find_all("time")
        # self.title_tags_contents = self.soup.find_all("title")
        # self.tr_tags_contents = self.soup.find_all("tr")
        # self.track_tags_contents = self.soup.find_all("track")
        # self.tt_tags_contents = self.soup.find_all("tt")
        # self.u_tags_contents = self.soup.find_all("u")
        # self.ul_tags_contents = self.soup.find_all("ul")
        # self.var_tags_contents = self.soup.find_all("var")
        # self.video_tags_contents = self.soup.find_all("video")
        # self.wbr_tags_contents = self.soup.find_all("wbr")
        self.comment_tags_contents = None
        self.doctype_tags_contents = None
        self.a_tags_contents = None
        self.abbr_tags_contents = None
        self.acronym_tags_contents = None
        self.address_tags_contents = None
        self.applet_tags_contents = None
        self.area_tags_contents = None
        self.article_tags_contents = None
        self.aside_tags_contents = None
        self.audio_tags_contents = None
        self.b_tags_contents = None
        self.base_tags_contents = None
        self.basefont_tags_contents = None
        self.bdi_tags_contents = None
        self.bdo_tags_contents = None
        self.big_tags_contents = None
        self.blockquote_tags_contents = None
        self.body_tags_contents = None
        self.br_tags_contents = None
        self.button_tags_contents = None
        self.canvas_tags_contents = None
        self.caption_tags_contents = None
        self.center_tags_contents = None
        self.cite_tags_contents = None
        self.code_tags_contents = None
        self.col_tags_contents = None
        self.colgroup_tags_contents = None
        self.data_tags_contents = None
        self.datalist_tags_contents = None
        self.dd_tags_contents = None
        self.del_tags_contents = None
        self.details_tags_contents = None
        self.dfn_tags_contents = None
        self.dialog_tags_contents = None
        self.dir_tags_contents = None
        self.div_tags_contents = None
        self.dl_tags_contents = None
        self.dt_tags_contents = None
        self.em_tags_contents = None
        self.embed_tags_contents = None
        self.fieldset_tags_contents = None
        self.figcaption_tags_contents = None
        self.figure_tags_contents = None
        self.font_tags_contents = None
        self.footer_tags_contents = None
        self.form_tags_contents = None
        self.frame_tags_contents = None
        self.frameset_tags_contents = None
        self.h1_tags_contents = None
        self.h2_tags_contents = None
        self.h3_tags_contents = None
        self.h4_tags_contents = None
        self.h5_tags_contents = None
        self.h6_tags_contents = None
        self.head_tags_contents = None
        self.header_tags_contents = None
        self.hr_tags_contents = None
        self.html_tags_contents = None
        self.i_tags_contents = None
        self.iframe_tags_contents = None
        self.img_tags_contents = None
        self.input_tags_contents = None
        self.ins_tags_contents = None
        self.kbd_tags_contents = None
        self.label_tags_contents = None
        self.legend_tags_contents = None
        self.li_tags_contents = None
        self.link_tags_contents = None
        self.main_tags_contents = None
        self.map_tags_contents = None
        self.mark_tags_contents = None
        self.meta_tags_contents = None
        self.meter_tags_contents = None
        self.nav_tags_contents = None
        self.noframes_tags_contents = None
        self.noscript_tags_contents = None
        self.object_tags_contents = None
        self.ol_tags_contents = None
        self.optgroup_tags_contents = None
        self.option_tags_contents = None
        self.output_tags_contents = None
        self.p_tags_contents = None
        self.param_tags_contents = None
        self.picture_tags_contents = None
        self.pre_tags_contents = None
        self.progress_tags_contents = None
        self.q_tags_contents = None
        self.rp_tags_contents = None
        self.rt_tags_contents = None
        self.ruby_tags_contents = None
        self.s_tags_contents = None
        self.samp_tags_contents = None
        self.script_tags_contents = None
        self.section_tags_contents = None
        self.select_tags_contents = None
        self.small_tags_contents = None
        self.source_tags_contents = None
        self.span_tags_contents = None
        self.strike_tags_contents = None
        self.strong_tags_contents = None
        self.style_tags_contents = None
        self.sub_tags_contents = None
        self.summary_tags_contents = None
        self.sup_tags_contents = None
        self.svg_tags_contents = None
        self.table_tags_contents = None
        self.tbody_tags_contents = None
        self.td_tags_contents = None
        self.template_tags_contents = None
        self.textarea_tags_contents = None
        self.tfoot_tags_contents = None
        self.th_tags_contents = None
        self.thead_tags_contents = None
        self.time_tags_contents = None
        self.title_tags_contents = None
        self.tr_tags_contents = None
        self.track_tags_contents = None
        self.tt_tags_contents = None
        self.u_tags_contents = None
        self.ul_tags_contents = None
        self.var_tags_contents = None
        self.video_tags_contents = None
        self.wbr_tags_contents = None

        def get_doctype(soup):
            doctype = None
            # 1 # items = [item for item in soup.contents if isinstance(item, Doctype)]
            # 1 # doctype = items[0] if items else None
            # 2 # doctype = next(item for item in soup.contents if isinstance(item, Doctype))
            for item in soup.contents:
                if isinstance(item, Doctype):
                    doctype = item.extract()
            return doctype

        def get_head_title():
            head_title = None
            head_title = self.soup.html.head.title.string.strip()
            return head_title

        def get_canonical_link_html():
            canonical_link_html = None
            canonical_link_html = self.soup.find("link", rel = "canonical")
            return canonical_link_html

        def get_canonical_link_href():
            canonical_link_href = None
            canonical_link_href = self.soup.find("link", rel = "canonical")['href'].strip()
            return canonical_link_href

        def get_canonical_link__id():
            canonical_link_id = None
            canonical_link_id = self.soup.find("link", rel = "canonical")['id'].strip()
            return canonical_link_id

        def get_meta_author():
            meta_author = None
            meta_author = self.soup.find("meta", author = True)['author'].strip()
            return meta_author

        def get_meta_charset():
            meta_charset = None
            meta_charset = self.soup.find("meta", charset = True)['charset'].strip()
            return meta_charset

        def get_meta_description():
            meta_description = None
            meta_description = self.soup.find("meta", description = True)['description'].strip()
            return meta_description

        def get_meta_keywords():
            meta_keywords = None
            meta_keywords = self.soup.find("meta", keywords = True)['keywords'].strip()
            return meta_keywords

        def get_meta_viewport():
            meta_viewport = None
            meta_viewport = self.soup.find("meta", viewport = True)['viewport'].strip()
            return meta_viewport

        def get_meta_robots():
            meta_robots = None
            meta_robots = self.soup.find("meta", robots = True)['content'].strip()
            return meta_robots

        def get_meta_tag_list():
            meta_tag_list = None
            pass

        def get_comment_tags_contents():
            if self.comment_tags_contents is None:
                self.comment_tags_contents = self.soup.find_all("comment")
            return self.comment_tags_contents

        def get_doctype_tags_contents():
            if self.doctype_tags_contents is None:
                self.doctype_tags_contents = self.soup.find_all("doctype")
            return self.doctype_tags_contents

        def get_a_tags_contents():
            if self.a_tags_contents is None:
                self.a_tags_contents = self.soup.find_all("a")
            return self.a_tags_contents

        def get_abbr_tags_contents():
            if self.abbr_tags_contents is None:
                self.abbr_tags_contents = self.soup.find_all("abbr")
            return self.abbr_tags_contents

        def get_acronym_tags_contents():
            if self.acronym_tags_contents is None:
                self.acronym_tags_contents = self.soup.find_all("acronym")
            return self.acronym_tags_contents

        def get_address_tags_contents():
            if self.address_tags_contents is None:
                self.address_tags_contents = self.soup.find_all("address")
            return self.address_tags_contents

        def get_applet_tags_contents():
            if self.applet_tags_contents is None:
                self.applet_tags_contents = self.soup.find_all("applet")
            return self.applet_tags_contents

        def get_area_tags_contents():
            if self.area_tags_contents is None:
                self.area_tags_contents = self.soup.find_all("area")
            return self.area_tags_contents

        def get_article_tags_contents():
            if self.article_tags_contents is None:
                self.article_tags_contents = self.soup.find_all("article")
            return self.article_tags_contents

        def get_aside_tags_contents():
            if self.aside_tags_contents is None:
                self.aside_tags_contents = self.soup.find_all("aside")
            return self.aside_tags_contents

        def get_audio_tags_contents():
            if self.audio_tags_contents is None:
                self.audio_tags_contents = self.soup.find_all("audio")
            return self.audio_tags_contents

        def get_b_tags_contents():
            if self.b_tags_contents is None:
                self.b_tags_contents = self.soup.find_all("b")
            return self.b_tags_contents

        def get_base_tags_contents():
            if self.base_tags_contents is None:
                self.base_tags_contents = self.soup.find_all("base")
            return self.base_tags_contents

        def get_basefont_tags_contents():
            if self.basefont_tags_contents is None:
                self.basefont_tags_contents = self.soup.find_all("basefont")
            return self.basefont_tags_contents

        def get_bdi_tags_contents():
            if self.bdi_tags_contents is None:
                self.bdi_tags_contents = self.soup.find_all("bdi")
            return self.bdi_tags_contents

        def get_bdo_tags_contents():
            if self.bdo_tags_contents is None:
                self.bdo_tags_contents = self.soup.find_all("bdo")
            return self.bdo_tags_contents

        def get_big_tags_contents():
            if self.big_tags_contents is None:
                self.big_tags_contents = self.soup.find_all("big")
            return self.big_tags_contents

        def get_blockquote_tags_contents():
            if self.blockquote_tags_contents is None:
                self.blockquote_tags_contents = self.soup.find_all("blockquote")
            return self.blockquote_tags_contents

        def get_body_tags_contents():
            if self.body_tags_contents is None:
                self.body_tags_contents = self.soup.find_all("body")
            return self.body_tags_contents

        def get_br_tags_contents():
            if self.br_tags_contents is None:
                self.br_tags_contents = self.soup.find_all("br")
            return self.br_tags_contents

        def get_button_tags_contents():
            if self.button_tags_contents is None:
                self.button_tags_contents = self.soup.find_all("button")
            return self.button_tags_contents

        def get_canvas_tags_contents():
            if self.canvas_tags_contents is None:
                self.canvas_tags_contents = self.soup.find_all("canvas")
            return self.canvas_tags_contents

        def get_caption_tags_contents():
            if self.caption_tags_contents is None:
                self.caption_tags_contents = self.soup.find_all("caption")
            return self.caption_tags_contents

        def get_center_tags_contents():
            if self.center_tags_contents is None:
                self.center_tags_contents = self.soup.find_all("center")
            return self.center_tags_contents

        def get_cite_tags_contents():
            if self.cite_tags_contents is None:
                self.cite_tags_contents = self.soup.find_all("cite")
            return self.cite_tags_contents

        def get_code_tags_contents():
            if self.code_tags_contents is None:
                self.code_tags_contents = self.soup.find_all("code")
            return self.code_tags_contents

        def get_col_tags_contents():
            if self.col_tags_contents is None:
                self.col_tags_contents = self.soup.find_all("col")
            return self.col_tags_contents

        def get_colgroup_tags_contents():
            if self.colgroup_tags_contents is None:
                self.colgroup_tags_contents = self.soup.find_all("colgroup")
            return self.colgroup_tags_contents

        def get_data_tags_contents():
            if self.data_tags_contents is None:
                self.data_tags_contents = self.soup.find_all("data")
            return self.data_tags_contents

        def get_datalist_tags_contents():
            if self.datalist_tags_contents is None:
                self.datalist_tags_contents = self.soup.find_all("datalist")
            return self.datalist_tags_contents

        def get_dd_tags_contents():
            if self.dd_tags_contents is None:
                self.dd_tags_contents = self.soup.find_all("dd")
            return self.dd_tags_contents

        def get_del_tags_contents():
            if self.del_tags_contents is None:
                self.del_tags_contents = self.soup.find_all("del")
            return self.del_tags_contents

        def get_details_tags_contents():
            if self.details_tags_contents is None:
                self.details_tags_contents = self.soup.find_all("details")
            return self.details_tags_contents

        def get_dfn_tags_contents():
            if self.dfn_tags_contents is None:
                self.dfn_tags_contents = self.soup.find_all("dfn")
            return self.dfn_tags_contents

        def get_dialog_tags_contents():
            if self.dialog_tags_contents is None:
                self.dialog_tags_contents = self.soup.find_all("dialog")
            return self.dialog_tags_contents

        def get_dir_tags_contents():
            if self.dir_tags_contents is None:
                self.dir_tags_contents = self.soup.find_all("dir")
            return self.dir_tags_contents

        def get_div_tags_contents():
            if self.div_tags_contents is None:
                self.div_tags_contents = self.soup.find_all("div")
            return self.div_tags_contents

        def get_dl_tags_contents():
            if self.dl_tags_contents is None:
                self.dl_tags_contents = self.soup.find_all("dl")
            return self.dl_tags_contents

        def get_dt_tags_contents():
            if self.dt_tags_contents is None:
                self.dt_tags_contents = self.soup.find_all("dt")
            return self.dt_tags_contents

        def get_em_tags_contents():
            if self.em_tags_contents is None:
                self.em_tags_contents = self.soup.find_all("em")
            return self.em_tags_contents

        def get_embed_tags_contents():
            if self.embed_tags_contents is None:
                self.embed_tags_contents = self.soup.find_all("embed")
            return self.embed_tags_contents

        def get_fieldset_tags_contents():
            if self.fieldset_tags_contents is None:
                self.fieldset_tags_contents = self.soup.find_all("fieldset")
            return self.fieldset_tags_contents

        def get_figcaption_tags_contents():
            if self.figcaption_tags_contents is None:
                self.figcaption_tags_contents = self.soup.find_all("figcaption")
            return self.figcaption_tags_contents

        def get_figure_tags_contents():
            if self.figure_tags_contents is None:
                self.figure_tags_contents = self.soup.find_all("figure")
            return self.figure_tags_contents

        def get_font_tags_contents():
            if self.font_tags_contents is None:
                self.font_tags_contents = self.soup.find_all("font")
            return self.font_tags_contents

        def get_footer_tags_contents():
            if self.footer_tags_contents is None:
                self.footer_tags_contents = self.soup.find_all("footer")
            return self.footer_tags_contents

        def get_form_tags_contents():
            if self.form_tags_contents is None:
                self.form_tags_contents = self.soup.find_all("form")
            return self.form_tags_contents

        def get_frame_tags_contents():
            if self.frame_tags_contents is None:
                self.frame_tags_contents = self.soup.find_all("frame")
            return self.frame_tags_contents

        def get_frameset_tags_contents():
            if self.frameset_tags_contents is None:
                self.frameset_tags_contents = self.soup.find_all("frameset")
            return self.frameset_tags_contents

        def get_h1_tags_contents():
            if self.h1_tags_contents is None:
                self.h1_tags_contents = self.soup.find_all("h1")
            return self.h1_tags_contents

        def get_h2_tags_contents():
            if self.h2_tags_contents is None:
                self.h2_tags_contents = self.soup.find_all("h2")
            return self.h2_tags_contents

        def get_h3_tags_contents():
            if self.h3_tags_contents is None:
                self.h3_tags_contents = self.soup.find_all("h3")
            return self.h3_tags_contents

        def get_h4_tags_contents():
            if self.h4_tags_contents is None:
                self.h4_tags_contents = self.soup.find_all("h4")
            return self.h4_tags_contents

        def get_h5_tags_contents():
            if self.h5_tags_contents is None:
                self.h5_tags_contents = self.soup.find_all("h5")
            return self.h5_tags_contents

        def get_h6_tags_contents():
            if self.h6_tags_contents is None:
                self.h6_tags_contents = self.soup.find_all("h6")
            return self.h6_tags_contents

        def get_head_tags_contents():
            if self.head_tags_contents is None:
                self.head_tags_contents = self.soup.find_all("head")
            return self.head_tags_contents

        def get_header_tags_contents():
            if self.header_tags_contents is None:
                self.header_tags_contents = self.soup.find_all("header")
            return self.header_tags_contents

        def get_hr_tags_contents():
            if self.hr_tags_contents is None:
                self.hr_tags_contents = self.soup.find_all("hr")
            return self.hr_tags_contents

        def get_html_tags_contents():
            if self.html_tags_contents is None:
                self.html_tags_contents = self.soup.find_all("html")
            return self.html_tags_contents

        def get_i_tags_contents():
            if self.i_tags_contents is None:
                self.i_tags_contents = self.soup.find_all("i")
            return self.i_tags_contents

        def get_iframe_tags_contents():
            if self.iframe_tags_contents is None:
                self.iframe_tags_contents = self.soup.find_all("iframe")
            return self.iframe_tags_contents

        def get_img_tags_contents():
            if self.img_tags_contents is None:
                self.img_tags_contents = self.soup.find_all("img")
            return self.img_tags_contents

        def get_input_tags_contents():
            if self.input_tags_contents is None:
                self.input_tags_contents = self.soup.find_all("input")
            return self.input_tags_contents

        def get_ins_tags_contents():
            if self.ins_tags_contents is None:
                self.ins_tags_contents = self.soup.find_all("ins")
            return self.ins_tags_contents

        def get_kbd_tags_contents():
            if self.kbd_tags_contents is None:
                self.kbd_tags_contents = self.soup.find_all("kbd")
            return self.kbd_tags_contents

        def get_label_tags_contents():
            if self.label_tags_contents is None:
                self.label_tags_contents = self.soup.find_all("label")
            return self.label_tags_contents

        def get_legend_tags_contents():
            if self.legend_tags_contents is None:
                self.legend_tags_contents = self.soup.find_all("legend")
            return self.legend_tags_contents

        def get_li_tags_contents():
            if self.li_tags_contents is None:
                self.li_tags_contents = self.soup.find_all("li")
            return self.li_tags_contents

        def get_link_tags_contents():
            if self.link_tags_contents is None:
                self.link_tags_contents = self.soup.find_all("link")
            return self.link_tags_contents

        def get_main_tags_contents():
            if self.main_tags_contents is None:
                self.main_tags_contents = self.soup.find_all("main")
            return self.main_tags_contents

        def get_map_tags_contents():
            if self.map_tags_contents is None:
                self.map_tags_contents = self.soup.find_all("map")
            return self.map_tags_contents

        def get_mark_tags_contents():
            if self.mark_tags_contents is None:
                self.mark_tags_contents = self.soup.find_all("mark")
            return self.mark_tags_contents

        def get_meta_tags_contents():
            if self.meta_tags_contents is None:
                self.meta_tags_contents = self.soup.find_all("meta")
            return self.meta_tags_contents

        def get_meter_tags_contents():
            if self.meter_tags_contents is None:
                self.meter_tags_contents = self.soup.find_all("meter")
            return self.meter_tags_contents

        def get_nav_tags_contents():
            if self.nav_tags_contents is None:
                self.nav_tags_contents = self.soup.find_all("nav")
            return self.nav_tags_contents

        def get_noframes_tags_contents():
            if self.noframes_tags_contents is None:
                self.noframes_tags_contents = self.soup.find_all("noframes")
            return self.noframes_tags_contents

        def get_noscript_tags_contents():
            if self.noscript_tags_contents is None:
                self.noscript_tags_contents = self.soup.find_all("noscript")
            return self.noscript_tags_contents

        def get_object_tags_contents():
            if self.object_tags_contents is None:
                self.object_tags_contents = self.soup.find_all("object")
            return self.object_tags_contents

        def get_ol_tags_contents():
            if self.ol_tags_contents is None:
                self.ol_tags_contents = self.soup.find_all("ol")
            return self.ol_tags_contents

        def get_optgroup_tags_contents():
            if self.optgroup_tags_contents is None:
                self.optgroup_tags_contents = self.soup.find_all("optgroup")
            return self.optgroup_tags_contents

        def get_option_tags_contents():
            if self.option_tags_contents is None:
                self.option_tags_contents = self.soup.find_all("option")
            return self.option_tags_contents

        def get_output_tags_contents():
            if self.output_tags_contents is None:
                self.output_tags_contents = self.soup.find_all("output")
            return self.output_tags_contents

        def get_p_tags_contents():
            if self.p_tags_contents is None:
                self.p_tags_contents = self.soup.find_all("p")
            return self.p_tags_contents

        def get_param_tags_contents():
            if self.param_tags_contents is None:
                self.param_tags_contents = self.soup.find_all("param")
            return self.param_tags_contents

        def get_picture_tags_contents():
            if self.picture_tags_contents is None:
                self.picture_tags_contents = self.soup.find_all("picture")
            return self.picture_tags_contents

        def get_pre_tags_contents():
            if self.pre_tags_contents is None:
                self.pre_tags_contents = self.soup.find_all("pre")
            return self.pre_tags_contents

        def get_progress_tags_contents():
            if self.progress_tags_contents is None:
                self.progress_tags_contents = self.soup.find_all("progress")
            return self.progress_tags_contents

        def get_q_tags_contents():
            if self.q_tags_contents is None:
                self.q_tags_contents = self.soup.find_all("q")
            return self.q_tags_contents

        def get_rp_tags_contents():
            if self.rp_tags_contents is None:
                self.rp_tags_contents = self.soup.find_all("rp")
            return self.rp_tags_contents

        def get_rt_tags_contents():
            if self.rt_tags_contents is None:
                self.rt_tags_contents = self.soup.find_all("rt")
            return self.rt_tags_contents

        def get_ruby_tags_contents():
            if self.ruby_tags_contents is None:
                self.ruby_tags_contents = self.soup.find_all("ruby")
            return self.ruby_tags_contents

        def get_s_tags_contents():
            if self.s_tags_contents is None:
                self.s_tags_contents = self.soup.find_all("s")
            return self.s_tags_contents

        def get_samp_tags_contents():
            if self.samp_tags_contents is None:
                self.samp_tags_contents = self.soup.find_all("samp")
            return self.samp_tags_contents

        def get_script_tags_contents():
            if self.script_tags_contents is None:
                self.script_tags_contents = self.soup.find_all("script")
            return self.script_tags_contents

        def get_section_tags_contents():
            if self.section_tags_contents is None:
                self.section_tags_contents = self.soup.find_all("section")
            return self.section_tags_contents

        def get_select_tags_contents():
            if self.select_tags_contents is None:
                self.select_tags_contents = self.soup.find_all("select")
            return self.select_tags_contents

        def get_small_tags_contents():
            if self.small_tags_contents is None:
                self.small_tags_contents = self.soup.find_all("small")
            return self.small_tags_contents

        def get_source_tags_contents():
            if self.source_tags_contents is None:
                self.source_tags_contents = self.soup.find_all("source")
            return self.source_tags_contents

        def get_span_tags_contents():
            if self.span_tags_contents is None:
                self.span_tags_contents = self.soup.find_all("span")
            return self.span_tags_contents

        def get_strike_tags_contents():
            if self.strike_tags_contents is None:
                self.strike_tags_contents = self.soup.find_all("strike")
            return self.strike_tags_contents

        def get_strong_tags_contents():
            if self.strong_tags_contents is None:
                self.strong_tags_contents = self.soup.find_all("strong")
            return self.strong_tags_contents

        def get_style_tags_contents():
            if self.style_tags_contents is None:
                self.style_tags_contents = self.soup.find_all("style")
            return self.style_tags_contents

        def get_sub_tags_contents():
            if self.sub_tags_contents is None:
                self.sub_tags_contents = self.soup.find_all("sub")
            return self.sub_tags_contents

        def get_summary_tags_contents():
            if self.summary_tags_contents is None:
                self.summary_tags_contents = self.soup.find_all("summary")
            return self.summary_tags_contents

        def get_sup_tags_contents():
            if self.sup_tags_contents is None:
                self.sup_tags_contents = self.soup.find_all("sup")
            return self.sup_tags_contents

        def get_svg_tags_contents():
            if self.svg_tags_contents is None:
                self.svg_tags_contents = self.soup.find_all("svg")
            return self.svg_tags_contents

        def get_table_tags_contents():
            if self.table_tags_contents is None:
                self.table_tags_contents = self.soup.find_all("table")
            return self.table_tags_contents

        def get_tbody_tags_contents():
            if self.tbody_tags_contents is None:
                self.tbody_tags_contents = self.soup.find_all("tbody")
            return self.tbody_tags_contents

        def get_td_tags_contents():
            if self.td_tags_contents is None:
                self.td_tags_contents = self.soup.find_all("td")
            return self.td_tags_contents

        def get_template_tags_contents():
            if self.template_tags_contents is None:
                self.template_tags_contents = self.soup.find_all("template")
            return self.template_tags_contents

        def get_textarea_tags_contents():
            if self.textarea_tags_contents is None:
                self.textarea_tags_contents = self.soup.find_all("textarea")
            return self.textarea_tags_contents

        def get_tfoot_tags_contents():
            if self.tfoot_tags_contents is None:
                self.tfoot_tags_contents = self.soup.find_all("tfoot")
            return self.tfoot_tags_contents

        def get_th_tags_contents():
            if self.th_tags_contents is None:
                self.th_tags_contents = self.soup.find_all("th")
            return self.th_tags_contents

        def get_thead_tags_contents():
            if self.thead_tags_contents is None:
                self.thead_tags_contents = self.soup.find_all("thead")
            return self.thead_tags_contents

        def get_time_tags_contents():
            if self.time_tags_contents is None:
                self.time_tags_contents = self.soup.find_all("time")
            return self.time_tags_contents

        def get_title_tags_contents():
            if self.title_tags_contents is None:
                self.title_tags_contents = self.soup.find_all("title")
            return self.title_tags_contents

        def get_tr_tags_contents():
            if self.tr_tags_contents is None:
                self.tr_tags_contents = self.soup.find_all("tr")
            return self.tr_tags_contents

        def get_track_tags_contents():
            if self.track_tags_contents is None:
                self.track_tags_contents = self.soup.find_all("track")
            return self.track_tags_contents

        def get_tt_tags_contents():
            if self.tt_tags_contents is None:
                self.tt_tags_contents = self.soup.find_all("tt")
            return self.tt_tags_contents

        def get_u_tags_contents():
            if self.u_tags_contents is None:
                self.u_tags_contents = self.soup.find_all("u")
            return self.u_tags_contents

        def get_ul_tags_contents():
            if self.ul_tags_contents is None:
                self.ul_tags_contents = self.soup.find_all("ul")
            return self.ul_tags_contents

        def get_var_tags_contents():
            if self.var_tags_contents is None:
                self.var_tags_contents = self.soup.find_all("var")
            return self.var_tags_contents

        def get_video_tags_contents():
            if self.video_tags_contents is None:
                self.video_tags_contents = self.soup.find_all("video")
            return self.video_tags_contents

        def get_wbr_tags_contents():
            if self.wbr_tags_contents is None:
                self.wbr_tags_contents = self.soup.find_all("wbr")
            return self.wbr_tags_contents
