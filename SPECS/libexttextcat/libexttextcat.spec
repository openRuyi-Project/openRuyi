# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libexttextcat
Version:        3.4.8
Release:        %autorelease
Summary:        Language identification using text fingerprints
License:        BSD-3-Clause
URL:            https://wiki.documentfoundation.org/Libexttextcat
VCS:            git:https://git.libreoffice.org/libexttextcat
#!RemoteAsset:  sha256:76fabd6247b89bfa61671f021470f115ea3f643f809516f8bb5beb2a722b8563
Source0:        https://github.com/LibreOffice/libexttextcat/archive/refs/tags/v%{version}.tar.gz#/libexttextcat-%{version}.tar.gz
BuildSystem:    autotools
# Upstream declaration in v3.4.8 uses a 32-bit size on LP64.
# https://github.com/LibreOffice/libexttextcat/blob/4872bb3ee1e47b076517dc0787cee5215aa34f60/src/wg_mempool.c#L86
Patch2000:      2000-match-memory-pool-prototype.patch

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
libexttextcat identifies the language of a text by comparing its
character n-grams with reference fingerprints. The package includes
the fingerprint database and the createfp utility.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%prep -a
# Generate configure and the host-triplet support files from the upstream tag.
autoreconf -fi

%files
%doc README
%license LICENSE
%{_bindir}/createfp
%{_datadir}/libexttextcat/
%{_libdir}/libexttextcat-2.0.so.*

%files devel
%{_includedir}/libexttextcat/
%{_libdir}/libexttextcat-2.0.so
%{_libdir}/pkgconfig/libexttextcat.pc
%{_datadir}/vala/vapi/libexttextcat.vapi

%changelog
%autochangelog
