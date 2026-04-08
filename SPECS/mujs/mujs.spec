# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mujs
Version:        1.3.9
Release:        %autorelease
Summary:        An embeddable Javascript interpreter
License:        ISC
URL:            https://mujs.com/
VCS:            git:https://cgit.ghostscript.com/cgi-bin/cgit.cgi/mujs.git
#!RemoteAsset:  sha256:956d5a20dd4efe5aa58673558787b9e2539255f9bf62585e90e1921fa040d89d
Source:         https://mujs.com/downloads/mujs-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags} -fPIC -Wl,-soname,libmujs.so.0"
BuildOption(build):  release
BuildOption(build):  prefix=%{_prefix}
BuildOption(build):  libdir=%{_libdir}
BuildOption(install):  install-shared
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  libdir=%{_libdir}

BuildRequires:  make
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(readline)

%description
MuJS is a lightweight Javascript interpreter designed for embedding in other software
to extend them with scripting capabilities.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# No configure.
%conf

%install -a
mv %{buildroot}%{_libdir}/libmujs.so %{buildroot}%{_libdir}/libmujs.so.0
ln -sf libmujs.so.0 %{buildroot}%{_libdir}/libmujs.so
rm -f %{buildroot}%{_libdir}/libmujs.a

# No tests.
%check

%files
%license COPYING
%doc AUTHORS README docs
%{_bindir}/mujs
%{_bindir}/mujs-pp
%{_libdir}/libmujs.so.0

%files devel
%license COPYING
%doc AUTHORS README
%{_libdir}/pkgconfig/mujs.pc
%{_includedir}/mujs.h
%{_libdir}/libmujs.so

%changelog
%autochangelog
