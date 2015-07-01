<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="utf-8" indent="yes"/>

  <xsl:template match="/">
    <xsl:text disable-output-escaping="yes">&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"></xsl:text>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"> <!-- YIKES! -->
  <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <title>KYOCERA Document Solutions | Mobile Print FAQ</title>
    <meta name="Description" content="" />
    <meta name="Keywords" content="" />
    <meta http-equiv="content-script-type" content="text/javascript" />
    <meta http-equiv="content-style-type" content="text/css" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta name="robots" content="index,follow" />
    <meta name="dc.date" content="2015-04-23" /><!-- YIKES!!! -->
    <meta name="viewport" content="width=device-width,user-scalable=no" />
    <link rel="stylesheet" type="text/css" href="/data/css/responsive/common.css" />
    <link rel="stylesheet" type="text/css" href="/data/css/responsive/header.css" />
    <link rel="stylesheet" type="text/css" href="/support/common/css/style.css" />
    <link rel="stylesheet" type="text/css" href="/support/common/css/style_breakpoint_1.css" />
    <link rel="stylesheet" type="text/css" href="/support/common/css/style_breakpoint_2.css" />
    <link rel="stylesheet" type="text/css" href="css/style.css" />
    <script type="text/javascript" src="/data/js/v5/en/jquery-1.8.1.min.js"></script>
    <script type="text/javascript" src="/data/js/v5/en/jquery-ui-1.9.1.custom.min.js"></script>
    <script type="text/javascript" src="/data/js/v5/en/augment.min.js"></script>
    <script type="text/javascript" src="/data/js/responsive/base.js"></script>
    <script type="text/javascript" src="js/faq.config.js"></script>
    <script type="text/javascript" src="js/faq.config.en.js"></script><!-- YIKES!!! -->
    <script type="text/javascript" src="/support/common/js/faq.category_list.js"></script>
    <script type="text/javascript" src="/support/common/js/faq.answer_section.js"></script>
    <script type="text/javascript" src="/support/common/js/faq.analytics.js"></script>
    <script type="text/javascript" src="/support/common/js/faq.misc.js"></script>
    <script type="text/javascript" src="/support/common/js/faq.jquery.toggle_menu.js"></script>
    <script type="text/javascript" src="/support/common/js/faq.init.js"></script>
    <script type="text/javascript" src="/support/common/js/faq.main.js"></script>
  </head>
  <body>
<xsl:text disable-output-escaping="yes"><!--#include virtual="/data/include/gtm.html"--></xsl:text>
    <div id="all">
      <xsl:text disable-output-escaping="yes"><!--#include virtual="/data/include/responsive/header.html" --></xsl:text>
      <div class="location_area">
        <p class="location"><a href="/download/index.html">Support &amp; Download</a>&nbsp;&gt;&nbsp;<strong>KYOCERA Mobile Print FAQ</strong></p>
      </div>
      <div id="content">
        <div id="content_header">
          <img src="images/pict_large_printer.gif" alt="" class="header_icon" />
          <h1 class="header_message"><a href="./">Mobile Print <br />FAQ</a></h1>
          <xsl:text disable-output-escaping="yes"><!--#include virtual="include/lang_menu.html" --></xsl:text>
        </div><xsl:text disable-output-escaping="yes"><!-- /#content_header --></xsl:text>
        <div id="content_body">
          <div id="answer_section">



          </div><xsl:text disable-output-escaping="yes"><!-- /#answer_section --></xsl:text>

          <div id="category_list">
            <!-- APPLY CAT LIST -->
          </div><xsl:text disable-output-escaping="yes"><!-- /#category_list --></xsl:text>

          <div id="bottom_menu">
            <xsl:text disable-output-escaping="yes"><!--#include virtual="include/contact_menu.html" --></xsl:text>
            <div class="store_icon mini">
              <a href="http://itunes.apple.com/us/app/kyocera-mobile-print/id510179385?ls=1&mt=8" target="_blank"><img src="/support/common/images/btn_appstore.gif" alt="KYOCERA Mobile Print iPhone Download" width="138" height="47" /></a>
              <a href="https://play.google.com/store/apps/details?id=com.kyocera.kyoprint&feature=search_result#?t=W251bGwsMSwxLDEsImNvbS5reW9jZXJhLmt5b3ByaW50Il0" target="_blank"><img src="/support/common/images/btn_googleplay.gif" alt="KYOCERA Mobile Print Android Download" width="138" height="48" /></a>
            </div>
          </div>
        </div><xsl:text disable-output-escaping="yes"><!-- /#content_body --></xsl:text>
      </div><xsl:text disable-output-escaping="yes"><!-- /#content --></xsl:text>
      <xsl:text disable-output-escaping="yes"><!--#include virtual="/data/include/responsive/footer.html" --></xsl:text>
      <xsl:text disable-output-escaping="yes"><!--#include virtual="/data/include/responsive/overlay.html" --></xsl:text>
    </div>
  </body>
  <xsl:text disable-output-escaping="yes"><!--#include virtual="/data/include/beacon.html" --></xsl:text>
</html>
  </xsl:template>


  <xsl:template match="*[contains(@class,' map/topicref ')]">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>



</xsl:stylesheet>