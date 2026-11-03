# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libodfgen
Version:        0.1.8
Release:        %autorelease
Summary:        OpenDocument generator for document converters
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://sourceforge.net/p/libwpd/wiki/libodfgen/
VCS:            git:https://git.code.sf.net/p/libwpd/libodfgen
#!RemoteAsset:  sha256:55200027fd46623b9bdddd38d275e7452d1b0ff8aeddcad6f9ae6dc25f610625
Source0:        https://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
BuildSystem:    autotools

# Upstream commit for the 0.1.8 series.
# https://sourceforge.net/p/libwpd/libodfgen/ci/4da0b148def5b40ee60d4cd79762c0f158d64cc7/
Patch0:         0001-include-cstdint.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-test

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)

%description
libodfgen turns librevenge events into OpenDocument text, spreadsheet,
presentation and drawing documents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%check -a
# Run the upstream document generation smoke tests.
%{__make} -C test launch_all

%files
%doc AUTHORS README
%license COPYING.LGPL COPYING.MPL
%{_libdir}/libodfgen-0.1.so.*

%files devel
%{_includedir}/libodfgen-0.1/
%{_libdir}/libodfgen-0.1.so
%{_libdir}/pkgconfig/libodfgen-0.1.pc

%changelog
%autochangelog
