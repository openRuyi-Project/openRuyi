# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond bootstrap 1

Name:           freetype
Version:        2.14.3
Release:        %autorelease
Summary:        A free and portable font rendering engine
License:        (FTL OR GPL-2.0-or-later) AND BSD-3-Clause AND MIT AND MIT-Modern-Variant AND LicenseRef-openRuyi-Public-Domain AND Zlib
URL:            https://www.freetype.org
VCS:            git:https://gitlab.freedesktop.org/freetype/freetype.git
#!RemoteAsset:  sha256:36bc4f1cc413335368ee656c42afca65c5a3987e8768cc28cf11ba775e785a5f
Source0:        http://download.savannah.gnu.org/releases/freetype/freetype-%{version}.tar.xz
#!RemoteAsset:  sha256:66a988d8bbb58f83efafe555678ac172f70f0b060cf61424fe5460157470fd21
Source1:        http://download.savannah.gnu.org/releases/freetype/freetype-doc-%{version}.tar.xz
Source2:        ftconfig.h
BuildSystem:    autotools

BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libbrotlidec)
%if %{without bootstrap}
BuildRequires:  pkgconfig(harfbuzz)
%endif
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-zlib=yes
BuildOption(conf):  --with-bzip2=yes
BuildOption(conf):  --with-png=yes
BuildOption(conf):  --enable-freetype-config
%if %{without bootstrap}
BuildOption(conf):  --with-harfbuzz=yes
%else
BuildOption(conf):  --with-harfbuzz=no
%endif
BuildOption(conf):  --with-brotli=yes
BuildOption(install):  gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

Provides:       %{name}-bytecode
Provides:       %{name}-subpixel

%patchlist
freetype-2.3.0-enable-spr.patch
freetype-2.2.1-enable-valid.patch
freetype-2.6.5-libtool.patch
freetype-2.8-multilib.patch
freetype-2.10.0-internal-outline.patch
freetype-2.10.1-debughook.patch

%description
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. FreeType is a library which can open and
manage font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.

%package        devel
Summary:        FreeType development libraries and header files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The freetype-devel package includes the static libraries and header files
for the FreeType font rendering engine.

Install freetype-devel if you want to develop programs which will use
FreeType.

%prep -a
tar xf %{SOURCE1} -C ..

%conf -p
# fix libtool rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' builds/unix/libtool || :
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' builds/unix/libtool || :

%install -a
# fix multilib issues
%define wordsize %{__isa_bits}
mv $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig.h \
   $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig-%{wordsize}.h
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig.h

# clean .a / .la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%files
%license LICENSE.TXT docs/FTL.TXT docs/GPLv2.TXT
%{_libdir}/libfreetype.so.*
%doc README

%files devel
%doc docs/CHANGES docs/formats.txt docs/ft2faq.html
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_libdir}/libfreetype.so
%{_bindir}/freetype-config
%{_libdir}/pkgconfig/freetype2.pc
%doc docs/design
%doc docs/glyphs
%doc docs/reference
%doc docs/tutorial
%{_mandir}/man1/*

%changelog
%autochangelog
