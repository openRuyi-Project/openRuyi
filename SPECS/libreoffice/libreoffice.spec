# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# LibreOffice installs its own libraries in a private directory outside the system linker path.
# Exclude all private libraries from global Provides and matching internal DT_NEEDED Requires.
%global __provides_exclude_from ^%{_libdir}/libreoffice/program/.*[.]so([.].*)?$
%global _lo_privlibs lib.+lo
%global _lo_privlibs %{_lo_privlibs}|libcomphelper|libi18nlangtag|libi18nutil|libucbhelper
%global _lo_privlibs %{_lo_privlibs}|liblocaledata_en|libpackage2|libpyuno|libsofficeapp
%global _lo_privlibs %{_lo_privlibs}|libunopkgapp|libxmlsecurity|libxsec_xmlsec
%global __requires_exclude ^((%{_lo_privlibs})[.]so[(][)]|libuno_[^.]+[.]so[.]3)

Name:           libreoffice
Version:        26.8.2.2
Release:        %autorelease
Summary:        Desktop office suite for OpenDocument and Microsoft Office files
License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-openRuyi-AGG-2.3 AND MIT AND (GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1) AND (MPL-1.1 OR GPL-2.0-or-later)
URL:            https://www.libreoffice.org/
VCS:            git:https://git.libreoffice.org/core.git
#!RemoteAsset:  sha256:f0012302d9cc70955bd55890d3aaccf6c55677c4a6a46e1003f996b1b0dae8e7
Source0:        https://download.documentfoundation.org/libreoffice/src/26.8.2/%{name}-%{version}.tar.xz
#!RemoteAsset:  sha256:1a3b6077ebfac899f2c31666d283e29e94c2d30704dd162fda7ba06d77212dd2
Source1:        https://download.documentfoundation.org/libreoffice/src/26.8.2/%{name}-translations-%{version}.tar.xz
#!RemoteAsset:  sha256:a3624f6f0ac46a7e190969d405aa7a07dbc342baf69f81192487575bf64055a5
Source2:        https://dev-www.libreoffice.org/src/pdfium-8073.tar.bz2
BuildSystem:    autotools

BuildOption(prep):  -b 1
BuildOption(conf):  --enable-release-build
BuildOption(conf):  --with-vendor=openRuyi
# Build Simplified Chinese UI/resources for openRuyi's langpacks-zh integration.
BuildOption(conf):  --with-lang=zh-CN
BuildOption(conf):  --with-theme=colibre
BuildOption(conf):  --enable-split-app-modules
BuildOption(conf):  --enable-build-opensymbol
BuildOption(conf):  --enable-python=system
BuildOption(conf):  PYTHON_CFLAGS="$(pkg-config --cflags python3-embed)"
BuildOption(conf):  PYTHON_LIBS="$(pkg-config --libs python3-embed)"
BuildOption(conf):  --disable-fetch-external
BuildOption(conf):  --with-external-tar=%{_sourcedir}
BuildOption(conf):  --with-parallelism=%{_smp_build_ncpus}
# Use system fonts; tests guarded by HAVE_MORE_FONTS are omitted.
BuildOption(conf):  --without-fonts
# Java components, JUnit tests and Java export validators are excluded by this configuration.
BuildOption(conf):  --without-java
BuildOption(conf):  --disable-skia
BuildOption(conf):  --with-system-libs
# Box2D 3 detection leaves the linker library variable unset.
BuildOption(conf):  _BOX2D_LIB=box2d
# libeot 0.0.3 sorts below 0.01 in pkg-config; keep LIBEOT_CFLAGS non-empty when -I/usr/include is stripped.
BuildOption(conf):  LIBEOT_CFLAGS="$(pkg-config --cflags libeot) "
BuildOption(conf):  LIBEOT_LIBS="$(pkg-config --libs libeot)"
# PDFium 8073 uses absl::Cleanup and absl::flat_hash_set in addition to absl::InlinedVector.
BuildOption(conf):  ABSEIL_CFLAGS="$(pkg-config --cflags absl_cleanup absl_flat_hash_set absl_inlined_vector) "
BuildOption(conf):  ABSEIL_LIBS="$(pkg-config --libs absl_cleanup absl_flat_hash_set absl_inlined_vector)"
# Define SYSTEM_OPENSSL for translation units that include curlinit.hxx before config_crypto.h.
BuildOption(conf):  CXXFLAGS="%{build_cxxflags} -DSYSTEM_OPENSSL=1"
# AFDKO 5 provides makeotf as its supported font-generation command.
BuildOption(conf):  MAKEOTF=%{_bindir}/makeotf
# Use the in-tree tools/source/misc/fix16.cxx implementation; libfixmath is not packaged separately.
BuildOption(conf):  --without-system-libfixmath
BuildOption(install):  distro-pack-install

BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  clang
BuildRequires:  cmake(FastFloat)
BuildRequires:  cmake(dragonbox)
BuildRequires:  cmake(frozen)
BuildRequires:  firebird-devel
BuildRequires:  flex
BuildRequires:  fontforge
# Writer, Calc and Impress layout fixtures use Liberation, DejaVu Sans and Noto Sans.
BuildRequires:  fonts-dejavu
BuildRequires:  fonts-liberation
# The Draw contour-text fixture also needs a CJK fallback.
BuildRequires:  fonts-noto-sans-cjk-static
BuildRequires:  fonts-noto-static
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glm-devel
BuildRequires:  gnupg
BuildRequires:  gperf
BuildRequires:  hyphen-devel
BuildRequires:  icu4c
# xmlsec1-nss.pc links against libltdl, whose linker file is owned by libtool.
BuildRequires:  libtool
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  lpsolve-devel
BuildRequires:  make
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(absl_cleanup)
BuildRequires:  pkgconfig(absl_flat_hash_set)
BuildRequires:  pkgconfig(absl_inlined_vector)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(box2d)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(coinmp)
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gpgmepp)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz-icu)
BuildRequires:  pkgconfig(harfbuzz-subset)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libabw-0.1)
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(libcmis-0.6)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libe-book-0.1)
BuildRequires:  pkgconfig(libeot)
BuildRequires:  pkgconfig(libepubgen-0.1)
BuildRequires:  pkgconfig(libetonyek-0.1)
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libexttextcat)
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblangtag)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libmwaw-0.3)
BuildRequires:  pkgconfig(libnumbertext)
BuildRequires:  pkgconfig(libodfgen-0.1)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(liborcus-0.21)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libstaroffice-0.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libzmf-0.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(md4c-html)
BuildRequires:  pkgconfig(mdds-3.0)
BuildRequires:  pkgconfig(mythes)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  pkgconfig(raptor2)
BuildRequires:  pkgconfig(redland)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmlsec1-nss)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
# Barcode generation requires zxing-cpp >= 3.2.0 built with writers enabled.
BuildRequires:  pkgconfig(zxing) >= 3.2.0
BuildRequires:  poppler-data
BuildRequires:  python-afdko
BuildRequires:  python3dist(lxml)
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  zxcvbn-c-devel

Requires:       %{name}-base%{?_isa} = %{version}-%{release}
Requires:       %{name}-calc%{?_isa} = %{version}-%{release}
Requires:       %{name}-draw%{?_isa} = %{version}-%{release}
Requires:       %{name}-impress%{?_isa} = %{version}-%{release}
Requires:       %{name}-math%{?_isa} = %{version}-%{release}
Requires:       %{name}-writer%{?_isa} = %{version}-%{release}

%patchlist
# Backport only the slideshow Box2D 3.2 API hunk from upstream commit 8927e95539463a027c6f28da2ac5ac46746cf1bd.
# https://github.com/LibreOffice/core/commit/8927e95539463a027c6f28da2ac5ac46746cf1bd
1000-support-box2d-3.2-slideshow.patch
# System lp_solve 5.5.2.14 finds the true knapsack optimum (6987 instead of 6981).
# Backport only the expected-value correction while retaining this release's lp_solve engine.
# https://github.com/LibreOffice/core/commit/bfc9cfdecf54885bb0d38ad29fee36affd0d9df5
1001-correct-knapsack-optimum.patch
# Keep the upstream outline fixture on its intended Writer filter and template.
2000-keep-writer-html-template-and-test-isolation.patch
# Keep document formula settings local and restore the export test locale.
2001-preserve-calc-document-settings-and-test-locales.patch
# Preserve encoded formula errors across external-reference and inline matrix aggregates on architectures with canonical NaNs.
2002-preserve-formula-errors-in-matrix-aggregates.patch
%ifarch riscv64
# Honor the native call-stack ABI and synchronize generated bridge instructions.
2003-flush-generated-riscv64-bridge-instructions.patch
2004-honor-stack-layout-in-riscv64-bridge-calls.patch
%endif

%description
LibreOffice provides word processing, spreadsheets, presentations, drawings,
formula editing and database access. This package installs all applications.
Java components, including the HSQLDB engine, JDBC, Report Builder and the
Java-based script providers, are not included.

%package        core
Summary:        Shared runtime and desktop integration for LibreOffice
Provides:       bundled(agg) = 2.3
Provides:       bundled(libfixmath)
Provides:       bundled(pdfium) = 8073
Recommends:     fonts-dejavu
Recommends:     fonts-liberation
Recommends:     sane-backends
# GPGME uses the external OpenPGP engine for document signing and encryption.
Requires:       gnupg
# PDF import converts embedded CID fonts with makeotf.
Requires:       python-afdko

%description    core
The shared LibreOffice runtime includes the application launcher, UNO
components, document filters and desktop integration.

%package        base
Summary:        Database front end for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    base
Base edits database tables, queries and forms. It connects to embedded
Firebird databases and external database servers through native drivers or ODBC.

%package        calc
Summary:        Spreadsheet editor for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    calc
Calc edits spreadsheets, calculates formulas and creates charts.

%package        draw
Summary:        Drawing and diagram editor for LibreOffice
Requires:       poppler-data
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    draw
Draw creates vector drawings, diagrams and multipage illustrations.

%package        impress
Summary:        Presentation editor for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    impress
Impress creates slide presentations with drawings, transitions and
speaker notes.

%package        math
Summary:        Formula editor for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    math
Math typesets mathematical expressions for use in LibreOffice documents.

%package        writer
Summary:        Word processor for LibreOffice
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    writer
Writer edits text documents and reads and writes OpenDocument Text
and Microsoft Word files.

%package        langpack-zh
Summary:        Simplified Chinese translations for LibreOffice
Recommends:     (fonts-noto-sans-cjk-vf or fonts-noto-sans-cjk-static)
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-core and langpacks-zh)

%description    langpack-zh
Simplified Chinese menus, messages, templates and configuration resources
for LibreOffice.

%prep -a
# Regenerate configure from configure.ac; LibreOffice does not use automake or libtoolize.
autoconf -I m4

# Remove tests that cannot run reliably in the openRuyi build root from Module_*.mk
# so the default autotools `make check` runs unitcheck, slowcheck, subsequentcheck and uicheck.
skip_tests=(
    # Fixture state/order leaks and GnuPG socket path limits in the build root.
    basic:CppunitTest_basic_macros
    sc:CppunitTest_sc_ucalc_formula
    sc:CppunitTest_sc_tiledrendering
    sw:CppunitTest_sw_tiledrendering
    sw:CppunitTest_sw_uiwriter4
    unoxml:CppunitTest_unoxml_rdftest
    vcl:CppunitTest_vcl_text
    xmlsecurity:CppunitTest_xmlsecurity_signing
    xmlsecurity:CppunitTest_xmlsecurity_signing2
    xmlsecurity:UITest_xmlsecurity_gpg
    # Font-dependent bullet character-grid dialog and disabled Java HSQLDB UI tests.
    sw:UITest_writer_tests2
    dbaccess:UITest_edit_field
    dbaccess:UITest_query
    # Layout and export fixtures requiring unbundled Carlito (Calibri metrics).
    chart2:CppunitTest_chart2_import
    chart2:CppunitTest_chart2_import2
    chart2:CppunitTest_chart2_export2
    svx:CppunitTest_svx_unit
    sc:CppunitTest_sc_jumbosheets_test
    sc:CppunitTest_sc_subsequent_export_test4
    sc:CppunitTest_sc_subsequent_filters_test3
    sc:CppunitTest_sc_uicalc2
    sc:CppunitTest_sc_vba_macro_test
    sd:CppunitTest_sd_layout_tests
    sw:CppunitTest_sw_core_objectpositioning
    sw:CppunitTest_sw_globalfilter
    sw:CppunitTest_sw_odfexport3
    sw:CppunitTest_sw_ooxmlexport11
    sw:CppunitTest_sw_ooxmlexport12
    sw:CppunitTest_sw_ooxmlexport13
    sw:CppunitTest_sw_ooxmlexport21
    sw:CppunitTest_sw_ooxmlexport23
    sw:CppunitTest_sw_ooxmlexport25
    sw:CppunitTest_sw_ooxmlexport26
    sw:CppunitTest_sw_ooxmlexport_de_locale
    sw:CppunitTest_sw_ooxmlimport
    sw:CppunitTest_sw_uiwriter3
    sw:CppunitTest_sw_ww8export2
    vcl:CppunitTest_vcl_pdfexport
    # Layout fixtures requiring unbundled Source Han Serif SC, Reem Kufi, Caladea,
    # Amiri, Linux Libertine G, or full upstream Noto / Hebrew font families.
    sw:CppunitTest_sw_core_text
    svgio:CppunitTest_svgio
    sw:CppunitTest_sw_core_layout
    sw:CppunitTest_sw_layoutwriter
    sw:CppunitTest_sw_layoutwriter2
    sw:CppunitTest_sw_layoutwriter3
    sw:CppunitTest_sw_layoutwriter4
    sw:CppunitTest_sw_layoutwriter5
    sw:CppunitTest_sw_layoutwriter6
    vcl:CppunitTest_vcl_pdfexport2
)
for entry in "${skip_tests[@]}"; do
    mod=${entry%%:*}
    target=${entry#*:}
    mk="$mod/Module_${mod}.mk"
    grep -qE '^[[:space:]]*'"$target"'[[:space:]]*\\$' "$mk"
    sed -i -E '/^[[:space:]]*'"$target"'[[:space:]]*\\$/d' "$mk"
done

%install -a
# LibreOffice also loads localized registries and templates from its own tree.
# Keep its catalog lookup path while allowing find_lang to identify the domains.
resources=%{_libdir}/%{name}/program/resource
catalogs=%{_datadir}/%{name}/locale
install -d "%{buildroot}$catalogs/zh_CN"
mv "%{buildroot}$resources/zh_CN/LC_MESSAGES" "%{buildroot}$catalogs/zh_CN/"
ln -sr "%{buildroot}$catalogs/zh_CN/LC_MESSAGES" "%{buildroot}$resources/zh_CN/LC_MESSAGES"
sed -i "\|$resources/zh_CN/LC_MESSAGES|d" file-lists/lang_zh_CN_list.txt
# Define the language package manually to include .xcd registries and .bau autotext
# alongside gettext catalogs; find_lang does not discover these LibreOffice files.
# Depend on libreoffice-core rather than the full suite required by the default
# language-package template.
%find_lang %{name} --all-name

# KDE/Qt desktop integration is not enabled in this build.
rm -f "%{buildroot}%{_datadir}/metainfo/org.libreoffice.kde.metainfo.xml"

# Java integration is disabled by --without-java.
rm -f "%{buildroot}%{_libdir}/%{name}/program/java-set-classpath"
sed -i '\|/program/java-set-classpath$|d' file-lists/common_list.txt

# RPM reads desktop MIME types through these links while the files are staged.
xdg=%{buildroot}%{_libdir}/%{name}/share/xdg
applications=%{buildroot}%{_datadir}/applications
ln -srf "$xdg/base.desktop" "$applications/%{name}-base.desktop"
ln -srf "$xdg/calc.desktop" "$applications/%{name}-calc.desktop"
ln -srf "$xdg/draw.desktop" "$applications/%{name}-draw.desktop"
ln -srf "$xdg/impress.desktop" "$applications/%{name}-impress.desktop"
ln -srf "$xdg/math.desktop" "$applications/%{name}-math.desktop"
ln -srf "$xdg/startcenter.desktop" "$applications/%{name}-startcenter.desktop"
ln -srf "$xdg/writer.desktop" "$applications/%{name}-writer.desktop"
ln -srf "$xdg/xsltfilter.desktop" "$applications/%{name}-xsltfilter.desktop"
ln -srf %{buildroot}%{_libdir}/%{name}/program/soffice %{buildroot}%{_bindir}/%{name}
ln -srf %{buildroot}%{_libdir}/%{name}/program/soffice %{buildroot}%{_bindir}/soffice

# Bash looks up completions by command name.
completions=%{bash_completions_dir}
ln -s libreoffice.sh "%{buildroot}$completions/libreoffice"
ln -s libreoffice.sh "%{buildroot}$completions/soffice"
ln -s libreoffice.sh "%{buildroot}$completions/loffice"
ln -s libreoffice.sh "%{buildroot}$completions/lofromtemplate"
ln -s libreoffice.sh "%{buildroot}$completions/unopkg"
ln -s libreoffice.sh "%{buildroot}$completions/lowriter"
ln -s libreoffice.sh "%{buildroot}$completions/loweb"
ln -s libreoffice.sh "%{buildroot}$completions/lobase"
ln -s libreoffice.sh "%{buildroot}$completions/localc"
ln -s libreoffice.sh "%{buildroot}$completions/lodraw"
ln -s libreoffice.sh "%{buildroot}$completions/loimpress"
ln -s libreoffice.sh "%{buildroot}$completions/lomath"
printf '%s\n' "$completions/libreoffice" "$completions/soffice" "$completions/loffice" "$completions/lofromtemplate" "$completions/unopkg" >> file-lists/common_list.txt
printf '%s\n' "$completions/lowriter" "$completions/loweb" >> file-lists/writer_list.txt
printf '%s\n' "$completions/lobase" >> file-lists/base_list.txt
printf '%s\n' "$completions/localc" >> file-lists/calc_list.txt
printf '%s\n' "$completions/lodraw" >> file-lists/draw_list.txt
printf '%s\n' "$completions/loimpress" >> file-lists/impress_list.txt
printf '%s\n' "$completions/lomath" >> file-lists/math_list.txt

# The installer lists private directories in several application manifests.
# The core runtime owns them so individual applications can be removed safely.
sed -n '/^%%dir /p' file-lists/*_list.txt |
    sort -u | sed "\|$resources/zh_CN/LC_MESSAGES|d" > file-lists/directories.list
sed -i '/^%%dir /d' file-lists/*_list.txt
cat file-lists/common_list.txt file-lists/lang_en_US_list.txt file-lists/gnome_list.txt |
    sort -u > file-lists/core.list
sed -i '/\/LICENSE\(\.html\)\?$/d' file-lists/core.list
sort -u file-lists/base_list.txt file-lists/postgresql_list.txt > file-lists/base.list

%files

%files core -f file-lists/core.list -f file-lists/directories.list
%doc README.md
%license COPYING COPYING.LGPL COPYING.MPL
%license workdir/UnpackedTarball/pdfium/LICENSE workdir/UnpackedTarball/pdfium/third_party/agg23/copying
%license %{_libdir}/libreoffice/LICENSE
%license %{_libdir}/libreoffice/LICENSE.html
%dir %{_datadir}/libreoffice
%dir %{_datadir}/libreoffice/locale
%{_libdir}/libreoffice/share/libreofficekit/

%files base -f file-lists/base.list
%{_datadir}/metainfo/libreoffice-base.appdata.xml

%files calc -f file-lists/calc_list.txt
%{_datadir}/metainfo/libreoffice-calc.appdata.xml

%files draw -f file-lists/draw_list.txt
%{_datadir}/metainfo/libreoffice-draw.appdata.xml

%files impress -f file-lists/impress_list.txt
%{_datadir}/metainfo/libreoffice-impress.appdata.xml

%files math -f file-lists/math_list.txt

%files writer -f file-lists/writer_list.txt
%{_datadir}/metainfo/libreoffice-writer.appdata.xml

%files langpack-zh -f file-lists/lang_zh_CN_list.txt -f %{name}.lang
%lang(zh) %dir %{_datadir}/libreoffice/locale/zh_CN
%lang(zh) %dir %{_datadir}/libreoffice/locale/zh_CN/LC_MESSAGES
%lang(zh) %{_libdir}/libreoffice/program/resource/zh_CN/LC_MESSAGES

%changelog
%autochangelog
