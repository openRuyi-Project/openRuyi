# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ncurses
Version:        6.5
Release:        %autorelease
Summary:        Terminal control library
License:        MIT
URL:            https://invisible-island.net/ncurses/ncurses.html
VCS:            git:git://ncurses.scripts.mit.edu/ncurses.git
#!RemoteAsset:  sha256:136d91bc269a9a5785e5f9e980bc76ab57428f604ce3e5a5a90cebc767971cc6
Source:         https://invisible-mirror.net/archives/ncurses/ncurses-%{version}.tar.gz
BuildSystem:    autotools

# Patch for removing hardcoded path
Patch0:         0001-ncurses-config.patch
# Patch for cleaning up and simplying the linking process
Patch1:         0002-ncurses-libs.patch
# Patch for adding terminal definition for rxvt-unicode
Patch2:         0003-ncurses-urxvt.patch
# Patch for fixing backspace key configuration in rxvt and screen terminals
Patch3:         0004-ncurses-kbs.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gpm-devel
BuildRequires:  pkgconfig

%description
The ncurses (new curses) library is a free software emulation of
curses in System V Release 4.0 (SVr4), and more. It uses terminfo
format, supports pads and color and multiple highlights and forms
characters and function-key mapping, and has all the other SVr4-curses
enhancements over BSD curses.

%package        devel
Summary:        Development files for the ncurses library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains development files for the ncurses library,
including headers, symbolic links for libraries, and pkg-config files.

%conf
export CFLAGS="%{build_cflags} -std=gnu17"
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --disable-static \
    --enable-colorfgbg \
    --enable-hard-tabs \
    --enable-overwrite \
    --enable-pc-files \
    --with-versioned-syms=yes \
    --enable-xmc-glitch \
    --disable-wattr-macros \
    --disable-root-environ \
    --with-cxx-shared \
    --with-ospeed=unsigned \
    --with-pkg-config-libdir=%{_libdir}/pkgconfig \
    --with-shared \
    --with-terminfo-dirs=%{_sysconfdir}/terminfo:%{_datadir}/terminfo \
    --with-termlib=tinfo \
    --with-ticlib=tic \
    --with-xterm-kbs=DEL \
    --without-ada

%install -a
find %{buildroot} -type f -name "*.a" -delete -print
mkdir -p %{buildroot}%{_sysconfdir}/terminfo
xz NEWS

(cd %{buildroot}%{_libdir} && for i in lib*w.so; do ln -s $i `echo $i | sed 's/w\\.so$/.so/'`; done)
(cd %{buildroot}%{_libdir}/pkgconfig && for i in *w.pc; do ln -s $i `echo $i | sed 's/w\\.pc$/.pc/'`; done)
(cd %{buildroot}%{_bindir} && for i in ncursesw*-config; do ln -s $i `echo $i | sed 's/w//'`; done)

%files
%license COPYING
%doc ANNOUNCE AUTHORS NEWS.xz README TO-DO
%doc misc/ncurses.supp
%{_bindir}/[cirt]*
%dir %{_sysconfdir}/terminfo
%{_datadir}/tabset
%dir %{_datadir}/terminfo
%{_datadir}/terminfo/*
%{_libdir}/lib*.so.*
%{_mandir}/man1/[cirt]*
%{_mandir}/man5/*
%{_mandir}/man7/*

%files devel
%{_bindir}/ncurses*-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/form.pc
%{_libdir}/pkgconfig/formw.pc
%{_libdir}/pkgconfig/menu.pc
%{_libdir}/pkgconfig/menuw.pc
%{_libdir}/pkgconfig/ncurses++.pc
%{_libdir}/pkgconfig/ncurses++w.pc
%{_libdir}/pkgconfig/ncurses.pc
%{_libdir}/pkgconfig/ncursesw.pc
%{_libdir}/pkgconfig/panel.pc
%{_libdir}/pkgconfig/panelw.pc
%{_libdir}/pkgconfig/tinfo.pc
%{_includedir}/*.h
%{_mandir}/man1/ncurses*-config*
%{_mandir}/man3/*
%doc doc/html/

%changelog
%autochangelog
