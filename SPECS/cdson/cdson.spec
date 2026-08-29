# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cdson
Version:        1.0.0
Release:        %autorelease
Summary:        C library for the DSON data serialization format, for humans
License:        MPL-2.0
URL:            https://github.com/frozencemetery/cdson
#!RemoteAsset:  sha256:7384d2bd30e55e8929c7ad113fa7b83c5aa8aef86116e9359e680178c587e75a
Source0:        https://github.com/frozencemetery/cdson/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dc_args=-Wno-error=unused-result

BuildRequires:  meson

%patchlist
# https://github.com/frozencemetery/cdson/commit/f1b3389a7fc4a1b8594a5dee415c3ecf80b413aa
0001-tests-fix-build-on-legacy-32-bit-machines.patch
# https://github.com/frozencemetery/cdson/commit/b92cbab48a7f1f79b6095382d605692f9cee93a6
0002-build-version-the-shared-objects.patch

%description
A pure C parsing and serialization library for the DSON data serialization
format, for humans. cdson is believed to have complete spec coverage, though
as with any project, there may still be bugs.

%package        devel
Summary:        Development headers for cdson
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
A pure C parsing and serialization library for the DSON data serialization
format, for humans. cdson is believed to have complete spec coverage, though
as with any project, there may still be bugs.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cdson library.

%files
%license LICENSE
%{_libdir}/libcdson.so.*

%files devel
%{_includedir}/cdson.h
%{_libdir}/pkgconfig/cdson.pc
%{_libdir}/libcdson.so

%changelog
%autochangelog
