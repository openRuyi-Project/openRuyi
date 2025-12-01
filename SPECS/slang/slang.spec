# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           slang
Version:        2.3.3
Release:        %autorelease
Summary:        An interpreted language and programming library
License:        GPL-2.0-or-later
URL:            https://www.jedsoft.org/slang/
#!RemoteAsset
Source0:        https://www.jedsoft.org/releases/slang/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildRequires:      gcc libpng-devel zlib-devel
BuildRequires:      libpng-devel
BuildRequires:      zlib-devel

BuildOption(conf): --with-pnglib=%{_libdir}
BuildOption(conf): --with-pnginc=%{_includedir}
BuildOption(conf): --with-zlib=%{_libdir}
BuildOption(conf): --with-zinc=%{_includedir}
BuildOption(conf): --without-pcre

%description
S-Lang is a multi-platform programmer's library designed to allow
a developer to create robust multi-platform software. It provides
facilities required by interactive applications such as display/
screen management, keyboard input, keymaps, and so on.

%package     devel
Summary:     Development files for %{name}
Requires:    %{name} = %{version}-%{release}

%description devel
Files for %{name} development.

%package     help
Summary:     Help files for %{name}
BuildArch:   noarch

%description help
Help files for %{name}.

%prep
%autosetup -p1
sed -i '/^INSTALL_MODULE=/s/_DATA//' configure

%install
%make_install install-all INSTALL="install -p"

mkdir -p %{buildroot}%{_includedir}/slang
ln -s ../slang.h %{buildroot}%{_includedir}/slang/slang.h
ln -s ../slcurses.h %{buildroot}%{_includedir}/slang/slcurses.h

%files
%config(noreplace) %{_sysconfdir}/slsh.rc
%license COPYING
%doc NEWS
%{_libdir}/libslang.so.2
%{_libdir}/libslang.so.2.*
%{_libdir}/%{name}
%{_bindir}/slsh
%{_datadir}/slsh

%files devel
%doc doc/text/*.txt doc/README doc/*.txt
%{_libdir}/libslang.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libslang.a
%{_includedir}/slang.h
%{_includedir}/slcurses.h
%{_includedir}/%{name}

%files help
%{_mandir}/man1/slsh.1*
/usr/share/doc/slang/v2
/usr/share/doc/slsh

%changelog
%{?autochangelog}
