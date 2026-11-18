# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libeot
Version:        0.0.3
Release:        %autorelease
# Upstream changed versioning from 0.01 to 0.0.3, and RPM sorts 0.01 > 0.0.3; keep Epoch permanently.
Epoch:          1
Summary:        Embedded OpenType font decoder
License:        MPL-2.0
URL:            https://github.com/umanwizard/libeot
#!RemoteAsset:  sha256:2cb904cbe291019b928dbc2231620bcf273be0298f596c2494348e7be1d7051a
Source0:        https://github.com/umanwizard/libeot/archive/refs/tags/v%{version}.tar.gz#/libeot-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
libeot reads Embedded OpenType fonts from documents and web pages.
The eot2ttf utility extracts the underlying TrueType font.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%prep -a
# Generate configure and the host-triplet support files from the upstream tag.
autoreconf -fi

%files
%license LICENSE PATENTS
%{_bindir}/eot2ttf
%{_libdir}/libeot.so.*

%files devel
%{_includedir}/libeot/
%{_libdir}/libeot.so
%{_libdir}/pkgconfig/libeot.pc

%changelog
%autochangelog
