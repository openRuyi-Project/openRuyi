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
License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND LGPL-2.1-only AND LGPL-3.0-only AND MIT AND (GPL-2.0-only OR LGPL-2.1-only OR MPL-1.1) AND (MPL-1.1 OR GPL-2.0-or-later)
URL:            https://www.libreoffice.org/
VCS:            git:https://git.libreoffice.org/core
#!RemoteAsset:  sha256:f0012302d9cc70955bd55890d3aaccf6c55677c4a6a46e1003f996b1b0dae8e7
Source0:        https://download.documentfoundation.org/libreoffice/src/%{release_series}/%{name}-%{version}.tar.xz
#!RemoteAsset:  sha256:1a3b6077ebfac899f2c31666d283e29e94c2d30704dd162fda7ba06d77212dd2
Source1:        https://download.documentfoundation.org/libreoffice/src/%{release_series}/%{name}-translations-%{version}.tar.xz
# Exact fonts used by the upstream tests; excluded from the installed packages.
#!RemoteAsset:  sha256:b98b67602a2c8880a1770f0b9e37c190f29a7e2ade5616784f0b89fbdb75bf52
Source2:        https://dev-www.libreoffice.org/src/alef-1.001.tar.gz
#!RemoteAsset:  sha256:cae999a9fc5638cb69cf0812e8bca1437ef1ebbf094f8b3c5b3f0a3ea2ef8c3a
Source3:        https://github.com/aliftype/amiri/releases/download/1.001/Amiri-1.001.zip
#!RemoteAsset:  sha256:c48d1c2fd613c9c06c959c34da7b8388059e2408d2bb19845dc3ed35f76e4d09
Source4:        https://commondatastorage.googleapis.com/chromeos-localmirror/distfiles/crosextrafonts-20130214.tar.gz#/368f114c078f94214a308a74c7e991bc-crosextrafonts-20130214.tar.gz
#!RemoteAsset:  sha256:4bd12b6cbc321c1cf16da76e2c585c925ce956a08067ae6f6c64eff6ccfdaf5a
Source5:        https://commondatastorage.googleapis.com/chromeos-localmirror/distfiles/crosextrafonts-carlito-20130920.tar.gz#/c74b7223abe75949b4af367942d96c7a-crosextrafonts-carlito-20130920.tar.gz
#!RemoteAsset:  sha256:6daed104481007752a76905000e71c0093c591c8ef3017d1b18222c277fc52e3
Source6:        https://downloads.sourceforge.net/project/culmus/culmus/0.140/culmus-0.140.tar.gz
#!RemoteAsset:  sha256:7576310b219e04159d35ff61dd4a4ec4cdba4f35c00e002a136f00e96a908b0a
Source7:        https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-2.37.zip#/33e1e61fab06a547851ed308b4ffef42-dejavu-fonts-ttf-2.37.zip
#!RemoteAsset:  sha256:7191c669bf38899f73a2094ed00f7b800553364f90e2637010a69c0e268f25d0
Source8:        https://github.com/liberationfonts/liberation-fonts/files/7261482/liberation-fonts-ttf-2.1.5.tar.gz
#!RemoteAsset:  sha256:8879d89b5ff7b506c9fc28efc31a5c0b954bbe9333e66e5283d27d20a8519ea3
Source9:        https://github.com/liberationfonts/liberation-sans-narrow/files/2579431/liberation-narrow-fonts-ttf-1.07.6.tar.gz
#!RemoteAsset:  sha256:f596257c1db706ce35795b18d7f66a4db99d427725f20e9384914b534142579a
Source10:       https://dev-www.libreoffice.org/src/libre-hebrew-1.0.tar.gz
#!RemoteAsset:  sha256:54adcb2bc8cac0927a647fbd9362f45eff48130ce6e2379dc3867643019e08c5
Source11:       https://numbertext.org/linux/e7a384790b13c29113e22e596ade9687-LinLibertineG-20120116.zip
#!RemoteAsset:  sha256:34390882c196f032811f2a3db8982c1e839f69aae3e4c2c1fdd63203150690df
Source12:       https://github.com/notofonts/arabic/releases/download/NotoKufiArabic-v2.110/NotoKufiArabic-v2.110.zip
#!RemoteAsset:  sha256:6c050ab9bd087d69b733c505a7576e60c528c2f33cd7b91005a5bd7da4514032
Source13:       https://github.com/notofonts/arabic/releases/download/NotoNaskhArabic-v2.021/NotoNaskhArabic-v2.021.zip
#!RemoteAsset:  sha256:0c34df072a3fa7efbb7cbf34950e1f971a4447cffe365d3a359e2d4089b958f5
Source14:       https://github.com/notofonts/latin-greek-cyrillic/releases/download/NotoSans-v2.015/NotoSans-v2.015.zip
#!RemoteAsset:  sha256:a5a34ac1ea01d0d71c083f99440ebfb1f64224474a0d88bb7ef0e2f8d9a996d2
Source15:       https://github.com/notofonts/arabic/releases/download/NotoSansArabic-v2.010/NotoSansArabic-v2.010.zip
#!RemoteAsset:  sha256:eab89b99e134177ca6a3f9f0412a7cb812aafceb13175d686b4c45cb237f64ac
Source16:       https://github.com/notofonts/armenian/releases/download/NotoSansArmenian-v2.008/NotoSansArmenian-v2.008.zip
#!RemoteAsset:  sha256:10e85011008108308e6feab0408242acb07804da61ede3d3ff236461ae07ab1b
Source17:       https://github.com/notofonts/georgian/releases/download/NotoSansGeorgian-v2.005/NotoSansGeorgian-v2.005.zip
#!RemoteAsset:  sha256:df0a71814b4e63644cf40fcc4529111b61266b7a2dafbe95068b29a7520cc3cb
Source18:       https://github.com/notofonts/hebrew/releases/download/NotoSansHebrew-v3.001/NotoSansHebrew-v3.001.zip
#!RemoteAsset:  sha256:5a87c31b1a40ef8147c1e84437e5f0ceba2d4dbbfc0b56a65821ad29870da8c0
Source19:       https://github.com/notofonts/lao/releases/download/NotoSansLao-v2.003/NotoSansLao-v2.003.zip
#!RemoteAsset:  sha256:b12a1ff762680681b7ce4d98dd29a7f54d90f5bcadd10c955afc640a27b3a268
Source20:       https://github.com/notofonts/lisu/releases/download/NotoSansLisu-v2.102/NotoSansLisu-v2.102.zip
#!RemoteAsset:  sha256:0e9a43c8a4b94ac76f55069ed1d7385bbcaf6b99527a94deb5619e032b7e76c1
Source21:       https://github.com/notofonts/latin-greek-cyrillic/releases/download/NotoSerif-v2.015/NotoSerif-v2.015.zip
#!RemoteAsset:  sha256:b21c198a4c76ae598a304decefb3b5c2a4c2d4c3ae226728eff359185f291c6f
Source22:       https://github.com/notofonts/armenian/releases/download/NotoSerifArmenian-v2.008/NotoSerifArmenian-v2.008.zip
#!RemoteAsset:  sha256:cfb41a264b97d463bab6807a5be937ba4a6ddcfa93d519a21b98b0ba73ca27d4
Source23:       https://github.com/notofonts/georgian/releases/download/NotoSerifGeorgian-v2.003/NotoSerifGeorgian-v2.003.zip
#!RemoteAsset:  sha256:99523f4f21051495f18cbd5169ed0d1e9b395eefe770fece1844a4a7a00c46da
Source24:       https://github.com/notofonts/hebrew/releases/download/NotoSerifHebrew-v2.004/NotoSerifHebrew-v2.004.zip
#!RemoteAsset:  sha256:e96a303d3347790b0ef3db274971a989a736ce766ec9ea1bea0e1458568a80b2
Source25:       https://github.com/notofonts/lao/releases/download/NotoSerifLao-v2.003/NotoSerifLao-v2.003.zip
#!RemoteAsset:  sha256:94ae468fd88f37011607f03466bfc3a03fb617682b7bac6419b70de94cac22f0
Source26:       https://github.com/aliftype/reem-kufi/releases/download/v2.0/ReemKufi-2.0.zip
#!RemoteAsset:  sha256:251c8817ceb87d9b661ce1d5b49e732a0116add10abc046be4b8ba5196e149b5
Source27:       https://software.sil.org/downloads/r/scheherazade/Scheherazade-2.100.zip
BuildSystem:    autotools

BuildOption(prep):  -b 1
BuildOption(conf):  --enable-release-build
BuildOption(conf):  --with-vendor=openRuyi
BuildOption(conf):  --with-lang="en-US zh-CN"
BuildOption(conf):  --with-theme=colibre
BuildOption(conf):  --enable-split-app-modules
BuildOption(conf):  --enable-build-opensymbol
BuildOption(conf):  --enable-python=system
BuildOption(conf):  PYTHON_CFLAGS="$(pkg-config --cflags python3-embed)"
BuildOption(conf):  PYTHON_LIBS="$(pkg-config --libs python3-embed)"
BuildOption(conf):  --disable-fetch-external
BuildOption(conf):  --with-external-tar=%{_sourcedir}
BuildOption(conf):  --with-parallelism=%{_smp_build_ncpus}
# Enable the original font-sensitive assertions and upstream font targets.
BuildOption(conf):  --with-fonts
# Java components, JUnit tests and Java export validators are excluded by this configuration.
BuildOption(conf):  --without-java
BuildOption(conf):  --disable-odk
BuildOption(conf):  --disable-epm
BuildOption(conf):  --disable-skia
BuildOption(conf):  --with-system-dicts
BuildOption(conf):  --with-system-libs
# Box2D 3 detection leaves the linker library variable unset.
BuildOption(conf):  _BOX2D_LIB=box2d
# AFDKO 5 provides makeotf as its supported font-generation command.
BuildOption(conf):  MAKEOTF=%{_bindir}/makeotf
BuildOption(conf):  --without-system-libfixmath
BuildOption(install):  distro-pack-install
# Call gbuild directly: the top-level recursive make does not forward --old-file.
BuildOption(check):  -f Makefile.gbuild --keep-going subsequentcheck uicheck
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
BuildRequires:  cmake(FastFloat)
BuildRequires:  cmake(dragonbox)
BuildRequires:  firebird-devel >= 5
BuildRequires:  flex
BuildRequires:  fontforge
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
BuildRequires:  pkgconfig(pdfium)
BuildRequires:  pdfium(font-mapping)
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
# System-library integration for the PDF filters and their upstream tests.
2000-support-system-pdfium.patch
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
Requires:       pdfium(font-mapping)

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
# Keep upstream test fonts in instdir, but ship only the built OpenSymbol face.
fontdir=%{buildroot}%{_libdir}/%{name}/share/fonts/truetype
find "$fontdir" -type f \( -name '*.ttf' -o -name '*.otf' -o -name '*.ttc' \) ! -name opens___.ttf -delete
# Use the upstream runtime Fontconfig rules without the bundled test-font aliases.
{
    printf '<?xml version="1.0"?>\n<!DOCTYPE fontconfig SYSTEM "/etc/fonts/conf.d/fonts.dtd">\n<fontconfig>\n'
    cat extras/source/truetype/symbol/fc_local.snippet postprocess/fontconfig/fc_local.snippet
    printf '</fontconfig>\n'
} > "$fontdir/fc_local.conf"

# LibreOffice also loads localized registries and templates from its own tree.
# Keep its catalog lookup path while allowing find_lang to identify the domains.
resources=%{_libdir}/%{name}/program/resource
catalogs=%{_datadir}/%{name}/locale
install -d "%{buildroot}$catalogs/zh_CN"
mv "%{buildroot}$resources/zh_CN/LC_MESSAGES" "%{buildroot}$catalogs/zh_CN/"
ln -sr "%{buildroot}$catalogs/zh_CN/LC_MESSAGES" "%{buildroot}$resources/zh_CN/LC_MESSAGES"
sed -i "\|$resources/zh_CN/LC_MESSAGES|d" file-lists/lang_zh_CN_list.txt
%find_lang %{name} --all-name

# RPM reads desktop MIME types through these links while the files are staged.
for link in %{buildroot}%{_datadir}/applications/%{name}-*.desktop %{buildroot}%{_bindir}/{%{name},soffice}; do
    target=$(readlink "$link")
    ln -srf "%{buildroot}$target" "$link"
done

# Bash looks up completions by command name.
completions=%{_datadir}/bash-completion/completions
for cmd in libreoffice loffice lofromtemplate unopkg lowriter loweb lobase localc lodraw loimpress lomath; do
    manifest=$(grep -Flx "%{_bindir}/$cmd" file-lists/{common,writer,base,calc,draw,impress,math}_list.txt)
    ln -s libreoffice.sh "%{buildroot}$completions/$cmd"
    echo "$completions/$cmd" >> "$manifest"
done

# The installer lists private directories in several application manifests.
# The core runtime owns them so individual applications can be removed safely.
for list in file-lists/*_list.txt; do
    sed -n '/^%%dir /p' "$list"
done | sort -u | sed "\|$resources/zh_CN/LC_MESSAGES|d" > file-lists/directories.list
for list in file-lists/*_list.txt; do
    sed -i '/^%%dir /d' "$list"
done
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
