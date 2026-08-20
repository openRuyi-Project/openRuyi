# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _test_target test
%global luafilesystem_version 1_9_0

Name:           lua-filesystem
Version:        1.9.0
Release:        %autorelease
Summary:        File system library for the Lua programming language
License:        MIT
URL:            https://lunarmodules.github.io/luafilesystem/
VCS:            git:https://github.com/lunarmodules/luafilesystem.git
#!RemoteAsset:  sha256:1142c1876e999b3e28d1c236bf21ffd9b023018e336ac25120fb5373aade1450
Source:         https://github.com/lunarmodules/luafilesystem/archive/refs/tags/v%{luafilesystem_version}.tar.gz
BuildSystem:    autotools
BuildOption(build):  CFLAGS="%{optflags} -fPIC -I%{_includedir}"
BuildOption(build):  LIB_OPTION="-shared %{build_ldflags}"
BuildOption(install):  LUA_LIBDIR=%{lua_libdir}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(lua)

Requires:       lua

%description
LuaFileSystem is a Lua library that provides portable access to directory
structures and file attributes.

# No configure
%conf

%files
%license LICENSE
%doc README.md docs/*.html docs/*.css docs/*.png
%{lua_libdir}/lfs.so

%changelog
%autochangelog
