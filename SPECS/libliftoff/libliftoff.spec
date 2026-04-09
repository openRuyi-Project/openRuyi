# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libliftoff
Version:        0.5.0
Release:        %autorelease
Summary:        Lightweight KMS plane library
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libliftoff
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/emersion/libliftoff/-/archive/v%{version}/libliftoff-v%{version}.tar.gz
BuildSystem:    meson

# increases the default allocation timeout from 1ms to 100ms to provide more buffer for resource allocation tasks.
# just for tests.
Patch:          0001-increase-alloc-timeout.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  ninja
BuildRequires:  pkgconfig(libdrm)

%description
libliftoff eases the use of KMS planes from userspace. It allows users to
create "virtual planes" (layers), set KMS properties on them, and then
allocates hardware planes for these layers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSE
%doc README.md
%{_libdir}/libliftoff.so.0*

%files devel
%{_includedir}/libliftoff.h
%{_libdir}/libliftoff.so
%{_libdir}/pkgconfig/libliftoff.pc

%changelog
%autochangelog
