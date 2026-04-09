# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           lua-lpeg
Version:        1.1.0
Release:        %autorelease
Summary:        Parsing Expression Grammars for Lua
License:        MIT
URL:            http://www.inf.puc-rio.br/~roberto/lpeg/
VCS:            git:https://github.com/roberto-ieru/LPeg.git
#!RemoteAsset
Source0:        http://www.inf.puc-rio.br/~roberto/lpeg/lpeg-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  COPT="%{optflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"

BuildRequires:  gcc
BuildRequires:  pkgconfig(lua)

%description
LPeg is a new pattern-matching library for Lua, based on Parsing Expression
Grammars (PEGs).

# No configure
%conf

# No install
%install
install -d -m 0755 %{buildroot}%{lua_libdir}
install -d -m 0755 %{buildroot}%{lua_pkgdir}

install -p -m 0755 lpeg.so %{buildroot}%{lua_libdir}/lpeg.so.%{version}
ln -s lpeg.so.%{version} %{buildroot}%{lua_libdir}/lpeg.so

install -p -m 0644 re.lua %{buildroot}%{lua_pkgdir}/

%files
%doc HISTORY lpeg.html re.html lpeg-128.gif test.lua
%{lua_libdir}/*
%{lua_pkgdir}/*

%changelog
%autochangelog
