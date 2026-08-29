# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: Maybe enable this in the future
%bcond xindy 0

%global tl_year     2026
%global tl_snapshot 20260301

%define _configure ../configure

Name:           texlive
Version:        %{tl_snapshot}
Release:        %autorelease
Summary:        TeX Live binaries
License:        Apache-2.0 AND Artistic-2.0 AND BSD-3-Clause AND GFDL-1.1-or-later AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND Knuth-CTAN AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND LPPL-1.3a AND LPPL-1.3c AND MIT AND OFL-1.1 AND LicenseRef-openRuyi-Public-Domain
URL:            https://tug.org/texlive/
VCS:            git:https://github.com/TeX-Live/texlive-source.git
# Upstream does not provide a http(s) mirror for the source tarball
# See https://tug.org/historic/
#!RemoteAsset:  sha256:cb120d314d3ceb23ac608af17ddd2c623afcf02331f400a0f25eead5b8ac1d70
Source0:        https://mirror.nju.edu.cn/tex-historic/systems/texlive/%{tl_year}/texlive-%{tl_snapshot}-source.tar.xz
BuildSystem:    autotools

# Use gnu++17
Patch1000:      1000-fix-build-with-gcc-16.patch
Patch2000:      2000-add-luajit-support-for-riscv64.patch

BuildOption(prep):  -n texlive-%{tl_snapshot}-source
BuildOption(conf):  --disable-native-texlive-build
BuildOption(conf):  --disable-multiplatform
BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-dialog
BuildOption(conf):  --disable-t1utils
BuildOption(conf):  --disable-psutils
BuildOption(conf):  --disable-dvisvgm
BuildOption(conf):  --disable-xz
BuildOption(conf):  --with-banner-add="/%{_vendor_name}"
BuildOption(conf):  --with-system-zlib
BuildOption(conf):  --with-system-zziplib
BuildOption(conf):  --with-system-libpng
BuildOption(conf):  --with-system-pnglib
BuildOption(conf):  --with-system-ncurses
BuildOption(conf):  --with-system-gd
BuildOption(conf):  --with-system-freetype2
BuildOption(conf):  --with-system-pixman
BuildOption(conf):  --with-system-cairo
BuildOption(conf):  --with-system-harfbuzz
BuildOption(conf):  --with-system-icu
BuildOption(conf):  --with-system-graphite2
BuildOption(conf):  --with-system-gmp
BuildOption(conf):  --with-system-mpfr
BuildOption(conf):  --with-system-potrace
BuildOption(conf):  --with-system-libpaper
BuildOption(conf):  --with-freetype2-include=%{_includedir}/freetype2
%if %{with xindy}
BuildOption(conf):  --enable-xindy
%else
BuildOption(conf):  --disable-xindy
%endif
BuildOption(conf):  --disable-xindy-docs
BuildOption(conf):  --disable-xindy-rules
# Use system psutils
BuildOption(conf):  --disable-psutils
# We don't want Xorg stuff
BuildOption(conf):  --without-x
BuildOption(conf):  --disable-xdvik
BuildOption(conf):  --disable-xpdfopen
# TODO: enable this in the future maybe?
BuildOption(conf):  --disable-dvisvgm
BuildOption(build):  texmf=%{buildroot}%{_datadir}/texmf

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  libpaper-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  potrace-devel
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zziplib)
%if %{with xindy}
BuildRequires:  clisp
BuildRequires:  libffcall-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  libunistring-devel
%endif

Requires:       bash
Requires:       perl

Recommends:     texlive-texmf >= %{version}

Provides:       kpathsea = %{version}-%{release}
%if %{with xindy}
Provides:       xindy = %{version}-%{release}
%endif

%description
TeX Live is a distribution of the TeX typesetting system. This package
contains the architecture-dependent programs and shared libraries, including
TeX engines, kpathsea utilities, and helper programs built from the TeX Live
source tree.

The architecture-independent TeX macro packages, fonts, scripts, and
documentation are packaged separately in texlive-texmf.

%package        devel
Summary:        Development files for TeX Live libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers, pkg-config files, and unversioned shared library
symlinks for development against TeX Live libraries such as kpathsea, ptexenc,
and synctex.

%prep -a
# bibtex-x needs kpathsea flags when building against the packaged tree.
sed -i '/AC_SEARCH_LIBS/a KPSE_KPATHSEA_FLAGS' texk/bibtex-x/configure.ac
(cd texk/bibtex-x && autoreconf -fiv)

# t4ht is installed under the distribution texmf tree in distro packages.
sed -i 's/SELFAUTOPARENT/TEXMFROOT/' texk/tex4htk/t4ht.c

%conf -p
mkdir -p build
cd build

%build -p
cd build

%install -p
cd build

%install -a
# texlinks may run freshly installed TeX Live tools during %%install.
# Force them to use the libkpathsea just staged in %%{buildroot},
# instead of an older system libkpathsea from the build environment.
LD_PRELOAD=%{buildroot}%{_libdir}/libkpathsea.so.6 \
    make DESTDIR=%{buildroot} texlinks

install -d %{buildroot}%{_datadir}/texmf
# Data and documentation are packaged by texlive-texmf
rm -rf %{buildroot}%{_datadir}/texmf-dist
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_mandir}

# Remove links to texmf scripts.
# These belong to texlive-texmf, together with the script files under
# texmf-dist/scripts.
script_links=
for link in %{buildroot}%{_bindir}/*; do
    target="$(readlink -m "$link")"
    case "$target" in
        */scripts/*)
            script_links="$script_links $link"
            ;;
    esac
done
rm -f $script_links

# No static libraries
find %{buildroot}%{_libdir} -name '*.a' -delete

%check
# The upstream test suite is not enabled here because it expects a complete
# TeX Live runtime tree and is too expensive for a normal distribution build.

%files
%{_bindir}/afm2pl
%{_bindir}/afm2tfm
%{_bindir}/aleph
%{_bindir}/amstex
%{_bindir}/autosp
%{_bindir}/axohelp
%{_bindir}/bbox
%{_bindir}/bg5+latex
%{_bindir}/bg5+pdflatex
%{_bindir}/bg5conv
%{_bindir}/bg5latex
%{_bindir}/bg5pdflatex
%{_bindir}/bibtex
%{_bindir}/bibtex8
%{_bindir}/bibtexu
%{_bindir}/cef5conv
%{_bindir}/cef5latex
%{_bindir}/cef5pdflatex
%{_bindir}/cefconv
%{_bindir}/ceflatex
%{_bindir}/cefpdflatex
%{_bindir}/cefsconv
%{_bindir}/cefslatex
%{_bindir}/cefspdflatex
%{_bindir}/cfftot1
%{_bindir}/chkdvifont
%{_bindir}/chktex
%{_bindir}/csplain
%{_bindir}/ctangle
%{_bindir}/ctie
%{_bindir}/ctwill
%{_bindir}/ctwill-proofsort
%{_bindir}/ctwill-refsort
%{_bindir}/ctwill-twinx
%{_bindir}/cweave
%{_bindir}/detex
%{_bindir}/devnag
%{_bindir}/disdvi
%{_bindir}/dt2dv
%{_bindir}/dv2dt
%{_bindir}/dvi2tty
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dvicopy
%{_bindir}/dvidvi
%{_bindir}/dvigif
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6
%{_bindir}/dvilualatex
%{_bindir}/dvilualatex-dev
%{_bindir}/dviluatex
%{_bindir}/dvipdfm
%{_bindir}/dvipdfmx
%{_bindir}/dvipdft
%{_bindir}/dvipng
%{_bindir}/dvipos
%{_bindir}/dvips
%{_bindir}/dviselect
%{_bindir}/dvispc
%{_bindir}/dvitodvi
%{_bindir}/dvitomp
%{_bindir}/dvitype
%{_bindir}/eplain
%{_bindir}/eptex
%{_bindir}/etex
%{_bindir}/euptex
%{_bindir}/extconv
%{_bindir}/gbklatex
%{_bindir}/gbkpdflatex
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/gregorio
%{_bindir}/gsftopk
%{_bindir}/hbf2gf
%{_bindir}/hilatex
%{_bindir}/hishrink
%{_bindir}/histretch
%{_bindir}/hitex
%{_bindir}/inimf
%{_bindir}/initex
%{_bindir}/jadetex
%{_bindir}/kpseaccess
%{_bindir}/kpsereadlink
%{_bindir}/kpsestat
%{_bindir}/kpsewhich
%{_bindir}/lacheck
%{_bindir}/latex
%{_bindir}/latex-dev
%{_bindir}/lollipop
%{_bindir}/luacsplain
%{_bindir}/luahbtex
%{_bindir}/luajithbtex
%{_bindir}/luajittex
%{_bindir}/lualatex
%{_bindir}/lualatex-dev
%{_bindir}/luatex
%{_bindir}/mag
%{_bindir}/makeindex
%{_bindir}/makejvf
%{_bindir}/mendex
%{_bindir}/mex
%{_bindir}/mf
%{_bindir}/mf-nowin
%{_bindir}/mflua
%{_bindir}/mflua-nowin
%{_bindir}/mfluajit
%{_bindir}/mfluajit-nowin
%{_bindir}/mfplain
%{_bindir}/mft
%{_bindir}/mkindex
%{_bindir}/mkocp
%{_bindir}/mkofm
%{_bindir}/mllatex
%{_bindir}/mltex
%{_bindir}/mmafm
%{_bindir}/mmpfb
%{_bindir}/mpost
%{_bindir}/msxlint
%{_bindir}/odvicopy
%{_bindir}/odvitype
%{_bindir}/ofm2opl
%{_bindir}/omfonts
%{_bindir}/opl2ofm
%{_bindir}/optex
%{_bindir}/otangle
%{_bindir}/otfinfo
%{_bindir}/otftotfm
%{_bindir}/otp2ocp
%{_bindir}/outocp
%{_bindir}/ovf2ovp
%{_bindir}/ovp2ovf
%{_bindir}/patgen
%{_bindir}/pbibtex
# xpdfopen: No Xorg
#{_bindir}/pdfclose
%{_bindir}/pdfcsplain
%{_bindir}/pdfetex
%{_bindir}/pdfjadetex
%{_bindir}/pdflatex
%{_bindir}/pdflatex-dev
%{_bindir}/pdfmex
# xpdfopen: No Xorg
#{_bindir}/pdfopen
%{_bindir}/pdftex
%{_bindir}/pdftosrc
%{_bindir}/pdfxmltex
%{_bindir}/pdvitomp
%{_bindir}/pdvitype
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/pktogf
%{_bindir}/pktype
%{_bindir}/platex
%{_bindir}/platex-dev
%{_bindir}/pltotf
%{_bindir}/pmpost
%{_bindir}/pmxab
%{_bindir}/pooltype
%{_bindir}/ppltotf
%{_bindir}/prepmx
%{_bindir}/ps2pk
%{_bindir}/ptekf
%{_bindir}/ptex
%{_bindir}/ptftopl
%{_bindir}/r-mpost
%{_bindir}/r-pmpost
%{_bindir}/r-upmpost
%{_bindir}/scor2prt
%{_bindir}/sjisconv
%{_bindir}/sjislatex
%{_bindir}/sjispdflatex
%{_bindir}/synctex
%{_bindir}/t1dotlessj
%{_bindir}/t1lint
%{_bindir}/t1rawafm
%{_bindir}/t1reencode
%{_bindir}/t1testpage
%{_bindir}/t4ht
%{_bindir}/tangle
%{_bindir}/teckit_compile
%{_bindir}/tex
%{_bindir}/tex2aspc
%if %{with xindy}
%{_bindir}/tex2xindy
%endif
%{_bindir}/tex4ht
%{_bindir}/texlua
%{_bindir}/texluac
%{_bindir}/texluajit
%{_bindir}/texluajitc
%{_bindir}/texprof
%{_bindir}/texprofile
%{_bindir}/texsis
%{_bindir}/tftopl
%{_bindir}/tie
%{_bindir}/tpic2pdftex
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump
%{_bindir}/ttftotype42
%{_bindir}/twill
%{_bindir}/twill-refsort
%{_bindir}/upbibtex
%{_bindir}/updvitomp
%{_bindir}/updvitype
%{_bindir}/uplatex
%{_bindir}/uplatex-dev
%{_bindir}/upmendex
%{_bindir}/upmpost
%{_bindir}/uppltotf
%{_bindir}/uptex
%{_bindir}/uptftopl
%{_bindir}/utf8mex
%{_bindir}/vftovp
%{_bindir}/vlna
%{_bindir}/vptovf
%{_bindir}/weave
%{_bindir}/wofm2opl
%{_bindir}/wopl2ofm
%{_bindir}/wovf2ovp
%{_bindir}/wovp2ovf
# xdvik: No Xorg
#{_bindir}/xdvi
#{_bindir}/xdvi-xaw
%{_bindir}/xdvipdfmx
%{_bindir}/xdvipsk
%{_bindir}/xelatex
%{_bindir}/xelatex-dev
%{_bindir}/xetex
%if %{with xindy}
%{_bindir}/xindy.mem
%{_bindir}/xindy.run
%endif
%{_bindir}/xml2pmx
%{_bindir}/xmltex
%{_libdir}/libkpathsea.so.*
%{_libdir}/libptexenc.so.*
%{_libdir}/libsynctex.so.*
%{_libdir}/libtexlua53.so.*
%{_libdir}/libtexluajit.so.*
%{_datadir}/texmf

%files devel
%{_includedir}/kpathsea/*
%{_includedir}/ptexenc/*
%{_includedir}/synctex/*
%{_includedir}/texlua53/*
%{_includedir}/texluajit/*
%{_libdir}/libkpathsea.so
%{_libdir}/libptexenc.so
%{_libdir}/libsynctex.so
%{_libdir}/libtexlua53.so
%{_libdir}/libtexluajit.so
%{_libdir}/pkgconfig/kpathsea.pc
%{_libdir}/pkgconfig/ptexenc.pc
%{_libdir}/pkgconfig/synctex.pc
%{_libdir}/pkgconfig/texlua53.pc
%{_libdir}/pkgconfig/texluajit.pc

%changelog
%autochangelog
