# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zimg
Version:        3.0.6
Release:        %autorelease
Summary:        Scaling, color space conversion, and dithering library
License:        WTFPL
URL:            https://github.com/sekrit-twc/zimg
#!RemoteAsset
Source:         https://github.com/sekrit-twc/zimg/archive/refs/tags/release-%{version}.tar.gz
Patch:          0001-fix-build.patch
BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --enable-testapp

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
The "z" library implements the commonly required image processing basics of
scaling, color space conversion, and depth conversion.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -vif

%install -a
install -m 755 -p -D testapp %{buildroot}%{_bindir}/testapp

# Pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%files
%license COPYING
%doc README.md ChangeLog
%{_libdir}/libzimg.so.*

%files devel
%{_bindir}/testapp
%{_includedir}/*
%{_libdir}/libzimg.so
%{_libdir}/pkgconfig/zimg.pc

%changelog
%{?autochangelog}
