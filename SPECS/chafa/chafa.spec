# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           chafa
Version:        1.18.2
Release:        %autorelease
Summary:        Image-to-text converter for terminal
License:        LGPL-3.0-or-later
URL:            https://hpjansson.org/chafa/
VCS:            git:https://github.com/hpjansson/chafa
#!RemoteAsset:  sha256:0b8d9ba9f347e8b6c0c71878217c9b0e478b4a42aa4babea0bf20840567239c2
Source0:        https://github.com/hpjansson/chafa/releases/download/%{version}/chafa-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-gtk-doc

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  gtk-doc

%description
Chafa is a command-line utility that converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode character output that can
be displayed in a terminal.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%conf -p
autoreconf -fiv

%files
%doc README* NEWS
%license COPYING.LESSER
%{_bindir}/chafa
%{_mandir}/man1/chafa.1*
%{_libdir}/libchafa.so.*

%files devel
%{_includedir}/chafa/
%{_libdir}/pkgconfig/chafa.pc
%{_libdir}/libchafa.so
%{_libdir}/chafa/include/chafaconfig.h

%files doc
%license COPYING.LESSER
%doc %{_datadir}/gtk-doc/html/chafa

%changelog
%autochangelog
