# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libuv
Version:        1.53.0
Release:        %autorelease
Summary:        Asychronous I/O support library
License:        MIT
URL:            https://libuv.org
VCS:            git:https://github.com/libuv/libuv
#!RemoteAsset:  sha256:cb0d6dd2128d5a95bd242c6cc982a24fe608fa93da57b6b4ec763b0018c53e64
Source0:        https://dist.libuv.org/dist/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    autotools

# Stabilize Linux EFTYPE values; https://github.com/libuv/libuv/commit/a4d2bec8a2fc437ab98bc0741b6e4261a2cc475e.
Patch1000:      1000-linux-eftype.patch

BuildOption(conf):  --disable-static

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
libuv is a support library with a focus on asynchronous I/O. It was
primarily developed for use by Node.js, but it is also used by
Mozilla's Rust language, Luvit, Julia, pyuv, and others.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libuv is a support library with a focus on asynchronous I/O. It was
primarily developed for use by Node.js, but it is also used by
Mozilla's Rust language, Luvit, Julia, pyuv, and others.

%prep -a
./autogen.sh

%check
# skip tests as net is disable.

%files
%license LICENSE
%{_libdir}/libuv.so.*

%files devel
%doc AUTHORS CONTRIBUTING.md ChangeLog README.md
%license LICENSE
%{_libdir}/libuv.so
%{_includedir}/uv*
%{_libdir}/pkgconfig/libuv.pc

%changelog
%autochangelog
