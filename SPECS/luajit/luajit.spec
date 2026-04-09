# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: gns <wangbingzhen.riscv@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# LuaJIT is a rolling release, see http://luajit.org/status.html
# Use OpenResty branch, as their modifications are of optimizations and extensions.
# This also avoids having to package both vanilla LuaJIT and OR LuaJIT.
%global major 2.1
# The commit that could be patched
%global minor 20260114

Name:           luajit
Version:        %{major}+openresty%{minor}
Release:        %autorelease
Summary:        Just-In-Time Compiler for Lua
License:        MIT
URL:            http://luajit.org
VCS:            git:https://github.com/openresty/luajit2
#!RemoteAsset
Source0:        https://github.com/openresty/luajit2/archive/refs/tags/v%{major}-%{minor}.tar.gz#/luajit-openresty-v%{major}-%{minor}.tar.gz
# not autotools, use this for ease
BuildSystem:    autotools

# RISC-V 64 support, from https://github.com/openresty/luajit2/pull/236
# Should remove once PR is mereged.
Patch0:         0001-add_riscv_support.patch
# Preserve timestamps during installation
Patch1:         0002-preserve-timestamps.patch

BuildOption(build):  amalg Q= E=@: PREFIX=%{_prefix} TARGET_STRIP=:
BuildOption(build):  XCFLAGS="-DLUAJIT_ENABLE_LUA52COMPAT"
BuildOption(build):  CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"
BuildOption(build):  MULTILIB=%{_lib}
BuildOption(install):  PREFIX=%{_prefix} MULTILIB=%{_lib}

BuildRequires:  gcc
BuildRequires:  make

%description
LuaJIT implements the full set of language features defined by Lua 5.1.
The virtual machine (VM) is API- and ABI-compatible to the standard
Lua interpreter and can be deployed as a drop-in replacement.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

# Useful for Neovim, Aegisub, etc.
%package        static
Summary:        Static files for %{name}
Requires:       %{name}-devel = %{version}-%{release}

%description    static
This package contains static files for %{name}.

# overwrite conf process, don't do anything here
%conf

%install -a

# no tests.
%check

%files
%license COPYRIGHT
%doc README
%{_bindir}/luajit*
%{_libdir}/libluajit-*.so.*
%{_mandir}/man1/luajit.1*
%{_datadir}/luajit-%{major}

%files devel
%doc doc/*
%{_includedir}/luajit-%{major}/
%{_libdir}/libluajit-*.so
%{_libdir}/pkgconfig/luajit.pc

%files static
%{_libdir}/libluajit-*.a

%changelog
%autochangelog
