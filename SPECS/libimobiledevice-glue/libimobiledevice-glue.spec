# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libimobiledevice-glue
Version:        1.3.2
Release:        %autorelease
Summary:        Library with common code among libimobiledevice projects
License:        LGPL-2.1-or-later
URL:            https://github.com/libimobiledevice/libimobiledevice-glue
#!RemoteAsset:  sha256:1f780f40797e84ee60840a47d828f390071a0fb30501cb9ea092c2e8be6a874d
Source0:        https://github.com/libimobiledevice/libimobiledevice-glue/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libplist-2.0)

%description
The libimobiledevice-glue library is library with common code used by libraries
and tools around the libimobiledevice project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep -a
echo "%{version}" > .tarball-version

%conf -p
./autogen.sh

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libimobiledevice-glue-1.0.so.*

%files devel
%{_includedir}/libimobiledevice-glue/
%{_libdir}/libimobiledevice-glue-1.0.so
%{_libdir}/pkgconfig/libimobiledevice-glue-1.0.pc

%changelog
%autochangelog
