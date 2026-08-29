# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           luarocks
Version:        3.13.0
Release:        %autorelease
Summary:        Package manager for the Lua programming language
License:        MIT
URL:            https://luarocks.org
VCS:            git:https://github.com/luarocks/luarocks.git
#!RemoteAsset:  sha256:245bf6ec560c042cb8948e3d661189292587c5949104677f1eecddc54dbe7e37
Source:         https://luarocks.github.io/luarocks/releases/luarocks-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildRequires:  pkgconfig(lua)
BuildRequires:  unzip

Requires:       gcc
Requires:       lua
Requires:       make
Requires:       pkgconfig(lua)
Requires:       unzip

%description
LuaRocks is the package manager for the Lua programming language. It allows
the installation of Lua modules as self-contained packages called rocks,
which also contain version dependency information. LuaRocks supports both
local and remote repositories, and multiple local rocks trees.

%conf
./configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    --rocks-tree=%{_prefix} \
    --lua-version=%{lua_version} \
    --with-lua=%{_prefix} \
    --with-lua-interpreter=lua

%check
# No check

%files
%doc README.md CHANGELOG.md
%license COPYING
%{_bindir}/luarocks
%{_bindir}/luarocks-admin
%dir %{_sysconfdir}/luarocks
%config(noreplace) %{_sysconfdir}/luarocks/config-%{lua_version}.lua
%{_datadir}/lua/%{lua_version}/luarocks/

%changelog
%autochangelog
