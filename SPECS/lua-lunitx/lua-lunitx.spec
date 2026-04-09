# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lua-lunitx
Version:        0.8.1
Release:        %autorelease
Summary:        Unit testing framework for Lua
License:        MIT
URL:            https://github.com/dcurrie/lunit
#!RemoteAsset
Source:         https://github.com/dcurrie/lunit/archive/refs/tags/%{version}.tar.gz

BuildRequires:  pkgconfig(lua)

Provides:       lua-lunit = %{version}-%{release}

%description
Lunitx is an extended version of Lunit, a unit testing framework for Lua,
supporting Lua 5.2, 5.3, and 5.4.

%prep
%autosetup -n lunit-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
cp -p extra/lunit.sh %{buildroot}%{_bindir}/lunit

mkdir -p %{buildroot}%{lua_pkgdir}
cp -pr lua/* %{buildroot}%{lua_pkgdir}

%check
LUA_PATH='%{buildroot}%{lua_pkgdir}/?.lua;;' %{buildroot}%{_bindir}/lunit --dontforce test/selftest.lua

%files
%license LICENSE
%doc ANNOUNCE CHANGES DOCUMENTATION examples README*
%{_bindir}/lunit
%{lua_pkgdir}/*

%changelog
%autochangelog
