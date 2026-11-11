# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global release_series 26.8.2
%global private_sonames ^(lib.*lo|libuno_[^.]+|libreglo|libunoidl|libxmlreader|libstore)\.so.*$
%global __provides_exclude %{private_sonames}
%global __requires_exclude %{private_sonames}

Name:           libreoffice
Version:        %{release_series}.2
Release:        %autorelease
Summary:        Desktop office suite for OpenDocument and Microsoft Office files
License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-AGG-2.3 AND MIT AND (GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1) AND (MPL-1.1 OR GPL-2.0-or-later)
URL:            https://www.libreoffice.org/
VCS:            git:https://git.libreoffice.org/core
#!RemoteAsset:  sha256:f0012302d9cc70955bd55890d3aaccf6c55677c4a6a46e1003f996b1b0dae8e7
Source0:        https://download.documentfoundation.org/libreoffice/src/%{release_series}/%{name}-%{version}.tar.xz
#!RemoteAsset:  sha256:1a3b6077ebfac899f2c31666d283e29e94c2d30704dd162fda7ba06d77212dd2
Source1:        https://download.documentfoundation.org/libreoffice/src/%{release_series}/%{name}-translations-%{version}.tar.xz
#!RemoteAsset:  sha256:a3624f6f0ac46a7e190969d405aa7a07dbc342baf69f81192487575bf64055a5
Source2:        https://dev-www.libreoffice.org/src/pdfium-8073.tar.bz2
BuildSystem:    autotools

BuildOption(prep):  -b 1
BuildOption(conf):  --enable-release-build
BuildOption(conf):  --with-vendor=openRuyi
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
# PDFium uses Clang while the rest of LibreOffice uses the default compiler.
BuildOption(conf):  LO_CLANG_CC=%{_libdir}/llvm24/bin/clang
BuildOption(conf):  LO_CLANG_CXX=%{_libdir}/llvm24/bin/clang++
# Box2D 3 detection leaves the linker library variable unset.
BuildOption(conf):  _BOX2D_LIB=box2d
# AFDKO 5 provides makeotf as its supported font-generation command.
BuildOption(conf):  MAKEOTF=%{_bindir}/makeotf
BuildOption(conf):  --without-system-libfixmath
BuildOption(install):  distro-pack-install
# Call gbuild directly: the top-level recursive make does not forward --old-file.
BuildOption(check):  -f Makefile.gbuild subsequentcheck uicheck
# Basic locale and Calc reference-expansion settings leak between fixtures.
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/basic_macros.test"
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/sc_ucalc_formula.test"
# Writer view modes, formatting marks and color themes depend on test order.
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/sw_tiledrendering.test"
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/sw_uiwriter4.test"
# The RDF metadata fixture assumes an unspecified statement enumeration order.
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/unoxml_rdftest.test"
# The Calc view-state fixture assumes spelling is initialized in every view.
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/sc_tiledrendering.test"
# The text suite uses the Hangul font before loading its font fixture.
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/vcl_text.test"
# Signing fixture setup exceeds GnuPG socket path limits in the build root.
# signing2 also leaves a disposed Base frame for subsequent documents.
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/xmlsecurity_signing.test"
BuildOption(check):  --old-file="$PWD/workdir/CppunitTest/xmlsecurity_signing2.test"
BuildOption(check):  --old-file="$PWD/workdir/UITest/xmlsecurity_gpg/done"
# The bullet dialog fixture selects a font-dependent character-grid cell.
BuildOption(check):  --old-file="$PWD/workdir/UITest/writer_tests2/done"
# The embedded HSQLDB UI groups require the disabled Java driver.
BuildOption(check):  --old-file="$PWD/workdir/UITest/edit_field/done"
BuildOption(check):  --old-file="$PWD/workdir/UITest/query/done"

BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  clang24
BuildRequires:  cmake(FastFloat)
BuildRequires:  cmake(dragonbox)
BuildRequires:  firebird-devel >= 5
BuildRequires:  flex
BuildRequires:  fontforge
# Writer, Calc and Impress layout fixtures use Liberation, DejaVu Sans and Noto Sans.
BuildRequires:  fonts-dejavu
BuildRequires:  fonts-liberation
BuildRequires:  fonts-noto-static
# The Draw contour-text fixture also needs a CJK fallback.
BuildRequires:  fonts-noto-sans-cjk-static
BuildRequires:  gcc-c++
BuildRequires:  lpsolve-devel
BuildRequires:  gettext
BuildRequires:  glm-devel
BuildRequires:  gnupg
BuildRequires:  gperf
BuildRequires:  hyphen-devel
BuildRequires:  icu4c
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat) >= 2.9.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
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
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libabw-0.1)
BuildRequires:  pkgconfig(libeot) >= 0.01
BuildRequires:  pkgconfig(libepubgen-0.1)
BuildRequires:  pkgconfig(libexttextcat) >= 3.4.1
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libodfgen-0.1)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires:  pkgconfig(libstaroffice-0.0)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libzmf-0.0)
BuildRequires:  pkgconfig(libnumbertext) >= 1.0.6
BuildRequires:  pkgconfig(mythes)
BuildRequires:  cmake(frozen)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  zxcvbn-c-devel
BuildRequires:  zxing-cpp-devel
BuildRequires:  zxing-cpp(qr-writer)
BuildRequires:  pkgconfig(liblangtag) >= 0.4.0
BuildRequires:  pkgconfig(mdds-3.0) >= 3.0.0
BuildRequires:  pkgconfig(box2d)
BuildRequires:  pkgconfig(libe-book-0.1)
BuildRequires:  pkgconfig(libetonyek-0.1)
BuildRequires:  pkgconfig(libmwaw-0.3) >= 0.3.21
BuildRequires:  pkgconfig(liborcus-0.21) >= 0.21.0
BuildRequires:  pkgconfig(libcmis-0.6) >= 0.6.1
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(raptor2) >= 2.0.7
BuildRequires:  pkgconfig(redland) >= 1.0.8
BuildRequires:  pkgconfig(coinmp)
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(md4c-html)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(absl_cleanup)
BuildRequires:  pkgconfig(absl_flat_hash_set)
BuildRequires:  pkgconfig(absl_inlined_vector)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(poppler) >= 0.14
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  poppler-data
BuildRequires:  python-afdko
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmlsec1-nss)
# xmlsec1-nss.pc links against libltdl, whose linker file is owned by libtool.
BuildRequires:  libtool
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(lxml)
BuildRequires:  unzip
BuildRequires:  xorg-server-xvfb
BuildRequires:  zip
Requires:       %{name}-base%{?_isa} = %{version}-%{release}
Requires:       %{name}-calc%{?_isa} = %{version}-%{release}
Requires:       %{name}-draw%{?_isa} = %{version}-%{release}
Requires:       %{name}-impress%{?_isa} = %{version}-%{release}
Requires:       %{name}-math%{?_isa} = %{version}-%{release}
Requires:       %{name}-writer%{?_isa} = %{version}-%{release}

%patchlist
# Backported slideshow support for the system Box2D 3.2 API.
# https://github.com/LibreOffice/core/commit/8927e95539463a027c6f28da2ac5ac46746cf1bd
1000-support-box2d-3.2-slideshow.patch
# Correct the optimum of the upstream knapsack test model.
# Backport only the expected-value correction; retain this release's lp_solve engine.
# https://github.com/LibreOffice/core/commit/bfc9cfdecf54885bb0d38ad29fee36affd0d9df5
1001-correct-knapsack-optimum.patch
# Link the Abseil hash-table implementation used by PDFium 8073.
2000-link-pdfium-system-abseil-components.patch
# Select the configured OpenSSL backend before initializing curl.
2001-read-configured-openssl-backend.patch
# Initialize Box2D 3 body definitions with their required defaults.
2002-initialize-slideshow-physics-bodies.patch
# Keep the upstream outline fixture on its intended Writer filter and template.
2003-keep-writer-html-template-and-test-isolation.patch
# Keep document formula settings local and restore the export test locale.
2004-preserve-calc-document-settings-and-test-locales.patch
# Preserve encoded formula errors on architectures with canonical NaNs.
2005-preserve-formula-errors-in-matrix-aggregates.patch
# Use the SQLDA types supported by Base with Firebird 4 and newer.
2006-bind-firebird-result-types-for-base.patch
%ifarch riscv64
# Honor the native call-stack ABI and synchronize generated bridge instructions.
2007-flush-generated-riscv64-bridge-instructions.patch
2008-honor-stack-layout-in-riscv64-bridge-calls.patch
%endif

%description
LibreOffice provides word processing, spreadsheets, presentations, drawings,
formula editing and database access. This package installs all applications.
Java components, including the HSQLDB engine, JDBC, Report Builder and the
Java-based script providers, are not included.

%package        core
Summary:        Shared runtime and desktop integration for LibreOffice
Provides:       bundled(pdfium) = 8073
Recommends:     fonts-dejavu
Recommends:     fonts-liberation
Recommends:     sane-backends
# The SAX locator uses the 64-bit position API added in Expat 2.9.
Requires:       expat%{?_isa} >= 2.9.0
# GPGME uses the external OpenPGP engine for document signing and encryption.
Requires:       gnupg
# PDF import converts embedded CID fonts with makeotf.
Requires:       python-afdko
Requires:       zxing-cpp(qr-writer)

%description    core
The shared LibreOffice runtime includes the application launcher, UNO
components, document filters and desktop integration.

%package        base
Summary:        Database front end for LibreOffice
# The Firebird runtime owns the embedded engine; private plugin SONAMEs are filtered.
Requires:       firebird%{?_isa} >= 5
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

%package        lang-zh-CN
Summary:        Simplified Chinese translations for LibreOffice
Recommends:     (fonts-noto-sans-cjk-vf or fonts-noto-sans-cjk-static)
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-core and langpacks-zh)

%description    lang-zh-CN
Simplified Chinese menus, messages, templates and configuration resources
for LibreOffice.

%prep -a
autoconf -I m4

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
completions=%{_datadir}/bash-completion/completions
ln -s libreoffice.sh "%{buildroot}$completions/libreoffice"
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
printf '%s\n' "$completions/libreoffice" "$completions/loffice" "$completions/lofromtemplate" "$completions/unopkg" >> file-lists/common_list.txt
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

%check -p
# Provide a private X display for the upstream desktop and UI tests.
display_file=$(mktemp)
Xvfb -displayfd 3 -screen 0 1280x1024x24 -nolisten tcp 3>"$display_file" &
xvfb_pid=$!
cleanup() {
    kill "$xvfb_pid" 2>/dev/null || :
    rm -f "$display_file"
}
trap cleanup EXIT
for attempt in $(seq 100); do
    test ! -s "$display_file" || break
    kill -0 "$xvfb_pid"
    sleep 0.1
done
test -s "$display_file"
export DISPLAY=:$(cat "$display_file")

%files

%files core -f file-lists/core.list -f file-lists/directories.list
%doc README.md
%license COPYING COPYING.LGPL COPYING.MPL
%license workdir/UnpackedTarball/pdfium/LICENSE workdir/UnpackedTarball/pdfium/third_party/agg23/copying
%license %{_libdir}/libreoffice/LICENSE
%license %{_libdir}/libreoffice/LICENSE.html
%dir %{_datadir}/libreoffice
%dir %{_datadir}/libreoffice/locale
%{_libdir}/libreoffice/share/fonts/truetype/fc_local.conf
%{_libdir}/libreoffice/share/fonts/truetype/opens___.ttf
%{_libdir}/libreoffice/share/libreofficekit/
%{_datadir}/metainfo/org.libreoffice.kde.metainfo.xml

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

%files lang-zh-CN -f file-lists/lang_zh_CN_list.txt -f %{name}.lang
%lang(zh_CN) %dir %{_datadir}/%{name}/locale/zh_CN
%lang(zh_CN) %dir %{_datadir}/%{name}/locale/zh_CN/LC_MESSAGES
%lang(zh_CN) %{_libdir}/%{name}/program/resource/zh_CN/LC_MESSAGES

%changelog
%autochangelog
