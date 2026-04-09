# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond krun 0
%bcond wasm 0
%bcond criu 0
%bcond system_yajl 0

Name:           crun
Version:        1.26
Release:        %autorelease
Summary:        OCI runtime written in C
License:        GPL-2.0-only
URL:            https://github.com/containers/crun
#!RemoteAsset:  sha256:32211d0160ac092a71d1b0623232342d627dd601913a1fbb552d7d7d5b99bcc1
Source0:        https://github.com/containers/crun/releases/download/%{version}/crun-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules
%if %{with krun}
BuildOption(conf):  --with-libkrun
%endif
%if %{with wasm}
BuildOption(conf):  --with-wasmedge
%endif
%if %{without system_yajl}
BuildOption(conf):  --enable-embedded-yajl
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  python3-libmount
BuildRequires:  python3
%if %{with system_yajl}
BuildRequires:  pkgconfig(yajl)
%endif
%if %{with krun}
BuildRequires:  pkgconfig(libkrun)
%endif
%if %{with wasm}
BuildRequires:  wasmedge-devel
%endif
%if %{with criu}
BuildRequires:  pkgconfig(criu)
BuildRequires:  pkgconfig(libprotobuf-c)
%endif

Provides:       oci-runtime

%description
crun is a fast and low-memory OCI Container Runtime written in C.

%conf -p
./autogen.sh

%install -a
rm -rf %{buildroot}%{_libdir}/*.a

%check
# just skip tests as the env is not support.

%files
%license COPYING
%{_bindir}/crun
%{_mandir}/man1/crun.1*
%if %{with krun}
%{_bindir}/krun
%{_mandir}/man1/krun.1*
%endif
%if %{with wasm}
%{_bindir}/crun-wasm
%endif

%changelog
%autochangelog
