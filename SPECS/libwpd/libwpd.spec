# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libwpd
Version:        0.10.3
Release:        %autorelease
Summary:        WordPerfect document import library
License:        MPL-2.0
URL:            https://libwpd.sourceforge.net/
VCS:            git:https://git.code.sf.net/p/libwpd/code
#!RemoteAsset:  sha256:2465b0b662fdc5d4e3bebcdc9a79027713fb629ca2bff04a3c9251fdec42dd09
Source0:        https://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
BuildSystem:    autotools

# Upstream backport. Map WordPerfect 5 terminal sigma and variant rho to the correct Unicode characters.
# https://sourceforge.net/p/libwpd/code/ci/0d61d2c1e360bc9a3c16b068c1cf42a7a3ffb7b3/
Patch1000:      1000-correct-wordperfect-5-greek-characters.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tools

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)

%description
libwpd parses WordPerfect word-processing documents. The included
tools export them to HTML, plain text or raw document events.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc README
%license COPYING.LGPL COPYING.MPL
%{_bindir}/wpd2html
%{_bindir}/wpd2raw
%{_bindir}/wpd2text
%{_libdir}/libwpd-0.10.so.*

%files devel
%{_includedir}/libwpd-0.10/
%{_libdir}/libwpd-0.10.so
%{_libdir}/pkgconfig/libwpd-0.10.pc

%changelog
%autochangelog
