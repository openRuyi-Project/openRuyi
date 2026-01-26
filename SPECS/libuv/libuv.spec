# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libuv
Version:        1.51.0
Release:        %autorelease
Summary:        Asychronous I/O support library
License:        MIT
URL:            https://libuv.org
VCS:            git:https://github.com/libuv/libuv
#!RemoteAsset
Source0:        https://dist.libuv.org/dist/v%{version}/%{name}-v%{version}.tar.gz
#!RemoteAsset
Source1:        https://dist.libuv.org/dist/v%{version}/%{name}-v%{version}.tar.gz.sign
BuildSystem:    autotools

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
%{?autochangelog}
