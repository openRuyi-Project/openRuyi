# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lua-json
Version:        1.3.5
Release:        %autorelease
Summary:        JSON Parser/Constructor for Lua
License:        MIT
URL:            https://github.com/harningt/luajson
#!RemoteAsset:  sha256:d6f4a354c8325ff965170a7c273bcf3a54736ff09d742008086d19462262368f
Source:         https://github.com/harningt/luajson/archive/refs/tags/%{version}.tar.gz
Patch2000:      2000-use-buildroot-test-directory-iterator.patch
BuildArch:      noarch
BuildSystem:    autotools

BuildRequires:  pkgconfig(lua)
BuildRequires:  autoconf
BuildRequires:  automake
# Tests
BuildRequires:  findutils
BuildRequires:  libtool
BuildRequires:  lua-lpeg
BuildRequires:  lua-lunitx
BuildRequires:  make


Requires:       lua
Requires:       lua-lpeg

%description
LuaJSON is a customizable JSON decoder/encoder, using LPEG for parsing.

# No configure
%conf


%install
install -d -m 755 %{buildroot}%{lua_pkgdir}
install -p -m 0644 lua/*.lua %{buildroot}%{lua_pkgdir}/

%files
%doc LICENSE docs/LuaJSON.txt docs/ReleaseNotes-1.0.txt
%{lua_pkgdir}/*.lua

%changelog
%autochangelog
